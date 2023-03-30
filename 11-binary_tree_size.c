#include "binary_trees.h"

/**
 * binary_tree_size - this gets the size of tree
 * @tree: a pointer to the root node of the tree to transverse
 *
 * Return: 0 if tree is null or node depth in tree
 *
 */
size_t binary_tree_size(const binary_tree_t *tree)
{
	size_t tree_size = 1;

	if (tree == NULL)
		return (0);
	if (tree->left != NULL)
		tree_size += binary_tree_size(tree->left);
	if (tree->right != NULL)
		tree_size += binary_tree_size(tree->right);
	return (tree_size);
}
