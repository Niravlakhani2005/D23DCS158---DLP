%{
#include <stdio.h>
%}

%%
"charusat" { printf("university"); }
[^\n]+     { printf("%s", yytext); }
\n         { printf("\n"); return 0; }
%%

int yywrap(void) {
    return 1;
}

int main(void) {
    yylex();
    return 0;
}