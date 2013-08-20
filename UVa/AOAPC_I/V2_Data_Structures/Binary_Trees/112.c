/*
 * Problem: UVa 112 Tree Summing
 * Lang: ANSI C
 * Time: 0.035s
 * Author: minix
 */
#include <stdio.h>
#include <ctype.h>
#define N 10000
int s[N];
int main() {
  int t, l, p, sum, y, r, f;
  char c, pc;
  while (scanf("%d",&t) != EOF) {
    sum = 0; y = 0; r = 0;
    while ((c=getchar()) != '(');
    l = 1; p = 0; pc = '('; f = 1;
    while (l!=0) {
      if (c=='(' || c==')')
        pc = c;
      c = getchar();
      if (c==' '||c=='\n') continue;
      if (c=='-') { f *= -1; continue; }

      if (c=='(') { 
        if (pc=='(') { /* get a new number */
          r = 0;
          p = f * p;
          sum = sum + p; 
          s[l] = p; 
          f = 1;
          p=0; 
        }
        l++;
      }
      if (c==')') { 
        if (pc=='(') r++;
        if (pc==')') { sum -= s[l]; s[l] = 0;} /* back to upper layer */
        l--; 
        if (r==2 && pc=='(') { /* encounter a leaf */
          if (sum == t) {
            y = 1;
            break;
          }
        }
      }
      if (isdigit(c)) { 
        p = 10*p+c-'0'; 
      }
    }
    while (l!=0) {
      c = getchar();
      if (c=='(') l++;
      if (c==')') l--;
    }
    c = getchar();
    if (y) puts("yes");
    else puts("no");
  }

  return 0;
}
