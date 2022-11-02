#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
<<<<<<< HEAD
* check_cycle - checks if a singly linked list has a cycle in it
* @list: input head
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
=======
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: input head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
>>>>>>> a67641a2409a90d7664b80758a5cd5ab2f90bf63
int check_cycle(listint_t *list)
{
	listint_t *tmp;
	
	if (!list)
		return (0);
	while (list)
	{
		tmp = list;
		list = list->next;
		if (tmp <= list)
			return (1);
	}
	return (0);
}
