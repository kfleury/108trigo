#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## error_handling
## File description:
## error_handling
##

import sys


def usage():
    var = "USAGE\n" \
          "    ./108trigo fun a0 a1 a1 ...\n\n" \
          "DESCRIPTION\n" \
          "    fun     function to be applied, among at least \"EXP\", \"COS\", \"SIN\", \"COSH\"\n" \
          "            and \"SINH\"\n" \
          "    ai      coefficients of the matrix\n"
    print(var, end="")
    return 0


def parameter():
    if len(sys.argv) <= 2:
        sys.stderr.write("Not enough argument\n")
        sys.exit(84)
    if sys.argv[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        sys.stderr.write("Bad format, rerun with -h or --help\n")
        sys.exit(84)
    try:
        for count in range(2, len(sys.argv)):
            sys.argv[count] = float(sys.argv[count])
    except ValueError:
        sys.stderr.write("Argument must be a number\n")
        sys.exit(84)
