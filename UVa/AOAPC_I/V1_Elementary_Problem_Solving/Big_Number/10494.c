#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXN 10000
long long s[MAXN];
long long r[MAXN];
char line[MAXN];
long long n1[MAXN], n2[MAXN];
char s1[MAXN], s2[MAXN];

int main() {
  int i, j, k;
  long long c;
  long long t;
  long long sum;
  int len;
  char part[11];
  char oper;
  while (fgets (line, MAXN, stdin) != NULL) {
    i = j = k = c = 0;
    memset(s1,0,sizeof(s1)); memset(s2,0,sizeof(s2));
    memset(r,0,sizeof(r)); memset(s,0,sizeof(s));
    memset(n1,0,sizeof(n1)); memset(n2,0,sizeof(n2));
    while (line[i]!='\n' && isdigit(line[i])) s1[j++] = line[i++];
    while (line[i]!='\n' && !isdigit(line[i])) {if (line[i]=='/' || line[i]=='%') oper = line[i]; i++;}
    while (line[i]!='\n' && isdigit(line[i])) s2[k++] = line[i++];
    s1[j] = '\0'; s2[k] = '\0';

    for (i=0; i<j; i++) n1[i] = s1[i]-'0';
    sscanf (s2, "%lld", &t);

    sum = 0; k = 0;
    for (i=0; i<j; i++) {
      s[k++] = ((sum*10) + n1[i]) / t;
      sum = ((sum*10) + n1[i]) % t;
    }

    i = 0; while(i<MAXN && s[i]==0) i++;
    if (oper == '/') {
      if (i==MAXN) printf ("0\n");
      else { while (i<j) printf("%lld", s[i++]); printf("\n"); }
    } else {
      printf ("%lld\n", sum);
    }
  }
  return 0;
}
