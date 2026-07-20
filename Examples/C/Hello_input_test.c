#include <stdio.h>

int main(void)
{
    int input_test;

    printf("Hello C coding language!\n");
    printf("請輸入整數: ");

    if (scanf("%d", &input_test) != 1) {
        printf("輸入不是有效整數。\n");
        return 1;
    }

    printf("輸入: %d\n", input_test);
    return 0;
}
