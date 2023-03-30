#include "binary_trees.h"

/**
 * binary_tree_preorder - this goes thru a tree using a preorder transversal
 * @tree: a pointer to the root node of the tree to transverse
 * @func: a pointer to call each node in the tree
 * Returns: Nothing
 */
void binary_tree_preorder(const binary_tree_t *tree, void (*func)(int))
{
	if (tree == NULL || func == NULL)
		return;
	
	func(tree->n);
	binary_tree_preorder(tree->left, func);
	binary_tree_preorder(tree->right, func);
}
