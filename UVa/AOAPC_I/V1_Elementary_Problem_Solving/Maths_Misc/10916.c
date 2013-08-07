#include <stdio.h>
#include <math.h>

int main() {
  int y;
  int m, n;
  int i;
  double sum, bound;

  while (scanf ("%d", &y) != EOF) {
    if (y == 0) break;
    m = (y-1960)/10+2;
    bound = pow(2,m)*log(2);

    n = 1; sum = 0;
    while (sum < bound)
      sum += log(n++);

    printf ("%d\n", n-2);
  }

  return 0;
}
