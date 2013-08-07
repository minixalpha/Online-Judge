#include <stdio.h>
#include <string.h>

#define MAXN 200
char line1[MAXN];
char line2[MAXN];
char s1[MAXN],s2[MAXN],s3[MAXN],s4[MAXN],s5[MAXN];

int main() {
  int n;
  int i,j,p;
  int len1, len2;

  scanf ("%d\n", &n);
  for (p=0; p<n; p++) {
    memset(line1, '\0', MAXN); memset(line2, '\0', MAXN);
    memset(s1,0,MAXN); memset(s2,0,MAXN); memset(s3,0,MAXN);
    memset(s4,0,MAXN); memset(s5,0,MAXN);

    fgets(line1, MAXN, stdin);
    fgets(line2, MAXN, stdin);

    len1 = strlen(line1);
    len2 = strlen(line2);

    i = 0; j = 0;
    while (i<len1 && line1[i] != '<') {s1[j++] = line1[i++];}
    
    
    j = 0; i++;
    while (i<len1 && line1[i] != '>') {s2[j++] = line1[i++];}

    j = 0; i++;
    while (i<len1 && line1[i] != '<') {s3[j++] = line1[i++];}

    j = 0; i++;
    while (i<len1 && line1[i] != '>') {s4[j++] = line1[i++];}

    j = 0; i++;
    while (i<len1 && line1[i] != '\n') {s5[j++] = line1[i++];}

    for (i=0; i<len1; i++) 
      if (line1[i] != '<' && line1[i] != '>') putchar(line1[i]);

    i = 0;
    while (i<len2 && line2[i] != '.') {putchar(line2[i]); i++;}
    printf("%s%s%s%s\n", s4, s3, s2, s5);
  }

  return 0;
}
