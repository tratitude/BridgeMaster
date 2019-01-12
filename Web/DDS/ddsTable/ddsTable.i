%module ddsTable
%{
#include "ddsTable.h"
%}

typedef struct{
    char s[13]; // spade
    char h[13]; // hart
    char d[13]; // diamond
    char c[13]; // club
}Deck;
void ddsTable();