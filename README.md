# Programming and Scripting - Weekly Tasks
This repository contains solutions to the weekly tasks completed as part of the  **Programming and Scripting** module.

Each task focuses on a core Python programming concept, progressing from basic output and user input through file handling, algorithms, and data visualisations.

## Repository Structure
```
programming_scripting-pands-weekly-tasks/
├── helloworld.py          # Weekly Task 1 - Hello World
├── bank.py                # Weekly Task 2 - Bank amount calculator
├── accounts.py            # Weekly Task 3 - Account number masking
├── collatz.py             # Weekly Task 4 - Collatz sequence
├── weekday.py             # Weekly Task 5 - Weekday calculator
├── squareroot.py          # Weekly Task 6 - Square root approximation
├── week07-es.py           # Weekly Task 7 - Count letter e in text file
├── week07-test.txt        # Sample text file for testing Weekly task 7
├── week08-plottask.py     # Weekly Task 8 - Data visualisation
└── week08-plot.png        # Output image from Weekly task 8
```

## Weekly Tasks

### Weekly Task 1 -  Hello World (`helloworld.py`)
Prints `Hello, World` to the terminal . Used to verify the Python environment was set up correctly at the start of the module.

### Weekly Task 2 - Bank (`bank.py`)
Prompts the user to enter two amounts in cent, adds them as integers, then prints the total formatted as euros and cents (e.g. `€2.45`). Uses integer arithmetic to avoid floating-point rounding errors.

### Weekly Task 3 - Accounts (`accounts.py`)
Reads in a bank account number and masks all but the last 4 digits with `X` characters (e.g. `XXXXXX7890`). Handles account numbers of 4 characters or fewer by displaying them in full without masking.

### Weekly Task 4 - Collatz (`collatz.py`)
Takes a positive integer from the user and applies the Collatz sequence: if the number is even, divide by 2; if odd, multiply by 3 and add 1. Repeats until the value reaches 1, printing each step along the way.

### Weekly Task 5 - Weekday (`weekday.py`)
Uses Python's `datetime` module to check the current day of the week. Prints a message indicating whether today is a weekday (Monday-Friday) or a weekend (Saturday-Sunday). Requires no user input.

### Weekly Task 6 - Square Root (`squareroot.py`)
Takes a positive floating-point number form the user and approximates its square root using the Babylonian method (also known as Heron's method), without using built-in functions like `math.sqrt`. Iterates until the difference between estimates is less than 0.00001, then prints the result rounded to 1 decimal place. Includes a check to reject negative numbers.

### Weekly Task 7 - Count E's (`week07-es.py`)
Reads a `.txt` file supplied as a command-line arguement and counts all occurences of the letter `e` (both uppercase and lowercase). Includes error handling for: no arguement provided, non-`.txt` files, and files that do not exist. A sample test file (`week07-test.txt`) is included for testing.

### Weekly Task 8 - Plot Task (`week08-plottask.py`)
Uses `numpy` and `matplotlib` to display two plots on a single set of axes:
- A histogram of 1000 values form a normal distribution  (mean = 5, standard deviation = 2)
- A line plot of the function h(x) =  x³ over the range 0 to 10

The plot includes a title, axis labels, legend, and grid. The output is saved as `week08-plot.png`.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `datetime` | Weekday detection (Weekly task 5) |
| `sys` / `os` | Command-line arguements and file valdation (Weekly task 7) |
| `numpy` | Generating normal distribution data (Weekly task 8) |
| `matplotlib` | Data visualisation and plot output (Weekly task 8) |

## How to Run
### Prerequisites
- Python 3 installed
- Install required libraries:
```bash
pip install matplotlib numpy
```

### Running Individual tasks
```bash
python helloworld.py
python bank.py
python accounts.py
python collatz.py
python weekday.py
python squareroot.py
```

**Weekly task 7 requires a filename as a command-line arguement:**
```bash
python week07-es.py week07-test.txt
```

**Weekly task 8 will display a plot window and save `week08-plot.png`:**
```bash
python week08-plottask.py
```

## Note on Repository History
The weekly tasks were originally completed in a seperate repository during the module. Once the correct submission structure was clarified, the work was reorganised into this repository to meet the assessment requirments.

Original repository: https://github.com/aiswarialajan124-png/programming_scripting-pands-mywork

## References
The following resources were used across the weekly tasks:
- [Python Documentation - Input/Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Documentation - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Datetime Module](https://docs.python.org/3/library/datetime.html)
- [Python Math Module](https://docs.python.org/3/library/math.html#math.sqrt)
- [Matplotlib Documentation](https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py)
- [Real Python — Square Root Methods](https://realpython.com/python-square-root-function/)
- [OEIS — Collatz Sequence](https://oeis.org/A006577)

## Author
Aiswaria Lajan

