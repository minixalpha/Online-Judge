#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define DEBUG

#define N_IG 50+10
#define T_IG 200+10
#define M 100
#define N_KEY 3000+100
#define LM 10000
#define SN 15+10

char ignore[N_IG][M];
char title[T_IG][LM];
char keywords[N_KEY][M];
char line_words[SN][M];

int inList(char *s, char ig[N_KEY][M], int n) {
  int i;
  for (i=0; i<n; i++)
    if (!strcmp(ig[i], s)) return 1;
  return 0;
}

int compare (const void *_s, const void *_t) {
  char *s = (char *)_s;
  char *t = (char *)_t;

  return strcmp(s, t);
}

void split (char *line, int *n) {
  char word[M];
  int i, j, k;

  i = j = k = 0; 
  memset (line_words, 0, sizeof(line_words));
  while (line[i] != '\n') {
    if (line[i] != ' ') word[j++] = line[i];
    else { 
      word[j]='\0'; j = 0;
      strcpy(line_words[k++], word);
    }
    ++i;
  }
  word[j] = '\0';
  strcpy(line_words[k++], word);
  *n = k;
}

void upperCopy(char *s, char *t) {
  int i = 0;
  while (t[i]) { s[i] = toupper(t[i]); ++i; }
  s[i] = '\0';
}

void lowerCopy(char *s, char *t) {
  int i = 0;
  while (t[i]) { s[i] = tolower(t[i]); ++i; }
  s[i] = '\0';
}

int main() {
  int i, j, k;
  int ig_len, tt_len, key_len, cur_len;
  char cur_ignore[M];
  char tmp[M];
  int pre, haskey;

  i = 0; memset(ignore, 0, sizeof(ignore));
  while (scanf ("%s", cur_ignore)) {
    if (!strcmp(cur_ignore, "::")) break;
    else {
      upperCopy (ignore[i], cur_ignore);
      i++;
    }
  }
  ig_len = i;

#ifdef DEBUG_1
  for (i=0; i<ig_len; i++)
    printf ("%s ",ignore[i]);
  printf ("\n");
#endif

  getchar();

  j = 0; memset(title, 0, sizeof(title));
  while (fgets(title[j], LM, stdin) != NULL) ++j;
  tt_len = j;

  k = 0; memset(keywords, 0, sizeof(keywords));
  for (i=0; i<tt_len; i++) {
    split(title[i], &cur_len);
    for (j=0; j<cur_len; j++) {
      memset (tmp, 0, sizeof(tmp));
      upperCopy (tmp, line_words[j]);
      if (!inList(tmp, ignore, ig_len) && !inList(tmp, keywords, k))
        upperCopy (keywords[k++], line_words[j]);
    }
  }
  key_len = k;

  qsort (keywords, key_len, sizeof(keywords[0]), compare); 
#ifdef DEBUG_2
  for (i=0; i<key_len; i++)
    printf ("%d:%s ", i,keywords[i]);
  printf ("\n");
#endif

  for (k=0; k<key_len; k++) {
    for (i=0; i<tt_len; i++) {
      split (title[i], &cur_len);
      pre = -1; 
      while (1) {
        haskey = 0;
        for (j=0; j<cur_len; j++) {
          memset (tmp, 0, sizeof(tmp));
          upperCopy (tmp, line_words[j]);
          if (j>pre && !strcmp(keywords[k],tmp)) { pre=j; haskey=1; break;}
        }
        if (haskey) {
          for (j=0; j<cur_len; j++) {
            if (j!=pre) { 
              memset (tmp, 0, sizeof(tmp));
              lowerCopy (tmp, line_words[j]);
              printf ("%s", tmp);
              if (j!=(cur_len-1)) printf(" ");
            }
            else {
              memset (tmp, 0, sizeof(tmp));
              upperCopy (tmp, line_words[j]);
              printf ("%s", tmp);
              if (j!=(cur_len-1)) printf(" ");
            }
          } printf ("\n");
        } else {
          break;
        }
        
      }
    }
  }


  return 0;
}
