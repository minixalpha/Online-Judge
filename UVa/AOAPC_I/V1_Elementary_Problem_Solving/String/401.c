#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXN 100
char str[MAXN];

int isPa(char *s) {
  int len = strlen(s);
  int i, j;

  i = 0; j = len-1;
  while (i < j) {
    if (s[i] == s[j]) {i++; j--;}
    else return 0;
  }

  return 1;
}

int isMirror(char *s, char *alpha_mirror, char *digit_mirror) {
  int len = strlen(s);
  int i, j;

  i = 0; j = len-1;
  while (i <= j) {
    if (isalpha(s[i]) && alpha_mirror[ s[i]-'A' ] == s[j]) {i++;j--;}
    else if  (isdigit(s[i]) && digit_mirror[ s[i]-'0' ] == s[j]) {i++;j--;}
    else return 0;
  }

  return 1;
}

int main() {
  int isM, isP;
  char alpha_mirror[26] = {
    'A', ' ', ' ', ' ', '3',
    ' ', ' ', 'H', 'I', 'L', 
    ' ', 'J', 'M', ' ', 'O', 
    ' ', ' ', ' ', '2', 'T',
    'U', 'V', 'W', 'X', 'Y',
    '5'
  };

  char digit_mirror[10] = {
    '0', '1', 'S', 'E', ' ',
    'Z', ' ', ' ', '8', ' '
  };

  while (scanf("%s", str) != EOF) {
    isM = isMirror(str, alpha_mirror, digit_mirror);
    isP = isPa(str);

    if (!isM && !isP) printf ("%s -- is not a palindrome.\n", str);
    else if (!isM && isP) printf ("%s -- is a regular palindrome.\n", str);
    else if (isM && !isP) printf ("%s -- is a mirrored string.\n", str);
    else printf ("%s -- is a mirrored palindrome.\n", str);
    printf ("\n");
  }

  return 0;
}
