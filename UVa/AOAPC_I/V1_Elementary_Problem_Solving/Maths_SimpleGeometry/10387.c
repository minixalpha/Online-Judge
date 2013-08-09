#include <stdio.h>
#include <math.h>

#define PI acos(-1)

int main() {
  double a, b, s, m, n;
  double angle, velocity;

  while (scanf ("%lf%lf%lf%lf%lf", &a, &b, &s, &m, &n) != EOF) {
    if (a == 0 && b==0 && s==0 && m==0 && n==0) 
      break;
    angle = atan( (b*n)/(a*m) ) * 180 / PI;
    velocity = sqrt(b*n*b*n+a*m*a*m) / s;
    printf ("%.2lf %.2lf\n", angle, velocity);
  }

  return 0;
}
