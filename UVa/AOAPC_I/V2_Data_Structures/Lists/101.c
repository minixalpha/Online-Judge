/*
 * Problem: UVa 101 The Blocks Problem
 * Lang: ANSI C
 * Time: 0s
 * Author: minix
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 25
#define M 20

typedef struct _block {
  int seq;
  struct _block *top;
}Block;

typedef struct _node {
  Block *top;
  Block *ori;
  Block *pre;
  Block *roof;
  int cur_stack;
}Node;

void move_onto (Node nodes[N], int a, int b);
void move_over (Node nodes[N], int a, int b);
void pile_onto (Node nodes[N], int a, int b);
void pile_over (Node nodes[N], int a, int b);
int is_quit (char cmd[M]);
void implement_cmd (Node nodes[N], char cmd[M]);
void output (Node nodes[N], int n);
void init (Node nodes[N], int n);
Block * new_block (int seq);

void return_up_stacks (Node nodes[N], Block *block) {
  Block *cur = block->top;
  Block *next = NULL;
  int cur_seq;

  while (cur != NULL) {
    next = cur->top;
    cur_seq = cur->seq;
    cur->top = nodes[cur_seq].top;
    nodes[cur_seq].top = cur;
    nodes[cur_seq].cur_stack = cur_seq;
    nodes[cur_seq].pre = NULL;
    nodes[cur_seq].roof = cur;
    cur = next;
  }

  block->top = NULL;
  nodes[nodes[block->seq].cur_stack].roof = block;
}

void a2b (Node nodes[N], int a, int b) {
  Block *block_a = nodes[a].ori;
  Block *block_b = nodes[b].ori;

  if (nodes[a].pre != NULL) {
    nodes[a].pre->top = NULL;
  } else {
    nodes[a].top = NULL;
  }

  nodes[nodes[b].cur_stack].roof = nodes[nodes[a].cur_stack].roof;
  nodes[nodes[a].cur_stack].roof = nodes[a].pre;

  block_b->top = block_a;
  nodes[a].pre = block_b;
  nodes[a].cur_stack = nodes[b].cur_stack;
}

void move_onto (Node nodes[N], int a, int b) {
  Block *block_a = nodes[a].ori;
  Block *block_b = nodes[b].ori;

  return_up_stacks (nodes, block_a);
  return_up_stacks (nodes, block_b);

  a2b (nodes, a, b);
}

void move_over (Node nodes[N], int a, int b) {
  Block *block_a = nodes[a].ori;
  int cur_stack_b = nodes[b].cur_stack;

  return_up_stacks (nodes, block_a);

  a2b (nodes, a, nodes[cur_stack_b].roof->seq);
}

void a_block2b (Node nodes[N], int a, int b) {
  Block *block_a = nodes[a].ori;
  Block *next;

  a2b (nodes, a, b);
  next = block_a->top;
  while (next != NULL) {
    nodes[next->seq].cur_stack = nodes[b].cur_stack;
    next = next->top;
  }
}

void pile_onto (Node nodes[N], int a, int b) {
  Block *block_b = nodes[b].ori;

  return_up_stacks (nodes, block_b);
  a_block2b (nodes, a, b);
}

void pile_over (Node nodes[N], int a, int b) {
  int cur_stack_b = nodes[b].cur_stack;
  a_block2b (nodes, a, nodes[cur_stack_b].roof->seq);
}


void implement_cmd (Node nodes[N], char cmd[M]) {
  char action[M], type[M];
  int a, b;

  sscanf (cmd, "%s %d %s %d\n", action, &a, type, &b);
  if (nodes[a].cur_stack == nodes[b].cur_stack)
    return;

  if (!strcmp (action, "move") && !strcmp (type, "onto"))
    move_onto (nodes, a, b);
  else if (!strcmp (action, "move") && !strcmp (type, "over"))
    move_over (nodes, a, b);
  else if (!strcmp (action, "pile") && !strcmp (type, "onto"))
    pile_onto (nodes, a, b);
  else if (!strcmp (action, "pile") && !strcmp (type, "over"))
    pile_over (nodes, a, b); 
  else
    return;
}


int is_quit (char cmd[M]) {
  if (!strcmp (cmd, "quit\n"))
    return 1;
  else
    return 0;
}

void output (Node nodes[N], int n) {
  int i;
  Block *block;
  for (i=0; i<n; i++) {
    printf ("%d:", i);
    if (nodes[i].top != NULL) {
      block = nodes[i].top;
      while (block != NULL) {
        printf (" %d", block->seq);
        block = block->top;
      }
    }
    printf ("\n");
  }
}

Block * new_block (int seq) {
  Block *block = (Block *)malloc (sizeof(Block));
  block->seq = seq;
  block->top = NULL;
  return block;
}

void init (Node nodes[N], int n) {
  int i;
  Block *block;
  for (i=0; i<n; i++) {
    block = new_block (i);
    nodes[i].top = nodes[i].ori = nodes[i].roof = block;
    nodes[i].cur_stack = i;
    nodes[i].pre = NULL;
  }
}

int main() {
  int n;
  char cmd[M];
  Node nodes[N];
  int i;

  scanf ("%d\n", &n);
  init (nodes, n);

  while (fgets (cmd, M, stdin)) {
    if (is_quit (cmd))
      break;
    implement_cmd (nodes, cmd); 
  } 

   output (nodes, n); 

  return 0;
}

