#include <stdio.h>
#include <stdlib.h>
#include <matrix.h>
#include <util.h>
#include <mdot.h>
#include <mmagicdot.h>
#include <mmagicsum.h>
#include <mtranspose.h>
#include <wrapper.h>

#define PI 3.14

int test_index_of()
{
	t_matrix v;

	minit(0,&v,2,100,100);
	linspace(&v,0,99,10000);
	
	printf("%f\n", __real(get_from(&v,2,99,99)));
	printf("\n");
	
//	printm(&v);
	
	mclose(&v);
	printf("close v\n");
	
	return 0;
	
}

int m_init() {
	t_matrix v;
	double a;

	minit(0,&v,2,6,6);
	ones(&v);
	a = 44.0;
	put_at(&v,&a,2,3,3);
	printm(&v);
	printf("\n");
	
	//~ zeros(&v);
	//~ printm(&v);
	//~ printf("\n");
	
	//~ linspace(&v,0,35,33);
	//~ printm(&v);
	//~ printf("\n");
	
	//~ logspace(&v,0,35,36);
	//~ printm(&v);
	//~ printf("\n");
	
	mclose(&v);
	printf("close v\n");
	
	return 0;
}

int m_complex_init() {
	t_matrix v;
	double complex a;

	minit(1,&v,2,6,6);
	ones(&v);
	a = 5.0 + 6.0*I;
	put_at(&v,&a,2,3,3);
	printm(&v);
	printf("\n");
	
	//~ zeros(&v);
	//~ printm(&v);
	//~ printf("\n");
	
	//~ linspace(&v,0,35,36);
	//~ printm(&v);
	//~ printf("\n");
	
	//~ logspace(&v,0,35,36);
	//~ printm(&v);
	//~ printf("\n");
	
	mclose(&v);
	printf("close v\n");
	
	return 0;
}

int m_multiply() {
	
	t_matrix v;
	t_matrix k;
	t_matrix m;
	
	double complex a;
	a = 5.5 + 88*I;
		
	minit(1,&v,2,2,3);
	linspace(&v,1,6,6);
	put_at(&v,&a,2,1,2);
	printm(&v);
	printf("\n------------\n");
	
	minit(0,&k,2,3,4);
	linspace(&k,1,12,12);
	//~ put_at(&k,&a,2,0,1);
	printm(&k);
	printf("\n------------\n");
	
	mdot(&m,&v,&k);
	printm(&m);
	printf("\n------------\n");
	
	//~ mdot(&m,&k,&v);
	//~ printm(&m);
	//~ printf("\n------------\n");
	
	mclose(&v);
	mclose(&k);
	mclose(&m);
	
	return 0;
}

int m_transpose() {
	
	t_matrix v;
	t_matrix k;
	t_matrix m;
	
	minit(0,&v,2,1,3);
	linspace(&v,1,3,3);
	
	printm(&v);
	
	k = mtranspose(&v);
	printm(&k);
	
	mdot(&m,&v,&k);
	printm(&m);
	
	mdot(&m,&k,&v);
	printm(&m);
	
	mclose(&v);
	mclose(&k);
	mclose(&m);
	
	return 0;
}

int m_magicsum() {
	
	t_matrix v;
	t_matrix k;
	t_matrix m;
	
	minit(0,&v,2,1,3);
	linspace(&v,1,3,3);
	
	printm(&v);
	
	k = v;
	printm(&k);
	
	mmagicsum(&m,&v,&k);
	printm(&m);
	
	mclose(&v);
	mclose(&k);
	mclose(&m);
	
	return 0;
}

int put_submatrix() {
	
	t_matrix v;
	t_matrix k;
	
	minit(0,&v,2,3,3);
	linspace(&v,1,9,9);	
	printm(&v);
	
	minit(1,&k,2,6,5);
	printm(&k);
	
	put_submatrix_at(&k,&v,4,0,1,2,3);
	printm(&k);
	
	//~ put_submatrix_at(&k,&v,4,2,3,4,5); // nao funciona
	//~ printm(&k);
	
	v = mtranspose(&v);
	put_submatrix_at(&k,&v,4,3,2,5,4); //funciona
	printm(&k);
	
	mclose(&v);
	mclose(&k);
	
	return 0;
}

int main (void) {
	//~ test_index_of();
	//~ m_init();
	//~ m_complex_init();
	//~ m_multiply();
	//~ m_transpose();
	//~ m_magicsum();
	put_submatrix();
	
	return 0;
}
