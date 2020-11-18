"""
challenge.py
Name: Dani Sprague
Date: 2020-11-17

A submission for the second WWU WBC challenge.
"""

import sys

def number(n):
    """
    Determines the number of triangles within a single triangle.
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return 3*number(n-1) + 2

def ratio(n1, n2):
    """
    Determines the ratio between two steps of triangles (0-based).
    """

    return f"{2**(n2-n1)}:1\n"

def main():
    sys.setrecursionlimit(10000)
    with open("answers.txt", "w") as answers:
        with open("WBC_CodingChallenge2_Input.txt", "r") as questions:
            for line in questions:
                if line[0] == "N":
                    answers.write(f"{number(int(line.split()[1]))}\n")
                elif line[0] == "R":
                    answers.write(ratio(int(line.split()[1]), int(line.split()[2])))   

if __name__ == "__main__":
    main()