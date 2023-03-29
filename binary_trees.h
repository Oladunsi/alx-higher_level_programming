#ifndef BINARY_TREES_H
#define BINARY_TREES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
* struct binary_tree_s Binary Trees Node
* 
* @data - integer stored in node
* @parent - Pointer to parent node
* @left - Pointer to left child node
* @right - Pointer to right child node
*
*/

struct binary_tree_s{
    int data;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

typedef struct binary_tree_s binary_tree_t;
typedef struct binary_tree_s bst_t;
typedef struct binary_tree_s avl_t;
typedef struct binary_tree_s heap_t;

/* Printing helper function */
void binary_tree_print(const binary_tree_t *);

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);
#endif
