#include <stdio.h>
void mystery(int *ptra, int *ptrb)
{
    int *temp;
    temp = ptrb;
    ptrb = ptra;
    printf("%d", ptrb);
    ptra = temp;
    printf("%d\n", *temp);
}
int main()
{
    int a = 2016, b = 0, c = 4, d = 42;
    mystery(&a, &b);
    if (a < c)
        mystery(&c, &a);
    mystery(&a, &d);
    // printf("%d", a);
    int var = 10;
    int *ptrba;   // 포인터 변수 선언
    ptrba = &var; // 포인터 변수에 var의 주소 저장

    printf("ptra의 값: %p\n", ptrba);   // 포인터 변수 ptptrbaa의 값 출력
    printf("*ptra의 값: %d\n", *ptrba); // 포인터 변수가 가리키는 변수의 값 출력
    printf("&ptra의 값: %p\n", &ptrba); // 포인터 변수 ptra의 주소 출력

    return 0;
}