
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ARROW BREAK CASE CATCH CLASS COMMA COMMENT CONST CONSTRUCT CONTINUE DEFAULT DIVIDE DO DOLLAR ECHO ELSE ELSEIF EQ ERROR EXP EXTENDS FINALLY FLOAT FOR FOREACH FUNCTION GE GT IDENTICAL IDENTIFIER IF IMPLEMENTS INTEGER LBRACE LBRACKET LE LPAREN LT MINUS MOD NE NEW NEWLINE NOT NOT_IDENTICAL OR PHP_CLOSE PHP_OPEN PLUS PRIVATE PROTECTED PUBLIC RBRACE RBRACKET READLINE RETURN RPAREN SEMI SET STATIC STRING SWITCH THROW TIMES TRY TYPE USE VAR VARIABLE WHILEstatement : print SEMI\n                 | input SEMI\n                 | expression SEMI\n                 | declaration SEMI\n                 | object_declaration\n                 | class_declaration\n                 | array_declaration SEMI\n                 | property_declaration SEMI\n                 | function_statement\n                 | function_variable\n                 | function_anonymous\n                 | function_arrow\n                 | class_statement\n                 | while\n                 | ifstatements : statement statements\n                | statementdeclaration : VARIABLE SET expression\n                    | VARIABLE SET conditionclass_statement : CLASS IDENTIFIER LBRACE class_member_list RBRACEfunction_statement : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACEwhile : WHILE LPAREN expression RPAREN LBRACE statements RBRACEfunction_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACEprint : ECHO LPAREN expressions RPAREN\n                       | ECHO expressionsinput : VARIABLE SET READLINE LPAREN RPARENobject_declaration : VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMIarray_declaration : VARIABLE SET ARRAY LPAREN arrayArg RPAREN\n                        | VARIABLE SET ARRAY LPAREN empty RPARENarrayArg : index ARROW value\n                | index ARROW value arrayArg\n                | index ARROW value COMMA arrayArgif : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI\n            | IF LPAREN conditions RPAREN LBRACE statements RBRACE SEMI\n            | IF LPAREN condition RPAREN LBRACE statements RBRACE elseif\n            | IF LPAREN condition RPAREN LBRACE statements RBRACE elseelse : ELSE LBRACE statements RBRACE SEMIcondition : expression comparison_operator expressionconditions : LBRACE condition RBRACE logical_operator conditions\n                    | LBRACE condition RBRACEindex : INTEGER\n            | STRINGfunction_arrow : FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI\n                    | FUNCTION LPAREN VARIABLE RPAREN ARROW function_arrowcomparison_operator : LT\n                            | GT\n                            | LE\n                            | GE\n                            | EQ\n                            | NEvalue : VARIABLE\n            | INTEGER\n            | FLOAToperator : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDEexpression : value operator valueexpressions : expression COMMA expressions\n                    | expressionclass_declaration : CLASS IDENTIFIER LBRACE class_body RBRACEclass_body : class_member_listclass_member_list : class_member class_member_list\n                         | class_memberclass_member : property_declaration\n                    | method_declaration\n                    | constructor_declarationproperty_declaration : visibility VARIABLEmethod_declaration : visibility FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACEconstructor_declaration : visibility FUNCTION CONSTRUCT LPAREN parameters RPAREN LBRACE statements RBRACEvisibility : PUBLIC\n                  | PROTECTED\n                  | PRIVATEparameters : parameter COMMA parameters\n                    | parameterparameter : TYPE VARIABLE\n                 | VARIABLEelseif : ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE\n                | ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE elsefunction_anonymous : FUNCTION LPAREN parameters RPAREN use_clause_opt LBRACE statements RBRACEuse_clause_opt : USE LPAREN variables RPARENvariables : VARIABLE COMMA variables\n                | VARIABLElogical_operator : AND\n                        | ORempty :'
    
_lr_action_items = {'ECHO':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,195,196,198,199,],[17,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-61,-20,17,17,17,17,17,17,-44,17,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,17,17,17,17,-37,-78,-79,]),'VARIABLE':([0,6,7,10,11,12,13,14,15,16,17,20,22,23,28,29,30,31,32,33,34,35,36,37,41,42,43,44,45,46,51,53,54,56,64,68,72,78,79,80,81,82,83,84,93,98,113,114,120,122,123,124,126,129,133,134,135,138,140,149,150,155,156,157,159,165,168,169,171,173,174,175,178,183,184,185,186,195,196,198,199,],[18,-5,-6,-9,-10,-11,-12,-13,-14,-15,40,47,49,52,-71,-72,-73,-1,-2,-3,-4,-7,-8,40,40,40,-54,-55,-56,-57,66,40,40,40,95,99,40,40,-45,-46,-47,-48,-49,-50,49,95,-61,-20,40,18,18,18,18,40,18,18,154,-44,18,95,95,172,-43,-23,-22,-27,-21,-80,154,-33,-35,-36,-34,40,18,18,18,18,-37,-78,-79,]),'VAR':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,195,196,198,199,],[20,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-61,-20,20,20,20,20,20,20,-44,20,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,20,20,20,20,-37,-78,-79,]),'CLASS':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,86,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,195,196,198,199,],[21,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,112,-61,-20,21,21,21,21,21,21,-44,21,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,21,21,21,21,-37,-78,-79,]),'FUNCTION':([0,6,7,10,11,12,13,14,15,16,28,29,30,31,32,33,34,35,36,93,113,114,120,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,195,196,198,199,],[23,-5,-6,-9,-10,-11,-12,-13,-14,-15,-71,-72,-73,-1,-2,-3,-4,-7,-8,116,-61,-20,136,23,23,23,23,23,23,-44,23,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,23,23,23,23,-37,-78,-79,]),'WHILE':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,195,196,198,199,],[24,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-61,-20,24,24,24,24,24,24,-44,24,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,24,24,24,24,-37,-78,-79,]),'IF':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,195,196,198,199,],[25,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-61,-20,25,25,25,25,25,25,-44,25,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,25,25,25,25,-37,-78,-79,]),'INTEGER':([0,6,7,10,11,12,13,14,15,16,17,26,27,31,32,33,34,35,36,37,40,41,42,43,44,45,46,53,54,56,72,78,79,80,81,82,83,84,85,113,114,120,122,123,124,126,129,133,134,138,140,147,156,157,159,164,165,168,169,173,174,175,178,183,184,185,186,195,196,198,199,],[26,-5,-6,-9,-10,-11,-12,-13,-14,-15,26,-52,-53,-1,-2,-3,-4,-7,-8,26,-51,26,26,-54,-55,-56,-57,26,26,26,26,26,-45,-46,-47,-48,-49,-50,110,-61,-20,26,26,26,26,26,26,26,26,-44,26,110,-43,-23,-22,110,-27,-21,-80,-33,-35,-36,-34,26,26,26,26,26,-37,-78,-79,]),'FLOAT':([0,6,7,10,11,12,13,14,15,16,17,31,32,33,34,35,36,37,41,42,43,44,45,46,53,54,56,72,78,79,80,81,82,83,84,113,114,120,122,123,124,126,129,133,134,138,140,156,157,159,165,168,169,173,174,175,178,183,184,185,186,195,196,198,199,],[27,-5,-6,-9,-10,-11,-12,-13,-14,-15,27,-1,-2,-3,-4,-7,-8,27,27,27,-54,-55,-56,-57,27,27,27,27,27,-45,-46,-47,-48,-49,-50,-61,-20,27,27,27,27,27,27,27,27,-44,27,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,27,27,27,27,27,-37,-78,-79,]),'PUBLIC':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,49,63,89,90,91,92,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,193,194,195,196,198,199,],[28,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-68,28,28,-65,-66,-67,-61,-20,28,28,28,28,28,28,-44,28,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,28,28,28,-69,-70,28,-37,-78,-79,]),'PROTECTED':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,49,63,89,90,91,92,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,193,194,195,196,198,199,],[29,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-68,29,29,-65,-66,-67,-61,-20,29,29,29,29,29,29,-44,29,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,29,29,29,-69,-70,29,-37,-78,-79,]),'PRIVATE':([0,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,49,63,89,90,91,92,113,114,122,123,124,126,133,134,138,140,156,157,159,165,168,169,173,174,175,178,184,185,186,193,194,195,196,198,199,],[30,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-68,30,30,-65,-66,-67,-61,-20,30,30,30,30,30,30,-44,30,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,30,30,30,-69,-70,30,-37,-78,-79,]),'$end':([1,6,7,10,11,12,13,14,15,16,31,32,33,34,35,36,113,114,138,156,157,159,165,168,169,173,174,175,178,196,198,199,],[0,-5,-6,-9,-10,-11,-12,-13,-14,-15,-1,-2,-3,-4,-7,-8,-61,-20,-44,-43,-23,-22,-27,-21,-80,-33,-35,-36,-34,-37,-78,-79,]),'SEMI':([2,3,4,5,8,9,26,27,38,39,40,49,58,59,61,75,76,105,106,127,128,137,148,160,162,192,],[31,32,33,34,35,36,-52,-53,-25,-60,-51,-68,-18,-19,-58,-24,-59,-26,-38,-28,-29,156,165,173,178,196,]),'RBRACE':([6,7,10,11,12,13,14,15,16,26,27,31,32,33,34,35,36,40,49,61,87,88,89,90,91,92,103,106,113,114,115,138,139,140,141,142,146,151,152,156,157,158,159,165,168,169,173,174,175,178,188,189,190,193,194,196,197,198,199,],[-5,-6,-9,-10,-11,-12,-13,-14,-15,-52,-53,-1,-2,-3,-4,-7,-8,-51,-68,-58,113,114,-64,-65,-66,-67,125,-38,-61,-20,-63,-44,157,-17,159,160,162,168,169,-43,-23,-16,-22,-27,-21,-80,-33,-35,-36,-34,192,193,194,-69,-70,-37,198,-78,-79,]),'LPAREN':([17,23,24,25,50,52,57,60,112,119,131,132,136,176,],[37,51,53,54,64,69,77,85,130,135,149,150,155,183,]),'SET':([18,47,],[41,62,]),'PLUS':([18,19,26,27,40,],[-51,43,-52,-53,-51,]),'MINUS':([18,19,26,27,40,],[-51,44,-52,-53,-51,]),'TIMES':([18,19,26,27,40,],[-51,45,-52,-53,-51,]),'DIVIDE':([18,19,26,27,40,],[-51,46,-52,-53,-51,]),'IDENTIFIER':([21,23,116,],[48,50,131,]),'COMMA':([26,27,39,40,61,66,67,95,99,147,154,],[-52,-53,56,-51,-58,-77,98,-77,-76,164,171,]),'RPAREN':([26,27,39,40,55,61,65,66,67,69,70,71,73,76,77,85,94,95,99,106,107,108,121,125,130,147,153,154,161,163,166,167,172,179,182,187,],[-52,-53,-60,-51,75,-58,96,97,-75,100,101,102,104,-59,105,-86,117,-77,-76,-38,127,128,-74,-40,148,-30,170,-83,-39,-31,180,181,97,-32,-82,191,]),'LT':([26,27,40,58,61,74,],[-52,-53,-51,79,-58,79,]),'GT':([26,27,40,58,61,74,],[-52,-53,-51,80,-58,80,]),'LE':([26,27,40,58,61,74,],[-52,-53,-51,81,-58,81,]),'GE':([26,27,40,58,61,74,],[-52,-53,-51,82,-58,82,]),'EQ':([26,27,40,58,61,74,],[-52,-53,-51,83,-58,83,]),'NE':([26,27,40,58,61,74,],[-52,-53,-51,84,-58,84,]),'STRING':([26,27,40,85,147,164,],[-52,-53,-51,111,111,111,]),'READLINE':([41,],[57,]),'ARRAY':([41,],[60,]),'LBRACE':([48,54,100,101,102,104,117,118,143,144,145,170,177,180,181,191,],[63,72,122,123,124,126,133,134,72,-84,-85,-81,184,185,186,195,]),'TYPE':([51,64,98,149,150,],[68,68,68,68,68,]),'NEW':([62,],[86,]),'USE':([96,],[119,]),'ARROW':([97,109,110,111,],[120,129,-41,-42,]),'CONSTRUCT':([116,],[132,]),'AND':([125,],[144,]),'OR':([125,],[145,]),'ELSEIF':([160,],[176,]),'ELSE':([160,198,],[177,177,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,122,123,124,126,133,134,140,184,185,186,195,],[1,140,140,140,140,140,140,140,140,140,140,140,]),'print':([0,122,123,124,126,133,134,140,184,185,186,195,],[2,2,2,2,2,2,2,2,2,2,2,2,]),'input':([0,122,123,124,126,133,134,140,184,185,186,195,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'expression':([0,17,37,41,53,54,56,72,78,120,122,123,124,126,133,134,140,183,184,185,186,195,],[4,39,39,58,70,74,39,74,106,137,4,4,4,4,4,4,4,74,4,4,4,4,]),'declaration':([0,122,123,124,126,133,134,140,184,185,186,195,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'object_declaration':([0,122,123,124,126,133,134,140,184,185,186,195,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'class_declaration':([0,122,123,124,126,133,134,140,184,185,186,195,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'array_declaration':([0,122,123,124,126,133,134,140,184,185,186,195,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'property_declaration':([0,63,89,122,123,124,126,133,134,140,184,185,186,195,],[9,90,90,9,9,9,9,9,9,9,9,9,9,9,]),'function_statement':([0,122,123,124,126,133,134,140,184,185,186,195,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'function_variable':([0,122,123,124,126,133,134,140,184,185,186,195,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'function_anonymous':([0,122,123,124,126,133,134,140,184,185,186,195,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'function_arrow':([0,120,122,123,124,126,133,134,140,184,185,186,195,],[13,138,13,13,13,13,13,13,13,13,13,13,13,]),'class_statement':([0,122,123,124,126,133,134,140,184,185,186,195,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'while':([0,122,123,124,126,133,134,140,184,185,186,195,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'if':([0,122,123,124,126,133,134,140,184,185,186,195,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'value':([0,17,37,41,42,53,54,56,72,78,120,122,123,124,126,129,133,134,140,183,184,185,186,195,],[19,19,19,19,61,19,19,19,19,19,19,19,19,19,19,147,19,19,19,19,19,19,19,19,]),'visibility':([0,63,89,122,123,124,126,133,134,140,184,185,186,195,],[22,93,93,22,22,22,22,22,22,22,22,22,22,22,]),'expressions':([17,37,56,],[38,55,76,]),'operator':([19,],[42,]),'condition':([41,54,72,183,],[59,71,103,187,]),'parameters':([51,64,98,149,150,],[65,94,121,166,167,]),'parameter':([51,64,98,149,150,],[67,67,67,67,67,]),'conditions':([54,143,],[73,161,]),'comparison_operator':([58,74,],[78,78,]),'class_body':([63,],[87,]),'class_member_list':([63,89,],[88,115,]),'class_member':([63,89,],[89,89,]),'method_declaration':([63,89,],[91,91,]),'constructor_declaration':([63,89,],[92,92,]),'arrayArg':([85,147,164,],[107,163,179,]),'empty':([85,],[108,]),'index':([85,147,164,],[109,109,109,]),'use_clause_opt':([96,],[118,]),'statements':([122,123,124,126,133,134,140,184,185,186,195,],[139,141,142,146,151,152,158,188,189,190,197,]),'logical_operator':([125,],[143,]),'variables':([135,171,],[153,182,]),'elseif':([160,],[174,]),'else':([160,198,],[175,199,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> print SEMI','statement',2,'p_statement','parser.py',10),
  ('statement -> input SEMI','statement',2,'p_statement','parser.py',11),
  ('statement -> expression SEMI','statement',2,'p_statement','parser.py',12),
  ('statement -> declaration SEMI','statement',2,'p_statement','parser.py',13),
  ('statement -> object_declaration','statement',1,'p_statement','parser.py',14),
  ('statement -> class_declaration','statement',1,'p_statement','parser.py',15),
  ('statement -> array_declaration SEMI','statement',2,'p_statement','parser.py',16),
  ('statement -> property_declaration SEMI','statement',2,'p_statement','parser.py',17),
  ('statement -> function_statement','statement',1,'p_statement','parser.py',18),
  ('statement -> function_variable','statement',1,'p_statement','parser.py',19),
  ('statement -> function_anonymous','statement',1,'p_statement','parser.py',20),
  ('statement -> function_arrow','statement',1,'p_statement','parser.py',21),
  ('statement -> class_statement','statement',1,'p_statement','parser.py',22),
  ('statement -> while','statement',1,'p_statement','parser.py',23),
  ('statement -> if','statement',1,'p_statement','parser.py',24),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',27),
  ('statements -> statement','statements',1,'p_statements','parser.py',28),
  ('declaration -> VARIABLE SET expression','declaration',3,'p_declaration','parser.py',31),
  ('declaration -> VARIABLE SET condition','declaration',3,'p_declaration','parser.py',32),
  ('class_statement -> CLASS IDENTIFIER LBRACE class_member_list RBRACE','class_statement',5,'p_class_statement','parser.py',36),
  ('function_statement -> FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE','function_statement',8,'p_function_statement','parser.py',40),
  ('while -> WHILE LPAREN expression RPAREN LBRACE statements RBRACE','while',7,'p_while','parser.py',45),
  ('function_variable -> FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE','function_variable',7,'p_function_variable','parser.py',50),
  ('print -> ECHO LPAREN expressions RPAREN','print',4,'p_print','parser.py',55),
  ('print -> ECHO expressions','print',2,'p_print','parser.py',56),
  ('input -> VARIABLE SET READLINE LPAREN RPAREN','input',5,'p_input','parser.py',61),
  ('object_declaration -> VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMI','object_declaration',8,'p_object_declaration','parser.py',65),
  ('array_declaration -> VARIABLE SET ARRAY LPAREN arrayArg RPAREN','array_declaration',6,'p_array_declaration','parser.py',74),
  ('array_declaration -> VARIABLE SET ARRAY LPAREN empty RPAREN','array_declaration',6,'p_array_declaration','parser.py',75),
  ('arrayArg -> index ARROW value','arrayArg',3,'p_arrayArg','parser.py',79),
  ('arrayArg -> index ARROW value arrayArg','arrayArg',4,'p_arrayArg','parser.py',80),
  ('arrayArg -> index ARROW value COMMA arrayArg','arrayArg',5,'p_arrayArg','parser.py',81),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI','if',8,'p_if','parser.py',86),
  ('if -> IF LPAREN conditions RPAREN LBRACE statements RBRACE SEMI','if',8,'p_if','parser.py',87),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE elseif','if',8,'p_if','parser.py',88),
  ('if -> IF LPAREN condition RPAREN LBRACE statements RBRACE else','if',8,'p_if','parser.py',89),
  ('else -> ELSE LBRACE statements RBRACE SEMI','else',5,'p_else','parser.py',93),
  ('condition -> expression comparison_operator expression','condition',3,'p_condition','parser.py',97),
  ('conditions -> LBRACE condition RBRACE logical_operator conditions','conditions',5,'p_conditions','parser.py',104),
  ('conditions -> LBRACE condition RBRACE','conditions',3,'p_conditions','parser.py',105),
  ('index -> INTEGER','index',1,'p_index','parser.py',108),
  ('index -> STRING','index',1,'p_index','parser.py',109),
  ('function_arrow -> FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI','function_arrow',7,'p_function_arrow','parser.py',114),
  ('function_arrow -> FUNCTION LPAREN VARIABLE RPAREN ARROW function_arrow','function_arrow',6,'p_function_arrow','parser.py',115),
  ('comparison_operator -> LT','comparison_operator',1,'p_comparison_operator','parser.py',120),
  ('comparison_operator -> GT','comparison_operator',1,'p_comparison_operator','parser.py',121),
  ('comparison_operator -> LE','comparison_operator',1,'p_comparison_operator','parser.py',122),
  ('comparison_operator -> GE','comparison_operator',1,'p_comparison_operator','parser.py',123),
  ('comparison_operator -> EQ','comparison_operator',1,'p_comparison_operator','parser.py',124),
  ('comparison_operator -> NE','comparison_operator',1,'p_comparison_operator','parser.py',125),
  ('value -> VARIABLE','value',1,'p_value','parser.py',129),
  ('value -> INTEGER','value',1,'p_value','parser.py',130),
  ('value -> FLOAT','value',1,'p_value','parser.py',131),
  ('operator -> PLUS','operator',1,'p_operator','parser.py',140),
  ('operator -> MINUS','operator',1,'p_operator','parser.py',141),
  ('operator -> TIMES','operator',1,'p_operator','parser.py',142),
  ('operator -> DIVIDE','operator',1,'p_operator','parser.py',143),
  ('expression -> value operator value','expression',3,'p_expression','parser.py',146),
  ('expressions -> expression COMMA expressions','expressions',3,'p_expressions','parser.py',150),
  ('expressions -> expression','expressions',1,'p_expressions','parser.py',151),
  ('class_declaration -> CLASS IDENTIFIER LBRACE class_body RBRACE','class_declaration',5,'p_class_declaration','parser.py',154),
  ('class_body -> class_member_list','class_body',1,'p_class_body','parser.py',158),
  ('class_member_list -> class_member class_member_list','class_member_list',2,'p_class_member_list','parser.py',162),
  ('class_member_list -> class_member','class_member_list',1,'p_class_member_list','parser.py',163),
  ('class_member -> property_declaration','class_member',1,'p_class_member','parser.py',167),
  ('class_member -> method_declaration','class_member',1,'p_class_member','parser.py',168),
  ('class_member -> constructor_declaration','class_member',1,'p_class_member','parser.py',169),
  ('property_declaration -> visibility VARIABLE','property_declaration',2,'p_property_declaration','parser.py',173),
  ('method_declaration -> visibility FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE','method_declaration',9,'p_method_declaration','parser.py',177),
  ('constructor_declaration -> visibility FUNCTION CONSTRUCT LPAREN parameters RPAREN LBRACE statements RBRACE','constructor_declaration',9,'p_constructor_declaration','parser.py',181),
  ('visibility -> PUBLIC','visibility',1,'p_visibility','parser.py',185),
  ('visibility -> PROTECTED','visibility',1,'p_visibility','parser.py',186),
  ('visibility -> PRIVATE','visibility',1,'p_visibility','parser.py',187),
  ('parameters -> parameter COMMA parameters','parameters',3,'p_parameters','parser.py',191),
  ('parameters -> parameter','parameters',1,'p_parameters','parser.py',192),
  ('parameter -> TYPE VARIABLE','parameter',2,'p_parameter','parser.py',196),
  ('parameter -> VARIABLE','parameter',1,'p_parameter','parser.py',197),
  ('elseif -> ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE','elseif',7,'p_elseif','parser.py',202),
  ('elseif -> ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE else','elseif',8,'p_elseif','parser.py',203),
  ('function_anonymous -> FUNCTION LPAREN parameters RPAREN use_clause_opt LBRACE statements RBRACE','function_anonymous',8,'p_function_anonymous','parser.py',208),
  ('use_clause_opt -> USE LPAREN variables RPAREN','use_clause_opt',4,'p_use_clause_opt','parser.py',212),
  ('variables -> VARIABLE COMMA variables','variables',3,'p_variables','parser.py',216),
  ('variables -> VARIABLE','variables',1,'p_variables','parser.py',217),
  ('logical_operator -> AND','logical_operator',1,'p_logical_operator','parser.py',221),
  ('logical_operator -> OR','logical_operator',1,'p_logical_operator','parser.py',222),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',227),
]
