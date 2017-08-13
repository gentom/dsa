#include <stdio.h>
#include <stdlib.h>

int BubbleSort(int x[], int n);
void ShowData(int x[], int n);
void main(void);

#define NUM_DATA 10

int BubbleSort(int x[], int n)
{
    int i, j, temp;

    for (i = 0; i < n - 1; i++)
    {
        for (j = n - 1; j > i; j--)
        {
            if (x[j - 1] > x[j])
            {                /* if the previous is bigger than current one, */
                temp = x[j]; /* then change the position */
                x[j] = x[j - 1];
                x[j - 1] = temp;
            }
        }
        ShowData(x, NUM_DATA);
        printf("\n");
    }
}

void ShowData(int x[], int n)
{
    int i;

    for (i = 0; i < n; i++)
        printf("%d\t", x[i]);
}

void main(void)
{

    int x[NUM_DATA];
    for (int i = 0; i < NUM_DATA; i++)
    {
        x[i] = rand() % 50;
    }

    printf("Before:\n");
    ShowData(x, NUM_DATA);
    printf("\n");

    printf("\nsort start\n");
    BubbleSort(x, NUM_DATA);
    printf("sort finished\n");

    printf("\nAfter:\n");
    ShowData(x, NUM_DATA);
    printf("\n");
}