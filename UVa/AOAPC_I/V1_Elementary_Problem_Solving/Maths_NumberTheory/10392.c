#include <stdio.h>
#include <string.h>

#define N 1000000
long long prime[N];
short is_prime[N];

long long get_prime (long long prime[], long long n) {
  long long i, j, k;
  memset (is_prime, 0, sizeof(is_prime[0])*n);  

  j = 0;
  for (i=2; i<n; i++) {
    if (!is_prime[i]) prime[j++] = i;
    for (k=0; k<j && i*prime[k]<n; k++) {
      is_prime[ i*prime[k] ] = 1;
      if (!i%prime[k]) break;
    }
  }

  return j;
}

int main() {
  long long n;
  long long i;
  long long prime_num;

  prime_num = get_prime (prime, N);

  while (scanf ("%lld", &n) != EOF) {
    if (n == -1) break;

    for (i=0; i<prime_num && n!=1; i++) {
      while (n % prime[i] == 0) {
        printf ("    %lld\n", prime[i]);
        n /= prime[i];
      }
    }
    if (n != 1) printf ("    %lld\n", n);
    printf ("\n");
  }

  return 0;
}
