#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define LINEN 5100
#define LINEL 210
#define WORDN 5100
#define WORDL 100

char dict[WORDN][WORDL];

int in_wd_list(char *cur_word, char dict[WORDN][WORDL], int k) {
  int i;
  for (i=0; i<k; i++)
    if (!strcmp(cur_word, dict[i])) return 1;
  return 0;
}

int compare(const void *a, const void *b) {
  while (*(char*)a && *(char*)b && (*(char*)a == *(char*)b)) {a++; b++;}
  return *(char*)a - *(char*)b;
}

int main() {
  char cur_word[WORDL];
  char buf[WORDL];
  int i, j, k, len;
  memset(dict, 0, WORDL*WORDN);

  k = 0;
  while (scanf ("%s", buf) != EOF) {
    len = strlen(buf);
    i = 0;
    while (i<len && !isalpha(buf[i])) i++;
    while (i<len) {
      j = 0;
      while (i<len && isalpha(buf[i])) cur_word[j++] = tolower(buf[i++]);
      cur_word[j] = '\0';
      if (j && !in_wd_list(cur_word, dict, k))
        strcpy(dict[k++], cur_word);
      i++;
    }
  }
  qsort (dict, k, WORDL, compare);

  for (i=0; i<k; i++)
    puts(dict[i]);

  return 0;
}
