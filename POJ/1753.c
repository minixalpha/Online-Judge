/*
 * Problem: POJ 1753 Flip Game
 * Lang: ANSI C
 * Time: 469MS
 * Memory: 388K
 * Code Length: 1358B
 * Author: minix
 */

#include <stdio.h>
#define N 20
#define M 4

int data[N];
char rect[M][M];

void fan(char tmp[M][M], int i, int j) {
  if (i<0 || j<0 || i>=M || j>=M)
    return;
  if (tmp[i][j] == 'b') tmp[i][j]='w';
  else tmp[i][j] = 'b';
}

void flip(char tmp[M][M], int n) {
  int row=n/M, col=n%M;
  fan(tmp, row, col);
  fan(tmp, row-1, col);
  fan(tmp, row+1, col);
  fan(tmp, row, col-1);
  fan(tmp, row, col+1);
}

int achieve(char tmp[M][M]) {
  int i, j, c;
  c = tmp[0][0];
  for (i=0; i<M; i++)
    for (j=0; j<M; j++)
      if (tmp[i][j]!=c)
        return 0;
  return 1;
}

int cmk (int *p, int start, int end, int n, int begin) {
  int i, j;
  char tmp[M][M];
  if (n == 0) {
    for (i=0; i<M; i++)
      for (j=0; j<M; j++)
        tmp[i][j] = rect[i][j];
    for (i=begin-1; i>=0; i--) {
      flip (tmp, p[i]);
    }
    if (achieve (tmp))
      return 1;
  }
  for (i=start; i<=end; i++) {
    p[begin] = i;
    if (cmk (p, i+1, end, n-1, begin+1) == 1)
      return 1;
  }
  return 0;
}

int main() {
  int i, j;

  for (i=0; i<M; i++) {
    for (j=0; j<M; j++) 
      scanf ("%c", &rect[i][j]);
    getchar();
  }

  for (i=0; i<M*M; i++)
    if (cmk (data, 0, 15, i, 0) == 1)
      break;
  if (i != M*M)
    printf ("%d\n", i);
  else
    printf ("Impossible\n");
  return 0;
}
