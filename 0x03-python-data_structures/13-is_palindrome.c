#include "lists.h"

/**
 * reverse_listint - Will reverse the order of a singly linked list.
 * @head: head node pointer.
 *
 * Return: head node pointer of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - tells us whether the list is a palindrome.
 * @head: head node pointer.
 *
 * Return: is not palindrome - 0.
 * is palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *midway;
	size_t size = 0, i;

	/*if list is empty*/
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/*determining the size of the list*/
	temp = *head;
	while (temp != NULL)
	{
		size++;
		temp = temp->next;
	}

	/*move to list midpoint*/
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	midway = rev;

	temp = *head;
	while (rev != NULL)
	{
		if (temp->n != (*rev).n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&midway);

	return (1);
}
