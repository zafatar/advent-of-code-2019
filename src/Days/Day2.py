# src/Days/Day2.py

from src.Day import Day
from src.Puzzle import Puzzle


def process_intcode(intcode_input=[], value_pos_1=0, value_pos_2=0):
    """
    This method processes a given intcode input with the help of
    correction values for position 1 and 2.

    Keyword Arguments:
        intcode_input {list} -- list of integers of intcode (default: {[]})
        value_pos_1 {int} -- value for position 1 (default: {0})
        value_pos_2 {int} -- value for position 1 (default: {0})
    """
    intcode_input[1] = value_pos_1
    intcode_input[2] = value_pos_2

    index = 0
    while(index <= len(intcode_input)):
        op = intcode_input[index]
        if op == 1:
            intcode_input[intcode_input[index+3]] = intcode_input[intcode_input[index+1]] + intcode_input[intcode_input[index+2]]
        elif op == 2:
            intcode_input[intcode_input[index+3]] = intcode_input[intcode_input[index+1]] * intcode_input[intcode_input[index+2]]
        elif op == 99:
            break

        index += 4

    return intcode_input[0]


class Day2Puzzle1(Puzzle):
    """
    Day2 Puzzle1 class
    """
    def solve(self):
        print("Day2 - Puzzle1")
        masses = list(map(lambda x: int(x), self.input.split(',')))

        ret = process_intcode(intcode_input=masses, value_pos_1=12, value_pos_2=2)

        print("Solution for Day2 Puzzle1: {}".format(ret))


class Day2Puzzle2(Puzzle):
    """
    Day2 Puzzle2 class
    """
    def solve(self):
        print("Day2 - Puzzle2")
        raw_masses = list(map(lambda x: int(x), self.input.split(',')))

        expected = 19690720
        noun = 0
        verb = 0
        for i in range(0, 100):
            for j in range(0, 100):
                masses = raw_masses.copy()

                ret = process_intcode(intcode_input=masses,
                                      value_pos_1=i,
                                      value_pos_2=j)

                if ret == expected:
                    noun = i
                    verb = j
                    break

        ret = (100 * noun) + verb

        print("Solution for Day2 Puzzle1: {}".format(ret))


class Day2(Day):
    """
    Day2 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day2, self).__init__(day_number=2)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day2Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day2Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day2.day {}>".format(self.day_number)
