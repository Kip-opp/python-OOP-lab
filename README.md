# Bookstore OOP Lab

This project implements two simple Python classes to model objects in a bookstore environment: a `Book` and a `Coffee`. The goal of the lab is to practice core object-oriented programming concepts such as class creation, attributes, methods, property validation, and test-driven development. [web:262][web:267]

## Project Overview

The bookstore carries books for reading and coffee for purchase. To represent this scenario, the application includes:

- A `Book` class for modeling a readable book
- A `Coffee` class for modeling a coffee item sold in the store

Each class includes required attributes, validation rules, and behavior methods.

## Learning Goals

This lab focuses on:

- Creating Python classes
- Initializing objects with `__init__`
- Using properties for validation
- Writing instance methods
- Running tests with `pytest`
- Building clean, readable object-oriented code [web:262][web:266]

## Requirements

### Book
#### Attributes
- `title`
- `page_count`

#### Behavior
- `turn_page()` prints:
  `"Flipping the page...wow, you read fast!"`

#### Validation
- `page_count` must be an integer
- If invalid, print:
  `"page_count must be an integer"`

### Coffee
#### Attributes
- `size`
- `price`

#### Behavior
- `tip()` prints:
  `"This coffee is great, here’s a tip!"`
- `tip()` also increases the coffee price by `1`

#### Validation
- `size` must be one of:
  - `Small`
  - `Medium`
  - `Large`
- If invalid, print:
  `"size must be Small, Medium, or Large"`

## Project Structure

```bash
.
├── lib/
│   ├── book.py
│   └── coffee.py
├── testing/
│   ├── book_test.py
│   └── coffee_test.py
├── README.md
├── Pipfile
└── Pipfile.lock
```

## Setup

Install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

## Running Tests

Run all tests:

```bash
pytest -x
```

Run only the book tests:

```bash
pytest -x testing/book_test.py
```

Run only the coffee tests:

```bash
pytest -x testing/coffee_test.py
```

The `-x` flag is useful in test-driven development because it stops execution at the first failing test, making debugging faster and more focused. [web:266][web:272]

## Implementation Summary

### `Book` class
Located in `lib/book.py`.

Responsibilities:
- Store the book title
- Store and validate `page_count`
- Provide a `turn_page()` method that simulates reading behavior

Expected implementation notes:
- `title` should be required when creating the object
- `page_count` should be required and validated as an integer
- Invalid `page_count` input should print a warning message rather than silently failing

### `Coffee` class
Located in `lib/coffee.py`.

Responsibilities:
- Store coffee size and price
- Validate the allowed size values
- Provide a `tip()` method that increases the price

Expected implementation notes:
- `size` should be required when creating the object
- `price` should be required when creating the object
- `size` must be validated against the allowed set: `Small`, `Medium`, `Large`
- `tip()` should print the expected message and increment the price by `1`

## Example Usage

```python
from lib.book import Book
from lib.coffee import Coffee

book = Book("Clean Code", 464)
book.turn_page()
# Flipping the page...wow, you read fast!

coffee = Coffee("Medium", 4.5)
coffee.tip()
# This coffee is great, here’s a tip!

print(coffee.price)
# 5.5
```

## Development Workflow

### 1. Create a feature branch

```bash
git checkout -b feat/bookstore-oop-lab
```

### 2. Implement the classes

Write your code in:

- `lib/book.py`
- `lib/coffee.py`

### 3. Run tests until all pass

```bash
pytest -x
```

### 4. Stage and commit your work

```bash
git add .
git commit -m "feat: implement bookstore book and coffee classes"
```

### 5. Push your branch

```bash
git push origin feat/bookstore-oop-lab
```

### 6. Open PR and merge

After review, merge the feature branch into `main`.



## Deliverables

- A working `Book` class
- A working `Coffee` class
- Property validation for `page_count` and `size`
- Correct instance methods (`turn_page()` and `tip()`)
- Passing tests
