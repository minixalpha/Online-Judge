#include <stdio.h>

#define N 3650
#define P 100
int h[P];

int main() {
  int n, m, d, i, j, k, t, r;
  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%d", &d);
    scanf ("%d", &m);
    for (j=0; j<m; j++){
      scanf ("%d", &h[j]);
    }
    r = 0; t = 7;
    for (j=1; j<=d; j++) {
      for (k=0; k<m; k++)
        if (j%h[k]==0 && t!=5 &&t!=6) { r++; break; }
      t++; 
      if (t>7) t-= 7;
    }
    printf ("%d\n", r);
  }
  return 0;
}
