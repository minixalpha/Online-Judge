#include <stdio.h>

int isSubSum(int m, int n) {
  if (m < 0) return 0;
  if (m == 0 && n >= 0) return 1;
  if (n == 1 && m==1 ) return 1;
  if (n == 1 && m!=1 ) return 0;
  return isSubSum(m-n, n-1) || isSubSum(m, n-1);
}

int main() {
  int sum,gap,m,n;
  int i, j;

  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%d", &m);
    if (m<0) m *= -1;
    sum = 0; j = 1;
    while (1) {
      sum += j; 
      gap = sum - m;
      if (gap>=0 && gap%2==0 && isSubSum(gap/2,j))
        break;
      j++;
    }
    printf ("%d\n", j);
    if (i!=(n-1)) printf ("\n");
  }

  return 0;
}
