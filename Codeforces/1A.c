#include <stdio.h>
#include <math.h>

int main() {
  double n, m, a;
  while (scanf ("%lf%lf%lf", &n,&m,&a)!=EOF) {
    printf ("%.0lf\n", ceil(n/a)*ceil(m/a));
  }
  return 0;
}
