#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAXN 500
int sum[MAXN];
int bitp[MAXN];
int total[MAXN];
int tmp[MAXN];
char result[MAXN];

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

void bigprintdouble (int *s, int point) {
  int i = MAXN-1;
  int j = 0;
  point = MAXN - point;
  memset (result, 0, sizeof(result));
  while (i>0 && s[i] == 0) { i--; point--; if(!point) printf("."); if(point<0) result[j++]='0';}
  while (i>=0) { result[j++] = s[i--]+'0'; point--; if(!point) result[j++]='.'; }
  while (result[--j]=='0');
  if (result[j] == '.') j--;
  result[j+1] = '\0';
  puts(result);
}

void bigmul (int *s, int *t, int *result) {
  int i;
  memset (result, 0, sizeof(int)*MAXN);
  for (i=0; i<MAXN; i++) {
    bitmul (s, t[i], i);
    bigadd (result, bitp);
  }
}

void bigcopy (int *src, int *des) {
  int i;
  for (i=0; i<MAXN; i++) des[i] = src[i];
}

int main() {
  char _s[10], s[10];
  int n, i, j;
  int point;

  memset (_s, 0, sizeof(_s));
  memset (s, 0, sizeof(s));
  memset (sum, 0, sizeof(sum));
  memset (total, 0, sizeof(total));
  while (scanf("%s %d", _s, &n) != EOF) {
    point = i = j = 0;
    total[0] = 1; 
    while (_s[i] && _s[i] != '.') s[j++] = _s[i++];
    i++;
    while (_s[i]) { s[j++] = _s[i++]; point++; }
    s[j] = '\n';
    assign (sum, s);
    point *= n;

    while (n) {
      if (n & 1) {
        bigcopy(total, tmp);
        bigmul (tmp, sum, total);
      }

      n = n >> 1;
      bigcopy(sum, tmp);
      bigmul (tmp, tmp, sum);
    }
    bigprintdouble(total, point);

    memset (_s, 0, sizeof(_s));
    memset (s, 0, sizeof(s));
    memset (total, 0, sizeof(total));
    memset (sum, 0, sizeof(sum));
  }

  return 0;
}
