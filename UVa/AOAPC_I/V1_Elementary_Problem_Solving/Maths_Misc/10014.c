#include <stdio.h>

#define N 3000+100

double cdata[N];

int main() {
  int m, n;
  int i, j;
  double a0, anp1;
  double sum;

  scanf ("%d", &m);
  for (i=0; i<m; i++) {
    scanf ("%d", &n);
    scanf ("%lf", &a0);
    scanf ("%lf", &anp1);
    for (j=1; j<=n; j++) {
      scanf ("%lf", &cdata[j]);
    }
    sum = anp1 + n*a0;
    for (j=1; j<=n; j++)
      sum -= 2*(n+1-j)*cdata[j];
    printf ("%.2lf\n", sum/(n+1));
    if (i!=(m-1)) printf ("\n");
  }

  return 0;
}
