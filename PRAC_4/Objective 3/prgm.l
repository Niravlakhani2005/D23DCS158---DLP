%{
#include <stdio.h>
#include <stdlib.h>

int char_count = 0;
int word_count = 0;
int line_count = 0;
int space_count = 0;
int tab_count = 0;
%}

%%
\n      { line_count++; }
[ ]+    { space_count += yyleng; }
[\t]+   { tab_count += yyleng; }
[a-zA-Z]+ { 
            char_count += yyleng;
            word_count++;
        }
[^a-zA-Z \t\n]+ { 
            char_count += yyleng;
        }
%%

int yywrap(void) {
    return 1;
}

int main() {
    extern FILE *yyin;

    yyin = fopen("Input.txt", "r");

    yylex();
    fclose(yyin);

    printf("Characters: %d\n", char_count);
    printf("Words: %d\n", word_count);
    printf("Lines: %d\n", line_count);
    printf("Whitespaces: %d\n", space_count);
    printf("Tabs: %d\n", tab_count);

    return 0;
}