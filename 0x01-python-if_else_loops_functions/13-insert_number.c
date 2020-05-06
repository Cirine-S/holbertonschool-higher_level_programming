#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 *insert_node - insert a new node in a sorted list
 *@head: pointer to pointer of the first node in the list
 *@number: number to be inserted in the right position in the list
 *Return: address of the new element or Null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new, *current, *prev = NULL;
        current = *head;
        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;
        new->next = NULL;
        if (*head == NULL)
                *head = new;
        else
        {
                while (current)
                {
                        if (current->n < number)
                        {
                                prev = current;
                                current = current->next;
                        }
                        else
                                break;
                }
                if (!prev)
                {
                        new->next = current;
                        *head = new;
                }
                else
                {
                        new->next = current;
                        prev->next = new;
                }
        }
        return (new);
}
