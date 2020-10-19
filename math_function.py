#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## math_function
## File description:
## math_function
##

from math import *

import matrice


def exp_function(tab):
    mat = matrice.matrice_identity(len(tab))
    for i in range(1, 30):
        mult = matrice.matrice_multiplication_by_coef(tab, i)
        mult2 = matrice.matrice_division(mult, factorial(i))
        mat = matrice.matrice_addition(mat, mult2)
    return mat


def cos_function(tab):
    mat = matrice.matrice_identity(len(tab))
    for i in range(1, 30):
        if i % 2 == 0:
            mult = matrice.matrice_multiplication_by_coef(tab, 2 * i)
            mult2 = matrice.matrice_division(mult, factorial(2 * i))
            mat = matrice.matrice_addition(mat, mult2)
        else:
            mult = matrice.matrice_multiplication_by_coef(tab, 2 * i)
            mult2 = matrice.matrice_division(mult, factorial(2 * i))
            mat = matrice.matrice_substraction(mat, mult2)
    return mat


def sin_function(tab):
    mat = tab
    for i in range(1, 30):
        if i % 2 == 0:
            mult = matrice.matrice_multiplication_by_coef(tab, 2 * i + 1)
            mult2 = matrice.matrice_division(mult, factorial(2 * i + 1))
            mat = matrice.matrice_addition(mat, mult2)
        else:
            mult = matrice.matrice_multiplication_by_coef(tab, 2 * i + 1)
            mult2 = matrice.matrice_division(mult, factorial(2 * i + 1))
            mat = matrice.matrice_substraction(mat, mult2)
    return mat


def cosh_function(tab):
    mat = matrice.matrice_identity(len(tab))
    for i in range(1, 30):
        mult = matrice.matrice_multiplication_by_coef(tab, 2 * i)
        mult2 = matrice.matrice_division(mult, factorial(2 * i))
        mat = matrice.matrice_addition(mat, mult2)
    return mat


def sinh_function(tab):
    mat = tab
    for i in range(1, 30):
        mult = matrice.matrice_multiplication_by_coef(tab, 2 * i + 1)
        mult2 = matrice.matrice_division(mult, factorial(2 * i + 1))
        mat = matrice.matrice_addition(mat, mult2)
    return mat
