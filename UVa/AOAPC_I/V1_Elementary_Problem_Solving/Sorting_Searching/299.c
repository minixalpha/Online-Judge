#include <stdio.h>

int opt(int* train, int n) {
  int i, j;
  int tmp;
  int step=0;
  for (i=0; i<n; i++)
    for (j=i+1; j<n; j++)
      if (train[j]<train[i]) {
        step++;
        tmp=train[j]; train[j]=train[i]; train[i]=tmp;
      }
  return step;
}

int main() {
  int n, l;
  int i, j;
  int train[50+10];

  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%d", &l);
    for (j=0; j<l; j++)
      scanf ("%d", &train[j]);
    printf ("Optimal train swapping takes %d swaps.\n", opt(train, l));
  }
  return 0;
}
