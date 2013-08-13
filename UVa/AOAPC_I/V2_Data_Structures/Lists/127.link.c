#include <stdio.h>

#define N 52
#define M 3

typedef struct _Node {
  char info[M];
  struct _Node *left;
  struct _Node *right;
  struct _Node *down;
}Node;

int match (Node *na, Node *nb) {
  if (na->info[0] == nb->info[0] ||
      na->info[1] == nb->info[1])
    return 1;
  else
    return 0;
}

Node * delete (Node *node) {
  Node *left = node->left;
  Node *right = node->right;
  Node *down = node->down;

  if (node == NULL) return NULL;

  if (left != NULL) 
    left->right = right;
  if (right != NULL)
    right->left = left;

  return node;
}

Node * add (Node *des, Node *src) {
  Node *down = des->down;

  if (des == NULL || src == NULL)
    return NULL;

}

int main() {
  return 0;
}
