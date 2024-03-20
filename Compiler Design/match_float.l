%{
#include <stdio.h>
%}

%%

[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? {
    printf("Float = {%s}\n", yytext);
}

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
