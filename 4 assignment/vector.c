#include <Python.h>
#include "structmember.h"

typedef struct{
  PyObject_HEAD
  int x;
  int y;
} Vektorius;

static void Vektorius_dealloc(Vektorius* self){
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject * Vektorius_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Vektorius *self;

    self = (Vektorius *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->x = 0;
        self->y = 0;
    }

    return (PyObject *)self;
}

static int Vektorius_init(Vektorius *self, PyObject *args, PyObject *kwds)
{
    if (! PyArg_ParseTuple(args, "ii", &self->x, &self->y))
        return -1;
    return 0;
}

static PyMemberDef Vektorius_members[] = {
    {"x", T_INT, offsetof(Vektorius, x), 0, "x ašies kryptis"},
    {"y", T_INT, offsetof(Vektorius, y), 0, "y ašies kryptis"},
    {NULL}  /* Sentinel */
};

static PyObject * Vektorius_multiply(Vektorius* self, Vektorius* arg0)
{
    return Py_BuildValue("i", self->x*arg0->x + self->y*arg0->y);
}

static PyMethodDef Vektorius_methods[] = {
    {"multiply", (PyCFunction)Vektorius_multiply, METH_O, "Return result of vector's multiplication"},
    {NULL}  /* Sentinel */
};

static PyObject* Vektorius_str(Vektorius* self){
    return PyUnicode_FromFormat("(%i %i)", self->x, self->y);
}

static PyTypeObject vector_VektoriusType ={
  PyVarObject_HEAD_INIT(NULL, 0)
  "vector.Vektorius", /*tp_name*/
  sizeof(Vektorius), /*tp_basicsize*/
  0, /*tp_itemsize*/
  (destructor) Vektorius_dealloc, /*tp_dealloc*/
  0, /*tp_print*/
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  0, /*tp_reserved*/
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash */
  0, /*tp_call*/
  (reprfunc) Vektorius_str, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
  "Cia yra vektorius", /* tp_doc */
  0,
  0,
  0,
  0,
  0,
  0,
  Vektorius_methods, //cia bus metodai
  Vektorius_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc)Vektorius_init,
  0,
  Vektorius_new,
};

static struct PyModuleDef vectormodule ={
  PyModuleDef_HEAD_INIT,
  "vector", // name of module
  "Vektorius tipas", // module documentation, may be NULL
  -1, // size of per- interpreter state of the module, or -1 if the module keeps state in global variables.
  NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_vector (void){
  PyObject* m;
  //vector_VektoriusType.tp_new = PyType_GenericNew;
  if (PyType_Ready(&vector_VektoriusType)< 0)
    return NULL;
  m = PyModule_Create(&vectormodule);
  if (m == NULL)
    return NULL;
  Py_INCREF(&vector_VektoriusType);
  PyModule_AddObject(m, "Vektorius", (PyObject*)&vector_VektoriusType);
  return m;
  //return PyModule_Create (&spammodule);
}