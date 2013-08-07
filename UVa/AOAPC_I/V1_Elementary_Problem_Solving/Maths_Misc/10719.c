#include <stdio.h>
#include <string.h>

#define N 10000+10
#define M 100
int coeff[N];
int qcoeff[N];

int main() {
  int k, c;
  int m, n;
  int i, j;
  char num[M];

  while (scanf ("%d\n", &k) != EOF) {
    i=0; j=0;
    memset (qcoeff, 0, sizeof(int)*N);
    memset (coeff, 0, sizeof(int)*N);
    while (1) {
      c = getchar();
      if (c == ' ' || c == '\n') {
        num[j++] = '\0'; j = 0;
        sscanf (num, "%d", &coeff[i++]);
      } else {
        num[j++] = c;
      }
      if (c == '\n') break;
    }
    n = i;

    for (i=0; i<n-1; i++) {
      qcoeff[i] = coeff[i];
      coeff[i+1] = coeff[i+1] + k*coeff[i];
    }

    printf ("q(x):");
    for (i=0; i<n-1; i++)
      printf (" %d", qcoeff[i]);
    printf ("\n");
    printf ("r = %d\n\n", coeff[n-1]);
  }
  return 0;
}
