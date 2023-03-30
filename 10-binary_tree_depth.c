#include "binary_trees.h"

/**
 * binary_tree_depth - this gets the depth of a node in a tree
 * @tree: a pointer to the root node of the tree to transverse
 *
 * Return: 0 if tree is null or node depth in tree
 *
 */
size_t binary_tree_depth(const binary_tree_t *tree)
{
	size_t tree_depth = 0;

	if (tree == NULL)
		return (0);
	if (tree->parent != NULL)
		tree_depth += 1 + binary_tree_depth(tree->parent);
	return (tree_depth);
}
