#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>

#define MAXN 100
char line [MAXN];
char P[20],I[20],U[20];
int main() {
  int len, n;
  int i, j, k;
  double p,is,u;

  scanf ("%d\n", &n);
  for (i=1; i<=n; i++) {
    memset(line, 0, MAXN);
    memset(P, 0, 20);
    memset(I, 0, 20);
    memset(U, 0, 20);
    fgets(line, MAXN, stdin);

    len = strlen(line);
    for (j=0; j<len; j++) {
      if (line[j] == '=') {
        assert(j>0);
        k = 0;
        if (line[j-1] == 'P') {
          j ++;
          while (isdigit(line[j]) || line[j] == '.')
            P[k++] = line[j++];
          sscanf (P, "%lf", &p);
          if (line[j] == 'm') p /= 1000;
          if (line[j] == 'M') p *= 1000000;
          if (line[j] == 'k') p *= 1000;
        }
        if (line[j-1] == 'U') {
          j ++;
          while (isdigit(line[j]) || line[j] == '.')
            U[k++] = line[j++];
          sscanf (U, "%lf", &u);
          if (line[j] == 'm') u /= 1000;
          if (line[j] == 'M') u *= 1000000;
          if (line[j] == 'k') u *= 1000;
        }
        if (line[j-1] == 'I') {
          j ++;
          while (isdigit(line[j]) || line[j] == '.')
            I[k++] = line[j++];
          sscanf (I, "%lf", &is);
          if (line[j] == 'm') is /= 1000;
          if (line[j] == 'M') is *= 1000000;
          if (line[j] == 'k') is *= 1000;
        }
      }
    }

    printf ("Problem #%d\n", i);
    if (P[0] == '\0') printf ("P=%.2lfW\n", u * is);
    else if (I[0] == '\0') printf ("I=%.2lfA\n", p/u);
    else printf ("U=%.2lfV\n", p/is);
    printf ("\n");
  }

  return 0;
}
