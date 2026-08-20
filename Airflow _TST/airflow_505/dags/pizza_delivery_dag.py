from datetime import datetime , timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator , BranchPythonOperator
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.operators.bash import BashOperator

logger=LoggingMixin().log

ORDER_ID = "PIZZA-1002"
TOPPING_AVAILABLE = True


default_args = {
    "owner": "Anup",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

def receive_order():
    logger.info("New Pizza Order recieved: %s" , ORDER_ID)

    return ORDER_ID

def check_stock(ti):
    order_id = ti.xcom_pull(task_ids="receive_order")

    logger.info("checking ingredient stock for order : %s " , order_id)

    if TOPPING_AVAILABLE:
        logger.info("Required topping is available for order: %s" , order_id)
        return "prepare_pizza"
    else:
        logger.warning("Required tooping is not available for this order %s" , order_id)
        return "stock_unavailable"

def prepare_pizza():
    logger.info("preparing pizza for the customer ")

def stock_unavailable():
    logger.info("Pizza prepration Skipped Because of Topping is unvailable ")

def quality_check(ti):
    order_id = ti.xcom_pull(
        task_ids="receive_order"
    )

    quality_passed = True

    if quality_passed:
        logger.info(
            "Quality check passed for order: %s",
            order_id,
        )
        return

    logger.error(
        "Quality check failed for order: %s",
        order_id,
    )

def pack_order(ti):
    order_id = ti.xcom_pull(
        task_ids="receive_order"
    )

    logger.info(
        "Packing completed pizza for order: %s",
        order_id,
    )



with DAG(
    dag_id="pizza_delivery_dag",
    start_date=datetime(2026, 8, 17),
    schedule="0 12,19 * * *",
    catchup=False,
    default_args=default_args,
) as dag:

    receive_order_task = PythonOperator(
        task_id="receive_order",
        python_callable=receive_order,
    )

    check_stock_task = BranchPythonOperator(
        task_id="check_stock",
        python_callable=check_stock,
    )

    prepare_pizza_task = PythonOperator(
        task_id="prepare_pizza",
        python_callable=prepare_pizza,
    )
    
    stock_unavailable_task= PythonOperator(
        task_id="stock_unavailable",
        python_callable=stock_unavailable
    )

    bake_pizza_task = BashOperator(
        task_id="bake_pizza",
        bash_command='echo "Pizza is now baking int the oven."',
    )

    quality_check_task=PythonOperator(
        task_id="quality_check",
        python_callable=quality_check,
    )
    
    pack_order_task=PythonOperator(
        task_id="pack_order",
        python_callable=pack_order,
    )

    dispatch_task= BashOperator(
        task_id="dispatch_order",
        bash_command='echo "Pizza order dispatched for delivery"',
    )


receive_order_task >> check_stock_task

check_stock_task >> [prepare_pizza_task ,stock_unavailable_task]

prepare_pizza_task >> bake_pizza_task

bake_pizza_task >> quality_check_task

quality_check_task >> pack_order_task

pack_order_task >> dispatch_task


    