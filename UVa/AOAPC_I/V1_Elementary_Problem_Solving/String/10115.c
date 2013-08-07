#include <stdio.h>
#include <string.h>

#define N 20
#define MAXN 300
char find[N][MAXN];
char replace[N][MAXN];
char text[MAXN];
char newtext[MAXN];

void edit(int n ) {
  int flag;
  int i, j, k, t;
  int p, q, r;

  for (i=0; i<n; i++) {
    flag = 1;
    while (flag) {
      flag = 0;
      for (k=0; text[k]!='\n'; k++) {
        j = 0; t=k;
        while (find[i][j] != '\n' && text[t] != '\n') {
          if (find[i][j] != text[t]) break;
          else {j++; t++;}
        }
        if (find[i][j] == '\n') {
          flag = 1;
          r = 0;
          for (p=0; p<k; p++, r++) newtext[r] = text[p];
          for (q=0; replace[i][q]!='\n'; q++,r++) newtext[r] = replace[i][q];
          for (p=t; text[p]!='\n'; p++,r++) newtext[r] = text[p];
          newtext[++r] = '\n';
          while (r>=0) { text[r]=newtext[r]; r--; }
          break;
        }
      }
    }
  }
}

int main() {
  int n;
  int i;

  freopen ("autoedit.in", "r", stdin);
  freopen ("autoedit.out", "w", stdout);

  while (scanf ("%d\n", &n) != EOF) {
    memset (find, 0, N*MAXN);
    memset (replace, 0, N*MAXN);
    memset (text, 0, MAXN);
    memset (newtext, 0, MAXN);
    if (n == 0) break;
    for (i=0; i<n; i++) {
      fgets (find[i], MAXN, stdin);
      fgets (replace[i], MAXN, stdin);
    }
    fgets (text, MAXN, stdin);
    edit(n);
    puts(text);
  }

  return 0;
}
