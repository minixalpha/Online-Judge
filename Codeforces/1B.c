#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define N 100
char r[N],in[N],num[N];

int type(char in[N]) {
  int flag=0, i = 0;
  while (!isdigit(in[i]))
    i++;
  while (in[i]!='\n') {
    if (isalpha(in[i])) {
      flag = 1; break;
    }
    i++;
  }
  return flag;
}

int main() {
  int n, i,j,k,row, col, tcol;
  char c, p;
  scanf ("%d", &n);
  getchar();
  for (k=0; k<n; k++) {
    fgets (in, sizeof(in), stdin);
    if (type(in)==1) {
      sscanf(in, "%c%d%c%d\n",&c,&row,&p,&col);
      i = 0;
      while (col) {
        tcol = col % 26;
        if (tcol)
          r[i++] = col % 26 -1 + 'A';
        else {
          r[i++] = 'Z';
          col -= 26;
        }
        col /= 26;
      }
      r[i--] = '\0';
      j = 0;
      while (i>j){
        c = r[i];
        r[i] = r[j];
        r[j] = c;
        i--; j++;
      }
      printf ("%s%d\n", r, row);

    }else {
      col = 0; i=0;
      while (isalpha(in[i])) {
        col = 26*col+in[i]-'A'+1;
        i++;
      }
      row = 0;
      while (in[i]!='\n') {
        row = 10*row+in[i]-'0';
        i++;
      }
      printf ("R%dC%d\n", row, col);
    }
  }
  return 0;
}
