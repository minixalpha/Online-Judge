/*
 * Problem: UVa 127 - "Accordian" Patience
 * Lang: ANSI C
 * Time: 0.092
 * Author: minix
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define N 52
#define M 3

typedef struct _Node {
  int num;
  char info[M];
  struct _Node *left;
  struct _Node *right;
  struct _Node *down;
}Node;

typedef struct _List {
  Node * head;
  Node * tail;
  int num;
}List;


/* delete node, as pop in stack */
Node * delete (List *list, Node *node) {
  Node *left = node->left;
  Node *right = node->right;
  Node *down = node->down;

  if (node == NULL) return NULL;
  if (right == NULL)
    list->tail = left;

  if (down == NULL) {
    if (left != NULL) 
      left->right = right;
    if (right != NULL)
      right->left = left;
    list->num -= 1;
  } else {
    if (left != NULL) 
      left->right = down;
    if (right != NULL)
      right->left = down;
    down->left = left;
    down->right = right;
  }

  return node;
}

/* add node, as push in stack */
Node * add_top (Node *des, Node *src) {
  Node *left = des->left;
  Node *right = des->right;

  if (des == NULL || src == NULL)
    return NULL;

  if (left != NULL) 
    left->right = src;
  if (right != NULL)
    right->left = src;

  src->left = left;
  src->right = right;
  src->down = des;

  return src;
}

/* generate new node */
Node * new_node (char cards[M]) {
  Node * node = (Node *)malloc(sizeof(Node));
  memset (node->info, 0, sizeof(node->info[0])*M);
  strcpy (node->info, cards);
  node->left = node->right = node->down = NULL;
  node->num = 1;
  return node;
}

/* generate new list */
List * new_list () {
  List * list = (List *)malloc(sizeof(List));
  Node * node = (Node *)malloc(sizeof(Node));
  list->head = list->tail = node;
  list->num = 0;

  return list;
}

/* add node to list */
Node * add_to_list (List *list, Node *node) {
  if (list == NULL || node == NULL)
    return NULL;

  list->tail->right = node;
  node->left = list->tail;
  list->tail = node;
  list->num += 1;

  return node;
}

/* output list, use to test */
void output_list (List *list) {
  Node * node = list->head->right;
  Node * down = NULL;
  while (node != NULL) {
    printf ("%s ", node->info);
    down = node->down;
    while (down != NULL) {
      printf ("%s ", down->info);
      down = down->down;
    }
    printf ("\n");
    node = node->right;
  }
  printf ("\n");
}

/* free list */
void free_list (List *list) {
  Node * node = list->head->right;
  Node * next = node;

  while (node != NULL) {
    next = node->right;
    free (node);
    node = next;
  }
  
  list->tail = list->head;
  list->num = 0;
}

/* determine whether match or not */
int match (Node *na, Node *nb) {
  if (na->info[0] == nb->info[0] ||
      na->info[1] == nb->info[1])
    return 1;
  else
    return 0;
}

/* find pos of the node which is first match with currrent node */
Node * find_first_match (List *list, Node *node, Node *start) {
  if (list == NULL || node == NULL)
    return NULL;
  Node *head = list->head;

  if (start->left!=head \
      && start->left->left!= head \
      && start->left->left->left != head \
      && match (node, start->left->left->left)
      )
    return start->left->left->left;

  if (start->left != head \
      && match (node, start->left)
     )
    return start->left;

  return NULL;
}

/* find the final match node of current node */
Node * find_final_match (List *list, Node *node) {
  Node * match_node = find_first_match (list, node, node);
  Node * last_match_node = NULL;
  while (match_node != NULL) {
    last_match_node = match_node;
    match_node = find_first_match (list, node, last_match_node);
  }
  return last_match_node;
}

/* solutions at top level */
void solve (List *list) {
  Node *node = list->head->right;
  Node *match_node = NULL;

  while (node != NULL) {
    match_node = find_final_match (list, node);
    if (match_node != NULL) {
      delete (list, node);
      add_top (match_node, node);
      node->num = match_node->num + 1;

      node = node->right;
    } else {
      node = node->right;
    }
  }
}

/* output result */
void output_result (List *list) {
  Node * node = list->head->right;
  if (list->num > 1)
    printf ("%d piles remaining:", list->num);
  else
    printf ("%d pile remaining:", list->num);

  while (node != NULL) {
    printf (" %d", node->num);
    node = node->right;
  }
  printf ("\n");
}


int main() {
  int i;
  char card[M];
  Node *node;
  List *list = new_list();

  while (scanf ("%s", card) != EOF) {
    if (!strcmp (card, "#")) break;
    node = new_node (card); 
    add_to_list (list, node);

    for (i=0; i<N-1; i++) {
      scanf ("%s", card);
      node = new_node (card);
      add_to_list (list, node);
    }
    solve (list);
    output_result (list);

    /* output_list (list); */
    free_list (list);
  }

  return 0;
}
