// Generated from d:\HCMUT\HK221\PPL\Assignment\AST_Generator\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKOOLParser}.
 */
public interface BKOOLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKOOLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKOOLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(BKOOLParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(BKOOLParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#member}.
	 * @param ctx the parse tree
	 */
	void enterMember(BKOOLParser.MemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#member}.
	 * @param ctx the parse tree
	 */
	void exitMember(BKOOLParser.MemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#atrbDecl}.
	 * @param ctx the parse tree
	 */
	void enterAtrbDecl(BKOOLParser.AtrbDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#atrbDecl}.
	 * @param ctx the parse tree
	 */
	void exitAtrbDecl(BKOOLParser.AtrbDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#mutDecl}.
	 * @param ctx the parse tree
	 */
	void enterMutDecl(BKOOLParser.MutDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#mutDecl}.
	 * @param ctx the parse tree
	 */
	void exitMutDecl(BKOOLParser.MutDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#immutDecl}.
	 * @param ctx the parse tree
	 */
	void enterImmutDecl(BKOOLParser.ImmutDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#immutDecl}.
	 * @param ctx the parse tree
	 */
	void exitImmutDecl(BKOOLParser.ImmutDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#atrbInit}.
	 * @param ctx the parse tree
	 */
	void enterAtrbInit(BKOOLParser.AtrbInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#atrbInit}.
	 * @param ctx the parse tree
	 */
	void exitAtrbInit(BKOOLParser.AtrbInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#typ}.
	 * @param ctx the parse tree
	 */
	void enterTyp(BKOOLParser.TypContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#typ}.
	 * @param ctx the parse tree
	 */
	void exitTyp(BKOOLParser.TypContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#arrayTyp}.
	 * @param ctx the parse tree
	 */
	void enterArrayTyp(BKOOLParser.ArrayTypContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#arrayTyp}.
	 * @param ctx the parse tree
	 */
	void exitArrayTyp(BKOOLParser.ArrayTypContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#priTyp}.
	 * @param ctx the parse tree
	 */
	void enterPriTyp(BKOOLParser.PriTypContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#priTyp}.
	 * @param ctx the parse tree
	 */
	void exitPriTyp(BKOOLParser.PriTypContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#classTyp}.
	 * @param ctx the parse tree
	 */
	void enterClassTyp(BKOOLParser.ClassTypContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#classTyp}.
	 * @param ctx the parse tree
	 */
	void exitClassTyp(BKOOLParser.ClassTypContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void enterMethodDecl(BKOOLParser.MethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void exitMethodDecl(BKOOLParser.MethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#paraList}.
	 * @param ctx the parse tree
	 */
	void enterParaList(BKOOLParser.ParaListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#paraList}.
	 * @param ctx the parse tree
	 */
	void exitParaList(BKOOLParser.ParaListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#para}.
	 * @param ctx the parse tree
	 */
	void enterPara(BKOOLParser.ParaContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#para}.
	 * @param ctx the parse tree
	 */
	void exitPara(BKOOLParser.ParaContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#arrayLit}.
	 * @param ctx the parse tree
	 */
	void enterArrayLit(BKOOLParser.ArrayLitContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#arrayLit}.
	 * @param ctx the parse tree
	 */
	void exitArrayLit(BKOOLParser.ArrayLitContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(BKOOLParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(BKOOLParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#equalee}.
	 * @param ctx the parse tree
	 */
	void enterEqualee(BKOOLParser.EqualeeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#equalee}.
	 * @param ctx the parse tree
	 */
	void exitEqualee(BKOOLParser.EqualeeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#andOree}.
	 * @param ctx the parse tree
	 */
	void enterAndOree(BKOOLParser.AndOreeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#andOree}.
	 * @param ctx the parse tree
	 */
	void exitAndOree(BKOOLParser.AndOreeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#addSubee}.
	 * @param ctx the parse tree
	 */
	void enterAddSubee(BKOOLParser.AddSubeeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#addSubee}.
	 * @param ctx the parse tree
	 */
	void exitAddSubee(BKOOLParser.AddSubeeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#mulDivModee}.
	 * @param ctx the parse tree
	 */
	void enterMulDivModee(BKOOLParser.MulDivModeeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#mulDivModee}.
	 * @param ctx the parse tree
	 */
	void exitMulDivModee(BKOOLParser.MulDivModeeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#conCatee}.
	 * @param ctx the parse tree
	 */
	void enterConCatee(BKOOLParser.ConCateeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#conCatee}.
	 * @param ctx the parse tree
	 */
	void exitConCatee(BKOOLParser.ConCateeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#notee}.
	 * @param ctx the parse tree
	 */
	void enterNotee(BKOOLParser.NoteeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#notee}.
	 * @param ctx the parse tree
	 */
	void exitNotee(BKOOLParser.NoteeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#subAddee}.
	 * @param ctx the parse tree
	 */
	void enterSubAddee(BKOOLParser.SubAddeeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#subAddee}.
	 * @param ctx the parse tree
	 */
	void exitSubAddee(BKOOLParser.SubAddeeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#indexee}.
	 * @param ctx the parse tree
	 */
	void enterIndexee(BKOOLParser.IndexeeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#indexee}.
	 * @param ctx the parse tree
	 */
	void exitIndexee(BKOOLParser.IndexeeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#memAccessee}.
	 * @param ctx the parse tree
	 */
	void enterMemAccessee(BKOOLParser.MemAccesseeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#memAccessee}.
	 * @param ctx the parse tree
	 */
	void exitMemAccessee(BKOOLParser.MemAccesseeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(BKOOLParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(BKOOLParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#newee}.
	 * @param ctx the parse tree
	 */
	void enterNewee(BKOOLParser.NeweeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#newee}.
	 * @param ctx the parse tree
	 */
	void exitNewee(BKOOLParser.NeweeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(BKOOLParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(BKOOLParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#booleanLit}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLit(BKOOLParser.BooleanLitContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#booleanLit}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLit(BKOOLParser.BooleanLitContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#argLits}.
	 * @param ctx the parse tree
	 */
	void enterArgLits(BKOOLParser.ArgLitsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#argLits}.
	 * @param ctx the parse tree
	 */
	void exitArgLits(BKOOLParser.ArgLitsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(BKOOLParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(BKOOLParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#blockStmt}.
	 * @param ctx the parse tree
	 */
	void enterBlockStmt(BKOOLParser.BlockStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#blockStmt}.
	 * @param ctx the parse tree
	 */
	void exitBlockStmt(BKOOLParser.BlockStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#nullAbleDeclList}.
	 * @param ctx the parse tree
	 */
	void enterNullAbleDeclList(BKOOLParser.NullAbleDeclListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#nullAbleDeclList}.
	 * @param ctx the parse tree
	 */
	void exitNullAbleDeclList(BKOOLParser.NullAbleDeclListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#asmStmt}.
	 * @param ctx the parse tree
	 */
	void enterAsmStmt(BKOOLParser.AsmStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#asmStmt}.
	 * @param ctx the parse tree
	 */
	void exitAsmStmt(BKOOLParser.AsmStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(BKOOLParser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(BKOOLParser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(BKOOLParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(BKOOLParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(BKOOLParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(BKOOLParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(BKOOLParser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(BKOOLParser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStmt(BKOOLParser.ContinueStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStmt(BKOOLParser.ContinueStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(BKOOLParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(BKOOLParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKOOLParser#invokeStmt}.
	 * @param ctx the parse tree
	 */
	void enterInvokeStmt(BKOOLParser.InvokeStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKOOLParser#invokeStmt}.
	 * @param ctx the parse tree
	 */
	void exitInvokeStmt(BKOOLParser.InvokeStmtContext ctx);
}