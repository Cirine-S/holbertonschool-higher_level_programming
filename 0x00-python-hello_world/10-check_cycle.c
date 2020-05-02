#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 *check_cycle - function
 *@list: listint
 *Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *tmp = list;

	if (!list)
		return (0);
	while (tmp && tmp->next)
	{
		current = current->next;
		tmp = tmp->next->next;
		if (current == tmp)
			return (1);
	}
	return (0);
}
