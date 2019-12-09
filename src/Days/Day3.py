# src/Days/Day3.py

from src.Day import Day
from src.Puzzle import Puzzle


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def __repr__(self):
        return "Point: {} x {}".format(self.x, self.y)


class Intersection(Point):
    step_total = 0

    def __init__(self, x, y, step):
        super().__init__(x, y)
        self.step = step

    def __repr__(self):
        return "Intersection: {} x {} : {}".format(self.x, self.y, self.step)


class Day3Puzzle1(Puzzle):
    """
    Day3 Puzzle1 class
    """

    def solve(self):
        print("Day3 - Puzzle1")
        input_lines = self.input.split('\n')
        wires = []
        for input_line in input_lines:
            if input_line != '':
                wires.append(input_line.split(','))

        intersections = get_intersections(wires=wires)

        min_distance = 100000000
        for i in intersections:
            md = manhattan_distance_to_center(i)
            if md < min_distance:
                min_distance = md

        print("Solution for Day3 Puzzle1: {}".format(min_distance))


class Day3Puzzle2(Puzzle):
    """
    Day3 Puzzle2 class
    """

    def solve(self):
        print("Day3 - Puzzle2")
        input_lines = self.input.split('\n')
        wires = []
        for input_line in input_lines:
            if input_line != '':
                wires.append(input_line.split(','))

        intersections = get_intersections(wires=wires)

        steps = {}
        for i in intersections:
            key = "{}_{}".format(str(i.x), str(i.y))
            if key not in steps:
                steps[key] = i.step
            else:
                steps[key] += i.step

        min_steps = 100000000
        for key in steps:
            if steps[key] < min_steps:
                min_steps = steps[key]

        print("Solution for Day3 Puzzle2: {}".format(min_steps))


def get_intersections(wires=[]):
    """
    This methods runs over the wires and detects the intersections
    with list of useful stats.

    Keyword Arguments:
        wires {list} -- list of wires (default: {[]})
    """
    coordinate_matrice = {}
    intersections = []
    wire_count = 0
    for wire in wires:
        o = Point(0, 0)
        steps = 0
        for command in wire:
            direction, move = command[:1], int(command[1:])
            if direction == 'L':
                while(move > 0):
                    o.move_left()
                    steps += 1
                    update_coordinates(coordinates=coordinate_matrice,
                                        o=o, intersections=intersections,
                                        step=steps, wire=wire_count)
                    move -= 1

            elif direction == 'R':
                while(move > 0):
                    o.move_right()
                    steps += 1
                    update_coordinates(coordinates=coordinate_matrice,
                                        o=o, intersections=intersections,
                                        step=steps, wire=wire_count)
                    move -= 1

            elif direction == 'U':
                while(move > 0):
                    o.move_up()
                    steps += 1
                    update_coordinates(coordinates=coordinate_matrice,
                                        o=o, intersections=intersections,
                                        step=steps, wire=wire_count)
                    move -= 1

            elif direction == 'D':
                while(move > 0):
                    o.move_down()
                    steps += 1
                    update_coordinates(coordinates=coordinate_matrice,
                                        o=o, intersections=intersections,
                                        step=steps, wire=wire_count)
                    move -= 1

            else:
                print("Unknown direction")

        wire_count += 1

    return intersections


def update_coordinates(coordinates={}, o=None, intersections=[], step=0, wire=0):
    initial_values = {'count': 0, 'wire': 0, 'steps': 0}

    if o.x not in coordinates:
        coordinates[o.x] = {o.y: initial_values}
    elif o.y not in coordinates[o.x]:
        coordinates[o.x][o.y] = initial_values

    coordinates[o.x][o.y]['count'] = coordinates[o.x][o.y]['count'] + 1
    coordinates[o.x][o.y]['steps'] = coordinates[o.x][o.y]['steps'] + step

    if wire != coordinates[o.x][o.y]['wire'] and coordinates[o.x][o.y]['count'] == 2:
        intersection = Intersection(o.x, o.y, coordinates[o.x][o.y]['steps'])
        intersections.append(intersection)

    coordinates[o.x][o.y]['wire'] = wire


def manhattan_distance_to_center(point):
    return abs(point.x) + abs(point.y)


class Day3(Day):
    """
    Day3 Class with 2 puzzles.
    """

    def __init__(self):
        super(Day3, self).__init__(day_number=3)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day3Puzzle1(puzzle_number=puzzle_number,
                        day_number=self.day_number),
            Day3Puzzle2(puzzle_number=puzzle_number,
                        day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day3.day {}>".format(self.day_number)
