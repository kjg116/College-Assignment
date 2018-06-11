/*******************************************************************************
Date: April 12, 2017
Created By: Ed Luke
Edited By: Kelcy Gooch
*******************************************************************************/

#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <stdlib.h>

using namespace std;
#include "parseTree.h"
#include "interpreter.h"

// Recusively rename variables as long as they are not currently bound by
// slashdot operator
expressionP recursiveRenameVars(expressionP e, const string &name,
			     const string &toname) {
  switch(e->Type) {
	  case Expression::VARIABLE:
	    // If it is a variable and the name matches, do rename
	    if(e->name == name)
	      e->name = toname ;
	  case Expression::COMBINATOR:
	    // Ignore combinator variables
	    return e ;
	  case Expression::SLASHDOT:
	    // If operator not reusing name, continue to rename right branch
	    if(e->name != name)
	      e->updateRight(recursiveRenameVars(e->right,name,toname)) ;
	    return e ;
	  case Expression::APPLICATION:
	    // rename both sides of application
	    e->updateLeft(recursiveRenameVars(e->left,name,toname)) ;
	    e->updateRight(recursiveRenameVars(e->right,name,toname)) ;
	    return e ;
	  default:
	    throw "Unknown expression type in recursiveRenameVars()" ;
  }
}

/* Variation of recursiveRenameVars used to rename variables
 	 in slashdot expressions that are duplicate variable names */
expressionP recursiveSlashdot(expressionP e, const string &name, expressionP new_exp,
			     bool &sub, int &count) {
  switch(e->Type) {
	  case Expression::VARIABLE:
	    // If it is a variable and the name matches, do rename
	    if(e->name == name){
	      if(sub == true){
	      	return canonicalNoUnbound(new_exp->Copy(), count);
	      }
	      else{
	      	sub = true;
	      	return new_exp->Copy();
	      }
	  	}
	  case Expression::COMBINATOR:
	    // Ignore combinator variables
	    return e ;
	  case Expression::SLASHDOT:
	    // If operator not reusing name, continue to rename right branch
	    if(e->name != name)
	      e->updateRight(recursiveSlashdot(e->right,name, new_exp, sub, count));
	  	return e;
	  case Expression::APPLICATION:
	    // rename both sides of applicatio
	    e->updateLeft(recursiveSlashdot(e->left,name, new_exp, sub, count));
	    e->updateRight(recursiveSlashdot(e->right,name, new_exp, sub, count));
	    return e;
	  default:
	    throw "Unknown expression type in recursiveSlashdot()" ;
  }
}

/* Recursively mark all bound variables by prepending an underscore to the
   variable name. */
expressionP markBoundVariables(expressionP e) {
  switch(e->Type) {
	  case Expression::VARIABLE:
	  case Expression::COMBINATOR:
	    return e ;
	  case Expression::SLASHDOT:
	    { // For slashdot operator we first rename the variable by adding an
	      // underscore to mark this as a bound variable
	      string name = e->name ;
	      string toname = "_"+name ;
	      e->name = toname ;
	      // Update all bound variables in right expression
	      e->updateRight(recursiveRenameVars(e->right,name,toname)) ;
	      // Now mark any other slashdot bound variables on right side
	      e->updateRight(markBoundVariables(e->right)) ;
	      return e ;
	    }
	  case Expression::APPLICATION:
	    // mark both sides
	    e->updateLeft(markBoundVariables(e->left)) ;
	    e->updateRight(markBoundVariables(e->right)) ;
	    return e ;
	  default:
	    throw "Unknown expression type in markBoundVariables()" ;
  }
}

/* This procedure makes sure that all variables not marked with a leading
   underscore is changed to uppercase so unbound variables cannot capture
   bound ones */
expressionP markUnboundVariables(expressionP e) {
  switch(e->Type) {
	  case Expression::VARIABLE:
	    // If variable first character is lower case, change to upper case
	    if(e->name[0] >= 'a' && e->name[0] <= 'z')
	      e->name[0] = e->name[0] - 'a' + 'A' ;
	  case Expression::COMBINATOR:
	    return e ;
	  case Expression::SLASHDOT:
	    e->updateRight(markUnboundVariables(e->right)) ;
	    return e ;
	  case Expression::APPLICATION:
	    e->updateLeft(markUnboundVariables(e->left)) ;
	    e->updateRight(markUnboundVariables(e->right)) ;
	    return e ;
	  default:
	    throw "Unknown expression type in markUnboundVariables()" ;
  }
}

/* Convert integer count to a simple string for a variable name composed of
   lower case letters */
string integerToName(int count) {
  char namelist[] = "xyzabcdefghijklmnopqrstuvw" ;
  string name ;
  while(count > 25) {
    name = namelist[count%26] + name ;
    count = count/26 ;
  }
  name = namelist[count] + name ;
  return name ;
}

/* This replaces underscore named bound variables with a unique name
   based on the order that bound variables are encountered while searching
   the expression tree. */
expressionP prettyRenameVariables(expressionP e, int &count) {
  switch(e->Type) {
	  case Expression::VARIABLE:
	  case Expression::COMBINATOR:
	    return e ;
	  case Expression::SLASHDOT:
	    {
	      int current_var = count ;
	      count++ ;
	      prettyRenameVariables(e->right,count) ;
	      string name = e->name ;
	      string newname = integerToName(current_var) ;
	      e->name = newname ;
	      e->updateRight(recursiveRenameVars(e->right,name,newname)) ;
	    }
	    return e ;
	  case Expression::APPLICATION:
	    e->updateLeft(prettyRenameVariables(e->left,count)) ;
	    e->updateRight(prettyRenameVariables(e->right,count)) ;
	    return e ;
	  default:
	    throw "Unknown expression type in prettyRenameVariables()" ;
  }
}

/* Change all unbound variables to capitalized variables and
   rename all bound variables based on count of the binding scope
   so that substititions can be performed without variable capture*/
expressionP canonicalRenameBoundVars(expressionP e, int &count) {
  e = markBoundVariables(e) ;
  e = markUnboundVariables(e) ;
  e = prettyRenameVariables(e,count) ;
  return e ;
}

/* Variation of canonicalRenameBoundVars that doesn't affect
   unbound variables when substituting */
expressionP canonicalNoUnbound(expressionP e, int &count) {
  e = markBoundVariables(e) ;
  e = prettyRenameVariables(e,count) ;
  return e ;
}

/* Return true if expression has unbounded variables (only works after calling
   canonicalRenameBoundVars that converts unbound variables to uppercase) */
bool hasUnboundVars(expressionP e) {
    expressionP temp = e->Copy();
    switch (temp->Type) {
        case Expression::VARIABLE: {
            const char front = e->name[0];
            return front >= 'A' && front <= 'Z';
        }
        case Expression::COMBINATOR:
            return false;
        case Expression::SLASHDOT:
            return hasUnboundVars(e->right);
        case Expression::APPLICATION:
            return hasUnboundVars(temp->left) || hasUnboundVars(temp->right);
        default:
            throw "Unknown expression type in hasUnboundVars";
    }
}
//-----------------------------------------------------------------------------
// Recursive pre-order search for APPLICATION node to substitute and perform
// substitution.
// Input: e is the input expression that will be transformed
// Input: dictionary of combinators
// Input: count for unique variable names
// Output: found boolean set to true when substitution has been found (and
//         executed
// Output: returns new substitution expression, input expression is consumed
//-----------------------------------------------------------------------------
expressionP preOrderSubstitutionSearch(expressionP e, const expressionDictionary &dictionary, int &count, bool &found){
	switch(e->Type){

		// Return expression if variable or combinator
		case Expression::VARIABLE:
		case Expression::COMBINATOR:
			return e;

		// Traverse down and update the right side of the tree
		case Expression::SLASHDOT:
			e->updateRight(preOrderSubstitutionSearch(e->right, dictionary, count, found));
			return e;

		// Check the children of the application node
		case Expression::APPLICATION:
			switch(e->left->Type){

				// Break if found a variable
				case Expression::VARIABLE:
					break;

				// Substitute combinator expression if found in dictionary
				// Return error if not found
				case Expression::COMBINATOR:{
					if(dictionary.hasItem(e->left->name)){
						expressionP combinator = dictionary.getItem(e->left->name);
						found = true;
						e->updateLeft(canonicalNoUnbound(combinator, count));
					} else {
						throw "Combinator is not in dictionary";
					}
					break;
				}

				// Substitute slashdot variables
				case Expression::SLASHDOT:{
					found = true;
					bool sub = false;
					return recursiveSlashdot(e->left->right->Copy(), e->left->name, e->right->Copy(), sub, count);
				}

				// Break if found another application node
				case Expression::APPLICATION:
					break;
				default:
					throw "Unknown expression type in preOrderSubstitutionSearch";
			}

			/* Return expression if a slashdot or combinator was found
			   Traverse left side of tree if neither are found
			   Traverse right side of tree if still not found after the left side */
			if(found == true)
				return e;
			else {
				e->updateLeft(preOrderSubstitutionSearch(e->left, dictionary, count, found));
				if (found == true)
					return e;
				else{
					e->updateRight(preOrderSubstitutionSearch(e->right, dictionary, count, found));
					return e;
				}
			}
		default:
			throw "Unknown expression type in preOrderSubstitutionSearch";
	}
	return e;
}

/* Perform at most evalDepth steps of pre-order evaluations of input expression
   e.  If printLevel is nonzero, then print progress of evaluation.*/
expressionP evaluatePreOrder(expressionP e, const expressionDictionary &dictionary, int evalDepth, int printLevel){
	int count = 0, depth = 0;
	bool found = false;

	// Rename variables for duplicates
	e = canonicalNoUnbound(e, count);

	// Print out what we will be evaluating
	/*if(printLevel != 0) {
		cout << "evaluatePostOrder with expression: " << e->String() << endl;
	}*/

	// Traverse tree while allowed
	while(depth < evalDepth) {
		found = false;
		e = preOrderSubstitutionSearch(e, dictionary, count, found);

		// Exit if false
		if (found == false)
			break;

		// Print out current state of substitution
		if (printLevel != 0)
			cout << depth << "--" << e->String() << endl;

		depth++;
		if(depth == evalDepth){
			cout << "maximum number of steps exceeded!" << endl;
		}
	}

	// Rename variables for duplicates
	count = 0;
	return canonicalNoUnbound(e, count);
}

//-----------------------------------------------------------------------------
// Recursive post-order search for APPLICATION node to substitute and perform
// substitution.
// Input: e is the input expression that will be transformed
// Input: dictionary of combinators
// Input: count for unique variable names
// Output: found boolean set to true when substitution has been found (and
//         executed
// Output: returns new substitution expression, input expression is consumed
//-----------------------------------------------------------------------------
expressionP
postOrderSubstitutionSearch(expressionP e, const expressionDictionary &dictionary,
			    int &count, bool & found) {
	switch(e->Type){

		// Return expression if variable or combinator
		case Expression::VARIABLE:
		case Expression::COMBINATOR:
			return e;

		// Traverse down and update the right side of the tree
		case Expression::SLASHDOT:
			e->updateRight(postOrderSubstitutionSearch(e->right, dictionary, count, found));
			return e;

		/* Return expression if a slashdot or combinator was found
	 		Traverse left side of tree if neither are found
			Traverse right side of tree if still not found after the left side */
		case Expression::APPLICATION:
			e->updateLeft(postOrderSubstitutionSearch(e->left, dictionary, count, found));
			if(found == true)
				return e;
			else {
				e->updateRight(postOrderSubstitutionSearch(e->right, dictionary, count, found));
				if(found == true)
					return e;
			}

			switch(e->left->Type) {

				// Break if found a variable
				case Expression::VARIABLE:
					break;

				/* Substitute combinator expression if found in dictionary
				   Return error if not found */
				case Expression::COMBINATOR:{
					found = true;
					expressionP combinator = dictionary.getItem(e->left->name);
					if(combinator == 0)
						throw "Combinator is not in dictionary";
					else{
						e->updateLeft(canonicalNoUnbound(combinator, count));
						return e;
					}
				}

				// Substitute slashdot variables
				case Expression::SLASHDOT:{
					found = true;
					bool sub = false;
					return e = recursiveSlashdot(e->left->right->Copy(), e->left->name, e->right->Copy(), sub, count);
				}

				// Break if found another application node
				case Expression::APPLICATION:
					break;
				default:
					throw "Unknown expression type in postOrderSubstitutionSearch";
			}

			return e;
		default:
			throw "Unknown expression type in postOrderSubstitutionSearch";
	}
}

/* Perform at most maxNumSteps of post-order evaluations of input expression e.
   If printLevel is nonzero, then print progress of evaluation. */
expressionP evaluatePostOrder(expressionP e, const expressionDictionary &dictionary, int evalDepth, int printLevel){
	int count = 0, depth = 0;
	bool found = false;

	// Rename variables for duplicates
	e = canonicalNoUnbound(e, count);

	// Print out what we will be evaluating
	/*if(printLevel != 0) {
		cout << "evaluatePostOrder with expression: " << e->String() << endl;
	}*/

	// Traverse tree while allowed
	while(depth < evalDepth) {
		found = false;
		e = postOrderSubstitutionSearch(e, dictionary, count, found);

		// Exit if false
		if (found == false)
			break;

		// Print out current state of substitution
		if (printLevel != 0)
			cout << depth << "--" << e->String() << endl;

		depth++;
		if(depth == evalDepth){
			cout << "maximum number of steps exceeded!" << endl;
		}
	}

	// Rename variables for duplicates
	count = 0;
	return canonicalNoUnbound(e, count);
}
