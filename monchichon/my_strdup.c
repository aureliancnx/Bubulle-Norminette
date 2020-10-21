/*
** EPITECH PROJECT, 2020
** my_strdup.c
** File description:
** my_strdup.c
*/

#include <stdlib.h>

int my_strlen(char const *str);

char *my_strdup(char const *src)
{
    int i = 0;
    int a = my_strlen(src);
    char *dest = malloc(sizeof(char) * (a + 1));

    while (src[i]) {
        dest[i] = src[i];
        i++;
    }
    return (dest);
}