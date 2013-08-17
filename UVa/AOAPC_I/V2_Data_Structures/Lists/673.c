/* 
 * Problem: UVa 673 - Parentheses Balance
 * Lang: ANSI C
 * Time: 0.029s
 * Author: minix
 */
#include <stdio.h>
#include <string.h>
#define N 128+10
char str[N];
char stack[N];
int top;
int main() {
  int n, i, j, len;
  scanf ("%d", &n); getchar();
  for (i=0; i<n; i++) {
    memset (str, 0, sizeof(str[0])*N);
    top = -1;
    fgets (str, sizeof(str[0])*N, stdin);
    len = strlen(str)-1;
    for (j=0; j<len; j++) {
      if (str[j]=='(' || str[j]=='[') stack[++top] = str[j];
      else {
        if (top>=0 && str[j]==')' && stack[top]=='(') 
          top--;
        else if (top>=0 && str[j]==']' && stack[top]=='[')
          top--;
        else
          break;
      }
    }
    if (j==len && top==-1) printf ("Yes\n");
    else printf ("No\n");
  }
  return 0;
}
