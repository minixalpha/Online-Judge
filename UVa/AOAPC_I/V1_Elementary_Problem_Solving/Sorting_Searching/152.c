#include <stdio.h>
#include <string.h>
#include <float.h>
#include <math.h>

#define N 5000+100

typedef struct{
  int x;
  int y;
  int z;
}Point;

Point pts[N];

double dist(Point s, Point t) {
  double dis;
  dis = pow(s.x-t.x,2) + pow(s.y-t.y,2) + pow(s.z-t.z,2);
  return sqrt(dis);
}

int main() {
  int x, y, z;
  int i,j;
  int n;
  double min, cur_dist;
  int num[10];

  memset (num, 0, sizeof(num));
  i = 0;
  while (scanf ("%d%d%d", &x,&y,&z) == 3) {
    if (x==0 && y==0 && z==0) break;
    pts[i].x = x;
    pts[i].y = y;
    pts[i].z = z;
    i++;
  }
  
  n = i; 
  for (i=0; i<n; i++) {
    min = DBL_MAX;
    for (j=0; j<n; j++) if (j!=i) {
      cur_dist = dist(pts[i], pts[j]);
      if (cur_dist < min) min = cur_dist;
    }
    for (j=0; j<10; j++)
      if (min < (j+1)) { num[j]++; break; }
  }

  for (i=0; i<10; i++)
    printf ("%4d", num[i]);
  printf ("\n");

  return 0;
}
