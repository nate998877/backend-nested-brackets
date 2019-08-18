#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
takes input.txt and checks if the brackets that exist within it are valid and outputs the result to output.txt.
"""
__author__ = "nate998877"

import sys

# (  ) [  ] {  } <  > (*  *) brackets 2 check
def main(args):
    index = 1
    char = 0
    bracket_list = ["(",")","[","]","{","}","<",">","(*","*)"]
    bracket_queue = []
    output = []
    with open("input.txt") as lines:
        for (coke, line) in enumerate(lines):
            i = 0
            bracket_queue = []
            while i < len(line):
                try:
                    if bracket_list.index(line[i]) % 2 == 0:
                        if line[i] == "(" and line[i+1] == "*":
                            bracket_queue.append(("(*", i))
                        else:
                            bracket_queue.append((line[i], i))
                        i += 1
                    elif bracket_list.index(line[i]) % 2 == 1:
                        try:
                            bracket = bracket_queue.pop()
                            if line[i] == ")" and line[i-1] == "*" and line[i-2] != "(":
                                if bracket[char] == "(*":
                                    i += 1
                                else:
                                    output.append("NO " + str(i))
                                    break
                            elif bracket[char] == bracket_list[bracket_list.index(line[i])-1]:
                                i += 1
                            else:
                                if line[i] == ")" and bracket[char] == "(*":
                                    output.append("NO " + str(i))
                                else:
                                    output.append("NO " + str(i))
                                break
                        except:
                            output.append("NO " + str(i))
                            break
                except:
                    i+=1
            if(len(output) < coke+1):
                if len(bracket_queue) != 0:
                    if len(output) != coke+1:
                        bracket = bracket_queue.pop()
                        output.append("NO " + str(bracket[index]))
                else:
                    output.append("YES")
    with open("output.txt", "w+") as oh_yeah:
        for answer in output:
            oh_yeah.write(answer + "\n")


if __name__ == '__main__':
    main(sys.argv)
