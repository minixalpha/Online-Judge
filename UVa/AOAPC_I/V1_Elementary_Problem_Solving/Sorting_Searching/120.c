#include <stdio.h>
#include <string.h>
#include <ctype.h>

 #define DEBUG 

#define N 150
int i_pan[N];
int pan[N];
char c_pan[N];

int getMaxIndex (int *num, int s, int t) {
  int i;
  int max=num[s], maxi=s;
  for (i=s; i<=t; i++)
    if (num[i]>max) {max=num[i]; maxi=i;}
  return maxi;
}

int getMinIndex (int *num, int s, int t) {
  int i;
  int min=num[s], mini=s;
  for (i=s; i<=t; i++)
    if (num[i]<min) {min=num[i]; mini=i;}
  return mini;
}

void reverse (int *num, int s, int t) {
  int tmp;
  while (s < t) {
    tmp = num[s]; num[s] = num[t]; num[t] = tmp;
    s++; t--;
  }
}

int main() {
  int i, j, k, n;
  int maxi, mini, sum;
  char newitem[10];
  memset (c_pan, 0, sizeof(c_pan));
  while (fgets(c_pan, N, stdin)) {
    printf ("%s", c_pan);

    for (i=0,j=0,k=0; c_pan[i]!='\0'; i++) {
      if (c_pan[i]== ' ' || c_pan[i]=='\n') {
        newitem[k] = '\0';
        sscanf (newitem, "%d", &sum);
        i_pan[j++] = sum;
        k = 0;
      } else {
        newitem[k++] = c_pan[i];
      }
    }

    n = j;
    for (i=0, j=1; i<n; i++, j++)
      pan[j] = i_pan[i];
    reverse (pan, 1, n);

#ifdef DEBUG_1
    for (i=1; i<=n; i++)
      printf ("%d ", pan[i]);
    printf ("\n");
#endif

    for (i=1; i<n; i++) {
      maxi = getMaxIndex (pan, i, n);
        if (maxi == i) continue;
        if (maxi != n) {
          printf ("%d ", maxi);
          reverse (pan, maxi, n);
        }
        printf ("%d ", i);
        reverse (pan, i, n);
    }

    printf ("0\n");
    memset (c_pan, 0, sizeof(c_pan));
    
  }
  return 0;
}
