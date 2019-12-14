# src/Days/Day4.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day4Puzzle1(Puzzle):
    """
    Day4 Puzzle1 class
    """
    def solve(self):
        print("Day4 - Puzzle1")
        input_range = self.input.split('-')

        no_of_passwords = 0
        for number in range(int(input_range[0]), int(input_range[1])):
            if meets_criteria(number):
                no_of_passwords += 1

        print("Solution for Day4 Puzzle1: {}".format(no_of_passwords))


class Day4Puzzle2(Puzzle):
    """
    Day4 Puzzle2 class
    """
    def solve(self):
        print("Day4 - Puzzle1")
        input_range = self.input.split('-')

        no_of_passwords = 0
        for number in range(int(input_range[0]), int(input_range[1])):
            if meets_criteria(number) and meets_criteria_extended(number):
                no_of_passwords += 1

        print("Solution for Day4 Puzzle2: {}".format(no_of_passwords))


def meets_criteria(number=None):
    numbers = list(map(int, str(number)))

    if len(numbers) != 6:       # It is a six-digit number.
        return False

    for index in range(0, len(numbers)-1):
        if numbers[index+1] - numbers[index] < 0:  # decreasing False
            return False

    adj_digits = False
    for index in range(0, len(numbers)-1):
        if numbers[index+1] == numbers[index]:  # at least one double
            adj_digits = True

    if not adj_digits:
        return False

    return True


def meets_criteria_extended(number=None):
    numbers = list(map(int, str(number)))

    counts = {}
    for index in range(0, len(numbers)-1):
        str_nmr = str(numbers[index])
        if numbers[index+1] == numbers[index]:  # at least one double
            if str_nmr in counts:
                counts[str_nmr] += 1
            else:
                counts[str_nmr] = 2
        else:
            if str_nmr not in counts:
                counts[str_nmr] = 1

    for number in counts:
        if counts.get(number) == 2:  # at least a consecutive double.
            return True

    return False


class Day4(Day):
    """
    Day4 Class with 2 puzzles.
    """

    def __init__(self):
        super(Day4, self).__init__(day_number=4)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day4Puzzle1(puzzle_number=puzzle_number,
                        day_number=self.day_number),
            Day4Puzzle2(puzzle_number=puzzle_number,
                        day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day4.day {}>".format(self.day_number)
