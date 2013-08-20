/*
 * Problem: UVa 10050 Hartals
 * Lang: ANSI C
 * Time: 0.012s
 * Author: minix
 */
#include <stdio.h>
#include <string.h>

#define N 3650
#define P 100
int s[N];

int main() {
  int n, m, d, i, j, k, t, r, h;
  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    memset (s, 0, sizeof(s[0])*N);
    scanf ("%d", &d);
    scanf ("%d", &m);
    for (j=0; j<m; j++) {
      scanf ("%d", &h);
      t = h;
      while (t <= d) {
        s[t] = 1;
        t += h;
      }
    }
    t = 7; r = 0;
    for (j=1; j<=d; j++) {
      if (t!=5&&t!=6&&s[j]) r ++;
      t ++; if (t>7) t-= 7;
    }
    printf ("%d\n", r);
  }
  return 0;
}
