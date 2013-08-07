#include <stdio.h>
#include <string.h>

#define ROW 60
#define COL 50

int dish[ROW][COL];
int main() {
  int i, j, k, n, p;
  int dna[10];

  scanf ("%d", &n);

  for (i=0; i<n; i++) {
    for (p=0; p<10; p++)
      scanf ("%d", &dna[p]);
    memset (dish, 0, ROW*COL*sizeof(int));
    dish[0][20] = 1;
    for (j=1; j<50; j++) {
      for (k=1; k<=40; k++) {
        dish[j][k] = dna[dish[j-1][k-1] + dish[j-1][k] + dish[j-1][k+1]];
      }
    }

    for (j=0; j<50; j++) {
      for (k=1; k<=40; k++) {
        if (dish[j][k] == 0) putchar(' ');
        if (dish[j][k] == 1) putchar('.');
        if (dish[j][k] == 2) putchar('x');
        if (dish[j][k] == 3) putchar('W');
      }
      printf ("\n");
    }

    if (i!=(n-1)) printf ("\n");
  }

  return 0;
}
