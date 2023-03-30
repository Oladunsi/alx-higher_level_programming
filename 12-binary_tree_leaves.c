#include "binary_trees.h"

/**
 * binary_tree_leaves - this counts the leaves in a binary tree
 * @tree: a pointer to the root node of the tree to transverse
 *
 * Return: 0 if tree is null or counts leaves in tree
 *
 */
size_t binary_tree_leaves(const binary_tree_t *tree)
{
	size_t tree_leaves = 0;

	if (tree == NULL)
		return (0);
	if (tree->left == NULL && tree->right == NULL)
		tree_leaves += 1;
	tree_leaves += binary_tree_leaves(tree->left);
	tree_leaves += binary_tree_leaves(tree->right);
	return (tree_leaves);
}
