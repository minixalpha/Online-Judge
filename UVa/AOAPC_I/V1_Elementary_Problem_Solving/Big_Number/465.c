#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

#define MAXN 1000
int bit0[MAXN];
int bit1[MAXN];
char cbit0[MAXN];
char cbit1[MAXN];
char line[MAXN];
int sum[MAXN];
int bitp[MAXN];
int max[MAXN];

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

int moreThanMax (int *n, int *max) {
  int i = MAXN-1;
  while (i>=0 && n[i] == max[i]) i--;
  if (i>=0 && n[i] > max[i]) return 1;
  return 0;
}

int totalZero(char *s) {
  int i = 0;
  while (i<MAXN && s[i]!='\n' && s[i]=='0') ++i;
  if (i==MAXN || s[i]=='\n') return 1;
  return 0;
}

int main() {
  int i=0, j=0, k=0;
  int c;
  char oper = ' ';
  int next = 0;
  int needCompu = 1;
  memset (max, 0, sizeof(int)*MAXN);
  int int_max = INT_MAX;
  while (int_max) {max[i++] = int_max%10; int_max/=10;}

/*  while (fgets(line, MAXN, stdin) != NULL) {
    memset (sum, 0, sizeof(int)*MAXN);
    needCompu = 1; i = j = k = 0;
    while (i<MAXN && line[i]!='\n' && isdigit(line[i])) cbit0[j++] = line[i++];
    while (i<MAXN && line[i]!='\n' && !isdigit(line[i])) { if (line[i]!=' ') oper = line[i]; i++; }
    while (i<MAXN && line[i]!='\n' && isdigit(line[i])) cbit1[k++] = line[i++];
    cbit0[j] = cbit1[k] = '\n'; */

  memset (sum, 0, sizeof(int)*MAXN);
  needCompu = 1; i = j = k = 0;
  while ( (c=getchar()) != EOF ) {
    putchar(c);
    if (c != '\n') {
      if (c == '+' || c == '*') {oper = c; next = 1; continue;}
      if (j<MAXN && !next && isdigit(c)) cbit0[j++] = c;
      if (k<MAXN && next && isdigit(c)) cbit1[k++] = c;
    } else {
      cbit0[j] = cbit1[k] = '\n';
      memset (bit0, 0, sizeof(int)*MAXN);
      memset (bit1, 0, sizeof(int)*MAXN);
      assign (bit0, cbit0); 
      assign (bit1, cbit1);

    /*  printf ("%s", line); */
    /*  if ((j>10&&!totalZero(cbit0)) || moreThanMax (bit0, max)) { needCompu = 0; printf ("first number too big\n"); }
      if ((k>10&&!totalZero(cbit1)) || moreThanMax (bit1, max)) { needCompu = 0; printf ("second number too big\n"); } */

      if (moreThanMax (bit0, max)) { needCompu = 0; printf ("first number too big\n"); }
      if (moreThanMax (bit1, max)) { needCompu = 0; printf ("second number too big\n"); }

      if (needCompu) {
        if (oper == '*') bigmul(bit0, bit1);
        if (oper == '+') { bigadd(sum, bit0); bigadd(sum, bit1); }
        if (moreThanMax (sum, max)) printf ("result too big\n");
      } else {
        if (! (oper=='*' && (cbit0[0]=='0'||cbit1[0]=='0')))
          printf ("result too big\n");
      }

      memset (sum, 0, sizeof(int)*MAXN);
      needCompu = 1; i = j = k = 0;
      next = 0;
    }
  }

  return 0;
}
