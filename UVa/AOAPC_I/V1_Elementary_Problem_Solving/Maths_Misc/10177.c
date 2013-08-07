#include <stdio.h>

/* use double instead of int */
int main() {
  int n, i;
  double s2, r2, s3, r3, s4, r4;
  double sum;

  while (scanf ("%d", &n) != EOF) {
    s2 = s3 = s4 = 0;
    for (i=1; i<=n; i++) {
      sum = (n+1-i)*(n+1-i);
      s2 += sum;
      sum *= (n+1-i);
      s3 += sum;
      sum *= (n+1-i);
      s4 += sum;
    }



    r2 = r3 = r4 = 0;
    for (i=1; i<=n; i++) {
      sum = (n+1-i)*((1+n)*n/2);
      r2 += sum;
      sum *= ((1+n)*n/2);
      r3 += sum;
      sum *= ((1+n)*n/2);
      r4 += sum;
    }
    r2 -= s2;
    r3 -= s3;
    r4 -= s4;

    printf ("%.0lf %.0lf %.0lf %.0lf %.0lf %.0lf\n", s2, r2, s3, r3, s4, r4);
  }

  return 0;
}
