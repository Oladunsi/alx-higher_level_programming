#include "binary_trees.h"

/**
 * binary_tree_is_leaf - Checks if a node is a leaf of a binary tree.
 * @node: node to check if is a leaf.
 * Return: 0 if tree is empty or node has child(red)
 *         1 if node doesn't have any child and not NULL.
 */

int binary_tree_is_leaf(const binary_tree_t *node)
{
	if (node == NULL || node->left != NULL || node->right != NULL)
		return (0);
	return (1);
}
