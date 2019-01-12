/*
   DDS, a bridge double dummy solver.

   Copyright (C) 2006-2014 by Bo Haglund /
   2014-2016 by Bo Haglund & Soren Hein.

   See LICENSE and README.
*/


// Test program for the CalcDDtablePBN function.
// Uses the hands pre-set in hands.cpp.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "../include/dll.h"
#include "hands.h"
#include "ddsTable.h"

void FileTable(ddTableResults * table, char fileOut[100]);

void ddsTable(char fileIn[100], char fileOut[100])
{
  ddTableDealPBN tableDealPBN;
  ddTableResults table;
  int res;
  char line[80];
  bool match;
  char vul[10];

#if defined(__linux) || defined(__APPLE__)
  SetMaxThreads(0);
#endif
  FILE *db = fopen(fileIn, "r");
  if(!db) {
    fprintf(stderr,"fopen() failed in file %s at line # %d", __FILE__,__LINE__);
    exit(EXIT_FAILURE);
  }
  fgets(tableDealPBN.cards, 70, db);
  fclose(db);
  printf("%s\n", tableDealPBN.cards);
  for (int handno = 0; handno < 1; handno++)
  {

    //strcpy(tableDealPBN.cards, PBN[handno]);

    res = CalcDDtablePBN(tableDealPBN, &table);

    if (res != RETURN_NO_FAULT)
    {
      ErrorMessage(res, line);
      printf("DDS error: %s\n", line);
    }

    match = CompareTable(&table, handno);

    sprintf(line,
            "CalcDDtable, hand %d: %s\n",
            handno + 1, (match ? "OK" : "ERROR"));

    //PrintPBNHand(line, tableDealPBN.cards);

    PrintTable(&table);
    FileTable(&table, fileOut);
  }
}
void FileTable(ddTableResults * table, char fileOut[100])
{
  FILE *result = fopen(fileOut, "w");
  if(!result) {
    fprintf(stderr,"fopen() failed in file %s at line # %d", __FILE__,__LINE__);
    exit(EXIT_FAILURE);
  }
  fprintf(result, "%d %d %d %d ",
         table->resTable[4][0],
         table->resTable[4][2],
         table->resTable[4][1],
         table->resTable[4][3]);

  for (int suit = 0; suit < DDS_SUITS; suit++)
  {
    fprintf(result, "%d %d %d %d ",
           table->resTable[suit][0],
           table->resTable[suit][2],
           table->resTable[suit][1],
           table->resTable[suit][3]);
  }
  fclose(result);
}