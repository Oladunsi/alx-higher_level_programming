#include "main.h"

/**
* _puts_recursion - a function that prints a string, followed by a new line
* @s: An input string
*
*Return: Nothing
*/

void _puts_recursion(char *s)
{
	if (*s != '\0')
	{
		_putchar(*s);
		s++;
		_puts_recursion(s);
	}
	else if (*s == '\0')
	{
		_putchar('\0');
		_putchar('\n');
	}	return;
}
