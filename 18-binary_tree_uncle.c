#include "binary_trees.h"

binary_tree_t *binary_tree_sibling(binary_tree_t *node);

/**
 * binary_tree_uncle - this finds the sibling of a node.
 * @node: a pointer to the node of the tree to get sibling
 *
 * Return: 0 if tree is null or counts leaves in tree
 *
 */

binary_tree_t *binary_tree_uncle(binary_tree_t *node)
{
	if (node == NULL)
		return (NULL);
	return (binary_tree_sibling(node->parent));
}

/**
 * binary_tree_sibling - this finds the sibling of a node.
 * @node: a pointer to the node of the tree to get sibling
 *
 * Return: 0 if tree is null or counts leaves in tree
 *
 */

binary_tree_t *binary_tree_sibling(binary_tree_t *node)
{
	if (node == NULL || node->parent == NULL)
		return (NULL);
	if (node->parent->left == node)
		return (node->parent->right);
	else
		return (node->parent->left);
}
