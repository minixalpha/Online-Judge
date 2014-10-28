#include <stdio.h>

int array[1000000];

int main(void) {
    int n, i, start, mid, end, min;
    while(scanf("%d", &n) > 0) {

        for (i=0; i<n; i++) {
            scanf("%d", &array[i]);
        }

        start = 0;
        end = n - 1; 
        if (start == end) { 
            printf("%d\n", array[0]); 
            continue;
        }
        if (array[start] < array[end]) {
            printf("%d\n", array[0]); 
            continue;
        }

        while (start < end) {
            mid = start + (end - start) / 2;
            if (mid>=1 && array[mid]<array[mid-1]) {
                printf("%d\n", array[mid]);
                break;
            } else if (mid < n-1 && array[mid]>array[mid+1]) {
                printf("%d\n", array[mid+1]);
                break;
            } else {
                if (array[mid] > array[0]) {
                    start = mid + 1;
                } else if (array[mid] < array[0]) {
                    end = mid - 1;
                } else {
                    printf("%d\n", array[0]);
                    break;
                }
            }
        }
    }
    return 0;
}
