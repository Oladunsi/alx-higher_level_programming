#include "binary_trees.h"

/*
* binary_tree_node - Create a binary tree
* @parent - pointer to parent node for the binary tree
* @value - value to put into node
*
*/

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new;

	new = malloc(sizeof(binary_tree_t));
	if (new == NULL)
		return (NULL);

	new->data = value;
	new->parent = parent;
	new->left = NULL;
	new->right = NULL;

	return (new);
}
