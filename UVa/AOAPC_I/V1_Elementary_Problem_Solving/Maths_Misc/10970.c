#include <stdio.h>

#define M 300+10
#define N 300+10
int dict[M][N];

int main() {
  int m, n;
  int i, j;
  for (i=1; i<M; i++)
    for (j=1; j<N; j++)
      dict[i][j] = i*j-1;

  while (scanf ("%d%d",&m,&n) != EOF) {
    printf ("%d\n", dict[m][n]);
  }
  return 0;
}
