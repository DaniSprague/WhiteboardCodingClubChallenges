"""
challenge.py
Name: Dani Sprague
Date: 2020-12-15

A submission for the third WWU WBC challenge.
"""

def spin(string, num):
    kept = string[0:-num]
    return string[-num:] + kept

def exchange(string, index1, index2):
    val1 = string[index1]
    l_string = list(string)
    l_string[index1] = l_string[index2]
    l_string[index2] = val1
    return "".join(l_string)

def partner(string, letter1, letter2):
    return exchange(string, string.index(letter1), string.index(letter2))

def main():
    string = "abcdefghijklmnop"
    with open("WBC_CodingChallenge3_Input.txt", "r") as input:
        commands = input.readline().split(",")
        for command in commands:
            if command[0] == "s":
                string = spin(string, int(command[1:]))
            elif command[0] == "x":
                string = exchange(string, int(command[1:command.index("/")]), int(command[command.index("/") + 1:]))
            elif command[0] == "p":
                string = partner(string, command[1:command.find("/")], command[command.find("/") + 1:])
    print(string)


if __name__ == "__main__":
    main()
