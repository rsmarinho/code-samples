#include <stdio.h>
#include "util.h"

t_matrix mtranspose(t_matrix * v)
{
	void * a = malloc(sizeof(double) + sizeof(double)*v->type);
		
	t_matrix ans;	
	minit(v->type,&ans,v->dim,v->n_dim[1],v->n_dim[0]);
	
	for (int i=0; i<ans.n_dim[0];i++) {
		for (int j=0; j<ans.n_dim[1];j++) {
			a = get_from(v,2,j,i);
			put_at(&ans,a,2,i,j);
		}
	}
	
	return ans;
}
