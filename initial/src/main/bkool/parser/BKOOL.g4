grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// parser

program: classDecl* EOF;

// 2.Program structure

// 2.1.class declaration
classDecl: CLASS ID (EXTENDS ID)? LP member* RP;
member: atrbDecl | methodDecl;

// 2.2.attribute declaration

atrbDecl: immutDecl | mutDecl;
mutDecl: STATIC? typ ID atrbInit? (CM ID atrbInit?)* SM;
immutDecl: (FINAL | FINAL STATIC | STATIC FINAL)? typ ID atrbInit (CM ID atrbInit)* SM;
// atrbDecl: atrbType? atrb SM;
// atrbType: FINAL | STATIC | FINAL STATIC | STATIC FINAL;
// atrb: typ (atrbInit (CM atrbInit)*);
atrbInit: EQQ exp;
typ: priTyp | classTyp | VOID | arrayTyp;
arrayTyp:  priTyp LS INTLIT RS;
priTyp: INT | FLOAT | STRING | BOOLEAN;
classTyp: ID;

// 2.3.method declaration
methodDecl: STATIC? typ? ID LB paraList? RB blockStmt;
paraList: para (SM para)*;
para: typ ID (CM ID)*;
// blockStmt below

// 3.7.5.array literal
arrayLit: LP literal (CM literal)* RP;

// 4.3.class typ

// 5.Expression
exp: equalee (LESS | LEQ | GREATER | GEQ) equalee
	| equalee;
equalee: andOree (EQ | NEQ) andOree
	| andOree;
andOree: addSubee (AND | OR) andOree
	| addSubee;
addSubee: addSubee (ADD | SUB) mulDivModee
	| mulDivModee;
mulDivModee: mulDivModee (MUL | INTDIV | FLDIV | MOD) conCatee
	| conCatee;
conCatee: conCatee (CONCAT) notee
	| notee;
notee: (NOT) notee
	| subAddee;
subAddee:  (SUB | ADD) subAddee
	| indexee;
indexee: memAccessee LS exp RS 
	| memAccessee;
memAccessee: memAccessee DOT ID 
	| memAccessee DOT ID LB argLits? RB
	| atom;
atom: THIS | ID | literal | newee | arrayLit;
newee: NEW ID LB argLits? RB;
literal: INTLIT | FLOATLIT | STRINGLIT | booleanLit;
booleanLit: TRUE | FALSE;
argLits: exp (CM exp)*;


// 5.8.this


// 5.9.operator precedence and associativity

// 5.10.typ coercion

// 5.11.evaluation order

// 6.Statement

stmt: blockStmt
	| asmStmt
	| ifStmt
	| forStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| atrbDecl
	| invokeStmt;

// 6.1.block statement
// blockStmt: LP (FINAL? atrb SM)* nullAbleStmtList? RP;
blockStmt: LP nullAbleDeclList* stmt* RP;
nullAbleDeclList: FINAL? typ ID atrbInit (CM ID atrbInit)* SM ;

// 6.2.assignment statement
asmStmt: lhs ASSIGN exp SM;
lhs: indexee | memAccessee DOT ID | ID;

// 6.3.if statement
ifStmt: IF exp THEN stmt
	| IF exp THEN stmt ELSE stmt;

 // 6.4.for statement
forStmt: FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt;

// 6.5.break statement
breakStmt: BREAK SM;

//6.6.continue statement
continueStmt: CONTINUE SM;

// 6.7.return statement
returnStmt: RETURN exp SM;

// 6.8.method invocation statement
invokeStmt: memAccessee DOT ID LB argLits? RB SM;
// 7.Scope

// 8.IO

// 3.Lexical Structure

// 3.2.comment
CMTLINE: '#' ~[\r\n]* -> skip;
CMTBLOCK: '/*' .*? '*/' -> skip;

// 3.4.keyword
ASSIGN: ':=';
CLASS: 'class';
EXTENDS: 'extends';
STATIC: 'static';
FINAL: 'final';
BOOLEAN: 'boolean';
BREAK: 'break';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
IF: 'if';
INT: 'int';
STRING: 'string';
THEN: 'then';
FOR: 'for';
THIS: 'this';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
TO: 'to';
DOWNTO: 'downto';

// 3.5.operator
ADD: '+';
SUB: '-';
MUL: '*';
FLDIV: '/';
INTDIV: '\\';
MOD: '%';
NEQ: '!=';
EQ: '==';
EQQ: '=';
LESS: '<';
GREATER: '>';
LEQ: '<=';
GEQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCAT: '^';
NEW: 'new';

// 3.6.separator
SM: ';';
CM: ',';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
LS: '[';
RS: ']';
CL: ':';
DOT: '.';

// 3.7.literal

// 3.7.1.integer literal
INTLIT: [1-9][0-9]* | [0];

// 3.7.2.float literal
FLOATLIT: INTLIT DECIMAL? EXPONENT 
	| INTLIT DECIMAL EXPONENT?;
fragment DECIMAL: DOT [0-9]*;
fragment EXPONENT: [Ee][+-]?[1-9][0-9]*;

INFL: INTLIT | FLOATLIT;

// 3.7.3.boolean literal

// 3.7.4.string literal

STRINGLIT:  '"' CHAR*	'"';


fragment CHAR: ESC | ~ [\r\n\\"];
fragment ESC: '\\' ([btnfr"\\]);
fragment ILL_ESC: '\\' ~([btnfr"\\]) | ~'\\';
// 3.3.identifier
ID: [a-zA-Z_][a-zA-Z0-9_]*;


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	'"' CHAR* ([\r\nEOF] | ~'"') {
	err_char = ['\r','\n',EOFError]
	if self.text[-1] in err_char:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE:
	'"' CHAR* ILL_ESC {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR:
	. {
	raise ErrorToken(self.text)
};

