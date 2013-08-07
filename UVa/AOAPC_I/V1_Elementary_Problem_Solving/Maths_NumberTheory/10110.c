#include <stdio.h>
#include <math.h>

int main() {
  long long n, qn;

  while (scanf ("%lld", &n) != EOF) {
    if (n == 0) break;

    qn = (long long)sqrt(n);

    if (qn*qn == n) printf ("yes\n");
    else printf ("no\n");
  }

  return 0;
}
