#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    //////메모리값 테스트//////////
    // char든 int든 double이든 123만 같은 메몰 ㅣ참조하고 4이상으로다같음
    int *a = (int *)malloc(sizeof(int));

    printf("&a: %d\n", a);
    printf("*a: %p\n\n\n", *a);
    printf("*func add: %p\n\n\n", *(int *)malloc(sizeof(int)));

    *a = 10;
    printf("&a: %d\n", a);
    printf("*a: %p\n\n\n", *a);

    free(a);
    printf("&a: %d\n", a);
    printf("*a: %p\n\n\n", *a);
    int c, b;
    c = a + b;
    printf("%d", c);
}
