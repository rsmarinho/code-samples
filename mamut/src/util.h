#ifndef _UTIL_H_
#define _UTIL_H_

#include <stdlib.h> // malloc and free functions
#include <matrix.h>

#define __complex(FUNC) *((double complex *) FUNC)
#define __real(FUNC) *((double *) FUNC)

//modify matrix
int ones(t_matrix * v);
int zeros(t_matrix * v);
int eye(t_matrix * v);

int linspace(t_matrix * v, double start, double end, int n);
int logspace(t_matrix * v, double start, double end, int n);

//operate over matrix
void * det(t_matrix * v);
t_matrix * tran(t_matrix *v);

//utility functions
int put_submatrix_at(t_matrix * v, t_matrix * k, int n_args, ...);

#endif

