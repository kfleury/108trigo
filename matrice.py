#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## calcul_on_matrice
## File description:
## calcul_on_matrice
##

def matrice_addition(one, two):
    mat = []
    for i in range(len(one)):
        mat2 = []
        for j in range(len(one[0])):
            mat2.append(one[i][j] + two[i][j])
        mat.append(mat2)
    return mat


def matrice_substraction(one, two):
    mat = []
    for i in range(len(one)):
        mat2 = []
        for j in range(len(one[0])):
            mat2.append(one[i][j] - two[i][j])
        mat.append(mat2)
    return mat


def matrice_multiplication(one, two):
    mat = []
    for i in range(len(one)):
        mat2 = []
        for j in range(len(two)):
            count = 0
            for k in range(len(one)):
                count += one[i][k] * two[k][j]
            mat2.append(count)
        mat.append(mat2)
    return mat


def matrice_multiplication_by_coef(one, x_case):
    mat = one
    for i in range(x_case - 1):
        mat = matrice_multiplication(mat, one)
    return mat


def matrice_division(one, x_case):
    for i in range(len(one)):
        for j in range(len(one[0])):
            one[i][j] /= x_case
    return one


def matrice_identity(x_case):
    mat = []
    for i in range(x_case):
        mat2 = []
        for j in range(x_case):
            if j == i:
                mat2.append(1)
            else:
                mat2.append(0)
        mat.append(mat2)
    return mat


def matrice_initialisation(x_case, y_case):
    mat = []
    for i in range(x_case):
        mat2 = []
        for j in range(y_case):
            mat2.append(y_case)
        mat.append(mat2)
    return mat


def display_matrice(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            print("%.2f" % tab[i][j], end="")
            if j == (len(tab[i]) - 1):
                print("\n", end="")
            else:
                print("\t", end="")
