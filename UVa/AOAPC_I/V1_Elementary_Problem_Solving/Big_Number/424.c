#include <stdio.h>
#include <string.h>

#define MAXN 200
int bit[MAXN];
char cbit[MAXN];
int sum[MAXN];

void assign (int *n, char *s) {
  int i=0, j=0;
  while (s[i] != '\n') ++i;
  while (i>=1) n[j++] = s[--i]-'0';
}

void bigadd (int *sn, int *n) {
  int i, tmp, c = 0;
  for (i=0; i<MAXN; i++) {
    tmp = sn[i] + n[i] + c;
    sn[i] = tmp % 10;
    c = tmp / 10;
  }
}

void bigprint (int *s) {
  int i = MAXN-1;
  while (i>0 && s[i] == 0) i--;
  while (i>=0) printf ("%d", s[i--]);
  printf ("\n");
}

int main() {
  memset (sum, 0, sizeof(int)*MAXN);
  while (fgets(cbit, MAXN, stdin) != NULL) {
    if (cbit[0] == '0' && cbit[1] == '\n') break;
    memset (bit, 0, sizeof(int)*MAXN);
    assign (bit, cbit);
    bigadd (sum, bit);
  }

  bigprint (sum);

  return 0;
}


