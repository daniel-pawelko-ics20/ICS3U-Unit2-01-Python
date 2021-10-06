#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program calculates the area and perimeter of a circle
#    with a radius of 15 mm

from math import pi


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 15mm: ")
    print("")
    print(f"Area is {pi * 15 ** 2} mm².")
    print(f"Perimeter is {2 * pi * 15} mm.")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
