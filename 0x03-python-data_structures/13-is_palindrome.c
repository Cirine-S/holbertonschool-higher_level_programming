#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len, tab[1000], i = 0;

	if (!*head)
		return (1);
	while (current)
	{
		current = current->next;
		len++;
	}
	current = *head;
	while (current)
	{
		tab[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (tab[i] != tab[len - i - 1])
			return (0);
	}
	return (1);
}
