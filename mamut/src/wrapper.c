#include <stdio.h>
#include "wrapper.h"

int mabs(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = fabsf(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = cabsf(*a);
			a++;
		}
	} else {
		printf("mabs: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mexp(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = exp(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = cexp(*a);
			a++;
		}
	} else {
		printf("mexp: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mlog(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = log(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = clog(*a);
			a++;
		}
	} else {
		printf("mlog: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int msqrt(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = sqrt(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = csqrt(*a);
			a++;
		}
	} else {
		printf("msqrt: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mpow(t_matrix * v, double p)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = pow(*a,p);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = cpow(*a,p);
			a++;
		}
	} else {
		printf("mpow: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int msin(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = sin(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = csin(*a);
			a++;
		}
	} else {
		printf("msin: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mcos(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = acos(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = ccos(*a);
			a++;
		}
	} else {
		printf("mcos: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mtan(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = tan(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = ctan(*a);
			a++;
		}
	} else {
		printf("mtan: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int masin(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = asin(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = casin(*a);
			a++;
		}
	} else {
		printf("masin: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int macos(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = acos(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = cacos(*a);
			a++;
		}
	} else {
		printf("macos: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int matan(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = atan(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = catan(*a);
			a++;
		}
	} else {
		printf("matan: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int msinh(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = sinh(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = csinh(*a);
			a++;
		}
	} else {
		printf("msinh: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mcosh(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = acosh(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = ccosh(*a);
			a++;
		}
	} else {
		printf("mcosh: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int mtanh(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = tanh(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = ctanh(*a);
			a++;
		}
	} else {
		printf("mtanh: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int masinh(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = asinh(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = casinh(*a);
			a++;
		}
	} else {
		printf("masinh: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int macosh(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = acosh(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = cacosh(*a);
			a++;
		}
	} else {
		printf("macosh: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}

int matanh(t_matrix * v)
{	
	if (v->type == 0) {
		double *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = atanh(*a);
			a++;
		}
	} else if (v->type == 1) {
		double complex *a;
		a = v->vec;
		for (int i=0;i<v->length;i++) {
			*a = catanh(*a);
			a++;
		}
	} else {
		printf("matanh: not recognized type\n");
		exit(1); //err
	}
	
	return 0;
}
