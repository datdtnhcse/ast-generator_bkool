# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#extds.
    def visitExtds(self, ctx:BKOOLParser.ExtdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atrbDecl.
    def visitAtrbDecl(self, ctx:BKOOLParser.AtrbDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atrbType.
    def visitAtrbType(self, ctx:BKOOLParser.AtrbTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atrb.
    def visitAtrb(self, ctx:BKOOLParser.AtrbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atrbInit.
    def visitAtrbInit(self, ctx:BKOOLParser.AtrbInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayTyp.
    def visitArrayTyp(self, ctx:BKOOLParser.ArrayTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classTyp.
    def visitClassTyp(self, ctx:BKOOLParser.ClassTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paraList.
    def visitParaList(self, ctx:BKOOLParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para.
    def visitPara(self, ctx:BKOOLParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#litList.
    def visitLitList(self, ctx:BKOOLParser.LitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#equalee.
    def visitEqualee(self, ctx:BKOOLParser.EqualeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#andOree.
    def visitAndOree(self, ctx:BKOOLParser.AndOreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#addSubee.
    def visitAddSubee(self, ctx:BKOOLParser.AddSubeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mulDivModee.
    def visitMulDivModee(self, ctx:BKOOLParser.MulDivModeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#conCatee.
    def visitConCatee(self, ctx:BKOOLParser.ConCateeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#notee.
    def visitNotee(self, ctx:BKOOLParser.NoteeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subAddee.
    def visitSubAddee(self, ctx:BKOOLParser.SubAddeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexee.
    def visitIndexee(self, ctx:BKOOLParser.IndexeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memAccessee.
    def visitMemAccessee(self, ctx:BKOOLParser.MemAccesseeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atom.
    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#newee.
    def visitNewee(self, ctx:BKOOLParser.NeweeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#booleanLit.
    def visitBooleanLit(self, ctx:BKOOLParser.BooleanLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#argLits.
    def visitArgLits(self, ctx:BKOOLParser.ArgLitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockStmt.
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nullAbleStmtList.
    def visitNullAbleStmtList(self, ctx:BKOOLParser.NullAbleStmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmStmt.
    def visitAsmStmt(self, ctx:BKOOLParser.AsmStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#toDownto.
    def visitToDownto(self, ctx:BKOOLParser.ToDowntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakStmt.
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continueStmt.
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnStmt.
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invokeStmt.
    def visitInvokeStmt(self, ctx:BKOOLParser.InvokeStmtContext):
        return self.visitChildren(ctx)



del BKOOLParser