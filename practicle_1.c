#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool matchesPattern(const char *str)
{
    int len = strlen(str);

    if (len >= 2 && str[len - 1] == 'b' && str[len - 2] == 'b')
    {
        for (int i = 0; i < len - 2; i++)
        {
            if (str[i] != 'a')
            {
                return false;
            }
        }
        return true;
    }
    return false;
}

int main()
{
    int numCases;
    printf("Enter number of test cases: ");
    scanf("%d", &numCases);

    char str[100];
    for (int i = 0; i < numCases; i++)
    {
        printf("Enter test case %d: ", i + 1);
        scanf("%s", str);
        if (matchesPattern(str))
        {
            printf("%s - Accepted\n", str);
        }
        else
        {
            printf("%s - Rejected\n", str);
        }
    }

    return 0;
}
