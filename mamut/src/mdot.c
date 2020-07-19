#include <stdio.h>
#include "util.h"

int mdot(t_matrix * m, t_matrix * v, t_matrix * k)
{
	int op_type;

	if (v->n_dim[1]!=k->n_dim[0]) {
		printf("mdot: can't multiply, inner matrix dimensions must agree\n");
		printf("mdot: wrong matrix size\n");
		exit(1); //err
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
		printf("mdot: not recognized type\n");
		exit(1);
	}	
	
	if (!op_type) {
		minit(0,m,2,v->n_dim[0],k->n_dim[1]);
	} else {
		minit(1,m,2,v->n_dim[0],k->n_dim[1]);
	} 
			
	void * a = NULL;
	void * b = NULL;
	double real_c = 0.0;
	double complex complex_c = 0.0 + 0.0*I;
	
	switch (op_type) {
		case 0: for (int i=0;i<m->n_dim[0];i++) {
					for (int j=0;j<m->n_dim[1];j++) {
						for (int l=0;l<v->n_dim[1];l++) {
							a = get_from(v,2,i,l);
							b = get_from(k,2,l,j);
							real_c += __real(a)*__real(b);
						}
						put_at(m,&real_c,2,i,j);
						real_c = 0.0;
					}
				}
				break;
		case 1: for (int i=0;i<m->n_dim[0];i++) {
					for (int j=0;j<m->n_dim[1];j++) {
						for (int l=0;l<v->n_dim[1];l++) {
							a = get_from(v,2,i,l);
							b = get_from(k,2,l,j);
							complex_c += __real(a)*__complex(b);
						}
						put_at(m,&complex_c,2,i,j);
						complex_c = 0.0 + 0.0*I;
					}
				}
				break;
		case 2: for (int i=0;i<m->n_dim[0];i++) {
					for (int j=0;j<m->n_dim[1];j++) {
						for (int l=0;l<v->n_dim[1];l++) {
							a = get_from(v,2,i,l);
							b = get_from(k,2,l,j);
							complex_c += __complex(a)*__real(b);
						}
						put_at(m,&complex_c,2,i,j);
						complex_c = 0.0 + 0.0*I;
					}
				}
				break;
		case 3: for (int i=0;i<m->n_dim[0];i++) {
					for (int j=0;j<m->n_dim[1];j++) {
						for (int l=0;l<v->n_dim[1];l++) {
							a = get_from(v,2,i,l);
							b = get_from(k,2,l,j);
							complex_c += __complex(a)*__complex(b);
						}
						put_at(m,&complex_c,2,i,j);
						complex_c = 0.0 + 0.0*I;
					}
				}
				break;
		default: 
				printf("mdot: wrong matrix type\n");
				exit(1);
		}

	return 0;
}
