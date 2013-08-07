#include <stdio.h>
#include <math.h>

#define EPS 1e-8

int main() {
  double x1,y1,x2,y2;
  double ax1, ay1, ax2, ay2;
  double a, b;

  while (scanf ("%lf%lf%lf%lf", &x1, &y1, &x2, &y2) != EOF) {
    if (fabs(x1-x2)<EPS && fabs(y1-y2)<EPS) {
      printf ("Impossible.\n");
      continue;
    }

    a = (y1-y2+x2-x1)/2;
    b = (y1-y2-x2+x1)/2;

    ax1 = x2 - a;
    ay1 = y2 + b;
    ax2 = x2 + b;
    ay2 = y2 + a;

    printf ("%.10lf %.10lf %.10lf %.10lf\n", ax1, ay1, ax2, ay2);

  }

  return 0;
}
