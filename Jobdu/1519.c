#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    int val;
    struct _node *next;
}Node;

Node *newNode(int val, Node *next) {
    Node *nList = (Node *)malloc(sizeof(Node));
    nList->val = val;
    nList->next = next;
    return nList;
}

int main(void) {
    int n, m, k;
    int i, j;
    while (scanf("%d %d", &n, &m) > 0) {
        if (m == 0 && n == 0) {
            printf("NULL\n");
            continue;
        }

        Node *nList = newNode(0, NULL);
        Node *nTail = nList;
        Node *mList = newNode(0, NULL);
        Node *mTail = mList;

        for(i = 0; i < n; i++) {
            scanf("%d", &k);
            Node *nNode = newNode(k, NULL);
            nTail->next = nNode;
            nTail = nNode;
        }
        for(j = 0; j < m; j++) {
            scanf("%d", &k);
            Node *mNode = newNode(k, NULL);
            mTail->next = mNode;
            mTail = mNode;
        }

        Node *cList = newNode(0, NULL);
        Node *cTail = cList;

        Node *nCur = nList->next;
        Node *mCur = mList->next;

        Node *next = NULL;

        while (nCur != NULL && mCur != NULL) {
            if (nCur->val < mCur->val) {
                next = nCur->next;
                cTail->next = nCur;
                cTail = nCur;
                nCur->next = NULL;
                nCur = next;
            } else {
                next = mCur->next;
                cTail->next = mCur;
                cTail = mCur;
                mCur->next = NULL;
                mCur = next;
            }
        }

        if (nCur != NULL) {
            cTail->next = nCur;
            cTail = nTail;
        }

        if (mCur != NULL) {
            cTail->next = mCur;
            cTail = mTail;
        }

        Node *cCur = cList->next;
        printf ("%d", cCur->val);
        cCur = cCur->next;
        while (cCur != NULL) {
            printf (" %d", cCur->val);
            cCur = cCur->next;
        }
        printf("\n");
    }
    return 0;
}
