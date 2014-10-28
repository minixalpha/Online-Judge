#include <stdio.h>

int array[1000];
int left[1000];
int right[1000];
int queue[1000];

int main(void) {
    int n, i, j, c, l, r;
    scanf("%d", &n);
    for(i=0; i<n; i++) {
        scanf("%d", &array[i]);
    }
    for(i=0; i<n; i++) {
        scanf("%c", &c);
        if (c == 'd') {
            scanf("%d %d", &l, &r);
            left[i] = l;
            right[i] = r;
        } else if (c == 'l') {
            scanf("%d", &l);
            left[i] = l;
        } else if (c == 'r') {
            scanf("%d", &r);
            right[i] = r;
        }
    }
    i = 0, j = 0;
    return 0;
}
