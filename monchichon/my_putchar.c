/*
** EPITECH PROJECT, 2020
** task01
** File description:
** my_putchar.c
*/

#include <unistd.h>

void my_putchar(char c)
{
    write (1, &c, 1);
}
