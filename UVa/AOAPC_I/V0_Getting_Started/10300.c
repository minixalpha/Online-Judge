#include <stdio.h>
/*#define LOCAL*/

#define MAXN 25
int data[MAXN][3];

int main() {
#ifdef LOCAL
  freopen ("10300.in", "r", stdin);
#endif

  int i, j, k, n, f;
  int sum;
  scanf ("%d", &n);

  for (i=0; i<n; i++) {
    sum = 0;
    scanf ("%d", &f);
    for (j=0; j<f; j++)
    for (k=0; k<3; k++)
      scanf ("%d", &data[j][k]);
    for (j=0; j<f; j++)
      sum += data[j][0]*data[j][2];
    printf ("%d\n", sum);
  }

  return 0;
}
