#include <stdio.h>
#include <math.h>

int main() {
  double h, m;
  double degree;

  while (scanf ("%lf:%lf", &h, &m) != EOF) {
    if (h == 0 && m == 0) break;
    degree = fabs (m*6-h*30-0.5*m);
    if (degree > 180) 
      degree = 360-degree;
    printf ("%.3lf\n", degree);
  }

  return 0;
}
