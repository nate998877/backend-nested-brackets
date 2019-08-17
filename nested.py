#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
takes input.txt and checks if the brackets that exist within it are valid and outputs the result to output.txt.
"""
__author__ = "nate998877"

import sys
import re

# (  ) [  ] {  } <  > (*  *) brackets 2 check
def main(args):
    bracket_list = [("(",")"), ("[","]"), ("{","}"), ("<",">"), ("(*","*)")]
    bracket_queue = [] # I was going to use Queue.queue, but if you can't tell I was lazy with this one. I don't like the pythonic ways
    output = []
    with open("input.txt") as lines:
        for (coke, line) in enumerate(lines):
            i = 0
            bracket_queue = []
            while i < len(line):
                if line[i] == "(":
                    try:
                        if line[i+1] == "*":
                            bracket_queue.append(("*",i))
                            i = i + 2;
                            continue
                    except:
                        output.append("NO "+ str(i))
                        i = i+1
                        break
                if line[i] == "*":
                    try:
                        if line[i+1] == ")":
                            queue_tuple = bracket_queue.pop()
                            if queue_tuple[0] is not "*":
                                output.append("NO " + str(queue_tuple[1]))
                                i = i+2
                                break
                    except:
                        try:
                            queue_tuple = bracket_queue.pop()
                            output.append("NO "+ str(queue_tuple[1]))
                            i = i+1
                            break
                        except:
                            output.append("NO "+ str(i))
                            i = i+1
                            break
                for bracket_tuple in bracket_list:
                    if line[i] in bracket_tuple:
                        if bracket_list[0] == line[i]:
                            bracket_queue.append(line[i])
                        else:
                            try:
                                queue_tuple = bracket_queue.pop()
                                if line[i] != queue_tuple[0]:
                                    output.append("NO "+ str(queue_tuple[1]))
                                    i = i+1
                                    break
                            except:
                                output.append("NO "+ str(i))
                                i = i+1
                                break
                i = i+1
            if len(output)-1 != coke:
                output.append("YES")
    with open("output.txt", "w+") as oh_yeah:
        for answer in output:
            oh_yeah.write(answer + "\n")


if __name__ == '__main__':
    main(sys.argv)
