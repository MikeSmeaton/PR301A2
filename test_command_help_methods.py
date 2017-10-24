from main import main
import sys

"""
>>> main.py(sys.argv[1:])
>>> help quit
Quits the program. Takes no parameters.
>>> help open
Opens a file and saves it's data to the database. Takes a file path as parameter, which must end in .txt or .csv or .xlsx.
>>> help get

>>> help pie

>>> help line
Draws a scatter plot of Sales vs Age. Takes no parameters.
>>> help linegraph
Draws a scatter plot of Age vs Salary. Takes no parameters.
>>> help scatter

>>> help reload
Clears the current database of all data. Takes no parameters.
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
