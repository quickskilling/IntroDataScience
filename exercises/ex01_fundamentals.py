# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pyzmq",
# ]
# ///

import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise 1: Python Fundamentals 🐍

    **Practice what you learned!** Complete these exercises to build your Python skills.

    **Estimated time:** 30 minutes

    **Instructions:**
    - Read each TODO comment
    - Write code to complete the task
    - Run the cell to check your answer
    - Solutions are available in `solutions/ex01_fundamentals.py`

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-1: Variables and Basic Operations
    """)
    return


@app.cell
def _():
    # TODO: Create variables for a person's information
    # - name: your name as a string
    # - age: your age as an integer
    # - height: your height in meters as a float
    # - is_student: whether you're a student (True or False)

    name = "YourName"  # Replace with your name
    age = 0  # Replace with your age
    height = 0.0  # Replace with your height
    is_student = False  # Change if needed

    # Print them out
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}m")
    print(f"Student: {is_student}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-2: Math Operations
    """)
    return


@app.cell
def _():
    # TODO: Calculate the following:
    # 1. Sum of 45 and 67
    # 2. Product of 12 and 8
    # 3. 100 divided by 7 (keep decimals)
    # 4. 2 to the power of 10

    sum_result = 0  # TODO
    product = 0  # TODO
    division = 0  # TODO
    power = 0  # TODO

    print(f"Sum: {sum_result}")
    print(f"Product: {product}")
    print(f"Division: {division}")
    print(f"Power: {power}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-3: Working with Lists
    """)
    return


@app.cell
def _():
    # TODO: Create a list of your 5 favorite foods
    favorite_foods = []  # Add your foods here

    # TODO: Print the first food
    print(f"First food: ???")  # Fix this line

    # TODO: Print the last food
    print(f"Last food: ???")  # Fix this line

    # TODO: Add another food to the list
    # (use the append method)

    # TODO: Print the length of the list
    print(f"Number of foods: ???")  # Fix this line
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-4: Dictionary Practice
    """)
    return


@app.cell
def _():
    # TODO: Create a dictionary representing a book with:
    # - title: book title (string)
    # - author: author name (string)
    # - year: publication year (integer)
    # - pages: number of pages (integer)

    book = {
        # Add your key-value pairs here
    }

    # TODO: Print the book title and author
    print(f"Title: ???")  # Fix this line
    print(f"Author: ???")  # Fix this line

    # TODO: Add a new key "genre" with a value

    # TODO: Update the year to a different value

    print("\nUpdated book:", book)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-5: If/Else Logic
    """)
    return


@app.cell
def _():
    # TODO: Write code that checks a temperature and prints a message:
    # - If temp > 30: "It's hot!"
    # - If temp > 20: "It's warm"
    # - If temp > 10: "It's cool"
    # - Otherwise: "It's cold!"

    temperature = 25  # Try changing this value

    # Write your if/elif/else statements here

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-6: For Loop Practice
    """)
    return


@app.cell
def _():
    # TODO: Loop through this list and print each number multiplied by 3
    numbers = [2, 4, 6, 8, 10]

    # Write your loop here

    return


@app.cell
def _():
    # TODO: Use a for loop to calculate the sum of all numbers from 1 to 100
    total = 0

    # Write your loop here

    print(f"Sum of 1 to 100: {total}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-7: List Comprehension
    """)
    return


@app.cell
def _():
    # TODO: Create a list of squares for numbers 1 through 10
    # Use a list comprehension!

    squares = []  # Use list comprehension here

    print(f"Squares: {squares}")
    # Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    return


@app.cell
def _():
    # TODO: Create a list of only even numbers from this list
    # Use a list comprehension with a condition!

    all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    even_numbers = []  # Use list comprehension here

    print(f"Even numbers: {even_numbers}")
    # Expected: [2, 4, 6, 8, 10, 12]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-8: Function Basics
    """)
    return


@app.cell
def _():
    # TODO: Write a function that takes a name and returns a greeting
    # Example: greet("Alice") should return "Hello, Alice!"

    def greet(name):
        pass  # Replace with your code

    # Test your function
    print(greet("Alice"))
    print(greet("Bob"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-9: Function with Calculation
    """)
    return


@app.cell
def _():
    # TODO: Write a function that calculates the area of a rectangle
    # It should take width and height as parameters
    # It should return width * height

    def calculate_area(width, height):
        pass  # Replace with your code

    # Test your function
    area1 = calculate_area(5, 10)
    area2 = calculate_area(7, 3)

    print(f"Area 1: {area1}")  # Should be 50
    print(f"Area 2: {area2}")  # Should be 21
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1-10: Putting It Together
    """)
    return


@app.cell
def _():
    # TODO: Complete this function that analyzes a list of numbers
    # It should return a dictionary with:
    # - "count": number of items
    # - "sum": sum of all items
    # - "average": average of all items
    # - "max": maximum value
    # - "min": minimum value

    def analyze_numbers(numbers):
        # Write your code here
        result = {
            "count": 0,
            "sum": 0,
            "average": 0,
            "max": 0,
            "min": 0
        }
        return result

    # Test your function
    test_numbers = [10, 20, 30, 40, 50]
    analysis = analyze_numbers(test_numbers)

    print("Analysis of [10, 20, 30, 40, 50]:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")

    # Expected output:
    # count: 5
    # sum: 150
    # average: 30.0
    # max: 50
    # min: 10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Great Job!

    You've completed the fundamentals exercises!

    **What's next?**
    - Check your solutions against `solutions/ex01_fundamentals.py`
    - Move on to Exercise 2: Wrangle and Plot

    **Tips:**
    - If you got stuck, that's normal! Check the solutions and learn from them
    - Try modifying the exercises with your own data
    - Python gets easier with practice
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
