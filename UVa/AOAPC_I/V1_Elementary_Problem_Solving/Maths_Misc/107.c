#include <stdio.h>
#include <math.h>
#include <float.h>
#define EPS 1e-8 /* 1e-6 will get WA */

int main() {
  double m, n;
  double i, j;
  double sum;

  while (scanf ("%lf%lf", &n, &m) != EOF) {
    if (m==0 && n==0) break;
    if (m == 1) {
      printf ("%.0lf %.0lf\n",log(n)/log(2),n*2-1);
      continue;
    }
    i = 1;
    while (fabs(log(i+1)/log(i) - log(n)/log(m)) > EPS) i++;
    j = log(m)/log(i);
    sum = m * (pow((i+1)/i,j+1)-1) / ((i+1)/i-1);
    printf ("%.0lf %.0lf\n", (m-1)/(i-1), sum);
  }

  return 0;
}
