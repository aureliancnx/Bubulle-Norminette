/*
** EPITECH PROJECT, 2020
** my_str_isupper.c
** File description:
** my_str_isupper.c
*/

#include <stddef.h>

int my_str_isupper(char const *str)
{
    int i = 0;

    if (str == NULL)
    return (0);
    while (str[i]) {
        if (!(str[i] >= 65 && str[i] <= 90))
            return (0);
        i++;
    }
    return 1;
}
