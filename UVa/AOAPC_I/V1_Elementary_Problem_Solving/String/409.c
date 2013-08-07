#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXN 30
#define LEN 80
char key[MAXN][MAXN];
char excu[MAXN][LEN];
int num[MAXN];

int main() {
  int k, e;
  int i, j, p, q, r;
  int max, maxi;
  int c = 1;
  char cur_word[MAXN];
  int len;

  while (scanf ("%d%d\n", &k, &e) == 2) {
    for (i=0; i<k; i++)
      scanf ("%s\n", key[i]);
    for (i=0; i<e; i++) {
      memset (excu[i], 0, LEN);
      fgets(excu[i], LEN, stdin);
    }

    printf ("Excuse Set #%d\n", c++);
    memset(num, 0, sizeof(int)*MAXN);
    max = 0; maxi = 0;
    for (i=0; i<e; i++) {
      j = 0; p = 0; q = 0;
      len = strlen(excu[i]);
      /* printf ("len:%d\n", len); */
      while (j < len) {
        /* printf ("j:%d ", j); */
        if (!isalpha(excu[i][j] )) {
          cur_word[p] = '\0';
          for (r=0; r<k; r++) 
            if (!strcmp(cur_word, key[r])) { num[i]++; break; } 
          p = 0; j++;
        } else {
          cur_word[p++] = tolower(excu[i][j++]);
        }
      }
      /* printf ("q%d:%d\n", i, num[i]); */
      if (num[i] > max) { max = num[i]; }
    }
    for (i=0; i<e; i++)
      if (num[i] == max) printf("%s", excu[i]);
    printf ("\n");
  }
  return 0;
}

