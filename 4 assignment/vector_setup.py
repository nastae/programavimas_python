from distutils.core import setup, Extension
setup(name = 'vector', version = '1.0', ext_modules = [Extension('vector', ['vector.c'])])
