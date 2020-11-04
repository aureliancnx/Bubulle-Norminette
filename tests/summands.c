/*
** EPITECH PROJECT, 2020
** summands
** File description:
** do some calculs
*/

#include <stdlib.h>
#include "summands_tool.h"

char *number(char **str_ptr, char *base);
char *infin_add(char *nb_a, char *nb_b, char *base);
char *infin_sub(char *nb_a, char *nb_b, char *base);
char *summands(char **str_ptr, char *base, char *ops);
int division(int a, int b);
char *infin_multi(char *a, char *b, char *base, char *ops);
int modulo(int a, int b);
char *get_nb(char **str_ptr, char *base, char *ops);

char *calculs(char *a, char *b, char ope, char *ops, char *base)
{
    if (b == NULL || *b == 0 || ope == 0) {
        return (a);
    }
    if (ope == ops[2]) {
        if (*a == '-')
            return (infin_sub(b, a, base));
        return (infin_add(a, b, base));
    }
    if (ope == ops[3]) {
        char *r;
        if (b < 0)
            return (infin_add(a, b, base));
        return (infin_sub(a, b, base));
    }
    if (ope == ops[4]) {
        return (infin_multi(a, b, base, ops));
    }
    return (a);
}

int prioritary(char c, char *ops)
{
    if (c == ops[2] || c == ops[3])
        return (0);
    if (c == 0)
        return (0);
    return (1);
}

char get_operator(char **str_ptr)
{
    char c = **str_ptr;
    *str_ptr = *str_ptr + 1;
    return (c);
}

char *calcul_summands(tool_t tool)
{
    char *result;
    char s_ope = get_operator(tool.str);
    if (prioritary(s_ope, tool.ops) && prioritary(tool.ope, tool.ops) == 0) {
        char *third = get_nb(tool.str, tool.base, tool.ops);
        char *first = calculs(tool.se, third, s_ope, tool.ops, tool.base);
        char third_ope = get_operator(tool.str);
        char *s = summands(tool.str, tool.base, tool.ops);
        first = calculs(first, s, third_ope, tool.ops, tool.base);
        result = calculs(tool.nb, first, tool.ope, tool.ops, tool.base);
    } else {
        result = calculs(tool.nb, tool.se, tool.ope, tool.ops, tool.base);
        char *nb_third = get_nb(tool.str, tool.base, tool.ops);
        char thir_ope = get_operator(tool.str);
        char *s = summands(tool.str, tool.base, tool.ops);
        result = calculs(result, nb_third, s_ope, tool.ops, tool.base);
        result = calculs(result, s, thir_ope, tool.ops, tool.base);
    }
    return (result);
}

char *summands(char **str_ptr, char *base, char *ops)
{
    if (**str_ptr == '\0')
        return (NULL);
    char *result;
    char *nb = get_nb(str_ptr, base, ops);
    char operator = get_operator(str_ptr);
    char *second = get_nb(str_ptr, base, ops);
    tool_t new_tool;
    new_tool.base = base;
    new_tool.nb = nb;
    new_tool.ope = operator;
    new_tool.ops = ops;
    new_tool.se = second;
    new_tool.str = str_ptr;
    if (operator != '\0') {
        result = calcul_summands(new_tool);
    } else {
        return (nb);
    }
    return (result);
}
