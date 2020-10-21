/*
** EPITECH PROJECT, 2020
** my_strcat.c
** File description:
** my_strcat.c
*/

#include <stddef.h>
#include <stdio.h>

int my_strlen(char const *src);

char *my_strcat(char *dest, char const *src)
{
    int i = 0;
    int a = my_strlen(dest);

    if (src == NULL)
        return (NULL);
    while (src[i]) {
        dest[a + 1] = src[i];
        i++;
    }
    return (dest);
}