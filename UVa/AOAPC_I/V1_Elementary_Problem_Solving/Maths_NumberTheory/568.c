#include <stdio.h>

#define N 100000000000

int main() {
  long long sum;
  int i, n;

  while (scanf ("%d", &n) != EOF) {
    sum = 1;
    for (i=1; i<=n; i++) {
      sum *= i;
      sum %= N;
      while (sum % 10 == 0) sum /= 10;
    }
    while (sum != 0 && sum % 10 == 0) sum /= 10;
    printf ("%5d -> %lld\n", n, sum % 10);
  }

  return 0;
}
