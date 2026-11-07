"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    count=0
    v="AEIOUaeiou"
    for c in text:
        if c in v:
            count+=1
    return count 
    raise NotImplementedError("Part 1: implement vowel_count")


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    return [v for v in list if len(v)==2 ]
    raise NotImplementedError("Part 2: implement short_lists")


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    result=[]
    for i in items:
        if len(i)==2:
            r=[]
            if i[0]>i[1]:
                r.append(i[1])
                r.append(i[0])
            result.append(r)
        result.append(i)
    return result
    raise NotImplementedError("Part 3: implement ascending_pairs")


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    cents=first.cents+second.cents
    dollars=first.dollars+second.dollars
    cents=cents % 100
    return data.Price(dollars,cents)
    raise NotImplementedError("Part 4: implement add_prices")


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 6: implement books_by_author")


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 7: implement circle_bound")


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 8: implement below_pay_average")
