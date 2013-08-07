#include <stdio.h>

int main() {
  int n, i;
  long long k, a, b, c, d, j;

  scanf ("%d", &n);
  for (i=1; i<=n; i++) {
    scanf ("%lld", &k);
    for (j=2; j<k; j++)
      if (k % j == 0) break;
    a = j; b = k / j;

    for (j=j+1; j<k; j++)
      if (k % j == 0) break;
    c = j; d = k / j;
    printf ("Case #%d: %lld = %lld * %lld = %lld * %lld\n", i, k, a, b, c, d);
  }

  return 0;
}
