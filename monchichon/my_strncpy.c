/*
** EPITECH PROJECT, 2020
** my_strncpy.c
** File description:
** funccpys1ins2fornchar
*/

#include <stddef.h>

int my_putchar(char c);

int my_strlen(char const *str);

int my_putstr(char const *str);

char *my_strncpy(char *dest, char const *src, int n)
{
    int i = 0;
    int len = my_strlen(src);

    if (n > len)
        return dest[i] = '\0';
    if (src == NULL)
        return (NULL);
    while (src[i] && i < n) {
        dest[i] = src[i];
        i++;
    }
    return (dest);
}