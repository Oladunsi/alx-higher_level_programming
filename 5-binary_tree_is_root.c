#include "binary_trees.h"

/**
 * binary_tree_is_root - checks if the node is the root node in a tree
 * @node: node to check
 * Return: 0 if node has parent and node is NULL
 *         1 if node doesn't have parent and not NULL
 */

int binary_tree_is_root(const binary_tree_t *node)
{
	if (node == NULL || node->parent != NULL)
		return (0);
	return (1);
}
