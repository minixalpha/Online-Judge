#include <stdio.h>

int main() {
  double h, u, d, f;
  int day; 
  double ih, dc, hac, has;

  while (scanf ("%lf%lf%lf%lf", &h,&u,&d,&f) != EOF) {
    if (h == 0) break;
    day = 1; ih = 0; dc = u; hac = ih + dc; has = hac-d;


    f = f*u/100.0;
    while (hac <= h && has >= 0) { /* need has >= 0  to conver the failure on first day */
      day ++;
      ih = has; dc -= f; if(dc<0) dc = 0;
      hac = ih + dc; has = hac-d; 
      if (has < 0) break;
    }

    if (hac > h) printf ("success ");
    else printf ("failure ");
    printf ("on day %d\n", day);
  }
  return 0;
}
