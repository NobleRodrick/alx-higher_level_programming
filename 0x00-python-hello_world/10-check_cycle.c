#include "lists.h"

/**
 * check_cycle - checks if a there is a circle in the linked list
 * @list: the linked list
 *
 * Return: 1 if the list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *next1 = list;
	listint_t *next2 = list;

	if (!list)
		return (0);

	while (next1 && next2 && next2->next)
	{
		next1 = next1->next;
		next2 = next2->next->next;
		if (next1 == next2)
			return (1);
	}

	return (0);
}
