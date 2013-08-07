#include <stdio.h>
#include <string.h>

#define MAXN 1000
int secret[MAXN];
int guess[MAXN];
int s_use[MAXN];
int g_use[MAXN];

void hint (int *secret, int *guess, int n) {
  int strong = 0, weak = 0;
  int i, j;

  memset (s_use, 0, sizeof(s_use));
  memset (g_use, 0, sizeof(g_use));

  for (i=0; i<n; i++) 
    if (secret[i] == guess[i]) { strong++; s_use[i]=g_use[i]=1; }

  for (i=0; i<n; i++)
    for (j=0; j<n; j++)
      if (i!=j && !s_use[i] && !g_use[j] && secret[i]==guess[j]) {
        weak++;
        s_use[i] = g_use[j] = 1;
      }

  printf ("    (%d,%d)\n", strong, weak);
}

int main() {
  int i, n, count; 
  int allzero;

  count = 1;

  while (scanf ("%d", &n) != EOF) {
    if (n == 0) break;
    printf ("Game %d:\n", count++);

    for (i=0; i<n; i++)
      scanf ("%d", &secret[i]);
    while (1) {
      allzero = 1;
      for (i=0; i<n; i++) {
        scanf ("%d", &guess[i]);
        if (guess[i] != 0) allzero = 0;
      }
      if (allzero) break;

      hint(secret, guess, n);
    }
  }

  return 0;
}
