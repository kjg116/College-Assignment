//*****************************************************************************
// purpose: CSE 4713 / 6713 Assignment 1: Lexical Analyzer
// created: 2-2-2017
//  author: Kelcy Gooch
//*****************************************************************************

#ifndef LEXER_H
#define LEXER_H

// Include standard IO streams
#include <stdio.h>

// The lexical analyzer global variables and functions
extern void add_character();
extern void look_up(char charater);
extern void get_character();
extern void get_non_blank();
extern int   yylex();
extern FILE *yyin;         // input stream
extern FILE *yyout;        // output stream
//extern int   yyleng;       // length of current lexeme
extern char *yytext;      // text of current lexeme


						  // Maximum lexeme length
#define MAX_LEXEME_LEN 1000

						  // Character Codes
#define LETTER			0
#define DIGIT			1
#define UNKNOWN			99

							   // List of token codes
#define TOK_COMBINATOR	 1001  // keyword - combinator 
#define TOK_EVALUATE     1002  // keyword - evaluate   
#define TOK_DICTIONARY   1003  // keyword - dictionary
#define TOK_SET	         1004  // keyword - set
#define TOK_INT			 1100  // datatype - integer
#define TOK_FLOAT        1101  // datatype - float
#define TOK_STRING       1102  // datatype - string
#define TOK_SEMICOLON    2000  // punctuation - ;  
#define TOK_OPENPAREN    2001  // punctuation - (  
#define TOK_CLOSEPAREN   2002  // punctuation - )  
#define TOK_OPENBRACKET  2003  // punctuation - [  
#define TOK_CLOSEBRACKET 2004  // punctuation - ]  
#define TOK_OPENBRACE    2005  // punctuation - {  
#define TOK_CLOSEBRACE   2006  // punctuation - }   
#define TOK_COMMA        2007  // punctuation - ,  
#define TOK_SLASH		 3000  // operator - \

#define TOK_DOT          3001  // operator - . 
#define TOK_PLUS		 3002  // operator - +
#define TOK_MINUS		 3003  // operator - - 
#define TOK_MULTIPLY     3004  // operator - *   
#define TOK_DIVIDE       3005  // operator - /   
#define TOK_ASSIGN       3006  // operator - := 
#define TOK_EQUALTO		 3007  // operator - ==
#define TOK_LESSTHAN	 3008  // operator - <  
#define TOK_GREATERTHAN  3009  // operator - >  
#define TOK_NOTEQUALTO	 3010  // operator - <>
#define TOK_AND			 3011  // operator - and 
#define TOK_OR			 3012  // operator - or
#define TOK_NOT		     3013  // operator - not
#define TOK_LENGTH	     3014  // operator - length
#define TOK_IDENTIFIER	 4000  // abstraction - identifier
#define TOK_CIDENTIFIER	 4001  // abstraction - comment-indentifier
#define TOK_INTLIT		 4002  // abstraction - integer literal
#define TOK_FLOATLIT	 4003  // abstraction - floating-point literal
#define TOK_STRINGLIT	 4004  // abstraction - string literal
#define TOK_EOF          5000  // end of file
#define TOK_EOF_SL       5001  // end of file while parsing string literal
#define TOK_UNKNOWN      6000  // unknown lexeme
#define TOK_COMMENT		 6001

#endif

