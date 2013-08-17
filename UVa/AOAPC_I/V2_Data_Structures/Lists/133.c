/*
 * Problem: UVa 133 The Dole Queue
 * Lang: ANSI C
 * Time: 0.009s
 * Author: minix
 */
#include <stdio.h>

#define N 20

typedef struct _node {
  struct _node *pre;
  struct _node *next; 
  int seq;
}Node;

Node g_node[N];

int main() {
  int n, k, m, i;
  Node *pa = NULL;
  Node *pb = NULL;
  while (scanf ("%d%d%d", &n,&k,&m) != EOF) {
    if (n==0 && k==0 && m==0) break;
    /* init double & circle queue */
    for (i=1; i<=n; i++) {
      g_node[i].seq = i;
      g_node[i].pre = &g_node[i-1];
      g_node[i].next = &g_node[i+1];
    }
    g_node[1].pre = &g_node[n];
    g_node[n].next = &g_node[1];

    /* kill */
    pa = &g_node[1];
    pb = &g_node[n];

    while (n != 0) {
      for (i=1; i<=(k-1); i++)
        pa = pa->next;
      for (i=1; i<=(m-1); i++)
        pb = pb->pre;

      if (pa == pb) {
        printf ("%3d", pa->seq);
        pa->pre->next = pa->next;
        pa->next->pre = pa->pre;
        pa = pa->next;
        pb = pb->pre;
        n -= 1;
      } else {
        printf ("%3d%3d", pa->seq, pb->seq);
        n -= 2;
        if (pa->next == pb) {
          pa->pre->next = pb->next;
          pb->next->pre = pa->pre;
          pa = pb->next;
          pb = pa->pre;
        } else {
          pa->pre->next = pa->next;
          pa->next->pre = pa->pre;
          pb->pre->next = pb->next;
          pb->next->pre = pb->pre;
          pa = pa->next;
          pb = pb->pre;
        }
      }

      if (n != 0) printf (",");
    }
    printf ("\n");
  }
  return 0;
}
