/*
 * Problem: UVa 10152 - ShellSort
 * Lang: ANSI C
 * Time: 0.046
 * Author: minix
 */
#include <stdio.h>
#include <string.h>

#define N (200+10)
#define M (80+10)
char s[N][M];
char d[N][M];
int flag[N];

int main () {
  int count;
  int i, j, k;
  int n;

  scanf ("%d", &count);
  for (i=0; i<count; i++) {
    memset (flag, 0, sizeof(int)*N);
    scanf ("%d", &n);
    getchar();
    for (j=0; j<n; j++)
      fgets (s[j], sizeof(s[j][0])*M, stdin); 
    for (j=0; j<n; j++)
      fgets (d[j], sizeof(d[j][0])*M, stdin);

    /* find immobile sequence */
    for (j=n-1, k=n-1; j>=0; j--) {
      if (!strcmp (s[j],d[k])) { 
        flag[k] = 1;
        k -= 1;
      }
    }
    /* output mobile sequence */
    for (j=n-1; j>=0; j--) {
      if (flag[j] != 1)
        printf ("%s", d[j]);
    }

    printf ("\n");
  }
  return 0;
}
