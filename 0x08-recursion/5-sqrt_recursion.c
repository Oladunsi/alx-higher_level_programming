#include "main.h"

int finding_root(int num, int root);

/**
 * _sqrt_recursion - Returns the natural square root of a number.
 * @n: The number to return the square root of.
 *
 * Return: If n has a natural square root - the natural square root of n.
 *         If n does not have a natural square root - -1.
 */

int _sqrt_recursion(int n)
{
	int root = 0;

	if (n < 0)
		return (-1);

	if (n == 1)
		return (1);

	return (finding_root(n, root));
}

/**
 * finding_root - Finds the natural square root of an inputted number.
 * @num: The number to find the square root of.
 * @root: The root to be tested.
 *
 * Return: If the number has a natural square root - the square root.
 *         If the number does not have a natural square root - -1.
 */

int finding_root(int num, int root)
{
	if (root == num / 2)
		return (-1);

	if ((root * root) == num)
		return (root);

	return (finding_root(num, root + 1));
}
