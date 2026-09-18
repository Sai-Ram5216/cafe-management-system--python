# Cafe Management System

A simple console-based Cafe Management System developed using Python.

## Project Description

This project is a beginner-friendly Python console application that allows customers to view cafe menu categories, place multiple food or beverage orders, and calculate the total bill.

## Features

* Displays separate menu categories for beverages and snack items
* Allows customers to select food and beverage items
* Supports multiple orders
* Checks item availability
* Calculates the total bill automatically
* Provides an interactive console-based interface

## Menu

### Snack Items

| Item     | Price |
| -------- | ----: |
| Pizza    |  ₹120 |
| Veg Puff |   ₹40 |
| Egg Puff |   ₹50 |
| Burger   |   ₹80 |

### Beverages

| Item       | Price |
| ---------- | ----: |
| Ginger Tea |   ₹20 |
| Coffee     |   ₹40 |
| Green Tea  |   ₹50 |
| Lassi      |   ₹40 |

## Technologies Used

* Python

## Python Concepts Used

* Variables
* Dictionaries
* Conditional statements (`if`, `elif`, `else`)
* `while` loop
* User input
* String methods
* Membership operators
* Arithmetic operations

## How the Program Works

1. The program displays the Cafe Management System.
2. The customer chooses a menu category:

   * Beverages
   * Snack Items
3. The customer selects an item.
4. The program checks whether the item exists in the menu.
5. The selected item's price is added to the total amount.
6. The customer can continue placing additional orders.
7. When the customer finishes ordering, the final bill is displayed.

## How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code or a terminal and run:

```bash
cafe management system.py
```

Then follow the instructions displayed in the terminal.

## Sample Output

```text
Cafe Management System

Welcome to Sai's Restaurant

Choose your choice (beverages/snack items): beverages

ITEM : PRICE
ginger tea : 20
coffee : 40
green tea : 50
lassi : 40

Choose your item to order: coffee
Your order has been placed

Do you want to try other food item (yes/no): no

Your Bill to Pay: 40
Thank you
Visit again
```

## Purpose

This project was created to practice Python fundamentals and understand how basic programming concepts can be combined to build a simple real-world console application.
