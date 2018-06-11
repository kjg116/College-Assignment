//*****************************************************************************
// purpose: CSE 4713 / 6713 Assignment 2 Skeleton code
//*****************************************************************************
#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <stdlib.h>

using namespace std;

#include "lexer(1).h"
#include "parseTree.h"
#include "interpreter.h"

// Instantiate global variables
extern FILE *yyin;         // input stream
extern FILE *yyout;        // output stream
extern int   yyleng;       // length of current lexeme
extern char *yytext;       // text of current lexeme
extern int   yylex();      // the generated lexical analyzer
extern int yyLine;

// Function declarations for checking whether the current token is
// in the first set of each production rule.
bool IsFirstOfP(void);
bool IsFirstOfS(void);
bool IsFirstOfJ(void);
bool IsFirstOfK(void);
bool IsFirstOfL(void);
bool IsFirstOfM(void);
bool IsFirstOfA(void);
bool IsFirstOfF(void);
bool IsFirstOfI(void);
bool IsFirstOfE(void);
bool IsFirstOfT(void);
bool IsFirstOfR(void);

#define VERBOSE
expressionDictionary combinatorDictionary ;

// Production functions
void P(void);
void S(void);
void K(void);
void J(void);
void L(void);
expressionP A(void);
expressionP I(void);
expressionP F(void);
void M(void);
int E(void);
int T(void);
int R(void);

//Default set variables
int maxEvalSteps = 10000;
int preOrderEvaluate = 1;
int printLevel = 1;


//*****************************************************************************
// Function to help print the tree nesting
string psp( int n ) // Stands for p-space, but I want the name short
{
  string str( n, ' ' );
  return str;
}

// Needed global variables
int iTok;                  // The current token
typedef map<string, int> SymbolTableT;
SymbolTableT SymbolTable;  // The symbol table

#ifdef VERBOSE
int parsingDepth = -1 ;
#endif

//*****************************************************************************
// The main processing loop
int main( int argc, char* argv[] )
{
  int token;   // hold each token code

  yyLine = 1;
  // Set the input and output streams
  yyout = stdout;
  yyin = stdin;
  // Get the first token
  iTok = yylex();
  // Fire up the parser!
  try {
    // Process P Production
    P();

    if( iTok != TOK_EOF )
      throw "end of file expected, but there is more here!";
  }
  catch( char const *errmsg ) {
    cout << endl << "***ERROR (line " << yyLine << "): "<< errmsg << endl;
    exit(-1) ;
    while(!feof(yyin)) {
      iTok = yylex() ;
	  yyLine++;
	  if (iTok == TOK_SEMICOLON)
		  break;
    }
    iTok = yylex() ;
  }

  return 0;
}

//*****************************************************************************
// <P> --> <S> { <S> }
void P(void)
{
	static int Pcnt = 0; // Count the number of P's
	int CurPcnt = Pcnt++;
	char const *Perr =
		"statement does not start with recognized keyword";

	// This section should be expanded to implement the grammar rules for the
	// program
  
	if (iTok == TOK_EOF) {
		return;
	}

	while(iTok != TOK_EOF)
	{
		if (IsFirstOfS())
		{
			S();
		}
		else {
			throw Perr;
		}
	}
  cout << "Combinator Dictionary is:" << endl;
  combinatorDictionary.Print(cout);
  cout << "variableSettings:" << endl;
  cout << "maxEvalSteps: " << maxEvalSteps << endl;
  cout << "preOrderEvaluate: " << preOrderEvaluate << endl;
  cout << "printLevel: " << printLevel << endl;
}
//*****************************************************************************
// <s> --> (J | K | L | M) ';'
void S(void)
{
	static int Scnt = 0; // Count the number of S's
	int CurScnt = Scnt++;
	char const *Serr =
		"statement does not start with recognized keyword";

	// This section should be expanded to implement the grammar rules for the
	// program
	if (IsFirstOfK()) {
		K();
	}
	else if(IsFirstOfM()) {
		M();
	}
	else if (IsFirstOfJ()) {
		J();
	}
	else if (IsFirstOfL()) {
		L();
	}
	else {
		throw Serr;
	}
	iTok = yylex();
}
//*****************************************************************************
// <L> --> "dictionary"
void L(void)
{
	static int Lcnt = 0; // Count the number of L's
	int CurLcnt = Lcnt++;

	// This section should be expanded to implement the grammar rules for the
	// program

	cout << "Combinator Dictionary is:" << endl;

	combinatorDictionary.Print(cout);

	iTok = yylex();

}
//*****************************************************************************
// <K> --> "evaluate" A
void K(void)
{
	static int Kcnt = 0; // Count the number of K's
	int CurKcnt = Kcnt++;
	char const *Aerr =
		"expected: 'ID' | 'CID' | '\' | '{' | '(' ";
	expressionP expression;

	// This section should be expanded to implement the grammar rules for the
	// program

	iTok = yylex();

	if (IsFirstOfA()) {
		expression = A();
	}
	else {
		throw Aerr;
	}
  if (preOrderEvaluate != 0) {
    cout << "evaluatePreOrder with expression: " << expression->String() << endl;
    expression = evaluatePreOrder(expression, combinatorDictionary,
    maxEvalSteps, printLevel);
  }
  else {
    cout << "evaluatePostOrder with expression: " << expression->String() << endl;
    expression = evaluatePostOrder(expression, combinatorDictionary,
    maxEvalSteps, printLevel);
  }

	cout << "Expression Evaluates To: " << expression->String() << endl;

}
//*****************************************************************************
// <J> --> "combinator" ["evaluate"] ID A
void J(void)
{
  static int Jcnt = 0; // Count the number of J's
	int CurJcnt = Jcnt++;
	char const *Aerr =
		"expected: 'ID' | 'CID' | '\' | '{' | '(' ";
	string name;
	expressionP expression;

	// This section should be expanded to implement the grammar rules for the
	// program
  bool eval = false;
	iTok = yylex();

	switch (iTok) {
		case TOK_EVALUATE:
			iTok = yylex();
			if (iTok != TOK_IDENTIFIER) {
				throw "expected: Identifier";
			}
      eval = true;
		case TOK_IDENTIFIER:
      int count = 0;
			name = yytext;
			iTok = yylex();
			if (IsFirstOfA()) {
				expression = A();
      if (hasUnboundVars(canonicalRenameBoundVars(expression, count))){
        throw "Error in J function of Parser.cpp";
      } else {
        if(eval){
          int depth = 0;
          if (preOrderEvaluate != 0){
            expression = evaluatePreOrder(expression, combinatorDictionary, maxEvalSteps, 0);
          } else {
            expression = evaluatePostOrder(expression, combinatorDictionary, maxEvalSteps, 0);
          }
        }
      }
      if (combinatorDictionary.hasItem(name) != true){
        combinatorDictionary.insertItem(name, expression);
	    }
    }
  }
}
//*****************************************************************************
// <A> --> I {I}
expressionP A(void)
{
	static int Acnt = 0; // Count the number of A's
	int CurAcnt = Acnt++;
	char const *Ierr =
		"expected: 'ID' | 'CID' | '\' | '{' | '(' ";

	expressionP term;
	expressionP next_term;

	// This section should be expanded to implement the grammar rules for the
	// program
	if (IsFirstOfI()) {
		term = I();
	}
	else {
		throw Ierr;
	}

	while (IsFirstOfI())
	{
		next_term = I();
		term = makeApplication(term, next_term);
	}

	return term;
}
//*****************************************************************************
// <I> --> CID | ID | '(' A ')' | F
expressionP I(void)
{
	static int Icnt = 0; // Count the number of I's
	int CurIcnt = Icnt++;
	char const *Aerr =
		"expected: 'ID' | 'CID' | '\' | '{' | '(' ";
	char const *Ferr =
		"expected: '{' | 'slash' ";

	expressionP term;

	// This section should be expanded to implement the grammar rules for the
	// program
	switch (iTok)
	{
		case TOK_IDENTIFIER:
			term = makeVariable(yytext);
			iTok = yylex();
			break;

		case TOK_CIDENTIFIER:
      term = makeCombinator(yytext);
      term->name.erase(term->name.begin());
			iTok = yylex();
			break;

		case TOK_OPENPAREN:
			iTok = yylex();
			if (IsFirstOfA())
			{
				term = A();
			}
			else {
				throw Aerr;
			}
			if (iTok == TOK_CLOSEPAREN) {
				iTok = yylex();
			}
			else {
				throw "expected: )";
			}
			break;
		case TOK_SLASH:
			if (IsFirstOfF()) {
				term = F();
			}
			else {
				throw Ferr;
			}
			break;
		case TOK_OPENBRACE:
      //iTok = yylex();
			if (IsFirstOfF()) {
				term = F();
			}
			else {
				throw Ferr;
			}
			break;
	}

	return term;
}
//*****************************************************************************
// <F> --> "\" ID "." A | "{" F "}"
expressionP F(void)
{

	static int Fcnt = 0; // Count the number of I's
	int CurFcnt = Fcnt++;
	char const *Aerr =
		"Term does not start with 'ID' | 'CID' | '\' | '{' | '(' ";
	char const *Ferr =
		"expected:   'slash' | '{' ";
	char const *noiderr =
		"expected:  identifier";
	char const *nodoterr =
		"expected:  '.'";

	string name;
	expressionP argument;
	expressionP term;

	// This section should be expanded to implement the grammar rules for the
	// program
	switch (iTok)
	{
	case TOK_SLASH:
		iTok = yylex();
		if (iTok == TOK_IDENTIFIER) {
			name = yytext;
			iTok = yylex();
		}
		else {
			throw noiderr;
		}
		if (iTok == TOK_DOT) {
			iTok = yylex();
		}
		else {
			throw nodoterr;
		}
		while(IsFirstOfA()) {
			argument = A();
			term = makeSlashDot(name, argument);
		}
		break;

	case TOK_OPENBRACE:
		iTok = yylex();
		if (IsFirstOfF()) {
			term = F();
		} else {
			throw Ferr;
		}
		if (iTok == TOK_CLOSEBRACE) {
			iTok = yylex();
		} else {
			throw "expected: }";
		}
		break;
	}
	return term;
}
//*****************************************************************************
// <M> --> "set" ID E
void M(void) {

	int rValue;        // Value returned from expression
	static int Mcnt = 0; // Count the number of M's
	int CurMcnt = Mcnt++;


	// Next should be an identifier; save its name
	iTok = yylex();
	if (iTok != TOK_IDENTIFIER)
		throw "missing identifier in assignment statement";
	string IDname = yytext;

	// Next should be an expression
	iTok = yylex();
	if (IsFirstOfE())
		rValue = E();
	else
		throw "missing expression in assignment statement";

	// If the identifier is not yet in the symbol table, store it there
	SymbolTableT::iterator it = SymbolTable.find(IDname);
	//cout << "symbol table says: " << (it == SymbolTable.end()) << endl;
	if (it == SymbolTable.end()) {
		SymbolTable.insert(pair<string, int>(IDname, 1.0));
	}

	// Update ID in symbol table with value from expression
	it = SymbolTable.find(IDname);
	it->second = rValue;
	//cout << "key: " << it->first << " val: " << it->second << endl;

  if (it->first == "preOrderEvaluate")
      preOrderEvaluate = it->second;
  if (it->first == "maxEvalSteps")
      maxEvalSteps = it->second;
  if (it->first == "printLevel")
      printLevel = it->second;

}
//*****************************************************************************
// <E> --> T { ( + | - ) T}
int E(void) {
	int rValue1 = 0;   // The value to return
	int rValue2;
	static int Ecnt = 0; // Count the number of E's
	int CurEcnt = Ecnt++;
	char const *Terr =
		"term does not start with 'ID' | 'INTLIT' | '('";

	// We next expect to see a T
	if ( IsFirstOfT() )
		rValue1 = T();
	else
		throw Terr;

	// As long as the next token is + or -, keep parsing T's
	while (iTok == TOK_PLUS || iTok == TOK_MINUS)
	{
		int iTokLast = iTok;
		iTok = yylex();
		if ( IsFirstOfT() )
			rValue2 = T();
		else
			throw Terr;

		// Perform the operation to update rValue1 acording to rValue2
		switch (iTokLast)
		{
		case TOK_PLUS:
			rValue1 = rValue1 + rValue2;
			break;

		case TOK_MINUS:
			rValue1 = rValue1 - rValue2;
			break;
		}
	}

	return rValue1;
}
//*****************************************************************************
// <T> --> R { ( *  |  / ) R }
int T(void) {
	int rValue1 = 0;   // The value to return
	int rValue2;
	static int Tcnt = 0; // Count the number of T's
	int CurTcnt = Tcnt++;
	char const *Rerr =
		"factor does not start with 'ID' | 'INTLIT' | '('";

	// We next expect to see a R
	if (IsFirstOfR())
		rValue1 = R();
	else
		throw Rerr;

	// As long as the next token is * or /, keep parsing F's
	while (iTok == TOK_MULTIPLY || iTok == TOK_DIVIDE)
	{
		int iTokLast = iTok;
		iTok = yylex();
		if ( IsFirstOfR() )
			rValue2 = R();
		else
			throw Rerr;

		// Perform the operation to update rValue1 acording to rValue2
		switch (iTokLast)
		{
		case TOK_MULTIPLY:
			rValue1 = rValue1 * rValue2;
			break;

		case TOK_DIVIDE:
			rValue1 = rValue1 / rValue2;
			break;
		}
	}

	return rValue1;
}
//*****************************************************************************
// <R> --> INTLIT | (E)
int R(void) {
	int rValue = 0;           // the value to return
	SymbolTableT::iterator it;  // look up values in symbol table
	static int Rcnt = 0;        // Count the number of R's
	int CurRcnt = Rcnt++;


	switch(iTok) {
	case TOK_INTLIT:

		// Capture the value of this literal
		rValue = (int)atof(yytext);

		iTok = yylex();
		break;

	case TOK_OPENPAREN:
		// We expect (E); parse it
		iTok = yylex();
		rValue = E();
		if (iTok == TOK_CLOSEPAREN) {
			iTok = yylex();
		}
		else
			throw "expected: )";
		break;

	default:
		// If we made it to here, syntax error
		throw "factor does not start with 'ID' | 'INTLIT' | '('";
	}

	return rValue;
}
//*****************************************************************************
bool IsFirstOfP(void)
{
	return iTok == TOK_COMBINATOR || iTok == TOK_EVALUATE || iTok == TOK_DICTIONARY || iTok == TOK_SET;
}
//*****************************************************************************
bool IsFirstOfS(void)
{
	return iTok == TOK_COMBINATOR || iTok == TOK_EVALUATE || iTok == TOK_DICTIONARY || iTok == TOK_SET;
}
//*****************************************************************************
bool IsFirstOfJ(void)
{
	return iTok == TOK_COMBINATOR;
}
//*****************************************************************************
bool IsFirstOfK(void)
{
	return iTok == TOK_EVALUATE;
}
//*****************************************************************************
bool IsFirstOfL(void)
{
	return iTok == TOK_DICTIONARY;
}
//*****************************************************************************
bool IsFirstOfM(void)
{
	return iTok == TOK_SET;
}
//*****************************************************************************
bool IsFirstOfA(void)
{
	return iTok == TOK_IDENTIFIER || iTok == TOK_CIDENTIFIER || iTok == TOK_SLASH || iTok == TOK_OPENPAREN || iTok == TOK_OPENBRACE || iTok == TOK_OPENBRACKET;
}
//*****************************************************************************
bool IsFirstOfF(void)
{
	return iTok == TOK_SLASH || iTok == TOK_OPENBRACE || iTok == TOK_OPENBRACKET;
}
//*****************************************************************************
bool IsFirstOfI(void)
{
	return iTok == TOK_IDENTIFIER || iTok == TOK_CIDENTIFIER || iTok == TOK_SLASH || iTok == TOK_OPENPAREN || iTok == TOK_OPENBRACE || iTok == TOK_OPENBRACKET;
}
//*****************************************************************************
bool IsFirstOfE(void)
{
	return iTok == TOK_OPENPAREN || iTok == TOK_INTLIT;
}
//*****************************************************************************
bool IsFirstOfT(void)
{
	return iTok == TOK_OPENPAREN || iTok == TOK_INTLIT;
}
//*****************************************************************************
bool IsFirstOfR(void)
{
	return iTok == TOK_OPENPAREN || iTok == TOK_INTLIT;
}
//*****************************************************************************
