#  MAMUT
Matrix Multi-tool -  Pocket Set.

## To clone this repository just type:
```
git clone git@github.com:rsmarinho/mamut.git
```

## To send updated files to github use:
```
git add <file> (or <*>) ###-u for update

git commit -m "comentary"

git push origin master
```

## To run
```
make
./mamut
```

## What is being done
- put_submatrix_at() method: put a sub(smaller) matrix in a matrix at index;
- get_submatrix_from() method: get a sub(smaller) matrix of a matrix index;

## TODO
- Create error file to print errors on screen
- Creation of a simple shell to test
- Implement the matrix return for completing matrix method (zeros(), ones(), linspace(),...) to clean the use. These functions will automatically initiate the matrix (init_matrix())
- test put_at() method: putting a complex in a real matrix get error?

## DONE

- mdot()
```
Done
```
- Create a structure type that defines the vector used in the library (vector.h)..
```
It was done a matrix (h/c) file with matrix type and functions to manipulate this type
```
- Define basic functions to manipulate the vector (basic.h)
```
An util (h/c) file was created with matrix manipulation functions. New function methods must be created. Ideas?...
```
- Input/output matrix methods. There is no push/pull methods to add values on the matrix.
```
methods were implemented, but I still don't like how they work. The use of these methods is ugly.
```
