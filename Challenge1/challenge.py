"""
challenge.py
Name: Dani Sprague
Date: 2020-10-20

A submission for the first WWU WBC challenge.
"""

import collections

def main():
    diffs = list()
    with open('WBC_CodingChallenge1_Input.txt') as f:
        for number, line in enumerate(f):
            line = line.replace(' ', '')
            name, attributes = line.split('|')
            max_name = collections.Counter(name).most_common(1)[0][1]
            max_attr = collections.Counter(attributes).most_common(1)[0][1]
            diffs.append((abs(max_name - max_attr), number))
    diffs.sort()
    max1, max2 = diffs[len(diffs)-1]
    print(f"{max1}, {max2}")

if __name__ == "__main__":
    main()