/*
** EPITECH PROJECT, 2020
** my_str_isalpha.c
** File description:
** my_str_isalpha.c
*/

#include <stddef.h>

int my_str_isalpha(char const *str)
{
    int i = 0;

    if (str == NULL)
    return (0);
    while (str[i]) {
        if (!(str[i] >= 97 && str[i] <= 122) && !(str[i] >= 65 && str[i] <= 90))
            return (0);
        i++;
    }
    return 1;
}
