#include <stdio.h>
#include <string.h>

#define MAXN 600
int bit0[MAXN];
int bit1[MAXN];
char cbit0[MAXN];
char cbit1[MAXN];
int sum[MAXN];
int bitp[MAXN];

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

void bitmul (int *sn, int n, int f) {
  int i=0, j=0;
  int c=0, midr=0;
  memset (bitp, 0, sizeof(int)*MAXN);
  while (i<f && i<MAXN) i++;
  for (j=0; j<MAXN && i<MAXN; j++) {
    midr = sn[j]*n+c;
    bitp[i++] = midr % 10;
    c = midr / 10;
  }
}

void bigprint (int *s) {
  int i = MAXN-1;
  while (i>0 && s[i] == 0) i--;
  while (i>=0) printf ("%d", s[i--]);
  printf ("\n");
}

void bigmul (int *s, int *t) {
  int i;
  memset (sum, 0, sizeof(int)*MAXN);
  for (i=0; i<MAXN; i++) {
    bitmul (s, t[i], i);
    bigadd (sum, bitp);
  }
}


int main() {
  while (fgets(cbit0, MAXN, stdin) != NULL) {
    fgets(cbit1, MAXN, stdin);
    memset (bit0, 0, sizeof(int)*MAXN);
    memset (bit1, 0, sizeof(int)*MAXN);
    assign (bit0, cbit0); 
    assign (bit1, cbit1);
    bigmul(bit0, bit1);
    bigprint (sum);
  }


  return 0;
}
