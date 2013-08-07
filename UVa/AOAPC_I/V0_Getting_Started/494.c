#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXN 10000
char buf[MAXN];

int main() {
  int i, len, sum;
  int newword;
  while (fgets(buf, MAXN, stdin) !=NULL) {
    sum = 0; newword=0;
    len = strlen(buf);
    for (i=0; i<len; i++) {
      if (newword==0 && isalpha(buf[i])) {
        newword = 1;
        sum += 1;
      }
      if (!isalpha(buf[i]))
        newword = 0;
    }

    printf ("%d\n", sum);
  }
  return 0;
}
