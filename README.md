# Data Processor Task
## Member Data Management System

### Python Training – Integrated Core Concepts Assignment

---

## 1. Project Overview

The **Data Processor Task** is a modular Python application created for the Python Training – Integrated Core Concepts Assignment.

The project demonstrates how fundamental Python concepts can be combined to create a small, practical **Member Data Management System**.

The application starts with a hardcoded list of raw member dictionaries. It cleans and validates the data, creates `Member` objects for valid records, handles invalid records using a custom exception, filters members using Lambda and `filter()`, displays a processing summary, and packages the project into a Python Wheel (`.whl`) file for distribution.

---

## 2. Project Objectives

This project demonstrates:

- Python Lists
- Python Dictionaries
- Functions
- Modular programming
- Python imports
- Packages
- Classes and objects
- `__init__()`
- `self`
- Object attributes
- `__str__()`
- Custom exceptions
- `try-except`
- `raise`
- Regular Expressions
- String cleaning
- Lambda functions
- `filter()`
- Python packaging
- `setuptools`
- Wheel files
- `pyproject.toml`
- `setup.py`
- Installing and testing a Wheel package

---

## 3. Project Structure

```text
Python_Core_Assignment/
│
├── main.py
├── README.md
├── setup.py
├── pyproject.toml
│
└── my_processor/
    ├── __init__.py
    ├── core.py
    ├── utils.py
    └── exceptions.py
```

After building the package, generated files/folders may appear:

```text
Python_Core_Assignment/
│
├── build/
├── dist/
│   ├── data_processor_task-1.0.0-py3-none-any.whl
│   └── data_processor_task-1.0.0.tar.gz
│
├── data_processor_task.egg-info/
├── main.py
├── README.md
├── setup.py
├── pyproject.toml
│
└── my_processor/
    ├── __init__.py
    ├── core.py
    ├── utils.py
    └── exceptions.py
```

---

# 4. File-by-File Explanation

## `main.py`

The main execution file.

Responsibilities:

1. Defines raw member data.
2. Processes each record.
3. Creates `Member` objects.
4. Handles invalid records.
5. Stores valid members.
6. Filters Gmail members using Lambda and `filter()`.
7. Displays members and summary.

Run:

```bash
python main.py
```

## `my_processor/__init__.py`

Makes `my_processor` a Python package and contains the package version:

```python
__version__ = "1.0.0"
```

Check it with:

```python
import my_processor
print(my_processor.__version__)
```

Expected:

```text
1.0.0
```

## `my_processor/core.py`

Contains the main `Member` class and demonstrates:

- Classes
- Objects
- `__init__()`
- `self`
- Attributes
- Methods
- `__str__()`
- Validation
- Custom exceptions

Example:

```python
member = Member(
    "Anup Rathore",
    "anup@gmail.com",
    "9876543210"
)
```

## `my_processor/utils.py`

Contains reusable helper functions for:

- Cleaning names
- Validating names
- Validating emails
- Validating phone numbers

Regular Expressions are used for validation.

## `my_processor/exceptions.py`

Contains:

```python
InvalidMemberDataError
```

This custom exception is raised when member data is invalid.

## `setup.py`

Contains setuptools packaging configuration such as:

- Package name
- Version
- Description
- Author
- Python requirement
- Packages to include

## `pyproject.toml`

Contains modern Python build configuration including:

- Build system
- Build requirements
- Build backend
- Project metadata
- Python version
- Package discovery

---

# 5. Raw Member Data

The application uses a list containing dictionaries.

Example:

```python
raw_members = [
    {
        "name": "Anup Rathore",
        "email": "anup.rathore@gmail.com",
        "phone": "9876543210",
    },
    {
        "name": "John123",
        "email": "john@gmail.com",
        "phone": "9876543211",
    },
]
```

The outer structure is a List and every dictionary represents one member.

---

# 6. Data Structure Concepts

## List

A List stores multiple member records:

```python
members = []
```

Valid members are added with:

```python
members.append(member)
```

## Dictionary

A Dictionary represents one member:

```python
{
    "name": "Anup Rathore",
    "email": "anup@gmail.com",
    "phone": "9876543210"
}
```

---

# 7. Data Cleaning

Member names are cleaned before validation.

Example:

```text
"   Anup Rathore   "
```

becomes:

```text
"Anup Rathore"
```

using:

```python
name.strip()
```

---

# 8. Validation Rules

## Name

Valid names:

```text
Anup Rathore
John Doe
AAAAA
```

Invalid names:

```text
John123
123John
John@Doe
```

Rules:

- Only letters and spaces.
- No numbers.
- No special characters.

## Email

Valid:

```text
aaaaa@gmail.com
anup@gmail.com
john.doe@gmail.com
```

Invalid:

```text
rahulgmail.com
john@@gmail.com
@gmail.com
john gmail@gmail.com
```

The project checks email format, not whether the account actually exists.

## Phone

Exactly 10 digits are required.

Valid:

```text
9876543210
9123456789
```

Invalid:

```text
98765
98765abc10
98765-43210
98765 43210
```

Letters, spaces and special characters are rejected.

---

# 9. Regular Expressions

The Python `re` module is used for validation.

Phone validation uses a pattern equivalent to:

```text
^[0-9]{10}$
```

Meaning:

- `^` = start
- `[0-9]` = digit
- `{10}` = exactly 10 times
- `$` = end

Therefore `9876543210` is valid, while a number with fewer or more digits is invalid.

---

# 10. Object-Oriented Programming

The `Member` class represents a real-world member.

Conceptually:

```text
Member
├── name
├── email
└── phone
```

Example:

```python
member = Member(
    "Anup Rathore",
    "anup@gmail.com",
    "9876543210"
)
```

The object's data can be accessed using:

```python
member.name
member.email
member.phone
```

---

# 11. `__init__()` and `self`

`__init__()` runs automatically when a Member object is created.

Example:

```python
member = Member("Anup Rathore", "anup@gmail.com", "9876543210")
```

Python automatically invokes `__init__()`.

`self` refers to the current object:

```python
self.name = name
self.email = email
self.phone = phone
```

Each Member object therefore keeps its own values.

---

# 12. `__str__()`

The `__str__()` method provides readable output.

Instead of:

```text
<my_processor.core.Member object at 0x...>
```

the project produces:

```text
Member(Name=Anup Rathore, Email=anup@gmail.com, Phone=9876543210)
```

---

# 13. Custom Exception Handling

The project defines:

```python
InvalidMemberDataError
```

When validation fails:

```text
Invalid data
    ↓
Validation fails
    ↓
InvalidMemberDataError raised
    ↓
except block catches it
    ↓
Record is skipped
    ↓
Next record is processed
```

This prevents one invalid record from stopping the entire application.

---

# 14. Lambda and `filter()`

The project filters Gmail users using functional programming:

```python
gmail_members = list(
    filter(
        lambda member: member.email.endswith("@gmail.com"),
        members,
    )
)
```

The Lambda checks whether the email ends with:

```text
@gmail.com
```

Only matching members are retained.

---

# 15. Complete Processing Flow

```text
Raw Member Data
      ↓
List of Dictionaries
      ↓
Loop Through Records
      ↓
Create Member Object
      ↓
Clean Name
      ↓
Validate Name
      ↓
Validate Email
      ↓
Validate Phone
      ↓
   Valid?
   /    \
 Yes    No
  ↓      ↓
Store   Raise Custom Error
Member     ↓
  ↓      Skip Record
  └───┬──────┘
      ↓
Process Next Record
      ↓
Filter Gmail Members
      ↓
Display Summary
```

---

# 16. Expected Application Output

```text
==================================================
MEMBER DATA PROCESSING STARTED
==================================================

Processing: Anup Rathore
Validation Successful

Processing: John123
Error: Invalid name: John123
Skipping Record...

Processing: Rahul Sharma
Error: Invalid email: rahulgmail.com
Skipping Record...

Processing: Priya Verma
Error: Invalid phone number: 98765
Skipping Record...

Processing: Aman Singh
Validation Successful

==================================================
VALID MEMBERS
==================================================

Member(Name=Anup Rathore, Email=anup.rathore@gmail.com, Phone=9876543210)
Member(Name=Aman Singh, Email=aman.singh@gmail.com, Phone=9123456789)

==================================================
FILTERING GMAIL USERS
==================================================

Member(Name=Anup Rathore, Email=anup.rathore@gmail.com, Phone=9876543210)
Member(Name=Aman Singh, Email=aman.singh@gmail.com, Phone=9123456789)

==================================================
SUMMARY
==================================================

Total Records       : 5
Processed Successfully : 2
Failed Records      : 3
```

---

# 17. Environment Setup

Create the virtual environment:

```bash
python -m venv myenv
```

Windows PowerShell:

```powershell
myenv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
myenv\Scripts\activate
```

Linux/Mac:

```bash
source myenv/bin/activate
```

Install packaging tools:

```bash
python -m pip install --upgrade setuptools wheel build
```

---

# 18. Run the Application

Before packaging, test the project:

```bash
python main.py
```

The application should complete successfully and display validation results and the summary.

---

# 19. Build the Wheel

The assignment specifies:

```bash
python setup.py sdist bdist_wheel
```

After the command finishes, the `dist` directory should contain:

```text
dist/
├── data_processor_task-1.0.0-py3-none-any.whl
└── data_processor_task-1.0.0.tar.gz
```

The important deliverable is:

```text
data_processor_task-1.0.0-py3-none-any.whl
```

---

# 20. Understanding the Wheel Filename

Example:

```text
data_processor_task-1.0.0-py3-none-any.whl
```

Breakdown:

```text
data_processor_task → Distribution name
1.0.0               → Version
py3                 → Python 3
none                → No specific ABI
any                 → Platform independent
```

---

# 21. Install the Wheel

Install the generated package:

```bash
python -m pip install dist\data_processor_task-1.0.0-py3-none-any.whl
```

A successful installation should show:

```text
Successfully installed data_processor_task-1.0.0
```

---

# 22. Test the Installed Package

Start Python:

```bash
python
```

Then:

```python
from my_processor.core import Member

member = Member(
    "Anup Rathore",
    "anup@gmail.com",
    "9876543210"
)

print(member)
```

Expected:

```text
Member(Name=Anup Rathore, Email=anup@gmail.com, Phone=9876543210)
```

Check the package version:

```python
import my_processor

print(my_processor.__version__)
```

Expected:

```text
1.0.0
```

---

# 23. Invalid Data Tests

Invalid name:

```python
Member("Anup123", "anup@gmail.com", "9876543210")
```

Invalid email:

```python
Member("Anup Rathore", "anupgmail.com", "9876543210")
```

Invalid phone:

```python
Member("Anup Rathore", "anup@gmail.com", "98765")
```

Each should raise `InvalidMemberDataError`.

---

# 24. Why the Project Is Modular

Responsibilities are separated:

```text
utils.py
    ↓
Cleaning + Validation

core.py
    ↓
Member Class + OOP

exceptions.py
    ↓
Custom Error

main.py
    ↓
Application Flow
```

Benefits:

- Easier to understand
- Easier to maintain
- Easier to test
- Easier to reuse
- Easier to debug
- Clear separation of responsibilities

---

# 25. Technologies Used

- Python 3
- `re`
- Lists
- Dictionaries
- Functions
- Classes
- Objects
- Exception handling
- Lambda
- `filter()`
- setuptools
- Wheel
- `setup.py`
- `pyproject.toml`

No third-party runtime library is required by the application itself.

# 26. Submission Contents

The final submission should contain:

```text
Python_Core_Assignment/
│
├── main.py
├── README.md
├── setup.py
├── pyproject.toml
│
├── my_processor/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│   └── exceptions.py
│
└── dist/
    └── data_processor_task-1.0.0-py3-none-any.whl
```

Recommended screenshots:

1. Project structure.
2. Successful `python main.py` execution.
3. Wheel creation command.
4. Generated Wheel inside `dist/`.
5. Wheel installation.
6. Importing `Member`.
7. Successful creation and printing of a Member object.

---

# 27. Final Project Flow

```text
Python Fundamentals
        ↓
Raw Member Data
        ↓
Lists + Dictionaries
        ↓
Data Cleaning
        ↓
Regular Expression Validation
        ↓
Object-Oriented Programming
        ↓
Custom Exception Handling
        ↓
Lambda + filter()
        ↓
Working Application
        ↓
setuptools Packaging
        ↓
Wheel File
        ↓
pip Installation
        ↓
Package Import
        ↓
Successful Testing
```

---

# 29. Author Information

**Author:** Anup Rathore  
**Project:** Data Processor Task  
**Package Name:** `data_processor_task`  
**Python Package:** `my_processor`  
**Version:** `1.0.0`  
**Purpose:** Python Training – Integrated Core Concepts Assignment

---

# 30. Conclusion

The Data Processor Task combines core Python concepts into a complete modular application.

Raw member dictionaries are cleaned and validated using functions and Regular Expressions. Valid records are converted into `Member` objects using Object-Oriented Programming. Invalid records are safely handled using a custom exception. Lambda and `filter()` are used to demonstrate functional programming.

Finally, the application is packaged as a Python Wheel, installed with `pip`, imported, and tested independently.

The project therefore demonstrates the complete journey from Python fundamentals to a structured, reusable, and distributable Python application.

# Screenshots

![Output Screenshot](<Screenshot 2026-08-12 112248.png>)

![Dependencies Screenshot](<screenshots/Screenshot 2026-08-10 094649.png>)