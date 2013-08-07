#include <stdio.h>
#include <ctype.h>

int main() {
  int c, i, sum;

  sum = 0;
  while ((c=getchar()) != EOF) {
    if (c == '\n') putchar(c);
    else if (c == '!') putchar('\n');
    else if (isdigit(c)) sum += (c-'0');
    else {
      for (i=0; i<sum; i++) { 
        if (c == 'b') putchar (' ');
        else putchar(c); 
      }
      sum = 0;
    }
  }

  return 0;
}
