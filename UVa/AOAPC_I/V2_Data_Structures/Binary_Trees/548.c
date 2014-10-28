#include <stdio.h>
#define N 10000+100

int in[N], po[N];
int lin[N], lpo[N];
int p[N], l[N], r[N];
int g_sum = N, g_leaf = N;

void solve (int s, int e) {
  int v_e = po[e], v_s = po[s];
  int lin_e = lin[v_e], lin_s = lin[v_s];
  int ll, i;
  int n_l, n_r;

  if (e <= s) return;

  ll = lin_s;
  for (i=s; i<=e; i++)
    if (lin[po[i]]<ll) ll = lin[po[i]];

  n_l = lin_e - ll;
  n_r = e - s - n_l;


  if (n_l > 0) {
    l[v_e] = po[s+n_l-1];
    p[ l[v_e] ] = v_e;
  }
  if (n_r > 0) {
    r[v_e] = po[e-1];
    p[ r[v_e] ] = v_e;
  }

  if (n_l > 0)
    solve (ll, s+n_l-1 );
  if (n_r > 0)
    solve (e-n_r, e-1);
}

void check() {
  int i;
  printf (" ");
  for (i=1; i<=7; i++)
    printf ("%d ", i);
  printf ("\n");
  printf ("p");
  for (i=1; i<=7; i++)
    printf ("%d ", p[i]);
  printf ("\n");
  printf ("l");
  for (i=1; i<=7; i++)
    printf ("%d ", l[i]);
  printf ("\n");
  printf ("r");
  for (i=1; i<=7; i++)
    printf ("%d ", r[i]);
  printf ("\n");
}

void dfs (int v, int sum) {
  int vl = l[v], vr = r[v];
  if (vl==-1 && vr==-1) { 
    if (sum+v < g_sum) { g_sum = sum+v; g_leaf = v; }
    if (sum+v == g_sum && v < g_leaf) { g_leaf = v; }
 /*   printf ("s:%d\n", sum+v); */
    return;
  }
  if (vl != -1)
    dfs (vl, sum+v);
  if (vr != -1)
    dfs (vr, sum+v);
}

int main() {
  int i, j, k, m, n;
  char c;

  while (scanf ("%d",&n) != EOF) {
    i = 0; g_leaf = g_sum = N;
    in[i] = n;
    lin[n] = i;
    i++;
    c = getchar();
    while (c!='\n') {
      scanf ("%d", &n);
      in[i] = n;
      lin[n] = i;
      i++;
      c = getchar();
    }

    scanf ("%d", &n);
    i = 0;
    po[i] = n;
    lpo[n] = i;
    i++;
    c = getchar();
    while (c!='\n') {
      scanf ("%d", &n);
      po[i] = n;
      lpo[n] = i;
      i++;
      c = getchar();
    }

    m = i-1;
    for (i=0; i<N; i++)
      p[i] = l[i] = r[i] = -1;

    solve (0, m);

    dfs (po[m], 0);
    printf ("%d\n", g_leaf);
  }

  return 0;
}
