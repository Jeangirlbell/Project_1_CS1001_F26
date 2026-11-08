"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
import math

# Part 1: vowel_count
def vowel_count(text: str) -> int:
    """Counts the number of vowels (case-insensitive) in the given text string."""
    count = 0
    v = "AEIOUaeiou"
    for c in text:
        if c in v:
            count += 1
    return count 


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    """Returns a new list containing only the sublists of length 2 from the input."""
    return [v for v in items if len(v) == 2]


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    """Returns a new list where any sublist of length 2 has its elements sorted in ascending order."""
    result = []
    for i in items:
        if len(i) == 2:
            if i[0] > i[1]:
                result.append([i[1], i[0]])
            else:
                result.append([i[0], i[1]])
        else:
            result.append(i)
    return result


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    """Adds two Price objects together, handling cent overflow into dollars."""
    total_cents = first.cents + second.cents
    total_dollars = first.dollars + second.dollars + total_cents // 100
    remaining_cents = total_cents % 100
    return data.Price(total_dollars, remaining_cents)


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    """Calculates and returns the area of a given Rectangle."""
    length = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    width = abs(rectangle.bottom_right.y - rectangle.top_left.y)
    return length * width


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    """Returns a list of books written or co-authored by the specified author."""
    result = []
    for b in books:
        if author in b.authors:
            result.append(b)
    return result


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    """Computes the smallest bounding Circle that encloses the given Rectangle."""
    center = data.Point(
        (rectangle.top_left.x + rectangle.bottom_right.x) / 2,
        (rectangle.bottom_right.y + rectangle.top_left.y) / 2
    )
    radius = math.sqrt((rectangle.top_left.x - center.x) ** 2 + (rectangle.top_left.y - center.y) ** 2)
    return data.Circle(center, radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    """Returns a list of names of employees whose pay rate is strictly below the average pay rate."""
    if not employees:
        return []
    total_pay = 0.0
    result = []
    for emp in employees:
        total_pay += emp.pay_rate
    avg = total_pay / len(employees)
    for empl in employees:
        if empl.pay_rate < avg:
            result.append(empl.name)
    return result
