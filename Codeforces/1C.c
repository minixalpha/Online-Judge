#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define PI 3.1415926
#define EPS 1e-4

int cmp(const void *a, const void *b) {
  double da = *(double*)a;
  double db = *(double*)b;
  if (fabs(da-db)<EPS) return 0;
  if (da-db>EPS) return 1;
  return -1;
}

int istime(double x, double y) {
  int n = (int)(x/y+0.5);
  if (fabs(x-y*n)<EPS) return 1;
  else return 0;
}

double gcd(double x,double y)
{
    while(fabs(x)>EPS&&fabs(y)>EPS)
    {
        if(x>y)
            x-=floor(x/y)*y;
        else
          y-=floor(y/x)*x;
    }
    return x+y;
}

double dis(double x[2], double y[2]) {
  return sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]));
}

double area(double x[2], double y[2], double z[2]) {
  return fabs(
      (x[0]*y[1]+z[0]*x[1]+y[0]*z[1] - z[0]*y[1]-x[0]*z[1]-y[0]*x[1])/2
      );
}

double min(double x, double y) {
  if (x - y > EPS) return y;
  else return x;
}

int main() {
  double x[2], y[2], z[2], m[2];
  double xy,xz,yz;
  double p, q, l1, l2, l3;
  double s, d, cosd;
  double mx, my, mz;
  double da[3], t;
  while (scanf ("%lf%lf%lf%lf%lf%lf", &x[0], &x[1],&y[0],&y[1],&z[0],&z[1]) != EOF) {
    xy = dis(x,y); xz = dis(x,z); yz = dis(y,z);
    p = (xy*xy+xz*xz+yz*yz) / 2;
    q = 1/(1/(p-xy*xy)+1/(p-xz*xz)+1/(p-yz*yz));
    l1 = q/(p-xy*xy);
    l2 = q/(p-xz*xz);
    l3 = q/(p-yz*yz);
    m[0] = (1-l1)/2*z[0]+(1-l2)/2*y[0]+(1-l3)/2*x[0];
    m[1] = (1-l1)/2*z[1]+(1-l2)/2*y[1]+(1-l3)/2*x[1];
    mx = dis(m, x); my = dis(m, y); mz = dis(m, z);

    cosd = (mx*mx+my*my-xy*xy) / (2*mx*my);
    da[0] = acos(cosd);
    if (fabs(cosd+1)<EPS) da[0] = PI; 
    cosd = (mx*mx+mz*mz-xz*xz) / (2*mx*mz);
    da[1] = acos(cosd);
    if (fabs(cosd+1)<EPS) da[1] = PI; 
    cosd = (my*my+mz*mz-yz*yz) / (2*my*mz);
    da[2] = acos(cosd);
    if (fabs(cosd+1)<EPS) da[2] = PI; 
    qsort(da, 3, sizeof(double), cmp);
    d = da[0];
    t = 2;

    d = gcd (da[0], gcd(da[1],da[2]));

    while (!istime(2*PI, d)) {
       d /= t;
       t++;
    }

    s = mx*my*0.5*sin(d);
    printf ("%lf\n", PI/d*2*s);
    
  }
  return 0;
}
