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

void FileTable(ddTableResults * table);

void ddsTable()
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
  FILE *db = fopen("ddsDB.txt", "r");
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
    FileTable(&table);
  }
}
void FileTable(ddTableResults * table)
{
  FILE *result = fopen("ddsResult.txt", "w");
  fprintf(result, "%5d %5d %5d %5d\n",
         table->resTable[4][0],
         table->resTable[4][2],
         table->resTable[4][1],
         table->resTable[4][3]);

  for (int suit = 0; suit < DDS_SUITS; suit++)
  {
    fprintf(result, "%5d %5d %5d %5d\n",
           table->resTable[suit][0],
           table->resTable[suit][2],
           table->resTable[suit][1],
           table->resTable[suit][3]);
  }
  fclose(result);
}