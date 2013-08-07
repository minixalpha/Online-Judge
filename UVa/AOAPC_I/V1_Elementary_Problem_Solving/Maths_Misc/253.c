#include <stdio.h>
#include <string.h>

#define N 12+5
#define M 7
char input[N];
char rotated[N];
int map[][6] = {{1,6,2,5,3,4}, {2,5,6,1,3,4},{3,4,2,5,6,1},{4,3,2,5,1,6},{5,2,1,6,3,4},{6,1,5,2,3,4}};

void rota(char *s, int *m) {
  int i;
  for (i=0; i<6; i++)
    rotated[i] = s[ m[i]-1 ];
  rotated[i] = '\0';
}

void rightR(char *s) {
  int i;
  char tmp[N];
  strcpy (tmp, s);
  s[0] = tmp[0]; s[1] = tmp[1];
  s[2] = tmp[4]; s[3] = tmp[5];
  s[4] = tmp[3]; s[5] = tmp[2];
}


int main() {
  int i, j;
  char s[M], t[M];
  int find;
  while (scanf ("%s", input) != EOF) {
    find = 0;
    for (i=0; i<6; i++)
      s[i] = input[i];
    s[i] = '\0';
    for (i=6,j=0; i<12; i++, j++)
      t[j] = input[i];
    t[j] = '\0';

    rota (t, map[0]); strcpy (t, rotated);

    for (i=0; i<=5; i++) {
      rota (s, map[i]);
      if (!strcmp (rotated, t)) { printf ("TRUE\n"); find=1; break; }
      for (j=0; j<3; j++) {
        rightR(rotated);
        if (!strcmp (rotated, t)) { printf ("TRUE\n"); i=6; find=1; break; }
      }
    }

   if (!find) printf ("FALSE\n");
  }
  return 0;
}
