#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - fuction prints info concerting python
 * bytes, for python object
 *
 * @p: Object concerned
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, a, limit_val;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		limit_val = 10;
	else
		limit_val = size + 1;

	printf("  first %ld bytes:", limit_val);

	for (a = 0; a < limit_val; a++)
		if (str[a] >= 0)
			printf(" %02x", str[a]);
		else
			printf(" %02x", 256 + str[a]);

	printf("\n");
}

/**
 * print_python_list - Gives list info
 *
 * @p: object concerned
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, a;
	PyListObject *the_list;
	PyObject *objct;

	size = ((PyVarObject *)(p))->ob_size;
	the_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", the_list->allocated);

	for (a = 0; a < size; a++)
	{
		objct = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((objct)->ob_type)->tp_name);
		if (PyBytes_Check(objct))
			print_python_bytes(objct);
	}
