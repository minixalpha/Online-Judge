#include <stdio.h>
#include <string.h>

#define MAX 100000
int flag[MAX];

int solve(int z, int i, int m, int l) {
  int cycle;
  memset (flag, 0, sizeof(int)*MAX);

  cycle = 0;
  while (1) {
    l = (z*l%m+i) % m;
    if (flag[l] == 1) break;
    flag[l] = 1;
    cycle++;
  }

  return cycle;
}

int main() {
  int z, i, m, l;
  int index;

  index = 1;
  while (scanf ("%d%d%d%d", &z, &i, &m, &l) != EOF) {
    if (z==0 && i==0 && m==0 && l==0) break;
    solve(z,i,m,l);

    printf ("Case %d: %d\n", index++, solve(z,i,m,l)); 
  }

  return 0;
}
