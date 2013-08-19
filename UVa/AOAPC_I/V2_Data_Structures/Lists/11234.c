#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define T 200+10
#define N (10000+10)*4
char stack[N][N];
char line[N];
char term[N];

int main() {
  int n, i, j, k, len, top, layer, deep, all;
  char c[2];
  scanf ("%d", &n);

  for (i=0; i<n; i++) {
    scanf ("%s", line);
    getchar();

    top = -1;
    all = len = strlen(line);
    for (j=0; j<len; j++) {
      c[0]=line[j]; c[1]='\0';
      if (islower(line[j])) {
        top ++;
        stack[top][0]='(';
        stack[top][1]=line[j];
        stack[top][2]=')';
        stack[top][3]='\0';
      } else {
        strcpy (term, "(");
        strcat (term, stack[top]);
        strcat (term, stack[top-1]);
        strcat (term, c);
        strcat (term, ")");
        top -= 2;
        strcpy (stack[++top], term);
      }
    }
    len = strlen (stack[top]);
    deep = -1; layer = 0;
    for (j=len-1; j>=0; j--) {
      if (stack[top][j] == ')') layer ++;
      else if(stack[top][j] == '(') layer --;
      if (layer > deep) deep = layer;
    }

    line[all] = '\0';
    for (k=1; k<=deep; k++) {
      layer = 0;
      for (j=len-1; j>=0; j--) {
        if (stack[top][j] == ')') layer ++;
        else if(stack[top][j] == '(') layer --;
        if (layer == k && isalpha(stack[top][j])) 
          line [--all] = stack[top][j];
      }
    }
    puts (line);
  }
  return 0;
}
