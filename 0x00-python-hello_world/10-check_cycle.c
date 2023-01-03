#include <stdio.h>
#include "lists.h"

/** 
check_cycle - This function checks if singly linked list contain cycle
@list - Singly linked list
Return: 0 - if no cycle
        1 - if there is cycle 
*/
int check_cycle(listint_t *list)
{
	listint_t *init_node, *subsq_node;
	
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	init_node = list->next;
	subsq_node = list->next->next;
	
	while (init_node && subsq_node && subsq_node->next)
	{
		if (init_node == subsq_node)
			return (1);
		
		init_node = init_node->next;
		subsq_node = subsq_node->next->next;
	}
	
	return (0);
}

