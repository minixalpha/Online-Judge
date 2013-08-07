#include <stdio.h>

int main() {
  long long a,l,n; // be care of overflow
  int i;
  int count;

  i = 1;
  while (scanf("%lld%lld", &a, &l) == 2) {
    if (a<0 && l<0) { break; }
    n = a; count = 0;
    while (n <= l) {
      if (n == 1) { count++; break; }
      else if (n%2==0) n = n/2;
      else n = 3*n+1;
      count ++;
    }
    printf ("Case %d: A = %lld, limit = %lld, number of terms = %d\n", i++, a, l, count);
  }

  return 0;
}
