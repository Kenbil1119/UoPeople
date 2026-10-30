🍲 Food Menu Roster Generator

A simple Python application that generates a randomized four-week food menu roster using a list of menu items and a collection of quotes related to food, nutrition, and healthcare.

The application is designed to provide meal suggestions for an average Nigerian menu while encouraging awareness of food, nutrition, and healthy living.

📌 Table of Contents

- ["Overview"] (#overview)
- ["Features"] (#features)
- ["Technologies Used"] (#technologies-used)
- ["Project Structure"] (#project-structure)
- ["Requirements"] (#requirements)
- ["Installation"] (#installation)
- ["Usage"] (#usage)
- ["How It Works"] (#how-it-works)
- ["Sample Output"] (#sample-output)
- ["Limitations"] (#limitations)
- ["Possible Improvements"] (#possible-improvements)
- ["Author"] (#author)

## 📖 Overview

The Food Menu Roster Generator is a command-line Python program that randomly selects meals from a predefined menu list to create a four-week roster.

It uses the current month obtained from the system date to label the roster and displays a food-related quote for each week.

The program organizes the roster into seven days per week, with three meal categories per day:

- Breakfast
- Lunch
- Dinner

The menu selections are randomized, allowing different meal combinations to appear each time the program runs.

## ✨ Features

- Automatic Month Detection: Retrieves the current month using Python's "datetime" module.
- Randomized Meal Selection: Selects menu items randomly using Python's "random" module.
- Four-Week Roster: Generates a roster covering four weeks.
- Daily Meal Planning: Displays breakfast, lunch, and dinner for each day.
- Food-Related Quotes: Displays a randomly selected quote for each week.
- External Text Files: Stores menu items and quotes in separate text files, making the content easy to update without modifying the Python source code.
- Simple Command-Line Interface: Displays the roster directly in the terminal.

## 🛠️ Technologies Used

- Python 3: The programming language used to develop the application.
- "random": Selects random menu items and food-related quotes.
- "datetime": Retrieves the current month from the system date.
- Text Files: Stores menu items and quotes used by the application.

All Python modules used by the program are part of the Python standard library. No external Python packages are required.

## 📁 Project Structure

The project consists of three files:

```text
menu/
├── food_roster.py
├── menu_list.txt
└── food_quotes.txt
```
```text
File| Description
"food_roster.py"| Contains the Python code that generates and displays the menu roster.
"menu_list.txt"| Contains menu items used for randomized meal selection.
"food_quotes.txt"| Contains quotes related to food, nutrition, and healthcare.
```

## 📋 Requirements

Before running the application, ensure that you have:

- Python 3 installed on your computer.
- All three project files in the same directory.
- Read access to "menu_list.txt" and "food_quotes.txt".

> [!TIP]
> You can verify your Python installation by running:
```bash
python --version
```
> Depending on your environment, you may need to use:
```bash
python3 --version
```
## 🚀 Installation

1. Clone the repository

Open your terminal and run:
```bash
git clone https://github.com/Kenbil1119/UoPeople.git
```
2. Navigate to the project directory
```bash
cd UoPeople/menu
```
3. Verify the project files

> [!NOTE]
> Ensure that the following files are present:

```text
food_roster.py
menu_list.txt
food_quotes.txt
```
4. Run the application

On Windows, Linux, or macOS, run:
```bash
python food_roster.py
```
If your system uses "python3" to invoke Python, run:
```bash
python3 food_roster.py
```
The program will display the generated menu roster in your terminal.

## 💻 Usage

Once the application starts, it automatically:

1. Retrieves the current month.
2. Reads the menu items from "menu_list.txt".
3. Reads food-related quotes from "food_quotes.txt".
4. Generates four weeks of meal suggestions.
5. Displays a quote for each week.
6. Prints breakfast, lunch, and dinner suggestions for each day.

> [!NOTE]
> No interactive input is required.

> [!TIP]
> To generate another roster, run the program again. The randomized selections may produce a different combination of meals and quotes.

## ⚙️ How It Works

1. Importing the required modules

import random
from datetime import datetime

The "random" module provides random selection, while "datetime" retrieves information about the current date.

2. Defining the days of the week

```python
days = (
    'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY',
    'THURSDAY', 'FRIDAY', 'SATURDAY'
)
```
A tuple stores the seven days of the week. The program iterates over this tuple to organize the daily meal suggestions.

3. Retrieving the current month

```python
month = datetime.today().strftime('%B')
```
This expression obtains the current system date and formats the month as its full name, such as "October".

The month is used in the roster heading.

4. Reading the external text files

```python
with open('menu_list.txt', 'r') as menu_list:
    menus = menu_list.readlines()

with open('food_quotes.txt', 'r') as quotes:
    quotes = quotes.readlines()
```
The program reads the contents of both text files into lists.

Each line becomes an element in its corresponding list, allowing the program to select individual menu items and quotes.

5. Generating the four-week roster

```python
for week in range(4):
```
The outer loop runs four times, producing four weekly sections.

Within each week, the program displays a randomly selected quote and iterates through the seven days.

6. Selecting daily meals

```python
for meal in ('Breakfast', 'Lunch', 'Dinner'):
    print(f"{meal}: {random.choice(menus)}", end='')
```

For every day, the inner loop displays three meal categories.

The ```random.choice()``` function selects a menu item from the loaded menu list for each category.

Because each selection is independent, the same menu item may appear more than once, including on the same day.

## 🖥️ Sample Output

The following is an illustrative example of how the application may display its results. Actual meals and quotes depend on the contents of your text files and the random selections made when the program runs.

```text              
             -----=== October Menu Roster===-----

                  __________________
                 | WEEK 1 menu list |
                  ------------------
A good meal brings people together.

      SUNDAY
Breakfast: Bread and tea
Lunch: Jollof rice
Dinner: Beans and plantain

      MONDAY
Breakfast: Akara and pap
Lunch: Eba and egusi soup
Dinner: Yam porridge

...
```
The actual output formatting depends on the menu items, quotes, and spacing produced by your code.

> [!NOTE]
> ## ⚠️ Limitations
> The current implementation has some limitations:

> - Fixed duration: The program generates four weeks regardless of the number of weeks in the current month.
> - No date assignment: It displays the days of the week without assigning specific calendar dates to them.
> - Random repetition: The same meal can appear multiple times in the roster.
> - No dietary restrictions: The program does not filter meals according to allergies, medical needs, or dietary preferences.
> - File dependency: Both text files must exist in the program's working directory.
> - Limited error handling: The program does not explicitly handle missing files or empty menu and quote lists.
> - No persistence: The generated roster is displayed in the terminal but is not saved automatically.

## 🔮 Possible Improvements

Future versions could include:

- Generate a roster based on the actual calendar dates of a selected month.
- Add options for selecting a month and year.
- Reduce unnecessary repetition of meals.
- Categorize meals according to nutritional value or food groups.
- Add options for dietary preferences and allergies.
- Handle missing files and empty lists gracefully.
- Save generated rosters to a text file or PDF document.
- Introduce an interactive interface for selecting meals and customizing weekly plans.
- Expand the application to support additional Nigerian dishes and regional food preferences.

These are potential future enhancements and are not currently implemented.

## 👨‍💻 Author

Usman K. Saheed

GitHub: ["@Kenbil1119"] (https://github.com/Kenbil1119)

---

This project demonstrates the practical use of Python's built-in libraries, tuples, loops, file handling, formatted strings, and random selection.
