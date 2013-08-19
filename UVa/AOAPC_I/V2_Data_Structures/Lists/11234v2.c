/* 
 * Problem: UVa 11234 - Expressions
 * Lang: ANSI C
 * Time: 0.026s
 * Author: minix
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define N 10000+100
char s[N], re[N];
int l[N], r[N], stack[N], queue[N];

int main() {
  int n, i, j, len, top, head, tail, node;
  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%s", s);
    top = -1; head = tail = 0;
    len = strlen (s);
    for (j=0; j<len; j++) {
      if (islower(s[j])) {
        stack[++top] = j;
        l[j] = r[j] = -1;
      } else {
        l[j] = stack[top];
        r[j] = stack[top-1];
        top -= 2;
        stack[++top] = j;
      }
    }

    re[len--] = '\0';
    queue[tail++] = stack[top];
    while (head != tail) {
      node = queue[head++];
      re[len--] = s[node];
      if (r[node] != -1) queue[tail++] = r[node];
      if (l[node] != -1) queue[tail++] = l[node];
    }
    puts(re);
  }
  return 0;
}
