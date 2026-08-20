# 🍕 Pizza Delivery Pipeline - Apache Airflow

## Overview

This project implements a pizza delivery workflow using **Apache Airflow**. The DAG simulates the complete process from receiving a pizza order to dispatching it for delivery.

The project demonstrates important Airflow concepts including:

- Task orchestration and dependencies
- `PythonOperator`
- `BashOperator`
- `BranchPythonOperator`
- XCom communication
- Conditional branching
- Task skipping
- Logging and retries
- Cron scheduling
- REST API-based DAG triggering

---

## DAG Flow

The complete workflow contains 8 tasks:

```text
receive_order
      |
      v
check_stock
   /        \
  v          v
prepare_pizza   stock_unavailable
      |
      v
bake_pizza
      |
      v
quality_check
      |
      v
pack_order
      |
      v
dispatch_order
```

### Task Description

| Task | Operator | Description |
|---|---|---|
| `receive_order` | PythonOperator | Receives the pizza order and creates the order ID |
| `check_stock` | BranchPythonOperator | Checks topping availability and selects the next path |
| `prepare_pizza` | PythonOperator | Prepares the pizza |
| `stock_unavailable` | PythonOperator | Handles the unavailable topping scenario |
| `bake_pizza` | BashOperator | Simulates baking the pizza |
| `quality_check` | PythonOperator | Performs a quality check |
| `pack_order` | PythonOperator | Packs the completed pizza |
| `dispatch_order` | BashOperator | Simulates dispatching the order |

---

## Airflow Execution Flow

Airflow follows the dependencies defined in the DAG.

The execution starts with:

```text
receive_order
```

After it succeeds, Airflow allows:

```text
check_stock
```

to run.

The `check_stock` task then makes a decision based on topping availability.

### If topping is available

```text
receive_order
      ↓
check_stock
      ↓
prepare_pizza
      ↓
bake_pizza
      ↓
quality_check
      ↓
pack_order
      ↓
dispatch_order
```

### If topping is unavailable

```text
receive_order
      ↓
check_stock
      ↓
stock_unavailable
```

The pizza production tasks are skipped because it would not make business sense to continue the order without the required topping.

---

## XCom Communication

XCom stands for **Cross-Communication**. It is used by Airflow tasks to share small pieces of data.

In this project, the data passed through XCom is:

```text
ORDER_ID = PIZZA-1001
```

### Sending Data to XCom

The `receive_order` task returns the order ID:

```python
return ORDER_ID
```

When a task returns a value, Airflow automatically stores that value in XCom.

```text
receive_order
      |
      | returns "PIZZA-1001"
      v
Airflow XCom
```

### Reading Data from XCom

Other tasks retrieve the order ID using:

```python
order_id = ti.xcom_pull(
    task_ids="receive_order"
)
```

Here:

- `ti` represents the current Task Instance.
- `xcom_pull()` retrieves data stored in XCom.
- `task_ids="receive_order"` tells Airflow which task originally sent the data.

![Xcoms](<../Screenshots/Xcoms Pizza Delivery.png>)

### XCom Flow in This Project

```text
                    receive_order
                         |
                         | return ORDER_ID
                         v
                       XCom
                    "PIZZA-1001"
                    /      |      \
                   v       v       v
             check_stock quality_check pack_order
```

XCom is suitable here because an order ID is a small value. Large files or datasets should normally be stored outside XCom, such as in a database or cloud storage.

---

## Branching and Task Skipping

The `check_stock` task uses:

```python
BranchPythonOperator
```

Its job is to decide which downstream task should run.

```python
if TOPPING_AVAILABLE:
    return "prepare_pizza"

return "stock_unavailable"
```

### Available Topping

If:

```python
TOPPING_AVAILABLE = True
```

Airflow selects:

```text
prepare_pizza
```
![Available Toppings](<../Screenshots/Scenerio_1 If toppings are Available.png>)

and the production workflow continues. The `stock_unavailable` task is skipped.

### Unavailable Topping

If:

```python
TOPPING_AVAILABLE = False
```

Airflow selects:

```text
stock_unavailable
```

The `prepare_pizza` path is skipped, and its downstream tasks do not continue.

Expected task states:

```text
receive_order       SUCCESS
check_stock         SUCCESS
stock_unavailable   SUCCESS

prepare_pizza       SKIPPED
bake_pizza          SKIPPED
quality_check       SKIPPED
pack_order          SKIPPED
dispatch_order      SKIPPED
```

This demonstrates Airflow's conditional workflow execution.

![Unavailable Toppings](<../Screenshots/Scenerio_2 if toppings are unavailable.png>)

---

## Operators Used

### PythonOperator

Used to execute Python functions for tasks such as:

- Receiving an order
- Preparing pizza
- Handling unavailable stock
- Quality checking
- Packing the order

### BranchPythonOperator

Used by `check_stock` to select the correct workflow path. It returns the ID of the task that Airflow should execute next.

### BashOperator

Used for:

- `bake_pizza`
- `dispatch_order`

It executes Bash commands inside Airflow tasks.

---

## Reliability and Logging

The DAG includes retry handling:

```python
default_args = {
    "owner": "pizza_data_engineering",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}
```

If a task temporarily fails, Airflow can retry it up to two times with a two-minute delay between retries.

The DAG also uses Airflow logging to record important events such as:

- Order received
- Stock availability
- Branch selected
- Pizza preparation
- Quality check result
- Packing and dispatch
- Reasons for skipped tasks

---

## Schedule

The DAG uses:

```python
schedule="0 12,19 * * *"
```

This cron expression runs the DAG every day at:

- **12:00 PM** — Lunch rush
- **7:00 PM** — Dinner rush

`catchup=False` is used to prevent Airflow from automatically creating old DAG runs from the start date.

---

## Triggering the DAG Using Airflow REST API

In addition to triggering the DAG manually from the Airflow UI, the DAG can also be triggered programmatically through the **Airflow REST API**.

The API flow is:

```text
Airflow REST API
        |
        | Create DAG Run
        v
Airflow Scheduler
        |
        v
pizza_delivery_dag
        |
        v
Tasks Execute According to Dependencies
```

The API sends a request to Airflow asking it to create a new run of:

```text
pizza_delivery_dag
```

Airflow then creates a DAG run and returns information such as:

- DAG ID
- DAG Run ID
- Run state
- Execution or logical date

This allows external applications, scripts, or other systems to trigger the workflow without manually clicking the Trigger button in the Airflow UI.

![Airflow Api](<../Screenshots/Dag trigger through Swagger.png>)
![Airflow Api](<../Screenshots/Dag trigger through swagger show.png>)
---

## Project Flow Summary

```text
Pizza Order Received
        |
        v
Order ID Stored in XCom
        |
        v
Check Stock Reads Order ID
        |
        v
Is Topping Available?
    /               \
  YES                NO
   |                  |
   v                  v
Prepare Pizza   Stock Unavailable
   |
   v
Bake Pizza
   |
   v
Quality Check
   |
   v
Pack Order
   |
   v
Dispatch Order
```

![Dashboard](<../Screenshots/Dag Dashboard.png>)

## Author

**Anup Rathore**
