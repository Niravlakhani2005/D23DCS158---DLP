%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Grammar:
S → i E t S S' | a
S' → e S | ε
E → b
*/

int isValid = 1;
int pos = 0;
char *input_str; 

int parse_S();
int parse_S_PRIME();
int parse_E();

int match(char c) {
    if (input_str[pos] == c) {
        pos++;
        return 1;
    }
    return 0;
}

int parse_E() {
    return match('b');
}

int parse_S_PRIME() {
    if (input_str[pos] == 'e') {
        pos++;
        return parse_S();
    }
    return 1;
}

int parse_S() {
    int save_pos = pos;
    
    if (match('i')) {
        if (parse_E() && match('t')) {
            if (parse_S() && parse_S_PRIME()) {
                return 1;
            }
        }
        pos = save_pos; // Backtrack
        return 0;
    }
    
    if (match('a')) {
        return 1;
    }
    
    return 0;
}

%}

%%
.|\n    { }
%%

int yywrap() {
    return 1;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    input_str = argv[1]; 
    yy_scan_string("");
    yylex();
    
    if (parse_S() && input_str[pos] == '\0') {
        printf("Valid string\n");
    } else {
        printf("Invalid string\n");
    }
    
    return 0;
}