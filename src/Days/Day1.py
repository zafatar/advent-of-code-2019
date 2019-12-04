# src/Days/Day1.py

from src.Day import Day
from src.Puzzle import Puzzle

from math import floor


class Day1Puzzle1(Puzzle):
    """
    Day1 Puzzle1 class
    """
    def solve(self):
        print("Day1 - Puzzle1")
        masses = self.input.splitlines()

        sum_of_fuel_req = 0
        for mass in masses:
            fuel_req = floor(int(mass) / 3) - 2
            sum_of_fuel_req += fuel_req

        print("Solution for Day1 Puzzle1: {}".format(sum_of_fuel_req))


class Day1Puzzle2(Puzzle):
    """
    Day1 Puzzle2 class
    """
    def solve(self):
        print("Day1 - Puzzle2")
        masses = self.input.splitlines()

        sum_of_fuel_req = 0
        for mass in masses:
            while(int(mass) > 0):
                mass = floor(int(mass) / 3) - 2

                if(mass > 0):
                    sum_of_fuel_req += mass

        print("Solution for Day1 Puzzle1: {}".format(sum_of_fuel_req))


class Day1(Day):
    """
    Day1 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day1, self).__init__(day_number=1)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day1Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day1Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day1.day {}>".format(self.day_number)
