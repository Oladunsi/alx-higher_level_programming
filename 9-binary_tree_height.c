#include "binary_trees.h"

/**
 * binary_tree_height - this gets tree height
 * @tree: a pointer to the root node of the tree to transverse
 *
 * Returns: 0 if size_t tree is null or size of tree
 *
 */

size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t left_tree_height = 0, right_tree_height = 0;


	if (tree == NULL)
		return (0);
	if (tree->left != NULL)
		left_tree_height += 1 + binary_tree_height(tree->left);
	if (tree->right != NULL)
		right_tree_height += 1 + binary_tree_height(tree->right);
	if (left_tree_height > right_tree_height)
		return (left_tree_height);
	else
		return (right_tree_height);
}
