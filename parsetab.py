
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ARROW BREAK CASE CATCH CATCH CLASS COMMA COMMENT CONST CONSTRUCT CONTINUE DEFAULT DEFINE DIVIDE DO DOLLAR ECHO ELSE ELSEIF EQ ERROR EXCEPTION EXP EXTENDS FINALLY FLOAT FOR FOREACH FUNCTION GE GT IDENTICAL IDENTIFIER IF IMPLEMENTS INTEGER LBRACE LBRACKET LE LPAREN LT MINUS MOD NE NEW NEWLINE NOT NOT_IDENTICAL OR PHP_CLOSE PHP_OPEN PLUS PRIVATE PROTECTED PUBLIC RBRACE RBRACKET READLINE RETURN RPAREN SEMI SET STATIC STRING SWITCH THROW THROW TIMES TRY TRY TYPE USE VAR VARIABLE WHILEstatement : print SEMI\n                 | declaration SEMI\n                 | input SEMI\n                 | expression SEMI\n                 | object_declaration\n                 | class_declaration\n                 | array_declaration SEMI\n                 | property_declaration SEMI\n                 | function_statement\n                 | function_variable\n                 | function_anonymous\n                 | function_arrow\n                 | class_statement\n                 | while\n                 | constant_declaration\n                 | constant_use\n                 | try_catch\n                 | catch_item\n                 | ifstatements : statement statements\n                | statementdeclaration : VARIABLE SET value\n                    | VARIABLE SET STRING\n                    | VARIABLE SET expression\n                    | VARIABLE SET conditionclass_statement : CLASS IDENTIFIER LBRACE class_member_list RBRACEfunction_statement : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACEwhile : WHILE LPAREN expression RPAREN LBRACE statements RBRACEfunction_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACEprint : ECHO LPAREN value RPAREN\n            | ECHO value\n            | ECHO STRINGinput : VARIABLE SET READLINE LPAREN RPARENobject_declaration : VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMIarray_declaration : VARIABLE SET ARRAY LPAREN arrayArg RPAREN\n                        | VARIABLE SET ARRAY LPAREN empty RPARENarrayArg : index ARROW value\n                | index ARROW value arrayArg\n                | index ARROW value COMMA arrayArgif : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI\n            | IF LPAREN conditions RPAREN LBRACE statements RBRACE SEMI\n            | IF LPAREN condition RPAREN LBRACE statements RBRACE elseif\n            | IF LPAREN condition RPAREN LBRACE statements RBRACE elseelse : ELSE LBRACE statements RBRACE SEMIcondition : value comparison_operator valueconditions : LBRACE condition RBRACE logical_operator conditions\n                    | LBRACE condition RBRACEindex : INTEGER\n            | STRINGfunction_arrow : FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI\n                    | FUNCTION LPAREN VARIABLE RPAREN ARROW function_arrowcomparison_operator : LT\n                            | GT\n                            | LE\n                            | GE\n                            | EQ\n                            | NEvalue : VARIABLE\n            | INTEGER\n            | FLOAToperator : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDEexpression : value operator valueexpressions : expression COMMA expressions\n                    | expressionclass_declaration : CLASS IDENTIFIER LBRACE class_body RBRACEclass_body : class_member_listclass_member_list : class_member class_member_list\n                         | class_memberclass_member : property_declaration\n                    | method_declaration\n                    | constructor_declarationconstant_declaration : DEFINE LPAREN STRING COMMA expression RPAREN SEMI\n                            | CONST IDENTIFIER SET expression SEMIconstant_use : IDENTIFIERtry_catch : TRY LBRACE statements RBRACE catch_listcatch_list : catch_item catch_list\n                  | emptycatch_item : CATCH LPAREN EXCEPTION VARIABLE RPAREN LBRACE statements RBRACEproperty_declaration : visibility VARIABLEmethod_declaration : visibility FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACEconstructor_declaration : visibility FUNCTION CONSTRUCT LPAREN parameters RPAREN LBRACE statements RBRACEvisibility : PUBLIC\n                  | PROTECTED\n                  | PRIVATEparameters : parameter COMMA parameters\n                    | parameterparameter : TYPE VARIABLE\n                 | VARIABLEelseif : ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE\n                | ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE elsefunction_anonymous : FUNCTION LPAREN parameters RPAREN use_clause_opt LBRACE statements RBRACEuse_clause_opt : USE LPAREN variables RPARENvariables : VARIABLE COMMA variables\n                | VARIABLElogical_operator : AND\n                        | ORempty :'
    
_lr_action_items = {'ECHO':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[21,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,21,21,-100,-68,-26,21,21,-76,-78,-100,-80,21,21,21,21,-51,-79,21,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,21,21,21,21,-44,-92,-93,]),'VARIABLE':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,21,24,26,27,28,37,38,39,40,41,42,43,44,45,46,50,51,52,53,54,55,60,62,65,67,78,82,86,88,89,91,95,96,97,98,99,100,101,111,116,120,122,136,137,143,145,146,148,149,150,151,153,155,158,162,163,164,167,171,172,180,181,186,187,188,189,190,197,200,201,203,205,206,207,208,211,216,217,218,219,228,229,231,232,],[23,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,49,56,-77,58,61,-85,-86,-87,-1,-2,-3,-4,-7,-8,49,49,-61,-62,-63,-64,49,80,49,23,49,113,117,49,23,124,49,49,-52,-53,-54,-55,-56,-57,58,113,49,-100,-68,-26,49,23,23,-76,-78,-100,-80,23,23,49,23,23,185,-51,-79,23,113,113,204,-50,-29,-28,-75,-34,-27,-94,185,-81,-40,-42,-43,-41,49,23,23,23,23,-44,-92,-93,]),'VAR':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[24,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,24,24,-100,-68,-26,24,24,-76,-78,-100,-80,24,24,24,24,-51,-79,24,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,24,24,24,24,-44,-92,-93,]),'CLASS':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,104,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[25,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,25,25,135,-100,-68,-26,25,25,-76,-78,-100,-80,25,25,25,25,-51,-79,25,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,25,25,25,25,-44,-92,-93,]),'FUNCTION':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,37,38,39,40,41,42,43,44,45,65,88,111,122,136,137,143,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[28,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-85,-86,-87,-1,-2,-3,-4,-7,-8,28,28,139,-100,-68,-26,165,28,28,-76,-78,-100,-80,28,28,28,28,-51,-79,28,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,28,28,28,28,-44,-92,-93,]),'WHILE':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[29,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,29,29,-100,-68,-26,29,29,-76,-78,-100,-80,29,29,29,29,-51,-79,29,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,29,29,29,29,-44,-92,-93,]),'DEFINE':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[30,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,30,30,-100,-68,-26,30,30,-76,-78,-100,-80,30,30,30,30,-51,-79,30,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,30,30,30,30,-44,-92,-93,]),'CONST':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[31,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,31,31,-100,-68,-26,31,31,-76,-78,-100,-80,31,31,31,31,-51,-79,31,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,31,31,31,31,-44,-92,-93,]),'IDENTIFIER':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,25,26,28,31,40,41,42,43,44,45,65,88,122,136,137,139,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[26,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,57,-77,59,64,-1,-2,-3,-4,-7,-8,26,26,-100,-68,-26,160,26,26,-76,-78,-100,-80,26,26,26,26,-51,-79,26,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,26,26,26,26,-44,-92,-93,]),'TRY':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[32,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,32,32,-100,-68,-26,32,32,-76,-78,-100,-80,32,32,32,32,-51,-79,32,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,32,32,32,32,-44,-92,-93,]),'CATCH':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[33,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,33,33,33,-68,-26,33,33,-76,-78,33,-80,33,33,33,33,-51,-79,33,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,33,33,33,33,-44,-92,-93,]),'IF':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,65,88,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,228,229,231,232,],[34,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,34,34,-100,-68,-26,34,34,-76,-78,-100,-80,34,34,34,34,-51,-79,34,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,34,34,34,34,-44,-92,-93,]),'INTEGER':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,21,26,35,36,40,41,42,43,44,45,46,49,50,51,52,53,54,55,62,65,67,86,88,91,95,96,97,98,99,100,101,103,120,122,136,137,143,145,146,148,149,150,151,153,155,158,162,163,167,171,172,178,187,188,189,190,196,197,200,201,205,206,207,208,211,216,217,218,219,228,229,231,232,],[35,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,35,-77,-59,-60,-1,-2,-3,-4,-7,-8,35,-58,35,-61,-62,-63,-64,35,35,35,35,35,35,35,35,-52,-53,-54,-55,-56,-57,133,35,-100,-68,-26,35,35,35,-76,-78,-100,-80,35,35,35,35,35,-51,-79,35,133,-50,-29,-28,-75,133,-34,-27,-94,-81,-40,-42,-43,-41,35,35,35,35,35,-44,-92,-93,]),'FLOAT':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,21,26,40,41,42,43,44,45,46,50,51,52,53,54,55,62,65,67,86,88,91,95,96,97,98,99,100,101,120,122,136,137,143,145,146,148,149,150,151,153,155,158,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,216,217,218,219,228,229,231,232,],[36,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,36,-77,-1,-2,-3,-4,-7,-8,36,36,-61,-62,-63,-64,36,36,36,36,36,36,36,36,-52,-53,-54,-55,-56,-57,36,-100,-68,-26,36,36,36,-76,-78,-100,-80,36,36,36,36,36,-51,-79,36,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,36,36,36,36,36,-44,-92,-93,]),'PUBLIC':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,58,65,77,88,107,108,109,110,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,226,227,228,229,231,232,],[37,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,-82,37,37,37,37,-72,-73,-74,-100,-68,-26,37,37,-76,-78,-100,-80,37,37,37,37,-51,-79,37,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,37,37,37,-83,-84,37,-44,-92,-93,]),'PROTECTED':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,58,65,77,88,107,108,109,110,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,226,227,228,229,231,232,],[38,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,-82,38,38,38,38,-72,-73,-74,-100,-68,-26,38,38,-76,-78,-100,-80,38,38,38,38,-51,-79,38,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,38,38,38,-83,-84,38,-44,-92,-93,]),'PRIVATE':([0,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,58,65,77,88,107,108,109,110,122,136,137,145,146,148,149,150,151,153,155,162,163,167,171,172,187,188,189,190,197,200,201,205,206,207,208,211,217,218,219,226,227,228,229,231,232,],[39,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,-82,39,39,39,39,-72,-73,-74,-100,-68,-26,39,39,-76,-78,-100,-80,39,39,39,39,-51,-79,39,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,39,39,39,-83,-84,39,-44,-92,-93,]),'$end':([1,6,7,10,11,12,13,14,15,16,17,18,19,20,26,40,41,42,43,44,45,122,136,137,148,149,150,151,167,171,187,188,189,190,197,200,201,205,206,207,208,211,229,231,232,],[0,-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-1,-2,-3,-4,-7,-8,-100,-68,-26,-76,-78,-100,-80,-51,-79,-50,-29,-28,-75,-34,-27,-94,-81,-40,-42,-43,-41,-44,-92,-93,]),'SEMI':([2,3,4,5,8,9,35,36,47,48,49,58,69,70,71,72,73,94,121,128,129,156,157,166,170,179,192,194,225,],[40,41,42,43,44,45,-59,-60,-31,-32,-58,-82,-65,-22,-23,-24,-25,-30,148,-45,-33,-35,-36,187,190,197,206,211,229,]),'RBRACE':([6,7,10,11,12,13,14,15,16,17,18,19,20,26,35,36,40,41,42,43,44,45,49,58,87,88,105,106,107,108,109,110,122,123,126,128,136,137,138,148,149,150,151,167,168,169,171,173,177,182,183,187,188,189,190,191,197,200,201,205,206,207,208,211,221,222,223,226,227,229,230,231,232,],[-5,-6,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-77,-59,-60,-1,-2,-3,-4,-7,-8,-58,-82,122,-21,136,137,-71,-72,-73,-74,-100,-20,154,-45,-68,-26,-70,-76,-78,-100,-80,-51,188,189,-79,192,194,200,201,-50,-29,-28,-75,205,-34,-27,-94,-81,-40,-42,-43,-41,225,226,227,-83,-84,-44,231,-92,-93,]),'LPAREN':([21,28,29,30,33,34,59,61,74,75,135,142,160,161,165,209,],[46,60,62,63,66,67,78,83,102,103,159,164,180,181,186,216,]),'STRING':([21,35,36,49,55,63,103,178,196,],[48,-59,-60,-58,71,85,134,134,134,]),'PLUS':([22,23,35,36,49,70,],[51,-58,-59,-60,-58,51,]),'MINUS':([22,23,35,36,49,70,],[52,-58,-59,-60,-58,52,]),'TIMES':([22,23,35,36,49,70,],[53,-58,-59,-60,-58,53,]),'DIVIDE':([22,23,35,36,49,70,],[54,-58,-59,-60,-58,54,]),'SET':([23,56,64,],[55,76,86,]),'LBRACE':([32,57,67,118,119,125,127,140,141,152,174,175,176,202,210,213,214,224,],[65,77,91,145,146,153,155,162,163,172,91,-98,-99,-95,217,218,219,228,]),'RPAREN':([35,36,49,68,69,79,80,81,83,84,90,92,102,103,112,113,117,124,128,130,131,144,147,154,159,178,184,185,193,195,198,199,204,212,215,220,],[-59,-60,-58,94,-65,114,115,-89,118,119,125,127,129,-100,140,-91,-90,152,-45,156,157,-88,170,-47,179,-37,202,-97,-46,-38,213,214,115,-39,-96,224,]),'LT':([35,36,49,70,93,],[-59,-60,-58,96,96,]),'GT':([35,36,49,70,93,],[-59,-60,-58,97,97,]),'LE':([35,36,49,70,93,],[-59,-60,-58,98,98,]),'GE':([35,36,49,70,93,],[-59,-60,-58,99,99,]),'EQ':([35,36,49,70,93,],[-59,-60,-58,100,100,]),'NE':([35,36,49,70,93,],[-59,-60,-58,101,101,]),'COMMA':([35,36,49,80,81,85,113,117,178,185,],[-59,-60,-58,-91,116,120,-91,-90,196,203,]),'READLINE':([55,],[74,]),'ARRAY':([55,],[75,]),'TYPE':([60,78,116,180,181,],[82,82,82,82,82,]),'EXCEPTION':([66,],[89,]),'NEW':([76,],[104,]),'USE':([114,],[142,]),'ARROW':([115,132,133,134,],[143,158,-48,-49,]),'CONSTRUCT':([139,],[161,]),'AND':([154,],[175,]),'OR':([154,],[176,]),'ELSEIF':([192,],[209,]),'ELSE':([192,231,],[210,210,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[1,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'print':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'declaration':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'input':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'expression':([0,55,62,65,86,88,120,143,145,146,153,155,162,163,172,217,218,219,228,],[5,72,84,5,121,5,147,166,5,5,5,5,5,5,5,5,5,5,5,]),'object_declaration':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'class_declaration':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'array_declaration':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'property_declaration':([0,65,77,88,107,145,146,153,155,162,163,172,217,218,219,228,],[9,9,108,9,108,9,9,9,9,9,9,9,9,9,9,9,]),'function_statement':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'function_variable':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'function_anonymous':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'function_arrow':([0,65,88,143,145,146,153,155,162,163,172,217,218,219,228,],[13,13,13,167,13,13,13,13,13,13,13,13,13,13,13,]),'class_statement':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'while':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'constant_declaration':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'constant_use':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'try_catch':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'catch_item':([0,65,88,122,145,146,150,153,155,162,163,172,217,218,219,228,],[19,19,19,150,19,19,150,19,19,19,19,19,19,19,19,19,]),'if':([0,65,88,145,146,153,155,162,163,172,217,218,219,228,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'value':([0,21,46,50,55,62,65,67,86,88,91,95,120,143,145,146,153,155,158,162,163,172,216,217,218,219,228,],[22,47,68,69,70,22,22,93,22,22,93,128,22,22,22,22,22,22,178,22,22,22,93,22,22,22,22,]),'visibility':([0,65,77,88,107,145,146,153,155,162,163,172,217,218,219,228,],[27,27,111,27,111,27,27,27,27,27,27,27,27,27,27,27,]),'operator':([22,70,],[50,50,]),'condition':([55,67,91,216,],[73,90,126,220,]),'parameters':([60,78,116,180,181,],[79,112,144,198,199,]),'parameter':([60,78,116,180,181,],[81,81,81,81,81,]),'statements':([65,88,145,146,153,155,162,163,172,217,218,219,228,],[87,123,168,169,173,177,182,183,191,221,222,223,230,]),'conditions':([67,174,],[92,193,]),'comparison_operator':([70,93,],[95,95,]),'class_body':([77,],[105,]),'class_member_list':([77,107,],[106,138,]),'class_member':([77,107,],[107,107,]),'method_declaration':([77,107,],[109,109,]),'constructor_declaration':([77,107,],[110,110,]),'arrayArg':([103,178,196,],[130,195,212,]),'empty':([103,122,150,],[131,151,151,]),'index':([103,178,196,],[132,132,132,]),'use_clause_opt':([114,],[141,]),'catch_list':([122,150,],[149,171,]),'logical_operator':([154,],[174,]),'variables':([164,203,],[184,215,]),'elseif':([192,],[207,]),'else':([192,231,],[208,232,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> print SEMI','statement',2,'p_statement','parser.py',12),
  ('statement -> declaration SEMI','statement',2,'p_statement','parser.py',13),
  ('statement -> input SEMI','statement',2,'p_statement','parser.py',14),
  ('statement -> expression SEMI','statement',2,'p_statement','parser.py',15),
  ('statement -> object_declaration','statement',1,'p_statement','parser.py',16),
  ('statement -> class_declaration','statement',1,'p_statement','parser.py',17),
  ('statement -> array_declaration SEMI','statement',2,'p_statement','parser.py',18),
  ('statement -> property_declaration SEMI','statement',2,'p_statement','parser.py',19),
  ('statement -> function_statement','statement',1,'p_statement','parser.py',20),
  ('statement -> function_variable','statement',1,'p_statement','parser.py',21),
  ('statement -> function_anonymous','statement',1,'p_statement','parser.py',22),
  ('statement -> function_arrow','statement',1,'p_statement','parser.py',23),
  ('statement -> class_statement','statement',1,'p_statement','parser.py',24),
  ('statement -> while','statement',1,'p_statement','parser.py',25),
  ('statement -> constant_declaration','statement',1,'p_statement','parser.py',26),
  ('statement -> constant_use','statement',1,'p_statement','parser.py',27),
  ('statement -> try_catch','statement',1,'p_statement','parser.py',28),
  ('statement -> catch_item','statement',1,'p_statement','parser.py',29),
  ('statement -> if','statement',1,'p_statement','parser.py',30),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',33),
  ('statements -> statement','statements',1,'p_statements','parser.py',34),
  ('declaration -> VARIABLE SET value','declaration',3,'p_declaration','parser.py',37),
  ('declaration -> VARIABLE SET STRING','declaration',3,'p_declaration','parser.py',38),
  ('declaration -> VARIABLE SET expression','declaration',3,'p_declaration','parser.py',39),
  ('declaration -> VARIABLE SET condition','declaration',3,'p_declaration','parser.py',40),
  ('class_statement -> CLASS IDENTIFIER LBRACE class_member_list RBRACE','class_statement',5,'p_class_statement','parser.py',46),
  ('function_statement -> FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE','function_statement',8,'p_function_statement','parser.py',59),
  ('while -> WHILE LPAREN expression RPAREN LBRACE statements RBRACE','while',7,'p_while','parser.py',64),
  ('function_variable -> FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE','function_variable',7,'p_function_variable','parser.py',69),
  ('print -> ECHO LPAREN value RPAREN','print',4,'p_print','parser.py',74),
  ('print -> ECHO value','print',2,'p_print','parser.py',75),
  ('print -> ECHO STRING','print',2,'p_print','parser.py',76),
  ('input -> VARIABLE SET READLINE LPAREN RPAREN','input',5,'p_input','parser.py',87),
  ('object_declaration -> VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMI','object_declaration',8,'p_object_declaration','parser.py',91),
  ('array_declaration -> VARIABLE SET ARRAY LPAREN arrayArg RPAREN','array_declaration',6,'p_array_declaration','parser.py',95),
  ('array_declaration -> VARIABLE SET ARRAY LPAREN empty RPAREN','array_declaration',6,'p_array_declaration','parser.py',96),
  ('arrayArg -> index ARROW value','arrayArg',3,'p_arrayArg','parser.py',100),
  ('arrayArg -> index ARROW value arrayArg','arrayArg',4,'p_arrayArg','parser.py',101),
  ('arrayArg -> index ARROW value COMMA arrayArg','arrayArg',5,'p_arrayArg','parser.py',102),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI','if',8,'p_if','parser.py',107),
  ('if -> IF LPAREN conditions RPAREN LBRACE statements RBRACE SEMI','if',8,'p_if','parser.py',108),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE elseif','if',8,'p_if','parser.py',109),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE else','if',8,'p_if','parser.py',110),
  ('else -> ELSE LBRACE statements RBRACE SEMI','else',5,'p_else','parser.py',118),
  ('condition -> value comparison_operator value','condition',3,'p_condition','parser.py',122),
  ('conditions -> LBRACE condition RBRACE logical_operator conditions','conditions',5,'p_conditions','parser.py',136),
  ('conditions -> LBRACE condition RBRACE','conditions',3,'p_conditions','parser.py',137),
  ('index -> INTEGER','index',1,'p_index','parser.py',140),
  ('index -> STRING','index',1,'p_index','parser.py',141),
  ('function_arrow -> FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI','function_arrow',7,'p_function_arrow','parser.py',146),
  ('function_arrow -> FUNCTION LPAREN VARIABLE RPAREN ARROW function_arrow','function_arrow',6,'p_function_arrow','parser.py',147),
  ('comparison_operator -> LT','comparison_operator',1,'p_comparison_operator','parser.py',152),
  ('comparison_operator -> GT','comparison_operator',1,'p_comparison_operator','parser.py',153),
  ('comparison_operator -> LE','comparison_operator',1,'p_comparison_operator','parser.py',154),
  ('comparison_operator -> GE','comparison_operator',1,'p_comparison_operator','parser.py',155),
  ('comparison_operator -> EQ','comparison_operator',1,'p_comparison_operator','parser.py',156),
  ('comparison_operator -> NE','comparison_operator',1,'p_comparison_operator','parser.py',157),
  ('value -> VARIABLE','value',1,'p_value','parser.py',161),
  ('value -> INTEGER','value',1,'p_value','parser.py',162),
  ('value -> FLOAT','value',1,'p_value','parser.py',163),
  ('operator -> PLUS','operator',1,'p_operator','parser.py',172),
  ('operator -> MINUS','operator',1,'p_operator','parser.py',173),
  ('operator -> TIMES','operator',1,'p_operator','parser.py',174),
  ('operator -> DIVIDE','operator',1,'p_operator','parser.py',175),
  ('expression -> value operator value','expression',3,'p_expression','parser.py',178),
  ('expressions -> expression COMMA expressions','expressions',3,'p_expressions','parser.py',197),
  ('expressions -> expression','expressions',1,'p_expressions','parser.py',198),
  ('class_declaration -> CLASS IDENTIFIER LBRACE class_body RBRACE','class_declaration',5,'p_class_declaration','parser.py',201),
  ('class_body -> class_member_list','class_body',1,'p_class_body','parser.py',205),
  ('class_member_list -> class_member class_member_list','class_member_list',2,'p_class_member_list','parser.py',209),
  ('class_member_list -> class_member','class_member_list',1,'p_class_member_list','parser.py',210),
  ('class_member -> property_declaration','class_member',1,'p_class_member','parser.py',214),
  ('class_member -> method_declaration','class_member',1,'p_class_member','parser.py',215),
  ('class_member -> constructor_declaration','class_member',1,'p_class_member','parser.py',216),
  ('constant_declaration -> DEFINE LPAREN STRING COMMA expression RPAREN SEMI','constant_declaration',7,'p_constant_declaration','parser.py',221),
  ('constant_declaration -> CONST IDENTIFIER SET expression SEMI','constant_declaration',5,'p_constant_declaration','parser.py',222),
  ('constant_use -> IDENTIFIER','constant_use',1,'p_constant_use','parser.py',239),
  ('try_catch -> TRY LBRACE statements RBRACE catch_list','try_catch',5,'p_try_catch','parser.py',245),
  ('catch_list -> catch_item catch_list','catch_list',2,'p_catch_list','parser.py',249),
  ('catch_list -> empty','catch_list',1,'p_catch_list','parser.py',250),
  ('catch_item -> CATCH LPAREN EXCEPTION VARIABLE RPAREN LBRACE statements RBRACE','catch_item',8,'p_catch_item','parser.py',257),
  ('property_declaration -> visibility VARIABLE','property_declaration',2,'p_property_declaration','parser.py',279),
  ('method_declaration -> visibility FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE','method_declaration',9,'p_method_declaration','parser.py',283),
  ('constructor_declaration -> visibility FUNCTION CONSTRUCT LPAREN parameters RPAREN LBRACE statements RBRACE','constructor_declaration',9,'p_constructor_declaration','parser.py',287),
  ('visibility -> PUBLIC','visibility',1,'p_visibility','parser.py',291),
  ('visibility -> PROTECTED','visibility',1,'p_visibility','parser.py',292),
  ('visibility -> PRIVATE','visibility',1,'p_visibility','parser.py',293),
  ('parameters -> parameter COMMA parameters','parameters',3,'p_parameters','parser.py',297),
  ('parameters -> parameter','parameters',1,'p_parameters','parser.py',298),
  ('parameter -> TYPE VARIABLE','parameter',2,'p_parameter','parser.py',302),
  ('parameter -> VARIABLE','parameter',1,'p_parameter','parser.py',303),
  ('elseif -> ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE','elseif',7,'p_elseif','parser.py',308),
  ('elseif -> ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE else','elseif',8,'p_elseif','parser.py',309),
  ('function_anonymous -> FUNCTION LPAREN parameters RPAREN use_clause_opt LBRACE statements RBRACE','function_anonymous',8,'p_function_anonymous','parser.py',314),
  ('use_clause_opt -> USE LPAREN variables RPAREN','use_clause_opt',4,'p_use_clause_opt','parser.py',318),
  ('variables -> VARIABLE COMMA variables','variables',3,'p_variables','parser.py',322),
  ('variables -> VARIABLE','variables',1,'p_variables','parser.py',323),
  ('logical_operator -> AND','logical_operator',1,'p_logical_operator','parser.py',327),
  ('logical_operator -> OR','logical_operator',1,'p_logical_operator','parser.py',328),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',331),
]
