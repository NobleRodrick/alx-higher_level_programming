#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, allocation, i;
	PyObject *objct;

	size = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		objct = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(objct)->tp_name);
	}
}
