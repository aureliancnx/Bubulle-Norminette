/*
** EPITECH PROJECT, 2020
** my_strlen.c
** File description:
** my_strlen.c
*/

#include <stddef.h>

int my_strlen(char const *str)
{
    int i = 0;
    int count = 0;

    if (str == NULL) {
        return (-1);
    }
    while (str[i] != '\0') {
        count = count + 1;
        i++;
    }
    return count;
}