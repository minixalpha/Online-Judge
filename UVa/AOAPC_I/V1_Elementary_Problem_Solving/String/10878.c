#include <stdio.h>
#include <string.h>

#define MAX 20
char str[MAX];
int main() {
  int i;
  char * pos;
  int c;
  int pfactor[5] = {4, 8, 16, 32, 64};
  int nfactor[4] = {8,4,2,1};
  while (fgets(str, MAX, stdin)) {
    pos = strchr(str, '.');
    if (!pos) continue;
    c = 0;
    for (i=1; i<=4; i++) {
      if (*(pos-i) == 'o') c += pfactor[i];
      if (*(pos+i) == 'o') c += nfactor[i];
    }
    putchar(c);
  }

  return 0;
}
