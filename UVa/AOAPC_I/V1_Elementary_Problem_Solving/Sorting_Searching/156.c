#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define DEBUG

#define N 1000+10
#define M 20+5

char words[N][M];

int cmp (const void *_a, const void *_b) {
  char *a = (char *)_a;
  char *b = (char *)_b;
  return strcmp(a,b);
}

int cmpChar (const void *_a, const void *_b) {
  char *a = (char *)_a;
  char *b = (char *)_b;

  return *a-*b;
}

int isrearran (char *s, char *t) {
  char ts[M], tt[M];
  int i, j;
  memset (ts, 0, sizeof(ts));
  memset (tt, 0, sizeof(tt));
  i = j = 0;

  while (s[i]) { ts[i] = tolower(s[i]); i++; }
  while (t[j]) { tt[j] = tolower(t[j]); j++; }

  qsort (ts, i, sizeof(ts[0]), cmpChar);
  qsort (tt, i, sizeof(tt[0]), cmpChar);

  return !strcmp(ts, tt);
}

int main() {
  int i, j, k;
  int n;

  i = 0;
  while (scanf ("%s", words[i]) && strcmp(words[i], "#")) i++;
  n = i;

  qsort (words, n, sizeof(words[0]), cmp);

#ifdef DEBUG_1
  for (j=0; j<i; j++)
    printf ("%s \n", words[j]);
#endif

  for (i=0; i<n; i++) {
    for (j=0; j<n; j++) if (j!=i)
      if (isrearran (words[i], words[j])) break;
    if (j==n) printf ("%s\n", words[i]);
  }



  return 0;
}
