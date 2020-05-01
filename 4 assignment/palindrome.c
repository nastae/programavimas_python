#include <Python.h>

int palindrome(char str[])
{
    int l = 0;
    int h = strlen(str) - 1;

    while (h > l)
    {
        if (str[l++] != str[h--])
        {
            return 0;
        }
    }
    return 1;
}

static PyObject* isPalindrome(PyObject* self, PyObject* args)
{
    char* n;
    if(!PyArg_ParseTuple(args, "s", &n)) {
//    2. Papildyti funkciją klaidų objektais
        PyErr_SetString(PyExc_ValueError, "Wrong input!");
        return NULL;
    }

    if (palindrome(n) == 1)
        return Py_True;
    return Py_False;
}

static PyMethodDef myMethods[] = {
    { "isPalindrome", isPalindrome, METH_O, "Say if a text is palindrome" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "myModule",
    "Palindrome Module",
    -1,
    myMethods
};

PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}
