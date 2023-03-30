#include "binary_trees.h"

/**
 * binary_tree_balance - this measures the balance factor of a
 * binary tree.
 * @tree: a pointer to the root node of the tree to transverse
 *
 * Return: 0 if tree is null or counts leaves in tree
 *
 */

size_t binary_tree_height(const binary_tree_t *tree);


int binary_tree_balance(const binary_tree_t *tree)
{
	size_t tree_left = 0, tree_right = 0;

	if (tree == NULL)
		return (0);
	
	tree_left = binary_tree_height(tree->left);
	tree_right = binary_tree_height(tree->right);
	return (tree_left - tree_right);
}

/**
 * binary_tree_height - this gets tree height
 * @tree: a pointer to the root node of the tree to transverse
 *
 * Return: 0 if size_t tree is null or size of tree
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
	return (right_tree_height);
}

