# ==============================
# DATA ANALYZER AND TRANSFORMER
# ==============================

dataset = []
is_2d = False

# Global variable
dataset_summary = {}


# -------------------------------
# Input Data
# -------------------------------
def input_data():
    """Input 1D or 2D dataset."""

    global dataset, is_2d

    print("\n1. Enter 1D List")
    print("2. Enter 2D List")
    print("3. Use Sample Data")

    choice = input("Enter choice: ")

    if choice == "1":
        dataset = list(map(int, input("Enter numbers separated by spaces: ").split()))
        is_2d = False

    elif choice == "2":

        rows = int(input("Enter number of rows: "))
        dataset = []

        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            dataset.append(row)

        is_2d = True

    elif choice == "3":

        print("\n1. Sample 1D")
        print("2. Sample 2D")

        sample = input("Choice: ")

        if sample == "1":
            dataset = [34, 12, 56, 78, 43, 21, 90]
            is_2d = False

        else:
            dataset = [
                [12, 45, 67],
                [90, 11, 33],
                [25, 88, 14]
            ]
            is_2d = True

    print("Data Stored Successfully.")


# -------------------------------
# Display 2D Grid
# -------------------------------
def display_grid():
    """Display 2D list in grid."""

    if is_2d:
        print("\n2D Dataset")
        for row in dataset:
            for value in row:
                print(f"{value:5}", end="")
            print()
    else:
        print(dataset)


# -------------------------------
# Flatten Data
# -------------------------------
def flatten_data():
    """Convert 2D list into 1D."""

    if is_2d:
        return [item for row in dataset for item in row]
    return dataset


# -------------------------------
# Built-in Functions
# -------------------------------
def display_summary():
    """Display summary using built-in functions."""

    global dataset_summary

    data = flatten_data()

    if len(data) == 0:
        print("No data available.")
        return

    dataset_summary = {
        "Total Elements": len(data),
        "Sum": sum(data),
        "Minimum": min(data),
        "Maximum": max(data),
        "Average": round(sum(data) / len(data), 2)
    }

    print("\nDataset Summary")
    print("----------------")
    for key, value in dataset_summary.items():
        print(f"{key}: {value}")


# -------------------------------
# Average
# -------------------------------
def calculate_average(data):
    """Return average."""

    return sum(data) / len(data)


# -------------------------------
# Duplicates
# -------------------------------
def find_duplicates(data):
    """Find duplicate values."""

    duplicate = []

    for i in data:
        if data.count(i) > 1 and i not in duplicate:
            duplicate.append(i)

    return duplicate


# -------------------------------
# Unique Values
# -------------------------------
def unique_values(data):
    """Return unique values."""

    return list(set(data))


# -------------------------------
# *args Example
# -------------------------------
def show_args(*args):
    """Display multiple values using *args."""

    print("\nUsing *args")

    for value in args:
        print(value)


# -------------------------------
# **kwargs Example
# -------------------------------
def show_kwargs(**kwargs):
    """Display dataset information."""

    print("\nDataset Characteristics")

    for key, value in kwargs.items():
        print(f"{key} : {value}")


# -------------------------------
# Recursive Factorial
# -------------------------------
def factorial(n):
    """Calculate factorial recursively."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# -------------------------------
# Lambda Function
# -------------------------------
def filter_data():
    """Filter data using lambda."""

    data = flatten_data()

    value = int(input("Enter threshold: "))

    result = list(filter(lambda x: x >= value, data))

    print("Filtered Data:", result)


# -------------------------------
# Lambda with Map
# -------------------------------
def square_data():
    """Square every element."""

    data = flatten_data()

    result = list(map(lambda x: x * x, data))

    print("Squared Data")
    print(result)


# -------------------------------
# Return Multiple Values
# -------------------------------
def statistics(data):
    """Return multiple values."""

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average


# -------------------------------
# Sorting
# -------------------------------
def sort_data():
    """Sort data."""

    global dataset

    if is_2d:

        print("\nOriginal")
        display_grid()

        sorted_rows = sorted(dataset, key=lambda row: sum(row))

        print("\nSorted Rows (using sorted())")

        for row in sorted_rows:
            print(row)

    else:

        print("\n1. Ascending")
        print("2. Descending")

        ch = input("Choice: ")

        if ch == "1":
            dataset.sort()
        else:
            dataset.sort(reverse=True)

        print(dataset)


# -------------------------------
# Function Documentation
# -------------------------------
def function_docs():
    """Display __doc__."""

    print("\nFunction Descriptions")

    print(input_data.__doc__)
    print(display_summary.__doc__)
    print(factorial.__doc__)
    print(filter_data.__doc__)
    print(sort_data.__doc__)
    print(statistics.__doc__)


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n==============================")
    print("DATA ANALYZER & TRANSFORMER")
    print("==============================")

    print("1. Input Data")
    print("2. Display Data")
    print("3. Built-in Function Summary")
    print("4. Calculate Average")
    print("5. Find Duplicates")
    print("6. Display Unique Values")
    print("7. *args Example")
    print("8. **kwargs Example")
    print("9. Display Function Documentation")
    print("10. Factorial (Recursion)")
    print("11. Filter Data (Lambda)")
    print("12. Square Data (Map + Lambda)")
    print("13. Dataset Statistics")
    print("14. Sort Data")
    print("15. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        display_grid()

    elif choice == "3":
        display_summary()

    elif choice == "4":

        data = flatten_data()

        print("Average =", round(calculate_average(data), 2))

    elif choice == "5":

        data = flatten_data()

        print("Duplicates =", find_duplicates(data))

    elif choice == "6":

        data = flatten_data()

        print("Unique Values =", unique_values(data))

    elif choice == "7":

        show_args(10, 20, 30, 40, 50)

    elif choice == "8":

        data = flatten_data()

        show_kwargs(
            Total_Elements=len(data),
            Minimum=min(data),
            Maximum=max(data),
            Average=round(sum(data) / len(data), 2)
        )

    elif choice == "9":

        function_docs()

    elif choice == "10":

        num = int(input("Enter Number: "))
        print("Factorial =", factorial(num))

    elif choice == "11":

        filter_data()

    elif choice == "12":

        square_data()

    elif choice == "13":

        data = flatten_data()

        minimum, maximum, total, average = statistics(data)

        print("\nStatistics")
        print("Minimum :", minimum)
        print("Maximum :", maximum)
        print("Sum :", total)
        print("Average :", round(average, 2))

    elif choice == "14":

        sort_data()

    elif choice == "15":

        print("Thank You!")
        break

    else:

        print("Invalid Choice.")
