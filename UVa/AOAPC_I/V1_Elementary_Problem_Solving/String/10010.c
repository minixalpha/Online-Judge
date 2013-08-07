#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100
char data[MAX][MAX];
char str[MAX][MAX];
int gr, gc;

int isMatch(char data[][100], int j, int k, char*s) {
  int i;
  int len = strlen(s);
  int tmpj = j, tmpk = k;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (j<gr && data[j][k] == s[i]) j++;
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (j>=0 && data[j][k] == s[i]) j--;
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (k<gc && data[j][k] == s[i]) k++;
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (k>=0 && data[j][k] == s[i]) k--;
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (j>=0 && k<gc && data[j][k] == s[i]) {j--; k++;}
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (j>=0 && k>=0 && data[j][k] == s[i]) {j--; k--;}
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (j<gr && k>=0 && data[j][k] == s[i]) {j++; k--;}
    else break;
  }
  if (i==len) return 1;

  j = tmpj, k = tmpk;
  for (i=0; i<len; i++) {
    if (j<gr && k<gc && data[j][k] == s[i]) {j++; k++;}
    else break;
  }
  if (i==len) return 1;

  return 0;
}

int main() {
  int m, n, r, c;
  int i, j, k, p;
  int len;

  scanf ("%d", &n);

  for (p=0; p<n; p++) {
    scanf ("%d%d", &r, &c);
    gr = r; gc = c;
    for (j=0; j<r; j++)
      scanf ("%s", data[j]);
    scanf ("%d", &m);
    for (j=0; j<m; j++)
      scanf ("%s", str[j]);

    for (j=0; j<r; j++)
      for (k=0; k<c; k++)
        data[j][k] = tolower(data[j][k]);

    for (j=0; j<m; j++) {
      len = strlen(str[j]);
      for (k=0; k<len; k++)
        str[j][k] = tolower(str[j][k]);
    }

    for (i=0; i<m; i++) 
    for (j=0; j<r; j++) 
    for (k=0; k<c; k++) 
      if (isMatch(data, j, k, str[i])) { printf ("%d %d\n", j+1, k+1); j=r; k=c; }

   if (p!=(n-1)) printf ("\n");
  }

  return 0;
}
