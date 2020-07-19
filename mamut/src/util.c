#include <stdio.h>
#include "util.h"

int ones(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = 1.0;
			a++;
		}
	} else if (v->type == 1) {
		double complex * a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = 1.0 + 1.0*I;
			a++;
		}
	} else {
		printf("ones: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int zeros(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = 0.0;
			a++;
		}
	} else if (v->type == 1) {
		double complex * a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = 0.0 + 0.0*I;
			a++;
		}
	} else {
		printf("zeros: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int linspace(t_matrix * v, double start, double end, int n)
{		
	if (n > v->length) {
		printf("linspace: out of bounds\n");
		exit(1); //err
	}
	
	if (v->type == 0) {
		double p;
		double *a;
		p = (end-start)/(n-1);
		a = v->vec;
		for(int i=0;i<n;i++) {
			*a = start + i * p;
			a++;
		}
	} else if (v->type == 1) {
		double p;
		double complex * a;
		p = (end-start)/(n-1);
		a = v->vec;
		for(int i=0;i<n;i++) {
			*a = start + i * p + 0.0*I;
			a++;
		}
	} else {
		printf("linspace: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int logspace(t_matrix * v, double start, double end, int n)
{		
	if (n > v->length) {
		printf("logspace: out of bounds\n");
		exit(1); //err
	}
	
	if (v->type == 0) {
		double p;
		double * a;
		p = (end-start)/(n-1);
		a = v->vec;
		for(int i=0;i<n;i++) {
			*a = pow(10., start + i * p);
			a++;
		}
	} else if (v->type == 1) {
		double p;
		double complex * a;
		p = (end-start)/(n-1);
		a = v->vec;
		for(int i=0;i<n;i++) {
			*a = pow(10., start + i * p) + 0.0*I;
			a++;
		}
	} else {
		printf("logspace: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int put_submatrix_at(t_matrix * v, t_matrix * k, int n_args, ...)
{
	//~ int op_type;

	va_list valist;
	va_start(valist,n_args);
	unsigned int index_from[2];
	unsigned int index_to[2];
	
	index_from[0] = va_arg(valist,unsigned int);
	index_from[1] = va_arg(valist,unsigned int);
	index_to[0] = va_arg(valist,unsigned int);
	index_to[1] = va_arg(valist,unsigned int);
	va_end(valist);
		
	if (v->dim < k->dim) { // test for matrix size. K must be bigger than V
		printf("put_submatrix_at: wrong matrix size\n");
		exit(1); //err
	}
	int i_test = index_of(v, index_to[0], index_to[1]);
	if (i_test > v->length) { //test for out of bounds index
		printf("put_submatrix_at: index size, out of bounds\n");
		exit(1); //err
	}
	
	if (k->n_dim[0] > index_to[0]-v->n_dim[0] || 
		k->n_dim[1] > index_to[1]-v->n_dim[1] ) { // test to index diff
		printf("put_submatrix_at: index difference must be equal to submatrix size\n");
		exit(1); //err
	}	
	
	int k_size;
	
	if (!v->type && !k->type) {
		k_size = sizeof(double);
	} else if (!v->type && k->type) {
		k_size = 2*sizeof(double);
		printf("put_submatrix_at: lost imaginary part\n");
	} else if (v->type && !k->type) {
		k_size = sizeof(double);
	} else if (v->type && k->type) {
		k_size = 2*sizeof(double);
	} else {
		printf("put_submatrix_at: wrong matrix type\n");
		return -1;
	}
	
	void * a;
	double complex b = 0.0 + 0.0*I;
	unsigned index;
	
	if (v->type == 0) {
		for (unsigned int i=0; i<k->n_dim[0]; i++) {
			for (unsigned int j=0; j<k->n_dim[1]; j++) {
				index = index_of(k,j,i);
				a = get_mem_address(k, k_size, index);
				put_at(v, a, 2, i+index_from[0], j+index_from[1]);
			}
		} 
	} else if (v->type == 1) {
		for (unsigned int i=0; i<k->n_dim[0]; i++) {
			for (unsigned int j=0; j<k->n_dim[1]; j++) {
				index = index_of(k,j,i);
				a = get_mem_address(k, k_size, index);
				b = __real(a);
				put_at(v, &b, 2, i+index_from[0], j+index_from[1]);
			}
		} 
	} else {
		printf("put_submatrix_at: type error\n");
	}
	
	//~ switch (op_type) {
		//~ case 0: 
				//~ break;
		//~ case 1: 
				//~ break;
		//~ case 2: 
				//~ break;
		//~ case 3: 
				//~ break;
		//~ default: 
				//~ printf("mmagicsum: wrong matrix type\n");
				//~ exit(1);
	//~ }

	return 0;
}
