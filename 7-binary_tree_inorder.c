#include "binary_trees.h"

/**
 * binary_tree_inorder - this goes thru a tree using a inorder transversal
 * @tree: a pointer to the root node of the tree to transverse
 * @func: a pointer to call each node in the tree
 * Returns: Nothing
 */
void binary_tree_inorder(const binary_tree_t *tree, void (*func)(int))
{
	if (tree == NULL || func == NULL)
		return;
	binary_tree_inorder(tree->left, func);
	func(tree->n);
	binary_tree_inorder(tree->right, func);
}
