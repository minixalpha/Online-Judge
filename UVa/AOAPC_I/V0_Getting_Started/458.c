#include <stdio.h>

int main() {
  int c;
  while ( (c=getchar())!=EOF ) {
    if (c=='\n')
      printf ("\n");
    else
      printf ("%c", c-7);
  }

  return 0;
}
