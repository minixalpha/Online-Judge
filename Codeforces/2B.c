#include <stdio.h>
#include <string.h>
#include <limits.h>
#define N 1100
#define MAX LLONG_MAX
long long f2[N][N], f5[N][N], m[N][N];
long long af2[N][N], af5[N][N];
long long g_n;
char p2[N][N], p5[N][N], p[N*2];

long long min(long long x, long long y) { return (x<y)?x:y; }
long long legal(long long i, long long j) { return (i>=1&&j>=1&&i<=g_n&&j<=g_n)?1:0; }

void solve(long long i, long long j, long long af[N][N], long long f[N][N], char p[N][N]) {
  long long a, b, c, d, x, y;
  if (af[i][j] != -1) return;
  if (legal(i-1, j))
    solve (i-1, j, af, f, p); 
  if (legal(i, j-1))
    solve (i, j-1, af, f, p);

  if (legal(i-1, j)) {
    a = af[i-1][j] + f[i][j];
    x = a;
  } else {
    x = MAX;
  }
  if (legal(i, j-1)) {
    c = af[i][j-1] + f[i][j];
    y = c;
  } else {
    y = MAX;
  }

  if (x < y) {
    af[i][j] = a;
    p[i][j] = 'D';
  } else {
    af[i][j] = c;
    p[i][j] = 'R';
  }
}

void mp(char path[N][N]) {
  long long i, j, k;
  char c;
  i = j = g_n;
  k = 0;
  while (!(i==1&&j==1)) {
    p[k] = path[i][j];
    if (p[k] == 'D') 
      i -= 1;
    else
      j -= 1;
    k++;
  }
  p[k] = '\0';
  i = 0; j = k-1;
  while (i<=j) {
    c = p[i]; 
    p[i] = p[j];
    p[j] = c;
    i++; j--;
  }
}

int main() {
  long long i, j, k, n, s;
  long long x, y, z;
  scanf ("%lld", &n);
  g_n = n;
  memset (m, 0, sizeof(m));
  memset (f2, 0, sizeof(f2));
  memset (f5, 0, sizeof(f5));
  memset (af2, 0, sizeof(af2));
  memset (af5, 0, sizeof(af5));
  for (i=1; i<=n; i++) 
  for (j=1; j<=n; j++) 
    scanf ("%lld", &m[i][j]);

  z = 1;
  for (i=1; i<=n; i++) {
    for (j=1; j<=n; j++) {
      if (m[i][j])
        s = m[i][j];
      else {
        s = 10;
        x = i; z = 0;
      }

      f2[i][j] = 0;
      f5[i][j] = 0;
      while (s%10==0) { f2[i][j]++; f5[i][j]++; s/= 10; }
      while (s%2==0) { f2[i][j]++; s/=2; }
      while (s%5==0) { f5[i][j]++; s/=5; }
      af2[i][j] = af5[i][j] = -1;
    }
  }

  af2[1][1] = f2[1][1]; af5[1][1] = f5[1][1];
  solve (n, n, af2, f2, p2);
  solve (n, n, af5, f5, p5);
  if (min(af2[n][n], af5[n][n]) == 0  || z == 1) {
    if (af2[n][n] < af5[n][n]) {
      printf ("%lld\n", af2[n][n]);
      mp (p2);
    } else {
      printf("%lld\n", af5[n][n]);
      mp (p5);
    }
    printf ("%s\n", p);
  } else {
    i = 1; j = 1;
    printf ("1\n");
    while (i<x){ putchar('D'); i++; }
    while (j<n){ putchar('R'); j++; }
    while (i<n){ putchar('D'); i++; }
  }
  return 0;
}
