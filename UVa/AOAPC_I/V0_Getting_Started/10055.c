#include <stdio.h>

int main() {
  long long m,n;
  while (scanf("%lld%lld",&m,&n)==2) {
    printf("%lld\n", (n-m)>=0?(n-m):(m-n));
  }

  return 0;
}
