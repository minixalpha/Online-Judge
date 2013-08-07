#include <stdio.h>
#include <math.h>

int main() {
  int n, x, y, gap;
  int step, max;
  int i;

  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%d %d", &x, &y);
    gap = y - x; step = 0;

    if (gap == 0) { printf ("0\n"); continue; }
    max = (int)sqrt(gap);
    gap = gap - max*max;
    step += (2*max-1);
    while (gap != 0) {
      while (gap-max < 0) max--;
      step += 1; gap -= max;
    }
    
    printf ("%d\n", step);
  }
  
  return 0;
}
