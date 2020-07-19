#include <stdio.h>
#include "matrix.h"

//initiate a v matrix allocating memory for matrix type
//matrix usage is MXN where M is the number of lines
//and N is the numbert of columns
int minit(int type, t_matrix * v, int n_args, ...)
{
	int length = 1;

	va_list valist;
	va_start(valist,n_args);
	
	v->dim = n_args;
	v->n_dim = malloc(sizeof(int) * n_args);
	for (int i=0; i<n_args; i++) {
		v->n_dim[i] = va_arg(valist, int);
		length *= v->n_dim[i];
	}
	v->length = length;
	
	if (v->dim > 2) {
		printf("minit: only 2 dimensions coded\n");
		exit(1); //err
	}
	
	v->type = type;
	v->vec = malloc((sizeof(double) * (1 + v->type)) * length);
	
	va_end(valist);
	return 0;
}

//free memory of v matrix
int mclose(t_matrix * v)
{
	free(v->vec);
	free(v->n_dim);
	return 0;
}

int printm(t_matrix * v)
{
	if (v->type == 0) {
		double * a;
		printf("Type : real\n");
		printf("Dimesions : %d - ( ", v->dim);
		for(int i=0;i<v->dim;i++) {
			printf("%d ",v->n_dim[i]);
		}
		printf(")\n");
		printf("Length : %d\n\n",v->length);
		if(v->dim == 2) {
			for(int i=0;i<v->n_dim[0];i++) {
				for(int k=0;k<v->n_dim[1];k++) {
					a = (double *) get_from(v,2,i,k);
					printf("%3.1f\t", *a);
				}
				printf("\n");
			}
		}
	} else if (v->type == 1) {
		double complex * a;
		printf("Type : complex\n");
		printf("Dimesions : %d - ( ", v->dim);
		for(int i=0;i<v->dim;i++) {
			printf("%d ",v->n_dim[i]);
		}
		printf(")\n");
		printf("Length : %d\n\n",v->length);
		if(v->dim == 2) {
			for(int i=0;i<v->n_dim[0];i++) {
				for(int k=0;k<v->n_dim[1];k++) {
					a = (double complex *) get_from(v,2,i,k);
					printf("%3.1f%+3.1fi\t", crealf(*a), cimagf(*a));
					//printf("%3.1f\t", *a);
				}
				printf("\n");
			}
		}
	} else {
		printf("print: not recognized type\n");
		exit(1);
		return 1;
	}
	
	return 0;
}

//return the index of a given entry on the matrix
//the entry is given by a (a1,a2,...,an) type, depending
//on the matrix dimension, and the function return the 
//index used by matrix in memory.
unsigned int index_of(t_matrix * v, int n_args, ...)
{
	va_list valist;
	va_start(valist,n_args);
	
	int ans = v->n_dim[1];
	ans *= va_arg(valist,int);
	ans += va_arg(valist,int);
	
	va_end(valist);
	
	if (ans >= v->length) {
		printf("index_of: out of bounds\n");
		exit(1); //err
	}
	
	return ans;
}

//puts a given number in matrix v on a position given 
//in form (a1,a2,...,an)
int put_at(t_matrix * v, void * value, int n_args, ...)
{
	va_list valist;
	va_start(valist,n_args);
	
	int type_size = (sizeof(double) + sizeof(double) * v->type);
	
	int ans = v->n_dim[1];
	ans *= va_arg(valist,int);
	ans += va_arg(valist,int);
	
	va_end(valist);
	
	if (ans >= v->length) {
		printf("put_at: out of bounds. ans = %d\n", ans);
		exit(1); //err
	}
	
	if (v->type == 0) {
		double * a;
		a = ((double *) (v->vec + (type_size * ans)));
		*a = *((double *) value);
	} else if (v->type == 1) {
		double complex * a;
		a = ((double complex *) (v->vec + (type_size * ans)));
		*a = *((double complex *) value);
	} else {
		printf("put_at: type error\n");
	}
	//~ printf("put_at: ans = %d\n", ans);
	return 0;
}

//return an entry of the matrix. The entry is defined 
//in form (a1,a2,...,an)
void * get_from(t_matrix * v, int n_args, ...)
{
	va_list valist;
	va_start(valist,n_args);
	
	void * a = NULL;
	int type_size = (sizeof(double) + sizeof(double)*v->type);
	
	int ans = v->n_dim[1];
	ans *= va_arg(valist,int);
	ans += va_arg(valist,int);
	
	va_end(valist);
	
	if (ans >= v->length) {
		printf("get_from: out of bounds %i\n", ans);
		exit(1); //err
	}
	
	//return position type_syze*ans from vector representation of
	//type t_matrix
	//~ a = ((void *) (((__uint8_t *) v->vec) + ((__uint8_t) type_size * ans)));
	a = get_mem_address(v,type_size,ans);
	return a;
}

void * get_mem_address(t_matrix *v, unsigned int size, unsigned int ind) {
	void *ans = NULL;
	ans = ((void *) (((__uint8_t *) v->vec) + ((__uint8_t) size * ind)));
	return ans;
}
