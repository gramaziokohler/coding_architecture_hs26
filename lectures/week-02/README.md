# Coding Architecture I: HS26

## Week 02 - Lists, Sets and Relatives

![Course Banner](/_static/cai-banner_hs26.jpg)

## Table of Contents

- [Overview](#overview)
- [Slides](#slides)
- [Syncing your files](#syncing-your-files)
- [Roadmap: How to become a computational Designer](#roadmap-how-to-become-a-computational-designer)
- [Lists](#lists)
  - [Single vs Multiple values](#single-vs-multiple-values)
  - [List Operations](#list-operations)
  - [List indexing](#list-indexing)
- [Sets](#sets)
- [Dictionaries](#dictionaries)
- [Loops, Lists and Friends](#loops-lists-and-friends)
- [Code Examples](#code-examples)
- [Micro exercises](#micro-exercises)

## Overview

In this week’s lecture, we’ll start with a quick demonstration on how to sync your files from GitHub and set up your development environment in VSCode. Then, we’ll explore the **Roadmap to Becoming a Computational Designer**, outlining key skills and concepts, from basic programming to advanced computational techniques.

In the second part, we’ll focus on lists, sets, and other data structures, covering how to create, manipulate, and differentiate between single values and collections. You’ll learn how these concepts are applied in programming to manage and process multiple pieces of data efficiently.

Next, we’ll apply these techniques to geometric objects, demonstrating how loops and lists can be used to generate and manipulate geometries in 3D space, connecting coding techniques directly to design tasks in Rhino and Grasshopper.

We’ll conclude with a feedback session where you can ask questions and discuss any challenges from the lecture or assignments.

>**Learning Goals:** You should understand and use collections of values in Python and apply them to create geometric objects.

## Slides

[![Slides](../../_static/slides.png)](https://docs.google.com/presentation/d/1Z-dv_SOL42dn2PppM_ovUGKu_SlZPNxEsMK8zdFrEG0/edit?usp=drive_link)

<div style="display: flex; justify-content: center; align-items: center; height: 1vh;">
    <p style="font-size: 75%;">
        ↑ click to open ↑
    </p>
</div>

## Syncing your files

To synchronize the content of this week's lecture to your computer, use VS Code and click the "Sync" button in the bottom left corner. 

## Roadmap: How to become a computational Designer

See [here](/roadmap/README.md) for more information about the **Roadmap: becoming a computational designer**, including an explainer video.

[![Roadmap](/_static/roadmap-small.png)](/roadmap/roadmap.png)

## Data + Algorithms = Programs

We start off from the definition that we explored in class last week: programs are built using data and algorithms.


## Lists

Lists are a fundamental data structure in Python, designed to hold multiple values within a single container. You can think of lists as ordered collections of items, where each item can be of any type — numbers, strings, or even other lists. Analogously, a list can be compared to a physical folder containing multiple sheets of paper, where each sheet represents a data item. On each "sheet," you might have anything—text, numbers, diagrams, or even other folders (nested lists).

*Key Characteristics of Lists:* 

- Order: Lists maintain the order of elements as they are added.
- Mutability: Lists are mutable, meaning the contents of a list can be changed after creation (you can add, remove, or modify elements).
- Duplication: Lists allow for duplicate items, meaning the same value can appear more than once.

In computational design, lists are almost essential for maintaining ordered collections of geometric objects, such as points in space, vertices of a mesh, or a sequence of transformations.

### Single vs Multiple values 

```python
# ----------------------------------------
# ----------- Lists vs Values ------------

# a single value
my_value = 42

# a list of integers
my_first_list = [3, 2, 9]

# a list of numbers with and without decimals
my_list_1 = [42, 1.618, 3.14]

# Creating a list with string items
my_list_2 = ["abc", "xyz"]

# A mixed type list (this is specific to Python)
mixed_list = [42, "phi", "pi"]
```

### List Operations

```python
# -----------------------------------
# ------ Operations with Lists ------

# Append: Adds an item to the end of the list
my_first_list.append(4)
print(my_first_list)                # Output: [3, 2, 9, 4]

# Pop: Removes an item at the given index
popped_item = my_first_list.pop(2)  # Removes the item at index 2.
print(my_first_list)                # Output: [3, 2, 4]

# Insert: Inserts an item at a specified position
my_first_list.insert(1, 5)          # Inserts 5 at index 1
print(my_first_list)                # Output: [3, 5, 2, 4]

# Sorting the list
my_first_list.sort()
print(my_first_list)                # Output: [2, 3, 4, 5]

# Getting the length of the list
print(len(my_first_list))           # Output: 4

# Finding the minimum value
print(min(my_first_list))           # Output: 2

# Finding the maximum value
print(max(my_first_list))           # Output: 5

# Calculating the sum of elements
print(sum(my_first_list))           # Output: 14

# Zipping two lists (combining elements from two lists into one)
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
zipped_list = zip(list_a, list_b)
for item in zipped_list:
    print(item)                     # Output: (1, 'a'), (2, 'b'), (3, 'c')

# -------------------------------------
# ------------- List Help -------------

# Getting help on list methods
help(my_first_list)

# Getting the type of the object
print(type(my_first_list))          # Output: <class 'list'>

# Viewing all attributes and methods of list object
print(dir(my_first_list))
```

### List Indexing

```python
# ------------------------------
# --------- Indexing -----------

# Indexes start at 0 for the first element. Negative indexes start from the end with -1 being the last element.

values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Accessing the last item
print(values[-1])   # Output: 100

# Slicing from index 0 to 3 (includes index 0 but excludes index 4)
print(values[0:4])  # Output: [10, 20, 30, 40]

# Slicing from index 4 to the end of the list
print(values[4:])   # Output: [50, 60, 70, 80, 90, 100]

# Accessing every second item
print(values[::2])  # Output: [10, 30, 50, 70, 90]
```

## Sets

Sets are another data structure in Python, similar to lists, but with some important differences. A set is an **unordered collection** of **unique items**. This means that unlike lists, sets do not maintain the order of the elements, and they automatically remove duplicate entries.

Because of these characteristics, sets are particularly useful when you need to track a collection of distinct items, or when you need to perform operations such as unions, intersections, or differences between collections.

Differences between Sets and Lists:
- Order: Lists maintain the order of elements; sets do not.
- Duplicates: Lists can contain duplicate elements; sets automatically remove duplicates.
- Mutability: Both lists and sets are mutable, meaning you can add or remove items. Set elements must be hashable (e.g., numbers and strings); lists and dictionaries cannot be set elements.

<!-- > Mutability: Mutability refers to the ability of an object to be modified after it has been created. In programming, mutable objects can have their state or content changed, while immutable objects cannot be altered once created -->

We would use sets over lists when we need to work with unique elements and don't care about the order of the items. Sets are ideal for tasks like eliminating duplicates from a collection (such as intersection points), checking membership quickly, or performing mathematical operations like boolean union, intersection, and difference. If order matters or duplicates are necessary, then lists would be more appropriate.

### Set Operations

```python
# -------------------------------------
# --------------- Sets ----------------

# Creating a set with integer elements
my_set = {1, 2, 3, 3, 4}
print(my_set)                # Output: {1, 2, 3, 4}

# Adding an item to the set
my_set.add(5)
print(my_set)                # Output: {1, 2, 3, 4, 5}

# Removing an item from the set
my_set.remove(2)
print(my_set)                # Output: {1, 3, 4, 5}

# Checking membership
print(3 in my_set)           # Output: True
print(6 in my_set)           # Output: False

# -------------------------------------
# ---------- Set Operations -----------

# Union: Combines two sets into one, removing duplicates
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)             # Output: {1, 2, 3, 4, 5}

# Intersection: Returns the common elements between two sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)      # Output: {3}

# Difference: Returns the elements present in set_a but not in set_b
difference_set = set_a.difference(set_b)
print(difference_set)        # Output: {1, 2}

# Symmetric Difference: Returns elements that are in either set, but not in both
symmetric_difference = set_a.symmetric_difference(set_b)
print(symmetric_difference)  # Output: {1, 2, 4, 5}
```

## Dictionaries

Dictionaries are another important data structure in Python, designed to store data in *key-value* pairs. Unlike lists, which are indexed by position, dictionaries are indexed by *unique keys*, which must be hashable (e.g. strings and numbers). You can use dictionaries when you need to store data that should be easily accessed through a *meaningful identifier* rather than a *positional index*.

Think of a dictionary as a real-world dictionary: just as *words* point to their *definitions*, in Python dictionaries, *keys* map to corresponding *values*. This makes dictionaries incredibly useful for storing and retrieving data based on a specific identifier or label.

### Dictionary Operations

```python
# -----------------------------------------
# -------- Dictionary Operations ----------

# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values by key
print(person["name"])   # Output: Alice

# Adding or updating key-value pairs
person["age"] = 31
person["profession"] = "Architect"

# Removing a key-value pair
person.pop("city")

# Checking if a key exists in the dictionary
if "age" in person:
    print("Age is available")

# Iterating over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Accessing all keys
print(person.keys())    # Output: dict_keys(['name', 'age', 'profession'])

# Accessing all values
print(person.values())  # Output: dict_values(['Alice', 31, 'Architect'])
```

## Loops, Lists and Friends

Loops are a fundamental tool for interacting with lists and other datastructures in Python. When we need to perform operations on a large number of objects, loops become essential. In other words, loops enable us to access, modify, and process multiple values stored in a list without manually writing repetitive code for each element.

For instance, you can loop through a list of architectural elements and perform some transformation on them, or you can loop through a list of numbers and apply mathematical operations to them.

```python
# --------------------------------------
# ------- Looping through Lists --------

# Looping through a list and printing items
people = ["alberti", "durand", "gropius"]
for person in people:
    print(person)           # Output: alberti, durand, gropius

# when iterating over a list of numbers, the temporary variable is usually replaced with "i"
my_values = [1, 2, 3, 4, 5]
for i in my_values:
    print(i)                # Output: 1, 2, 3, 4, 5

# --------------------------------------
# -------- Looping through Sets --------

my_set = {"Apple", "Banana", "Cherry"}

for element in my_set:
    print(element)

# Note here that when we work with set, the order of the elements can vary!

# The output can be: Banana, Cherry, Apple
# But it can also be: Cherry, Apple, Banana
# Or any other order

# --------------------------------------
# ---- Looping through Dictionaries ----

# Looping through dictionary keys
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)              # Output: name, age, city

# Looping through dictionary values
for value in person.values():
    print(value)            # Output: John, 30, New York

# Looping through both keys and values
for key, value in person.items():
    print(key, ":", value)  # Output: name: John, age: 30, city: New York
```

### Loops in Detail

There are different types of loops in Python, and each offers a way to repeat a
block of code multiple times. Here, we’ll cover the most common loops in
Python (`for` and `while` loops) and how they can be used to interact with
lists and other sequences.

```python
# --------------------------------
# --------- For Loops ------------

# A for loop iterates over a sequence (like a list, tuple, string, or range).

# Basic For Loop example
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)          # Output: 1, 2, 3, 4, 5

# Looping through a string
word = "hello"
for letter in word:
    print(letter)       # Output: h, e, l, l, o

# Using range() in a for loop to create an iteration of n numbers
for i in range(3):
    print(i)            # Output: 0, 1, 2

# For loop with a start, stop, and step using range()
for i in range(1, 10, 2):
    print(i)            # Output: 1, 3, 5, 7, 9

# --------------------------------
# ------- Nested Loops -----------

# You can place loops inside loops, known as nested loops.
# Nested For Loop example
for i in range(3):      # Outer loop
    for j in range(2):  # Inner loop
        print(i, j)     # Output: (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)

# -------------------------------
# --------- While Loops ----------

# A while loop repeats as long as a condition is true.
# Basic While Loop example
count = 0
while count < 5:
    print(count)        # Output: 0, 1, 2, 3, 4
    count += 1
```

### More Loop Operations

```python
# --------------------------------
# --- Breaking Out of Loops ------

# The `break` statement can be used to stop the loop before it finishes.
for i in range(10):
    if i == 5:
        break                # Stops the loop when i == 5
    print(i)                 # Output: 0, 1, 2, 3, 4

# --------------------------------
# --- Skipping Iterations --------

# The `continue` statement skips the current iteration and moves to the next one.
for i in range(5):
    if i == 3:
        continue             # Skips the iteration where i == 3
    print(i)                 # Output: 0, 1, 2, 4

# --------------------------------
# ------ Else in Loops -----------

# Python loops can have an else clause, which executes after the loop ends.
# Notice that if you use `break` in the loop, the else clause will not execute.
for i in range(3):
    print(i)                 # Output: 0, 1, 2
else:
    print("Loop completed")  # Output: Loop completed.

# --------------------------------
# --------- Infinite Loops -------

# Be careful to avoid creating infinite loops.
# A loop that never terminates:
# while True:
#     print("This is an infinite loop")  # Uncommenting this will create an infinite loop
```

## Geometry

Python has no geometry types included, so we use [COMPAS](https://compas.dev) for this purpose.
COMPAS is a Python library for computational research and digital fabrication in architecture,
engineering, and design. It provides a toolbox for working with geometry and data structures,
and many more things.

```python
# --------------------------------
# ------------ Points ------------

from compas.geometry import Point

pt = Point(1, 0, 0)

# --------------------------------
# ------------ Boxes -------------

from compas.geometry import Box

box = Box(1, 2, 2)

# --------------------------------
# ---- Visualization in Rhino ----

from compas_rhino.conversions import point_to_rhino
from compas_rhino.conversions import box_to_rhino

a = point_to_rhino(pt)
b = box_to_rhino(box)

# --------------------------------
# --------- Point grid -----------

from compas.geometry import Point

points = []
for x in range(10):
    for y in range(15):
        point = Point(x, y, 0)
        points.append(point)
```
## Code examples

The following files are useful to follow the lecture content:

- [Starting point for exercises](./examples/00_for_exercises_hs26.gh)
- [Lists and Loops](./examples/01_lists_and_loops_hs26.gh)
- [Sets and Duplicates](./examples/02_sets_and_duplicates_hs26.gh)
- [Strings](./examples/03_strings_hs26.gh)


## Micro exercises

The following are very simple micro exercises that you can go through to practice some of the concepts of the current lecture. Each of them should not take more than 5 minutes to complete.

1. In a "Python 3 Script" component with two input parameters `x` and `y`, with **item access**, write a program that sums both input parameters and prints the output.

2. In a "Python 3 Script" component with one input parameter `numbers` with **list access**, write a program that sums all numbers and prints the output.

3. In the previous component, print the max and min values of the list.

4. In the previous component, print the median value of the list. You can assume that the list will always have an odd number of elements.

5. In the previous component, print the average of all values of the list.

6. In the previous component, print the list sorted in ascending order. Then print the list sorted in descending order.

7. In a "Python 3 Script" component with two input parameters called `first_list` and `second_list`, both with **list access**, write a program that prints the pairs of elements of each list, eg. the first element of `first_list` with the first of `second_list`, then second element of `first_list` with the second of `second_list`, and so on.

8. In a "Python 3 Script" component, define two variables `a` and `b` with two different values, eg. `42` and `23` respectively. Then, swap the values of the two variables, so that `a` becomes `23` and `b` becomes `42`. Print the values of `a` and `b` before and after the swap.

9. In a "Python 3 Script" component, define a variable called `values` and assign an empty list to it. Then append the values 0 to 9 to the list. Print the list.

10. In a "Python 3 Script" component, define a variable called `duplicates` and assign a list containing duplicates, eg. `[20, 20, 5, 32, 66, 20, 32, 9]`. Then, write a program that removes all duplicates from the list. Print the list before and after the removal.

11. In a "Python 3 Script" component with one input parameter `x` with **item access** connected with a number slider of decimal values, write a program that rounds the value up to 2 decimal places. Print the output.

<details>
  <summary><b>Solutions</b></summary>


1. 

```python
print(x + y)
```

2. 
    
```python
print(sum(numbers))
```

3. 

```python
print(max(numbers))
print(min(numbers))
```

4.
    
```python
numbers.sort()
median_index = int(len(numbers) / 2)
print(numbers[median_index])
```

or 

```python
median_index = len(numbers) // 2
print(sorted(numbers)[median_index])
```

or if you want to handle also the case of list with even number of elements:

```python
numbers.sort()
median_index = len(numbers) // 2
if len(numbers) % 2 == 0:
    print((numbers[median_index - 1] + numbers[median_index]) / 2)
else:
    print(numbers[median_index])
```

5. 
    
```python
print(sum(numbers) / len(numbers))
```

6. 
    
```python
print(sorted(numbers))
print(sorted(numbers, reverse=True))
```


7. 

```python
for i, j in zip(first_list, second_list):
    print(i, j)
```

or 

```python
for i in range(len(first_list)):
    print(first_list[i], second_list[i])
```

8. 

```python
a = 42
b = 23
print(a, b)
a, b = b, a
print(a, b)
```

9. 

```python
values = []
for i in range(10):
    values.append(i)
print(values)
```

or 

```python
values = list(range(10))
print(values)
```

10. 
    
```python
duplicates = [20, 20, 5, 32, 66, 20, 32, 9]
print(duplicates)
de_duplicated = list(set(duplicates))
print(de_duplicated)  # but notice that order of elements might have changed!
```

11.
    
```python
print(round(x, 2))
```
</details>

---

<p align="middle">
<img src="../../_static/gkr-logo.png" alt="Gramazio Kohler Research" height="150"/>
</p>
