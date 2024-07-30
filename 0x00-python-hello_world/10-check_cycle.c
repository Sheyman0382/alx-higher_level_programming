#include "lists.h"

/**
 * check_cycle - a program that checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;

	if (list == NULL)
		return 0;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}

	return (0);
}
