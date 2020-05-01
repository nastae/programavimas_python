# Testavimo scenarijai
### 1 ir 2 punktai. Funkcijos išplėtimas C kalboje.
py palindrome_setup.py build
py palindrome_setup.py install
py palindrome_c_extension.py

### 3 punktas. Vektoriaus duomenų tipas.
py vector_setup.py build
py vector_setup.py install
py vector_c_extension.py

### 4 punktas. Funkcijos įterpimas į C.
gcc -I/usr/include/python3.4m palindrome_embed.c -lpython3.4m
./a.out palindrome palindrome aba