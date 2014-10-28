#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    int val;
    struct _node *next;
}Node;

Node *make_list() {
    Node *list = (Node *)malloc(sizeof(Node));
    Node *tail = list;
    int n;
    while (scanf("%d", &n)) {
        if (n == -1) break;
        Node *node = (Node *)malloc(sizeof(Node));
        node->next = NULL;
        node->val = n;
        tail->next = node;
        tail = node;
    }
    return list;
}

Node *reverse_list(Node *list) {
    if (list == NULL) return NULL;

    Node *r_list = (Node *)malloc(sizeof(Node));
    r_list->next = NULL;

    Node *np = list->next;
    while (np != NULL) {
        list->next = np->next;
        np->next = r_list->next;
        r_list->next = np;
        np = list->next;
    }
    return r_list;
}

void *print_list(Node *list) {
    if (list == NULL) return;
    Node *p = list->next;
    while (p) {
        printf("%d\n", p->val);
        p = p->next;
    }
}

void recursive(Node *list) {
    if (list == NULL) return;
    recursive(list->next);
    printf("%d\n", list->val);
}

int main(void) {
    Node *list = make_list();
    /*
    Node *r_list = reverse_list(list);
    print_list(r_list);
    */
    recursive(list->next);
    return 0;
}
