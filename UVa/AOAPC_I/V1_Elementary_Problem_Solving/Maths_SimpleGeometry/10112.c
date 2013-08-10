/*
 * Problem: UVa 10112 - Myacm Triangles
 * Lang: ANSI C
 * Time: 0.009
 * Author: minix
 */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define N 100
#define EPS 1e-8

typedef struct _Mount{
  char label;
  int x;
  int y;
}Mount;

Mount mounts[N];

/* get size of triangle (a,b,c) */
double get_area(Mount a, Mount b, Mount c) {
  return fabs(0.5 * ((c.y-a.y)*(b.x-a.x) - (b.y-a.y)*(c.x-a.x)));
}
 
/* whether triangle (a,b,c) contains point d or not */
int contains(Mount a, Mount b, Mount c, Mount d) {
  double sum = get_area(a,b,d) + get_area(a,c,d) + get_area(b,c,d);
  double gap = sum - get_area(a,b,c);
  return (fabs(gap) < EPS) ? 1: 0;
}

void solve(Mount mounts[], int n, char result[]) {
  int i, j, k, s;
  double max = 0;

  for (i=0; i<n; i++)
    for (j=0; j<n; j++) {
      if (j == i) continue;
      for (k=0; k<n; k++) {
        if (k == j || k == i) continue;
        for (s=0; s<n; s++) {
          if (s == i || s == j || s == k)
            continue;
          if (contains(mounts[i], mounts[j], mounts[k], mounts[s]) == 1)
            break;
        }

        /* get max area */
        if ((s == n) && get_area(mounts[i], mounts[j], mounts[k]) > max) {
          max = get_area(mounts[i], mounts[j], mounts[k]);
          result[0] = mounts[i].label;
          result[1] = mounts[j].label;
          result[2] = mounts[k].label;
        }
      }
    }
  result[3] = '\0';
}

int cmp(const void *s, const void *t) {
  return *((char *)s) - *((char *)t);
}

int main() {
  int n, i;
  char result[4];

  while (1) {
    scanf ("%d", &n);
    if (n == 0)
      break;
    getchar(); /* read '\n' */

    for (i=0; i<n; i++) {
      scanf ("%c%d%d", &mounts[i].label, &mounts[i].x, &mounts[i].y);
      getchar();
    }

    solve (mounts, n, result);
    qsort (result, 3, sizeof(char), cmp);
    printf ("%s\n", result);

  }

  return 0;
}
