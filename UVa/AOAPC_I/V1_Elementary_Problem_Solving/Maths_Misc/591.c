#include <stdio.h>

#define N 50+10
#define H 100+10

int ht[N];

int main(void) {
  int n, sum, result, avg;
  int i, index;

  index = 1;
  while (1) {
    scanf ("%d", &n);
    if (n==0) break;
    for (i=0; i<n; i++)
      scanf ("%d", &ht[i]);

    sum = 0;
    for (i=0; i<n; i++) sum += ht[i];
    avg = sum / n;

    result = 0;
    for (i=0; i<n; i++) 
      if (ht[i]>avg) result += (ht[i]-avg);

    printf ("Set #%d\n", index++);
    printf ("The minimum number of moves is %d.\n\n", result);
  }
  return 0;
}
