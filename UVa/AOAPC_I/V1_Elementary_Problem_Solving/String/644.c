#include <stdio.h>
#include <string.h>

#define LEN 100
#define MAX 1000
char buf[LEN];
char data[MAX][LEN];

int isprefix(char *s, char *t) {
  int lens = strlen(s), lent = strlen(t);
  int i;
  if (lens > lent) return 0;
  for (i=0; i<lens; i++)
    if (s[i] != t[i]) return 0;
  return 1;
}

int main() {
  int count = 1;
  int i = 0, j = 0, k = 0;
  int flag;
  while (scanf ("%s", data[i++]) != EOF) {
    flag = 1;
    if (data[i-1][0] == '9') {
      for (j=0; flag&&j<i; j++) 
      for (k=0; flag&&k<i; k++)
        if (k!=j && isprefix(data[j], data[k])) {
          printf ("Set %d is not immediately decodable\n", count++);
          flag = 0;
        }
      if (flag == 1)
        printf ("Set %d is immediately decodable\n", count++);
      i = 0;
    }
  }
  return 0;
}
