/*
** EPITECH PROJECT, 2020
** my_str_isprintable.c
** File description:
** my_str_isprintable.c
*/

#include <stddef.h>

int my_str_isprintable(char const *str)
{
    int i = 0;

    if (str == NULL)
    return (0);
    while (str[i]) {
        if (!(str[i] == 127 || !(str[i] >= 0 && str[i] < 32)))
            return (0);
        i++;
    }
    return 1;
}
