#include <stdio.h>
#include <stdlib.h>

#define VO_N 5
#define ALPHA_N 26
#define NAME_N 211+10
#define VOL_LIM 21
#define COS_LIM 5

typedef struct {
  char alpha;
  int value;
}VT;

char vowels[VO_N] = {'A', 'E', 'I', 'O', 'U'};
int value[ALPHA_N];
char name[NAME_N];
VT vowelList[ALPHA_N];
VT consList[ALPHA_N]; 
char vl[NAME_N];
char cl[NAME_N];

int isVowel (char c) {
  int i;
  for (i=0; i<VO_N; i++)
    if (c == vowels[i]) return 1;
  return 0;
}

void initValue() {
  int i;
  for (i=0; i<ALPHA_N; i++)
    value[i] = i%9+1;
}

void initList() {
  int i, j;
  int c;

  i = j = 0;
  for (c='A'; c<='Z'; c++) {
    if (isVowel(c)) { vowelList[i].alpha = c; vowelList[i].value = value[c-'A']; i++;}
    else { consList[j].alpha = c; consList[j].value = value[c-'A']; j++;}
  }
}

int cmp (const void *_a, const void *_b) {
  VT *a = (VT *)_a;
  VT *b = (VT *)_b;
  if (a->value < b->value) return -1;
  if (a->value > b->value) return 1;
  return a->alpha - b->alpha;
}
void sortList() {
  qsort (vowelList, 5, sizeof(vowelList[0]), cmp);
  qsort (consList, 21, sizeof(consList[0]), cmp);
}

int cmpChar (const void *_a, const void *_b) {
  char *a = (char *)_a;
  char *b = (char *)_b;
  return *a-*b;
}
void getName (int n) {
  int i, j, k;
  int s, t;
  int vt, ct;
  int odd;

  j = k = 0;
  vt = ct = 0;
  s = t = 0;
  odd = 1;
  for (i=0; i<n; i++) {
    if (odd) { vl[s++] = vowelList[j].alpha; vt++; }
    else { cl[t++] = consList[k].alpha; ct++; }
    odd = !odd;

    if (vt == VOL_LIM) { j++; vt = 0; }
    if (ct == COS_LIM) { k++; ct = 0; }
  }
  qsort (vl, s, sizeof(vl[0]), cmpChar);
  qsort (cl, t, sizeof(cl[0]), cmpChar);

  odd = 1; s = t = 0;
  for (i=0; i<n; i++) {
    if (odd) {name[i] = vl[s++];}
    else {name[i] = cl[t++];}
    odd = !odd;
  }
  name[n] = '\0';
}

int main() {
  int n, len;
  int i, j;

  /* init value */
  initValue();
  initList();
  sortList();

#ifdef DEUBG
  for (i=0; i<5; i++) printf ("%c:%d ", vowelList[i].alpha, vowelList[i].value);
  printf ("\n");
  for (i=0; i<21; i++) printf ("%c:%d ", consList[i].alpha, consList[i].value);
  printf ("\n");
#endif

  scanf ("%d", &n);
  for (i=0; i<n; i++) {
    scanf ("%d", &len);
    printf ("Case %d: ", i+1);
    getName (len);
    printf ("%s\n", name);
  }

  return 0;
}
