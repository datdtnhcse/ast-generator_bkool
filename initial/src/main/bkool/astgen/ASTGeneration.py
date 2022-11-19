from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        # program: classDecl* EOF;
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        # classDecl: CLASS ID (EXTENDS ID)? LP member* RP;
        return ClassDecl(Id(ctx.ID(0).getText()), 
                        [self.visit(x) for x in ctx.member()], 
                        Id(ctx.ID(1).getText()) if ctx.EXTENDS() else None)  # type: ignore

    def visitMember(self, ctx:BKOOLParser.MemberContext):
        # member: atrbDecl | methodDecl;
        if ctx.atrbDecl():
            return ctx.atrbDecl().accept(self) # type:ignore
        else:
            return ctx.methodDecl().accept(self) # type:ignore
       

    def visitAtrbDecl(self, ctx:BKOOLParser.AtrbDeclContext):
        # atrbDecl: immutDecl | mutDecl;
        if ctx.immutDecl():
            return ctx.immutDecl().accept(self) # type:ignore
        else: 
            return ctx.mutDecl().accept(self) # type:ignore

    def visitMutDecl(self, ctx:BKOOLParser.MutDeclContext):
        # mutDecl: STATIC? typ ID atrbInit (CM ID atrbInit)* SM;
        kind = Static() if ctx.STATIC() else Instance()
        result = ''
        result += str(AttributeDecl(kind, 
                                    VarDecl(Id(ctx.ID(0).getText()), # type:ignore
                                            ctx.typ().accept(self), # type:ignore
                                            ctx.atrbInit(0).accept(self) if ctx.atrbInit(0) else None)))
                                
        if ctx.CM(): 
            size = len(ctx.CM()) # type:ignore
            for i in range(1, size + 1):
                result += ',' + str(AttributeDecl(kind, 
                                                  VarDecl(Id(ctx.ID(i).getText()),  # type:ignore
                                                          ctx.typ().accept(self), 
                                                          ctx.atrbInit(i).accept(self) if ctx.atrbInit(i) else None)))
        
        return result

    def visitImmutDecl(self, ctx:BKOOLParser.ImmutDeclContext):
        # immutDecl: (FINAL | FINAL STATIC | STATIC FINAL)? typ ID atrbInit (CM ID atrbInit)* SM;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, 
                                    ConstDecl(Id(ctx.ID(0).getText()), 
                                              ctx.typ().accept(self), 
                                              ctx.atrbInit(0).accept(self))))

        if ctx.CM():
            size = len(ctx.CM())
            for i in range(1, size+1):
                result += ',' + str(AttributeDecl(kind, 
                                                  ConstDecl(Id(ctx.ID(i).getText()), 
                                                            ctx.typ().accept(self), 
                                                            ctx.atrbInit(i).accept(self))))
        return result


    def visitAtrbInit(self, ctx:BKOOLParser.AtrbInitContext):
        # atrbInit: (EQQ exp)?;
        return ctx.exp().accept(self) if ctx.exp() else None

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
        return ClassType(Id(ctx.ID().getText()))

    def visitArrayTyp(self, ctx:BKOOLParser.ArrayTypContext):
        # arrayTyp:  priTyp LS INTLIT RS;
        return ArrayType(size(ctx.INTLIT().getText()),
                         ctx.priTyp().accept(self))

    def visitPriTyp(self, ctx:BKOOLParser.PriTypContext):
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
                          Id(ctx.ID().getText()),
                          ctx.paraList().accept(self) if ctx.paraList() else [],
                          ctx.typ().accept(self) if ctx.typ() else None,
                          ctx.blockStmt().accept(self)) # maybe fail

    def visitParaList(self, ctx:BKOOLParser.ParaListContext):
        # paraList: para (SM para)*;
        result = []
        result += ctx.para(0).accept(self)

        if ctx.SM(): 
            size = len(ctx.SM()) 
            for i in range(1, size + 1):
                result += ctx.para(i).accept(self)

        return result

    def visitPara(self, ctx:BKOOLParser.ParaContext):
        # para: typ ID (CM ID)*; 
        result = []
        result += [VarDecl(Id(ctx.ID(0).getText()),
                           ctx.typ().accept(self))]
        
        if ctx.CM():
            size = len(ctx.CM())
            for i in range(1, size + 1):
                result += [VarDecl(Id(ctx.ID(i).getText()),
                           ctx.typ().accept(self))]
        return result

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
            return ctx.equalee(0).accept(self)

    def visitEqualee(self, ctx:BKOOLParser.EqualeeContext):
        # equalee: andOree (EQ | NEQ) andOree | andOree;
        if ctx.getChildCount() == 3:
            return BinaryOp("==" if ctx.EQ() else "!=",
                            ctx.andOree(0).accept(self),
                            ctx.andOree(1).accept(self))
        else:
            return ctx.andOree(0).accept(self)

    def visitAndOree(self, ctx:BKOOLParser.AndOreeContext):
        # andOree: addSubee (AND | OR) andOree | addSubee;
        if ctx.getChildCount() == 3:
            return BinaryOp("&&" if ctx.AND() else "!=",
                            ctx.addSubee().accept(self),
                            ctx.andOree().accept(self))
        else:   
            return ctx.addSubee().accept(self)

    def visitAddSubee(self, ctx:BKOOLParser.AddSubeeContext):
        # addSubee: addSubee (ADD | SUB) mulDivModee | mulDivModee;
        if ctx.getChildCount() == 3:
            return BinaryOp("+" if ctx.ADD() else "-",
                            ctx.addSubee().accept(self),
                            ctx.mulDivModee().accept(self))
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

    def visitConCatee(self, ctx:BKOOLParser.ConCateeContext):
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
        else:
            return ctx.indexee().accept(self)

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
            return FieldAccess(ctx.memAccessee().accept(self),
                               Id(ctx.ID().getText()))
        elif ctx.getChildCount() == 1:
            return ctx.atom().accept(self)
        else:
            return CallExpr(ctx.memAccessee().accept(self),
                            Id(ctx.ID().getText()),
                            ctx.argLits().accept(self)) 

    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        # atom: THIS | ID | literal | newee | arrayLit;
        if ctx.THIS():
            return SelfLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.newee():
            return ctx.newee().accept(self)
        else:
            return ctx.arrayLit().accept(self)
    
    def visitNewee(self, ctx:BKOOLParser.NeweeContext):
        # newee: NEW ID LB argLits? RB;
        return NewExpr(Id(ctx.ID().getText()),
                       ctx.argLits().accept(self) if ctx.argLits() else [])
        
    def visitBooleanLit(self, ctx:BKOOLParser.BooleanLitContext): 
        # booleanLit: TRUE | FALSE;
        return bool(True) if ctx.TRUE() else bool(False)

    def visitArgLits(self, ctx:BKOOLParser.ArgLitsContext):
        # argLits: exp (CM exp)*;
        result = []
        result.append(ctx.exp(0).accept(self))
        if ctx.CM():
            size = len(ctx.CM())
            for i in range(1, size + 1):
                result.append(ctx.exp(i).accept(self))
        return result
    
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        # stmt: blockStmt | asmStmt | ifStmt | forStmt | breakStmt | continueStmt | returnStmt | atrbDecl | invokeStmt;
        if ctx.blockStmt():
            return ctx.blockStmt().accept(self)
        elif ctx.asmStmt():
            return ctx.asmStmt().accept(self)
        elif ctx.ifStmt():
            return ctx.ifStmt().accept(self)
        elif ctx.forStmt():
            return ctx.forStmt().accept(self)
        elif ctx.breakStmt():
            return ctx.breakStmt().accept(self)
        elif ctx.continueStmt():
            return ctx.continueStmt().accept(self)
        elif ctx.returnStmt():
            return ctx.returnStmt().accept(self)
        elif ctx.atrbDecl():
            return ctx.atrbDecl().accept(self)
        else:
            return ctx.invokeStmt().accept(self)

    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        # blockStmt: LP nullAbleDeclList* stmt* RP;
        return Block([self.visit(x) for x in ctx.nullAbleDeclList()] if ctx.nullAbleDeclList() else [],
                     [self.visit(y) for y in ctx.stmt()] if ctx.stmt() else [])
        
    def visitNullAbleDeclList(self, ctx:BKOOLParser.NullAbleDeclListContext): 
        # nullAbleDeclList: FINAL? typ ID atrbInit (CM ID atrbInit)* SM;
        result = []
        if ctx.FINAL():
            result.append(ConstDecl(Id(ctx.ID(i).getText()),
                                        ctx.typ().accept(self),
                                        ctx.atrbInit().accept(self)))
            if ctx.CM():
                size = len(ctx.CM())
                for i in range (1, size + 1):
                    result.append(ConstDecl(Id(ctx.ID(i).getText()),
                                            ctx.typ().accept(self),
                                            ctx.atrbInit().accept(self)))
        else:
            result.append(VarDecl(Id(ctx.ID(i).getText()),
                                  ctx.typ().accept(self),
                                  ctx.atrbInit().accept(self)))
            if ctx.CM():
                size = len(ctx.CM())
                for i in range (1, size + 1):
                    result.append(VarDecl(Id(ctx.ID(i).getText()),
                                          ctx.typ().accept(self),
                                          ctx.atrbInit().accept(self)))

    def visitAsmStmt(self, ctx:BKOOLParser.AsmStmtContext):
        # asmStmt: lhs ASSIGN exp SM;
        return Assign(ctx.lhs().accept(self),
                      ctx.exp().accept(self))

    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        # lhs: indexee | memAccessee DOT ID | ID;
        if ctx.getChildCount() == 3:
            return fieldAccess(ctx.memAccessee().accept(self),
                               Id(ctx.ID().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return ctx.indexee().accept(self)

    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        # ifStmt: IF exp THEN stmt | IF exp THEN stmt ELSE stmt;
        return If(ctx.exp().accept(self),
                  ctx.stmt(0).accept(self),
                  ctx.stmt(1).accept(self) if ctx.ELSE() else None)
    
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        # forStmt: FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt;
        return For(Id(ctx.ID().getText()),
                   ctx.exp(0).accept(self),
                   ctx.exp(1).accept(self),
                   bool(True) if ctx.TO() else bool(False), 
                   ctx.stmt().accept(self))

    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        # breakStmt: BREAK SM;
        return Break()

    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        # continueStmt: CONTINUE SM;
        return Continue()

    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        # returnStmt: RETURN exp SM;
        return Return(ctx.exp().accept(self))

    def visitInvokeStmt(self, ctx:BKOOLParser.InvokeStmtContext):
        # invokeStmt: memAccessee DOT ID LB argLits? RB SM;
        if ctx.argLits():
            return CallStmt(ctx.memAccessee().accept(self),
                            Id(ctx.ID().getText()),
                            ctx.argLits().accept(self))
        else: 
            return FieldAcess(ctx.memAccessee().accept(self),
                              Id(ctx.ID().getText()))


# argLits: exp (CM exp)*;

"""
breakStmt: BREAK SM;
"""


