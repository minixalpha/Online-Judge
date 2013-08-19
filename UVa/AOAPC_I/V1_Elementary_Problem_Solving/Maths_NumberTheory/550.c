/*
 * Problem: 550 - Multiplying by Rotation
 * Lang: ANSI C
 * Time: 0.026
 * Author: minix
 */

#include <stdio.h>

int main() {
  long long base, f1, f2;
  long long a1, a2, c, n;
  while (scanf ("%lld%lld%lld", &base, &f1, &f2) != EOF) {
    a1 = f1; c = 0; n = 1;
    while (1) {
      a2 = (f2 * a1 + c) % base;
      c = (f2 * a1 + c ) / base;
      if (a2 == f1 && c ==0) break;
      a1 = a2;
      n ++;
    }

    printf ("%lld\n", n);

  }
  return 0;
}
