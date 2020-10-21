/*
** EPITECH PROJECT, 2020
** test.c
** File description:
** testcriterionfortestfunctions
*/

#include <string.h>
#include <stddef.h>
#include <unistd.h>
#include <criterion/criterion.h>
#include <criterion/redirect.h>

int my_putstr(char const *str);

int my_strlen(char const *str);

int my_str_isalpha(char const *str);

int my_str_isnum(char const *str);

int my_str_islower(char const *str);

int my_str_isupper(char const *str);

int my_str_isprintable(char const *str);

int my_isneg(int nb);

void redirect_all_stdout(void)
{
    cr_redirect_stdout();
    cr_redirect_stderr();
}

Test (test_my_putstr, simple, .init=redirect_all_stdout)
{
    my_putstr("lolll");
    cr_assert_stdout_eq_str("lolll");
}

Test (test2_my_putstr, simple, .init=redirect_all_stdout)
{
    my_putstr(NULL);
    cr_assert("OK");
}

 Test (test3_my_putstr, simple, .init=redirect_all_stdout)
{
    my_putstr(" ");
    cr_assert_stdout_eq_str(" ");
}

Test(test_my_strlen, simple)
{
    char *str = "dmliujythgfvcdkuyjhtgfvduiyjhntbe";
    cr_assert_eq(my_strlen(str), strlen(str));
}

Test (test2_my_strlen, simple)
{
    char *str = "\0" ;
    cr_assert_eq(my_strlen(str), strlen(str));
}

Test (test3_my_strlen, simple)
{
    my_strlen(NULL);
    cr_assert("ok, jai pas crash");
}

Test (test1_my_str_isalpha, simple)
{
    char *str;
    cr_assert_eq(my_str_isalpha("zouzoudelta"), 1);
}

Test (test2_my_str_isalpha, simple)
{
    char *str;
    cr_assert_eq(my_str_isalpha("Ã§\'(-Ã§-Ã¨_\'("), 0);
}

Test (test3_my_str_isalpha, simple)
{
    my_str_isalpha(NULL);
    cr_assert("OK");
}

Test (test1_my_str_isnum, simple)
{
    char *str;
    cr_assert_eq(my_str_isnum("182645"), 1);
}

Test (test2_my_str_isnum, simple)
{
    char *str;
    cr_assert_eq(my_str_isnum("-124536"), 0);
}

Test (test3_my_str_isnum, simple)
{
    my_str_isnum(NULL);
    cr_assert("OK");
}

Test (test1_my_str_islower, simple)
{
    char *str;
    cr_assert_eq(my_str_islower("zfoihuz"), 1);
}

Test (test2_my_str_islower, simple)
{
    char *str;
    cr_assert_eq(my_str_islower("OZFZNCA"), 0);
}

Test (test3_my_str_islower, simple)
{
    my_str_islower(NULL);
    cr_assert("OK");
}

Test (test1_my_str_isupper,simple)
{
    char *str;
    cr_assert_eq(my_str_isupper("JESUISUNEMAJUSCULE"), 1);
}

Test (test2_my_str_isupper, simple)
{
    char *str;
    cr_assert_eq(my_str_isupper("jesuisuneminuscule"), 0);
}

Test (test3_my_str_isupper, simple)
{
    my_str_isupper(NULL);
    cr_assert("OK");
}

Test (test1_my_str_isprintable, simple)
{
    char *str;
    cr_assert_eq(my_str_isprintable("jesuisprintable....*"), 1);
}

Test (test2_my_str_isprintable, simple)
{
    char str[4];
    str[0] = 'A';
    str[1] = 'B';
    str[2] = 22;
    str[3] = '\0';
    cr_assert_eq(my_str_isprintable(str), 0);
}

Test (test3_my_str_isprintable, simple)
{
    my_str_isprintable(NULL);
    cr_assert_eq((NULL),0);
}

Test (test1_my_isneg, simple, .init=redirect_all_stdout)
{
    cr_redirect_stdout();
    my_isneg(18);
        cr_assert_stdout_eq_str("P");
}

Test (test2_my_isneg, simple, .init=redirect_all_stdout)
{
    cr_redirect_stdout();
    my_isneg(-18);
    cr_assert_stdout_eq_str("N");
}

Test (test3_my_isneg, simple)
{
    cr_redirect_stdout();
    my_isneg(0);
    cr_assert_stdout_eq_str("P");
}
