/*
 * Problem: 442 - Matrix Chain Multiplication
 * Lang: ANSI C
 * Time: 0.012s
 * Author: minix
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define N 26+5
#define M 1000
char line[M];
int row[N], col[N], top;
int stack_row[M], stack_col[M];

int main () {
  int n, i, sum;
  int cr, cc;
  char c;
  scanf ("%d", &n); getchar();
  for (i=0; i<n; i++) { 
    scanf ("%c %d %d", &c, &cr, &cc);
    row[c-'A'] = cr; col[c-'A'] = cc;
    getchar();
  }
  while(fgets (line, sizeof(line[0])*M, stdin)) {
    if (line[1]=='\n') {printf ("0\n"); continue;}
    i = 0; top = -1; sum = 0;
    while (line[i] != '\n') {
      if (line[i] == '(') { 
        top++; 
        stack_row[top] = stack_col[top] = line[i]; 
      }
      else if(isalpha(line[i])) {
        top++; 
        stack_row[top] = row[line[i]-'A']; 
        stack_col[top] = col[line[i]-'A'];
      } 
      else if (line[i] == ')') {
        if (stack_col[top-1] != stack_row[top]) { 
          printf ("error\n");break;
        }
        else {
          stack_row[top-2] = stack_row[top-1]; 
          stack_col[top-2] = stack_col[top];
          sum += stack_row[top-1]*stack_col[top-1]*stack_col[top];
          top -= 2;
        }
      }
      i++;
    }
    if (line[i]=='\n') printf ("%d\n", sum);
  }

  return 0;
}
