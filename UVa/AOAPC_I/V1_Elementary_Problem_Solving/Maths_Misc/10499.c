#include <stdio.h>

int main() {
  double n; /* n must be double */

  while (scanf ("%lf", &n) != EOF) {
    if (n < 0) break;
    if (n == 1) printf ("0%%\n");
    else printf ("%.0lf%%\n", ((n/4.0)*100));
  }

  return 0;
}
