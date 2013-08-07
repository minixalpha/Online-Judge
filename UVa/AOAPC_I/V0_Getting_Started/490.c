#include <stdio.h>
#include <string.h>

#define MAX 120
char data[MAX][MAX];
int len[MAX];

int main() {
  int i, j, maxlen, num;

  i = 0; maxlen = 0;
  while (fgets(data[i], MAX, stdin) != NULL) {
    len[i] = strlen(data[i])-1;
    if (len[i] > maxlen) maxlen = len[i];
    ++i;
  }

  j = 0; num = i-1;
  for (j=0; j<maxlen; j++) {
    for (i=num; i>=0; i--) {
      if (j<len[i]) printf("%c", data[i][j]);
      else printf(" ");
    }

    printf ("\n");
  }

  return 0;
}
