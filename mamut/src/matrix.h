#ifndef _MATRIX_H_
#define _MATRIX_H_

#include <math.h>   //used in logspace()
#include <stdlib.h> //malloc(), free() and rand() functions
#include <time.h>
#include <complex.h>
#include <stdarg.h>

typedef struct
{
	void * vec; // the vector itself
	int type; //tipo de vetor 0 = float, 1 = complex
	int length; //vector length
	int * n_dim; //set of dimensions
	int dim; //dimensions
	char * name; //matrix name identifyer
} t_matrix;

int minit(int type, t_matrix * v, int n_args,...);
int mclose(t_matrix * v);
int printm(t_matrix * v);

unsigned int index_of(t_matrix * v, int n_args, ...);
int put_at(t_matrix * v, void * value, int n_args, ...);
void * get_from(t_matrix * v, int n_args, ...);

void * get_mem_address(t_matrix *v, unsigned int size, unsigned int ind);
#endif
