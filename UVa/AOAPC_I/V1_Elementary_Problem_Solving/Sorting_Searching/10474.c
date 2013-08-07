#include <stdio.h>
#include <stdlib.h>

#define N 10000+100

int num[N];

int compare (const void *_a, const void *_b) {
  int *a = (int*)_a;
  int *b = (int*)_b;

  return *a-*b;
}

int main() {
  int n, q, t;
  int i, j, c;

  c = 1;
  while (scanf ("%d%d", &n, &q) == 2) {
    if (n == 0 && q == 0) break;
    for (i=0; i<n; i++) 
      scanf ("%d", &num[i]);
    qsort (num, n, sizeof(int), compare);

    printf ("CASE# %d:\n", c++);
    for (i=0; i<q; i++) {
      scanf ("%d", &t);
      for (j=0; j<n; j++)
        if (num[j] == t) {printf ("%d found at %d\n", t, j+1); break;}
      if (j == n) printf ("%d not found\n", t);
    }
  }
  
  return 0;
}
