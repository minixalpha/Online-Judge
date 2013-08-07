#include <stdio.h>
#include <math.h>

int main() {
  int t;
  int i;
  double m, n;

  scanf ("%d", &t);
  for (i=0; i<t; i++) {
    scanf ("%lf%lf", &n, &m);
    printf ("%.0lf\n", ( ceil((n-2)/3) ) * ( ceil((m-2)/3) ));
  }

  return 0;
}
