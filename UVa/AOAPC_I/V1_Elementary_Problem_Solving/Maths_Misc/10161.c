#include <stdio.h>
#include <math.h>

long long max (long long a, long long b) {
  return (a>b)?a:b;
}

long long min (long long a, long long b) {
  return (a<b)?a:b;
}

int main() {
  long long n;
  long long s, t;
  long long r, c;
  while (scanf ("%lld", &n) != EOF) {
    if (n == 0) break;
    s = (long long) sqrt(1.0*n);
    if (s*s == (long long)n) s = s - 1;
    t = s + 1;

    s = s * s + 1; t = t * t;

    if (t % 2 == 0) {
      printf ("%lld %lld\n", min((s+t)/2,n)-s+1, t-max((s+t)/2,n)+1 );
    } else {
      printf ("%lld %lld\n", t-max((s+t)/2,n)+1, min((s+t)/2,n)-s+1 );
    }
  }
  return 0;
}
