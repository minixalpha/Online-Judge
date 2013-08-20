/*
 * Problem: UVa 540 Team Queue
 * Lang: ANSI C
 * Time: 0.042s
 * Author: minix
 */
#include <stdio.h>

#define T 1000+10
#define N 1000000+10
int g[N];
int l[T];
int q[T], qh, qt;
int t[T][T],th[T], tt[T];

int main() {
  int n, m, i, j, k, e, cg;
  char line[50], cmd[10];

  k = 1;
  while (scanf("%d",&n)!=EOF) {
    if (n == 0) break;
    for (i=0; i<n; i++) {
      scanf("%d",&m);
      l[i] = -1; th[i] = tt[i] = 0;
      for (j=0; j<m; j++) {
        scanf ("%d",&e);
        g[e] = i;
      }
    }
    qh = qt = 0;
    printf ("Scenario #%d\n", k++);
    while (fgets(line,sizeof(line[0])*50,stdin)) {
      if (line[0]=='S') break;
      if (line[0]=='E') {
        sscanf (line, "%s %d\n", cmd, &e);
        cg = g[e];
        if (l[cg] == -1) {
          l[cg] = qt;
          q[qt++] = cg;
        }
        t[cg][tt[cg]++] = e;
      } else if (line[0]=='D') {
        cg = q[qh];
        printf ("%d\n", t[cg][th[cg]++]);
        if (th[cg] == tt[cg]) {
          qh++;
          l[cg] = -1;
        }
      }
    }
    printf ("\n");
  }
  return 0;
}

