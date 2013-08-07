#include <stdio.h>

int solve(int step, int mod) {
  int i;
  int sum,total;

  sum = total = 0;
  for (i=0; i<mod; i++) {
    sum += step;
    sum %= mod;
    total += sum;
  }

  return total == (mod*(mod-1)/2);
}

int main() {
  int step, mod;

  while (scanf ("%d%d", &step, &mod) != EOF) {
    printf ("%10d%10d    %s\n\n", step, mod, solve(step,mod) ? "Good Choice" : "Bad Choice");
  }

  return 0;
}
