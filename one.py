#!/usr/local/bin/python3.9


def get_two_to_goal(numbers, goal):
    remaining_to_goal = set()

    for i in numbers:
        if i in remaining_to_goal:
            return (i, goal - i)
        else:
            remaining_to_goal.add(goal - i)
    return (None, None)

if __name__ == "__main__":
    
    with open("input.txt", "r") as file:
        data = file.readlines()
        numbers = [int(i) for i in data]
    
    for i in range(len(numbers)):
        a, b = get_two_to_goal(
            numbers[i+1:len(numbers)], 2020 - numbers[i])
        if a is not None:
            print(a*b*numbers[i])
