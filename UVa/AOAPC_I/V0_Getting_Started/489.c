#include <stdio.h>
#include <string.h>

#define MAXN 1000
char sol[MAXN];
char guess[MAXN];
int clean[MAXN];
int main() {
  int n, len_sol, len_gue;
  int i, j;
  int right, wrong;
  int flag;
  while (scanf("%d", &n) != EOF) {
    if (n==-1) break;
    printf ("Round %d\n", n);
    scanf ("%s", sol);
    len_sol = strlen(sol);
    scanf ("%s", guess);
    len_gue = strlen(guess);

    right = wrong = 0;
    memset(clean, 0, sizeof(int)*MAXN);
    for (i=0; i<len_gue; i++) {
      flag = 0;
      for (j=0; j<len_sol; j++)
        if (!clean[j] && sol[j] == guess[i]) {flag = 1; right++; clean[j]=1;}
      if (flag == 0) wrong++;

      if (right == len_sol) { printf ("You win.\n"); break; }
      if (wrong >= 7) { printf ("You lose.\n"); break; }
    }

    if (i==len_gue) printf ("You chickened out.\n");

  }

  return 0;
}
