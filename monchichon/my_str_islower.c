/*
** EPITECH PROJECT, 2020
** my_str_islower.c
** File description:
** my_str_islower.c
*/

#include <stddef.h>

int my_str_islower(char const *str)
{
    int i = 0;

    if (str == NULL)
    return (0);
 i = 1;
    while (str[i]) {
        if (!(str[i] >= 97 && str[i] <= 122))
            return (0);
        i++;
    }
    return (1);
}
