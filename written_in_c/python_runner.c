#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        printf("running %s...\n\n", argv[1]);
        char program[256] = {"python \""};
        strcat(program, argv[1]);
        strcat(program, "\"");
        system(program);
        printf("\n----------pyfile finish----------\n");
        system("pause");
        return 0;
    }
}