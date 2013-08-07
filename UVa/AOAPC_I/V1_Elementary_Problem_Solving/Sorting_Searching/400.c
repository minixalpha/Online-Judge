#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define N 100+10
#define M 60+10

char names[N][M];

int cmp(const void *_a, const void *_b) {
  char *a = (char *)_a;
  char *b = (char *)_b;
  return strcmp(a, b);
}

int main() {
  int n, maxlen;
  int i, j, k;
  int r, c;
  while (scanf ("%d", &n) != EOF) {
    for (i=0; i<n; i++) scanf ("%s", names[i]);

    for (i=0; i<60; i++) printf("-");
    printf ("\n");

    qsort (names, n, sizeof(names[0]), cmp);
    maxlen = strlen(names[0]);
    for (i=1; i<n; i++)
      if (strlen(names[i]) > maxlen) maxlen = strlen(names[i]);
    c = 1 + (60-maxlen)/(maxlen+2);
    r = n / c;
    if (n % c != 0) r++;

    for (i=0; i<r; i++) {
      for (j=0; j<c; j++) 
        if (j*r+i < n) {
          printf ("%s", names[j*r+i]);
          for (k=strlen(names[j*r+i]); k<maxlen+2; k++) printf(" ");
        }
      printf ("\n");
    }
  }

  return 0;
}
