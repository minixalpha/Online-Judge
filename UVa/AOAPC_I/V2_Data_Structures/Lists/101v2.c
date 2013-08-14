#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define N 30
#define M 30

typedef struct _stack {
  int info[N];
  int top;
}Stack;

void push (Stack *stack, int n) {
  stack->info [++(stack->top)] = n;
}

int pop (Stack *stack) {
  return stack->info [(stack->top)--];
}

int get_top (Stack *stack) {
  return stack->info [stack->top];
}

int is_quit (char cmd[M]) {
  if (!strcmp (cmd, "quit\n"))
    return 1;
  else
    return 0;
}

void pop_to_init (Stack stacks[N], int locations[N], int a) {
  int pos = locations[a];
  int cur = get_top (&stacks[pos]);
  while (cur != a) {
    cur = pop (&stacks[pos]);
    push (&stacks[ cur ], cur);
    locations [cur] = cur;
    cur = get_top (&stacks[pos]);
  }
}

void stack2stack (Stack stacks[N], int locations[N], int src, int des, int top) {
  int cur_top;
  Stack tmp_stack;
  tmp_stack.top = 0;

  do {
    cur_top = pop (&stacks[src]);
    push (&tmp_stack, cur_top);
  }while (cur_top != top);

  while (tmp_stack.top != 0) {
    cur_top = pop (&tmp_stack);
    push (&stacks[des], cur_top);
    locations[cur_top] = des;
  }
}

void move_onto (Stack stacks[N], int locations[N], int a, int b) {
  pop_to_init (stacks, locations, a);
  pop_to_init (stacks, locations, b);
  pop (&stacks [ locations[a] ]);
  push (&stacks[ locations[b] ], a);
  locations[a] = locations[b];
}

void move_over (Stack stacks[N], int locations[N], int a, int b) {
  pop_to_init (stacks, locations, a);
  pop (&stacks [ locations[a] ]);
  push (&stacks [ locations[b] ], a);
  locations[a] = locations[b];
}


void pile_onto (Stack stacks[N], int locations[N], int a, int b) {
  pop_to_init (stacks, locations, b); 
  stack2stack (stacks, locations, locations[a], locations[b], a); 
  locations[a] = locations[b]; 
}

void pile_over (Stack stacks[N], int locations[N], int a, int b) {
  stack2stack (stacks, locations, locations[a], locations[b], a);
  locations[a] = locations[b];
}

void run_cmd(Stack stacks[N], int locations[N], char cmd[M]) {
  char action[M], type[M];
  int a, b;

  sscanf (cmd, "%s %d %s %d\n", action, &a, type, &b);

  if (a == b || locations[a] == locations[b])
    return;

  if (!strcmp (action, "move") && !strcmp (type, "onto"))
    move_onto (stacks, locations, a, b);
  else if (!strcmp (action, "move") && !strcmp (type, "over"))
    move_over (stacks, locations, a, b);
  else if (!strcmp (action, "pile") && !strcmp (type, "onto"))
    pile_onto (stacks, locations, a, b);
  else if (!strcmp (action, "pile") && !strcmp (type, "over"))
    pile_over (stacks, locations, a, b); 
  else
    return;
}

void output (Stack stacks[N], int n) {
  int i, j;
  for (i=0; i<n; i++) {
    printf ("%d:", i);
    if (stacks[i].top != 0) {
      for (j=1; j<=stacks[i].top; j++)
        printf (" %d", stacks[i].info[j]);
    }
    printf ("\n");
  }
}

int main() {
  int n, i;
  int locations[N];
  char cmd[M];
  Stack stacks[N];

  scanf ("%d\n", &n);
  for (i=0; i<n; i++) {
    stacks[i].top = 0;
    push (&stacks[i], i);
    locations[i] = i;
  }

  while (fgets (cmd, M, stdin)) {
    if (is_quit (cmd))
      break;
    run_cmd (stacks, locations, cmd);
  }

  output (stacks, n);
  return 0;
}
