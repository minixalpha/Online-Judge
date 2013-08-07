#include <stdio.h>

int main() {
  long long a, b, r, c;
  long long i, j;
  int times = 1;
  while (scanf ("%lld%lld", &a, &b) != EOF) {
    if (a==0 && b==0) break;
    r = b * (b-1) / 2;
    c = a * (a-1) / 2;

    printf ("Case %d: %lld\n", times++, r*c);
  }
  return 0;
}
