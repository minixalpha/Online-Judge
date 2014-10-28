#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    int val;
    struct _node *next;
}Node;

Node *new_node(int val, Node *next) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->val = val;
    node->next = next;
}

Node *make_list(int m) {
    Node *list = new_node(0, NULL);
    Node *tail = list;
    int i, n;
    for(i=0; i<m; i++) {
        scanf("%d", &n);
        Node *node = new_node(n, NULL);
        tail->next = node;
        tail = node;
    }
    return list;
}

Node *reverse_list(Node *list) {
    if (list == NULL) return NULL;

    Node *r_list = new_node(0, NULL);
    Node *np = list->next;
    while (np != NULL) {
        list->next = np->next;
        np->next = r_list->next;
        r_list->next = np;
        np = list->next;
    }
    free(list);
    return r_list;
}

void *print_list(Node *list) {
    if (list == NULL) return;

    Node *p = list->next;
    printf("%d", p->val);
    p = p->next;
    while (p != NULL) {
        printf(" %d", p->val);
        p = p->next;
    }
    printf("\n");
}

void free_list(Node *list) {
    Node *p, *np;
    p = list;
    while (p != NULL) {
        np = p->next;
        free(p);
        p = np;
    }
}

int main(void) {
    int m;
    while (scanf("%d", &m) == 1) {
        if (m == 0) {
            printf("NULL\n");
            continue;
        }
        Node *list = make_list(m);
        Node *r_list = reverse_list(list);
        print_list(r_list);
        free_list(r_list);
    }
    return 0;
}
