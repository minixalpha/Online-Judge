#include <stdio.h>

#define MAXN 15
char data[MAXN][30];
int pos[MAXN][2];

int main() {
  int i, j, n, min, gap, total;
  while (scanf("%d\n",&n) == 1) {
    if (n == 0) break;

    for (i=0; i<n; i++)
      fgets(data[i], 30, stdin);

    for (i=0; i<n; i++) {
      pos[i][0] = pos[i][1] = 0;
      for (j=0; j<25; j++) 
        if (data[i][j] == ' ') { pos[i][0] = j-1; break; }
      for (j=24; j>=0; j--)
        if (data[i][j] == ' ') { pos[i][1] = j; break; }
    }
    
    min = pos[0][1] - pos[0][0];
    for (i=1; i<n; i++) {
      gap = pos[i][1] - pos[i][0];
      min = (gap<min) ? gap : min;
    }

    total = 0;
    for (i=0; i<n; i++)
      total += (pos[i][1]-pos[i][0]-min);

    printf ("%d\n", total);

  }

  return 0;
}
