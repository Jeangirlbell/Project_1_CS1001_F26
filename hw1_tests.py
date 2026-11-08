"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).
"""

import unittest

import data
import hw1
import math


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("Apple"), 2)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [2, 3], [], [4, 5, 6], [7, 8]]), [[2, 3], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [], [1, 2, 3]]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[9, 2], [3, 1, 2], [5, 5]]), [[2, 9], [3, 1, 2], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual(hw1.ascending_pairs([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(3, 10), data.Price(2, 11)), data.Price(5, 21))

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(3, 75), data.Price(2, 50)), data.Price(6, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(2, 3), data.Point(7, 8))), 25)

    def test_rectangle_area_negative_coordinates(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-4, -5), data.Point(-1, -2))), 9)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        books = [data.Book(["A", "B"], "name1"), data.Book(["A", "C"], "name2")]
        self.assertEqual(hw1.books_by_author("A", books), [data.Book(["A", "B"], "name1"), data.Book(["A", "C"], "name2")])

    def test_books_by_author_no_matches(self):
        books = [data.Book(["A", "B"], "name1"), data.Book(["A", "C"], "name2")]
        self.assertEqual(hw1.books_by_author("D", books), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rect = data.Rectangle(data.Point(2, 3), data.Point(6, 7))
        cir = hw1.circle_bound(rect)
        self.assertEqual(cir.center, data.Point(4, 5))
        self.assertAlmostEqual(cir.radius, math.sqrt(8))

    def test_circle_bound_non_square_rectangle(self):
        rect = data.Rectangle(data.Point(0, 0), data.Point(6, 8))
        cir = hw1.circle_bound(rect)
        self.assertEqual(cir.center, data.Point(3, 4))
        self.assertAlmostEqual(cir.radius, 5)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        emp1 = data.Employee("Alice", 10.0)  
        emp2 = data.Employee("Bob", 30.0)   
        emp3 = data.Employee("Charlie", 20.0) 
        emp4 = data.Employee("David", 15.0) 
        employees = [emp1, emp2, emp3, emp4]
        self.assertEqual(hw1.below_pay_average(employees), ["Alice", "David"])

    def test_below_pay_average_equal_pay(self):
        emp1 = data.Employee("A", 15.0)
        emp2 = data.Employee("B", 15.0)
        self.assertEqual(hw1.below_pay_average([emp1, emp2]), [])


if __name__ == '__main__':
    unittest.main()
