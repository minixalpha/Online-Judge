#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define N (2000+10)
#define M (75+5)

typedef struct{
  char name[M];
  int num;
} Country;

char line[M];
char name[M];
Country cts[N];

int compare (const void *_a, const void *_b) {
  Country *a = (Country *)_a;
  Country *b = (Country *)_b;
  return strcmp(a->name, b->name);
}

int main() {
  int i, j, n, c;

  c = 0; 
  memset (line, 0, sizeof(line));
  memset (cts, 0, sizeof(cts));
      
  scanf ("%d\n", &n);
  for (i=0; i<n; i++) {
    fgets (line, M, stdin);
    for (j=0; line[j]!=' '; j++)
      name[j] = line[j];
    name[j] = '\0';

    for (j=0; j<c; j++) 
      if (!strcmp(cts[j].name, name)) { cts[j].num += 1; break; }
    if (j == c) { strcpy (cts[c].name, name); cts[c].num = 1; c++; }
  }

  qsort (cts, c, sizeof(Country), compare);

  for (i=0; i<c; i++)
    printf ("%s %d\n", cts[i].name, cts[i].num);
  return 0;
}
