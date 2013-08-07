#include <stdio.h>

int main() {
  int caseNum, amp, freq;
  int i,j,k,p;

  scanf ("%d", &caseNum);
  for (i=0; i<caseNum; i++) {
    scanf ("%d%d", &amp, &freq);
    for (j=0; j<freq; j++) {
      for (k=1; k<=amp; k++) {
        for (p=0; p<k; p++)
          printf("%d", k);
        printf ("\n");
      }
      for (k=k-2; k>=1; k--) {
        for (p=0; p<k; p++)
          printf("%d", k);
        printf ("\n");
      }
      if (j != freq-1)
        printf ("\n");
    }
    if (i != caseNum-1)
      printf ("\n");
  }

  return 0;
}
