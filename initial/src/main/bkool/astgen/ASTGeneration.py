from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        # program: classDecl* EOF;
        return Program([self.visit(x) for x in ctx.ClassDecl()])

    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        # classDecl: CLASS ID (EXTENDS ID)? LP member* RP;
        return ClassDecl(ctx.ID(0).getText(), 
                        [self.visit(x) for x in ctx.member], 
                        ID(ctx.ID(1).getText()) if ctx.EXTENDS() else None)

    def visitMember(self, ctx:BKOOLParser.MemberContext):
        # member: atrbDecl | methodDecl;
        if ctx.atrbDecl():
            return ctx.atrbDecl().accept(self)
        else: 
            return ctx.methodDecl().accept(self)

    def visitAtrbDecl(self, ctx:BKOOLParser.AtrbDeclContext):
        # atrbDecl: immutDecl | mutDecl;
        if ctx.imuDecl():
            return ctx.imuDecl().accept(self)
        else: 
            return ctx.mutDecl().accept(self)

    def visitMutDecl(self, ctx:BKOOLParser.ImuDeclContext):
        # mutDecl: STATIC? typ ID atrbInit? (CM ID atrbInit?)* SM;
        kind = Static() if ctx.STATIC() else Instance()
        result = ''
        result += str(AttributeDecl(kind, 
                                    VarDecl(ID(ctx.ID(0).getText()), 
                                            ctx.typ().accept(self), 
                                            ctx.atrbInit(0).accept(self) if ctx.atrbInit(0) else None)))
                                
        if ctx.CM(): 
            size = len(ctx.CM()) 
            for i in range(1, size + 1):
                result += ',' + str(AttributeDecl(kind, 
                                                  VarDecl(ID(ctx.ID(i).getText()), 
                                                          ctx.typ().accept(self), 
                                                          ctx.atrbInit(i).accept(self) if ctx.atrbInit(i) else None)))
        
        return result

    def visitAtrbInit(self, ctx:BKOOLParser.AtrbInitContext):
        # atrbInit: EQQ exp;
        return ctx.exp().accept(self)

    def visitTyp(self, ctx:BKOOLParser.TypContext):
        # typ: priTyp | classTyp | VOID | arrayTyp;
        if ctx.priTyp():
            return ctx.priTyp().accept(self)
        if ctx.VOID:
            return VoidType()
        if ctx.classTyp():
            return ctx.classTyp().accept(self)
        if ctx.arrayTyp():
            return ctx.arrayTyp().accept(self)

    def visitClassTyp(self, ctx:BKOOLParser.ClassTypContext):
        # classTyp: ID;
        return ClassType(ID(ctx.ID().getText()))

    def arrayTyp(self, ctx:BKOOLParser.ArrayTypContext):
        # arrayTyp:  priTyp LS INTLIT RS;
        return ArrayType(size(ctx.INTLIT().getText()),
                         ctx.priTyp().accept(self))

    def priTyp(self, ctx:BKOOLParser.PriTypContext):
        # priTyp: INT | FLOAT | STRING | BOOLEAN;
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():  
            return StringType()
        if ctx.BOOLEAN():
            return BooleanType()
    
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        # methodDecl: STATIC? typ? ID LB paraList? RB blockStmt;
        kind = Static() if ctx.STATIC() else Instance()
    
        return MethodDecl(kind, 
                          ID(ctx.ID().getText()),
                          ctx.paraList().accept(self),
                          ctx.typ().accept(self) if ctx.typ() else None,
                          ctx.blockStmt().accept(self)) # maybe fail

    def visitParaList(self, ctx:BKOOLParser.ParaListContext):
        # paraList: para ID (SM para)*;
        result = ''
        result += str(ctx.para().accept(self))

        if ctx.SM(): 
            size = len(ctx.SM()) 
            for i in range(1, size + 1):
                result += ',' + str(ctx.para().accept(self))

        return result

    def visitPara(self, ctx:BKOOLParser.ParaContext):
        # para: typ ID (CM ID)*; 
        result = ''
        result += str(VarDecl(ctx.ID().accept(self),
                              ctx.typ().accept(self),
                              None))
        
        if ctx.CM():
            size = len(ctx.CM())
            for i in range(1, size + 1):
                result += str(VarDecl(ctx.ID().accept(self),
                              ctx.typ().accept(self),
                              None))

    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        # arrayLit: LP literal (CM literal)* RP;   
        result = []
        result.append(ctx.literal(0).accept(self))

        if ctx.CM():
            size = len(ctx.CM())
            for i in range(1, size + 1):
                result.append(ctx.literal(i).accept(self))
        return ArrayLiteral(result) 

    
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        # literal: INTLIT | FLOATLIT | STRINGLIT | booleanLit;
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        if ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.booleanLit():
            return BooleanLiteral(ctx.booleanLit().accept(self))

    def visitExp(self, ctx:BKOOLParser.ExpContext):
        # exp: equalee (LESS | LEQ | GREATER | GEQ) equalee | equalee;
        if ctx.getChildCount() == 3:   
            if ctx.LESS():
                return BinaryOp("<",
                                ctx.equalee(0).accept(self),
                                ctx.equalee(1).accept(self))
            if ctx.LEQ():
                return BinaryOp("<=",
                                ctx.equalee(0).accept(self),
                                ctx.equalee(1).accept(self))
            if ctx.GREATER():
                return BinaryOp(">",
                                ctx.equalee(0).accept(self),
                                ctx.equalee(1).accept(self))
            if ctx.GEQ():
                return BinaryOp(">=",
                                ctx.equalee(0).accept(self),
                                ctx.equalee(1).accept(self))
        else:   
            return ctx.equalee().accept(self)

    def visitEqualee(self, ctx:BKOOLParser.EqualeeContext):
        # equalee: andOree (EQ | NEQ) andOree | andOree;
        if ctx.getChildCount() == 3:
            return BinaryOp("==" if ctx.EQ() else "!=",
                            ctx.andOree(0).accept(self),
                            ctx.andOree(1).accept(self))
        else:
            return ctx.andOree().accept(self)

    def visitAndOree(self, ctx:BKOOLParser.AndOreeContext):
        # andOree: addSubee (AND | OR) andOree | addSubee;
        if ctx.getChildCount() == 3:
            return BinaryOp("&&" if ctx.AND() else "!=",
                            ctx.addSubee().accept(ctx),
                            ctx.andOree().accept(ctx))
        else:   
            return ctx.addSubee().accept(self)

    def visitAddSubee(self, ctx:BKOOLParser.AddSubeeContext):
        # addSubee: addSubee (ADD | SUB) mulDivModee | mulDivModee;
        if ctx.getChildCount() == 3:
            return BinaryOp("+" if ctx.ADD() else "-",
                            ctx.addSubee().accept(ctx),
                            ctx.mulDivModee().accept(ctx))
        else:   
            return ctx.mulDivModee().accept(self)

    def visitMulDivModee(self, ctx:BKOOLParser.MulDivModeeContext):
        # mulDivModee: mulDivModee (MUL | INTDIV | FLDIV | MOD) conCatee | conCatee;
        if ctx.getChildCount() == 3:
            if ctx.MUL():
                return BinaryOp("*",
                                ctx.mulDivModee().accept(self),
                                ctx.conCatee().accept(self))
            elif ctx.INTDIV():
                return BinaryOp("/",
                                ctx.mulDivModee().accept(self),
                                ctx.conCatee().accept(self))
            elif ctx.FLDIV():
                return BinaryOp("\\",
                                ctx.mulDivModee().accept(self),
                                ctx.conCatee().accept(self))
            elif ctx.MOD():
                return BinaryOp("%",
                                ctx.mulDivModee().accept(self),
                                ctx.conCatee().accept(self))
        else:
            return ctx.conCatee().accept(self)

    def visitConCatee(self, ctx:BKOOLParser.ConcateeContext):
        # conCatee: conCatee (CONCAT) notee | notee;
        if ctx.getChildCount() == 3:
            return BinaryOp("^",
                            ctx.conCatee().accept(self),
                            ctx.notee().accept(self))
        else:
            return ctx.notee().accept(self)
    
    def visitNotee(self, ctx:BKOOLParser.NoteeContext):
        # notee: (NOT) notee | subAddee;
        if ctx.getChildCount() == 2:
            return UnaruOp("!", 
                           ctx.notee().accept(self))
        else:
            return ctx.subAddee().accept(self)

    def visitSubAddee(self, ctx:BKOOLParser.SubAddeeContext):
        # subAddee:  (SUB | ADD) subAddee | indexee;
        if ctx.getChildCount() == 2:
            return UnaryOp("+" if ctx.ADD() else "-",
                           ctx.subAddee().accept(self))
        return ctx.indexee.accept(self)

    def visitIndexee(self, ctx:BKOOLParser.IndexeeContext):
        # indexee: memAccessee LS exp RS | memAccessee;
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.memAccessee().accept(self),
                             ctx.exp().accept(self))
        else:
            return ctx.memAccessee().accept(self)

    def visitMemAccessee(self, ctx:BKOOLParser.MemAccesseeContext):
        # memAccessee: memAccessee DOT ID | memAccessee DOT ID LB argLits? RB | atom;
        if ctx.getChildCount() == 3:
            return fieldAccess(ctx.memAccessee().accept(self),
                               ID(ctx.ID().getText()))
        elif ctx.getChildCount() == 1:
            return ctx.atom().accept(self)
        else:
            return CallExpr(ctx.memAccessee().accept(self),
                            ID(ctx.ID().getText()),
                            ctx.argLits().accept(self)) # argLit not been supported yet

    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        # atom: THIS | ID | literal | newee | arrayLit;
        if ctx.THIS():
            return SelfLiteral()
        elif ctx.ID():
            return ID(ctx.ID().getText())
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.newee():
            return ctx.newee().accept(self)
        else:
            return ctx.arrayLit().accept(self)
    
    def visitNewee(self, ctx:BKOOLParser.NeweeContext):
        # newee: NEW ID LB argLits? RB;
        return NewExpr(ID(ctx.ID().getText()),
                       )




    """

literal: INTLIT | FLOATLIT | STRINGLIT | booleanLit;
booleanLit: 'true' | 'false';
argLits: exp (CM exp)*;

    """

    
