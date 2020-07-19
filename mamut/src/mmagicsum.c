#include <stdio.h>
#include "util.h"

int mmagicsum(t_matrix * ans, t_matrix * v, t_matrix * k)
{
	int op_type;
	
	if (v->dim != k->dim) {
		printf("mmagicsum: wrong matrix size\n");
		exit(1);
	}
	
	if (!v->type && !k->type) {
		op_type = 0; //both real
	} else if (!v->type && k->type) {
		op_type = 1; //v complex
	} else if (v->type && !k->type) {
		op_type = 2; //k complex
	} else if (v->type && k->type) {
		op_type = 3; //both complex
	} else {
		printf("mmagicsum: wrong matrix type\n");
		exit(1);
	}		
	
	ans->dim = v->dim;
	ans->n_dim = malloc(sizeof(int) * v->dim);
	ans->length = v->length;
	ans->type = 0;
	if (v->type || k->type) {
		ans->type = 1;
	}
	
	ans->vec = malloc((sizeof(double) + sizeof(double) * ans->type) * v->length);
	int v_size = (sizeof(double) + sizeof(double)*v->type);
	int k_size = (sizeof(double) + sizeof(double)*k->type);
	int ans_size  = (sizeof(double) + sizeof(double)*ans->type);
	void *v_val, *k_val;

	for (int i=0; i<v->dim;i++) {
		ans->n_dim[i] = v->n_dim[i];
	}
	
	switch (op_type) {
		case 0: for (unsigned int i=0;i<ans->length;i++) {
					double * a;
					v_val = get_mem_address(v,v_size,i);
					k_val = get_mem_address(k,k_size,i);
					a = get_mem_address(ans,ans_size,i);
					*a = __real(v_val) + __real(k_val);
				}
				break;
		case 1: for (unsigned int i=0;i<ans->length;i++) {
					double complex * a;
					v_val = get_mem_address(v,v_size,i);
					k_val = get_mem_address(k,k_size,i);
					a = get_mem_address(ans,ans_size,i);
					*a = __complex(v_val) + __real(k_val);
				}
				break;
		case 2: for (unsigned int i=0;i<ans->length;i++) {
					double complex * a;
					v_val = get_mem_address(v,v_size,i);
					k_val = get_mem_address(k,k_size,i);
					a = get_mem_address(ans,ans_size,i);
					*a = __complex(v_val) + __real(k_val);
				}
				break;
		case 3: for (unsigned int i=0;i<ans->length;i++) {
					double complex * a;
					v_val = get_mem_address(v,v_size,i);
					k_val = get_mem_address(k,k_size,i);
					a = get_mem_address(ans,ans_size,i);
					*a = __complex(v_val) + __complex(k_val);
				}
				break;
		default: 
				printf("mmagicsum: wrong matrix type\n");
				exit(1);
	}

	return 0;
}
