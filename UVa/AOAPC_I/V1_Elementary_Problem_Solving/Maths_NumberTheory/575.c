/*
 * Problem: UVa 575 - Skew Binary
 * Lang: ANSI C
 * Time: 0.015
 * Author: minix
 */

#include <stdio.h>
#include <string.h>

#define N 32+5
int base[N];
char input[N];

int main() {
  int i, j;
  int por, len;
  double sum;

  por = 2;
  for (i=1; i<=31; i++) {
    base[i] = por -1;
    por *= 2;
  }

  while (scanf ("%s", input) != EOF) {
    if (!strcmp(input,"0")) break;
    len = strlen (input);
    j = 1; sum = 0;
    for (i=len-1; i>=0; i--)
      sum += base[j++] * (input[i]-'0');
    printf ("%.0lf\n", sum);
  }

  return 0;
}
