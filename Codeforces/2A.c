#include <stdio.h>
#include <string.h>
#define N 1000
#define M 35
char name[N][M];
int score[N];
int win[N];

char in_name[N][M];
int in_score[N];

int main() {
  int n, i, j,k,sc, max;
  char na[M];
  scanf ("%d", &n);
  getchar();

  for (i=0; i<n; i++)  {
    scanf ("%s %d", in_name[i], &in_score[i]);
    getchar();
  }

  k = 0;
  memset (win, 0, sizeof(win));
  for (i=0; i<n; i++) {
    strcpy (na, in_name[i]);
    sc = in_score[i];
    for (j=0; j<k; j++)
      if (!strcmp(na, name[j])) break;
    if (j==k ) { 
      strcpy(name[k], na);
      score[k] = sc;
      k++;
    } else {
      score[j] += sc;
    }
  }

  max = score[0];
  if (max < 0) lost[0] = 1;
  for (i=1; i<k; i++)
    if (score[i]>max) max = score[i];

  for (i=0; i<k; i++)
    if (score[i]==max) win[i] = 1;

  k = 0;
  for (i=0; i<n; i++) {
    strcpy (na, in_name[i]);
    sc = in_score[i];
    for (j=0; j<k; j++)
      if (!strcmp(na, name[j])) break;
    if (j==k ) { 
      strcpy(name[k], na);
      score[k] = sc;
      if (score[k] >= max && win[k]==1) {
        puts(na); break;
      }
      k++;
    } else {
      score[j] += sc;
      if (score[j] >= max && win[j]==1) {
        puts(na); break;
      }
    }
  }

  return 0;
}
