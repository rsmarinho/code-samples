#ifndef _WRAPPER_H_
#define _WRAPPER_H_

#include <math.h> 

#ifndef _MATRIX_H_
#include <matrix.h>
#define _MATRIX_H_
#endif

//general functions
int mabs(t_matrix * v);

//exponential functions
int mexp(t_matrix * v);
int mlog(t_matrix * v);

//power functions
int msqrt(t_matrix * v);
int mpow(t_matrix * v, double p);

//trigonometric functions
int msin(t_matrix * v);
int mcos(t_matrix * v);
int mtan(t_matrix * v);
int masin(t_matrix * v);
int macos(t_matrix * v);
int matan(t_matrix * v);

//hyperbolic functions
int msinh(t_matrix * v);
int mcosh(t_matrix * v);
int mtanh(t_matrix * v);
int masinh(t_matrix * v);
int macosh(t_matrix * v);
int matanh(t_matrix * v);

#endif
