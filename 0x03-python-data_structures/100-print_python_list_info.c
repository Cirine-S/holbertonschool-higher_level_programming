#include <Python.h>

/**
 * print_python_list_info - void function
 * @p: pyobj
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int size, i = 0;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
	while (i < size)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
