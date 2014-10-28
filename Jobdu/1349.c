#include <stdio.h>

int array[1000000];

int main(void) {
    int m, n, i, key;
    int start, end, mid;
    scanf("%d", &n);
    for(i=0; i<n; i++)
        scanf("%d", &array[i]);
    scanf("%d", &m);
    for(i=0; i<m; i++) {
        scanf("%d", &key);
        
        start = 0;
        end = n-1;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (array[mid] == key) {
                break;
            } else if (array[mid] > key) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        if (start > end) {
            printf("%d\n", 0);
        } else {
            start = mid - 1;
            while (start >= 0 && array[mid] == array[start]) {
                start --;
            }
            end = mid + 1;
            while (end < n && array[mid] == array[end]) {
                end ++;
            }
            printf("%d\n", end - start - 1);
        }
    }
    return 0;
}
