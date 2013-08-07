#include <stdio.h>
#include <string.h>

#define N 1000
char input[N];

int isPos(char *input, int len) {
  if (!strcmp (input, "1")) return 1;
  if (!strcmp (input, "4")) return 1;
  if (!strcmp (input, "78")) return 1;
  return 0;
}

int isNeg(char *input, int len) {
  if (len >=2 && input[len-1]=='5' && input[len-2]=='3')
    return 1;
  return 0;
}

int isFailed(char *input, int len) {
  if (len >=2 && input[len-1]=='4' && input[0]=='9')
    return 1;
  return 0;
}

int isNotComp(char *input, int len) {
  if (len>=3 && input[0]=='1' && input[1]=='9' && input[2]=='0')
    return 1;
  return 0;
}

int main() {
  int n;
  int i, len;
  scanf ("%d", &n);

  for (i=0; i<n; i++) {
    scanf ("%s", input);
    len = strlen(input);
    if (isPos(input, len)) printf ("+\n");
    else if (isNeg(input, len)) printf ("-\n");
    else if (isFailed(input, len)) printf ("*\n");
    else if (isNotComp(input, len)) printf ("?\n");
  }
  return 0;
}
