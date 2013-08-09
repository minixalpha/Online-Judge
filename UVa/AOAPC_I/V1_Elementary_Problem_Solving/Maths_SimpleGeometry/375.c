#include <stdio.h>
#include <math.h>

#define TIME 1000000
#define LIMIT (0.000001*TIME)
#define PI acos(-1)

double getR (double b, double h) {
  return b*h/(b+2*sqrt(b*b/4+h*h));
}

double solve (double b, double h) {
  double sum, r, old_h;

  sum = 0.0;
  while ( (r=getR(b, h)) >= LIMIT) {
    sum += 2*PI*r;
    old_h = h;
    h -= 2*r;
    b = b*h/old_h;
  }

  return sum;
}

int main() {
  int n, i;
  double b, h, c;

  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%lf%lf", &b, &h);
    b *= TIME; h *= TIME;
    c = solve (b, h);
    printf ("%13.6f\n", c/TIME);
    if (i != (n-1)) 
      printf ("\n");
  }

  return 0;
}
