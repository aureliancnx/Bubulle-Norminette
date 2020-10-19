/*
** EPITECH PROJECT, 2020
** my_putstr.c
** File description:
** Put a string
*/
void my_putchar(char c);

void my_putstr(char const *str)
{
    int pos = 0;

    while (str[pos]) {
        my_putchar(str[pos]);
        pos += 1;
    }
}