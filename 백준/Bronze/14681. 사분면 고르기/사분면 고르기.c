#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, y;
    scanf("%d %d", &x, &y);
    x = x / abs(x);
    y = y / abs(y);
    switch (x)
    {
    case 1:
        switch (y)
        {
        case 1:
            printf("1");
            break;
        case -1:
            printf("4");
            break;
        default:
            break;
        }
        break;
    case -1:
        switch (y)
        {
        case 1:
            printf("2");
            break;
        case -1:
            printf("3");
            break;
        default:
            break;
        }
        break;
    default:
        break;
    }
}