#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define N 100000+10
#define PN 100

typedef struct {
  char name[PN];
  int num;
}ST;

ST sts[N];

char map[30] = {
  '2','2','2','3','3','3','4','4','4','5','5','5',\
  '6','6','6','7','0','7','7','8','8','8','9','9','9','0'\
};

void num2std_dial (char *tdial, char *dial) {
  int i, j;

  i = j = 0;
  while (i<3) { dial[i++] = tdial[j++]; }
  dial[i++] = '-';
  while (tdial[j]!='\0') { dial[i++] = tdial[j++]; }
  dial[i] = '\0';
}

int cmp (const void *_a, const void *_b) {
  ST *a = (ST *)_a;
  ST *b = (ST *)_b;
  return strcmp (a->name, b->name);
}

int main() {
  int n, m;
  int i, j, k, s;
  char dial[PN];
  char ndial[PN];
  int dup;
  int key_num;
  int len;
  int leni;
  int times;

  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    memset (sts, 0, sizeof(sts));
    dup = 0; key_num = 0;
    scanf ("%d", &m);
    for (j=0; j<m; j++) {
      memset (dial, 0, sizeof(dial));
      memset (ndial, 0, sizeof(ndial));
      scanf ("%s", dial); s = 0;
      for (k=0; dial[k]!='\0'; k++) {
        if (isdigit(dial[k])) ndial[s++] = dial[k];
        if (isalpha(dial[k])) ndial[s++] = map[ dial[k]-'A' ];
      }
      ndial[s] = '\0';
      strcpy (sts[key_num++].name, ndial);

    }

    qsort (sts, key_num, sizeof(sts[0]), cmp);
    times = 1;
    for (k=0; k<key_num; k++) {
      while ((k+1)<key_num && !strcmp(sts[k].name, sts[k+1].name)) {k++; times++;}
      if (times > 1) {
        num2std_dial (sts[k].name, dial);
        printf ("%s %d\n", dial, times);
        dup = 1;
      }
      times = 1;
    }

    if (dup == 0) printf ("No duplicates.\n");
    if (i!=(n-1)) printf ("\n");
  }

  return 0;
}
