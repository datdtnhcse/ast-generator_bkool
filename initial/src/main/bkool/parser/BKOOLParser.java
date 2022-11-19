// Generated from d:\HCMUT\HK221\PPL\Assignment\AST_Generator\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKOOLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CMTLINE=1, CMTBLOCK=2, ASSIGN=3, CLASS=4, EXTENDS=5, STATIC=6, FINAL=7, 
		BOOLEAN=8, BREAK=9, CONTINUE=10, DO=11, ELSE=12, FLOAT=13, IF=14, INT=15, 
		STRING=16, THEN=17, FOR=18, THIS=19, RETURN=20, TRUE=21, FALSE=22, VOID=23, 
		NIL=24, TO=25, DOWNTO=26, ADD=27, SUB=28, MUL=29, FLDIV=30, INTDIV=31, 
		MOD=32, NEQ=33, EQ=34, EQQ=35, LESS=36, GREATER=37, LEQ=38, GEQ=39, OR=40, 
		AND=41, NOT=42, CONCAT=43, NEW=44, SM=45, CM=46, LP=47, RP=48, LB=49, 
		RB=50, LS=51, RS=52, CL=53, DOT=54, INTLIT=55, FLOATLIT=56, INFL=57, STRINGLIT=58, 
		ID=59, WS=60, UNCLOSE_STRING=61, ILLEGAL_ESCAPE=62, ERROR_CHAR=63;
	public static final int
		RULE_program = 0, RULE_classDecl = 1, RULE_member = 2, RULE_atrbDecl = 3, 
		RULE_mutDecl = 4, RULE_immutDecl = 5, RULE_atrbInit = 6, RULE_typ = 7, 
		RULE_arrayTyp = 8, RULE_priTyp = 9, RULE_classTyp = 10, RULE_methodDecl = 11, 
		RULE_paraList = 12, RULE_para = 13, RULE_arrayLit = 14, RULE_exp = 15, 
		RULE_equalee = 16, RULE_andOree = 17, RULE_addSubee = 18, RULE_mulDivModee = 19, 
		RULE_conCatee = 20, RULE_notee = 21, RULE_subAddee = 22, RULE_indexee = 23, 
		RULE_memAccessee = 24, RULE_atom = 25, RULE_newee = 26, RULE_literal = 27, 
		RULE_booleanLit = 28, RULE_argLits = 29, RULE_stmt = 30, RULE_blockStmt = 31, 
		RULE_nullAbleDeclList = 32, RULE_asmStmt = 33, RULE_lhs = 34, RULE_ifStmt = 35, 
		RULE_forStmt = 36, RULE_breakStmt = 37, RULE_continueStmt = 38, RULE_returnStmt = 39, 
		RULE_invokeStmt = 40;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDecl", "member", "atrbDecl", "mutDecl", "immutDecl", 
			"atrbInit", "typ", "arrayTyp", "priTyp", "classTyp", "methodDecl", "paraList", 
			"para", "arrayLit", "exp", "equalee", "andOree", "addSubee", "mulDivModee", 
			"conCatee", "notee", "subAddee", "indexee", "memAccessee", "atom", "newee", 
			"literal", "booleanLit", "argLits", "stmt", "blockStmt", "nullAbleDeclList", 
			"asmStmt", "lhs", "ifStmt", "forStmt", "breakStmt", "continueStmt", "returnStmt", 
			"invokeStmt"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "':='", "'class'", "'extends'", "'static'", "'final'", 
			"'boolean'", "'break'", "'continue'", "'do'", "'else'", "'float'", "'if'", 
			"'int'", "'string'", "'then'", "'for'", "'this'", "'return'", "'true'", 
			"'false'", "'void'", "'nil'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
			"'/'", "'\\'", "'%'", "'!='", "'=='", "'='", "'<'", "'>'", "'<='", "'>='", 
			"'||'", "'&&'", "'!'", "'^'", "'new'", "';'", "','", "'{'", "'}'", "'('", 
			"')'", "'['", "']'", "':'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CMTLINE", "CMTBLOCK", "ASSIGN", "CLASS", "EXTENDS", "STATIC", 
			"FINAL", "BOOLEAN", "BREAK", "CONTINUE", "DO", "ELSE", "FLOAT", "IF", 
			"INT", "STRING", "THEN", "FOR", "THIS", "RETURN", "TRUE", "FALSE", "VOID", 
			"NIL", "TO", "DOWNTO", "ADD", "SUB", "MUL", "FLDIV", "INTDIV", "MOD", 
			"NEQ", "EQ", "EQQ", "LESS", "GREATER", "LEQ", "GEQ", "OR", "AND", "NOT", 
			"CONCAT", "NEW", "SM", "CM", "LP", "RP", "LB", "RB", "LS", "RS", "CL", 
			"DOT", "INTLIT", "FLOATLIT", "INFL", "STRINGLIT", "ID", "WS", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKOOLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BKOOLParser.EOF, 0); }
		public List<ClassDeclContext> classDecl() {
			return getRuleContexts(ClassDeclContext.class);
		}
		public ClassDeclContext classDecl(int i) {
			return getRuleContext(ClassDeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CLASS) {
				{
				{
				setState(82);
				classDecl();
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(88);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDeclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(BKOOLParser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(BKOOLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKOOLParser.ID, i);
		}
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public TerminalNode EXTENDS() { return getToken(BKOOLParser.EXTENDS, 0); }
		public List<MemberContext> member() {
			return getRuleContexts(MemberContext.class);
		}
		public MemberContext member(int i) {
			return getRuleContext(MemberContext.class,i);
		}
		public ClassDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterClassDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitClassDecl(this);
		}
	}

	public final ClassDeclContext classDecl() throws RecognitionException {
		ClassDeclContext _localctx = new ClassDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(CLASS);
			setState(91);
			match(ID);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EXTENDS) {
				{
				setState(92);
				match(EXTENDS);
				setState(93);
				match(ID);
				}
			}

			setState(96);
			match(LP);
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STATIC) | (1L << FINAL) | (1L << BOOLEAN) | (1L << FLOAT) | (1L << INT) | (1L << STRING) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				{
				setState(97);
				member();
				}
				}
				setState(102);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(103);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MemberContext extends ParserRuleContext {
		public AtrbDeclContext atrbDecl() {
			return getRuleContext(AtrbDeclContext.class,0);
		}
		public MethodDeclContext methodDecl() {
			return getRuleContext(MethodDeclContext.class,0);
		}
		public MemberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_member; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterMember(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitMember(this);
		}
	}

	public final MemberContext member() throws RecognitionException {
		MemberContext _localctx = new MemberContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_member);
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				atrbDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				methodDecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtrbDeclContext extends ParserRuleContext {
		public ImmutDeclContext immutDecl() {
			return getRuleContext(ImmutDeclContext.class,0);
		}
		public MutDeclContext mutDecl() {
			return getRuleContext(MutDeclContext.class,0);
		}
		public AtrbDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atrbDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterAtrbDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitAtrbDecl(this);
		}
	}

	public final AtrbDeclContext atrbDecl() throws RecognitionException {
		AtrbDeclContext _localctx = new AtrbDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_atrbDecl);
		try {
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				immutDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				mutDecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MutDeclContext extends ParserRuleContext {
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(BKOOLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKOOLParser.ID, i);
		}
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public TerminalNode STATIC() { return getToken(BKOOLParser.STATIC, 0); }
		public List<AtrbInitContext> atrbInit() {
			return getRuleContexts(AtrbInitContext.class);
		}
		public AtrbInitContext atrbInit(int i) {
			return getRuleContext(AtrbInitContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKOOLParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKOOLParser.CM, i);
		}
		public MutDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mutDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterMutDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitMutDecl(this);
		}
	}

	public final MutDeclContext mutDecl() throws RecognitionException {
		MutDeclContext _localctx = new MutDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_mutDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STATIC) {
				{
				setState(113);
				match(STATIC);
				}
			}

			setState(116);
			typ();
			setState(117);
			match(ID);
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQQ) {
				{
				setState(118);
				atrbInit();
				}
			}

			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(121);
				match(CM);
				setState(122);
				match(ID);
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQQ) {
					{
					setState(123);
					atrbInit();
					}
				}

				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(131);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImmutDeclContext extends ParserRuleContext {
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(BKOOLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKOOLParser.ID, i);
		}
		public List<AtrbInitContext> atrbInit() {
			return getRuleContexts(AtrbInitContext.class);
		}
		public AtrbInitContext atrbInit(int i) {
			return getRuleContext(AtrbInitContext.class,i);
		}
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public TerminalNode FINAL() { return getToken(BKOOLParser.FINAL, 0); }
		public TerminalNode STATIC() { return getToken(BKOOLParser.STATIC, 0); }
		public List<TerminalNode> CM() { return getTokens(BKOOLParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKOOLParser.CM, i);
		}
		public ImmutDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_immutDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterImmutDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitImmutDecl(this);
		}
	}

	public final ImmutDeclContext immutDecl() throws RecognitionException {
		ImmutDeclContext _localctx = new ImmutDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_immutDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(133);
				match(FINAL);
				}
				break;
			case 2:
				{
				setState(134);
				match(FINAL);
				setState(135);
				match(STATIC);
				}
				break;
			case 3:
				{
				setState(136);
				match(STATIC);
				setState(137);
				match(FINAL);
				}
				break;
			}
			setState(140);
			typ();
			setState(141);
			match(ID);
			setState(142);
			atrbInit();
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(143);
				match(CM);
				setState(144);
				match(ID);
				setState(145);
				atrbInit();
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(151);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtrbInitContext extends ParserRuleContext {
		public TerminalNode EQQ() { return getToken(BKOOLParser.EQQ, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public AtrbInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atrbInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterAtrbInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitAtrbInit(this);
		}
	}

	public final AtrbInitContext atrbInit() throws RecognitionException {
		AtrbInitContext _localctx = new AtrbInitContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_atrbInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(EQQ);
			setState(154);
			exp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypContext extends ParserRuleContext {
		public PriTypContext priTyp() {
			return getRuleContext(PriTypContext.class,0);
		}
		public ClassTypContext classTyp() {
			return getRuleContext(ClassTypContext.class,0);
		}
		public TerminalNode VOID() { return getToken(BKOOLParser.VOID, 0); }
		public ArrayTypContext arrayTyp() {
			return getRuleContext(ArrayTypContext.class,0);
		}
		public TypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typ; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterTyp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitTyp(this);
		}
	}

	public final TypContext typ() throws RecognitionException {
		TypContext _localctx = new TypContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_typ);
		try {
			setState(160);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(156);
				priTyp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(157);
				classTyp();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(158);
				match(VOID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(159);
				arrayTyp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayTypContext extends ParserRuleContext {
		public PriTypContext priTyp() {
			return getRuleContext(PriTypContext.class,0);
		}
		public TerminalNode LS() { return getToken(BKOOLParser.LS, 0); }
		public TerminalNode INTLIT() { return getToken(BKOOLParser.INTLIT, 0); }
		public TerminalNode RS() { return getToken(BKOOLParser.RS, 0); }
		public ArrayTypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayTyp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterArrayTyp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitArrayTyp(this);
		}
	}

	public final ArrayTypContext arrayTyp() throws RecognitionException {
		ArrayTypContext _localctx = new ArrayTypContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_arrayTyp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			priTyp();
			setState(163);
			match(LS);
			setState(164);
			match(INTLIT);
			setState(165);
			match(RS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PriTypContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BKOOLParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(BKOOLParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(BKOOLParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(BKOOLParser.BOOLEAN, 0); }
		public PriTypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_priTyp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterPriTyp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitPriTyp(this);
		}
	}

	public final PriTypContext priTyp() throws RecognitionException {
		PriTypContext _localctx = new PriTypContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_priTyp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << FLOAT) | (1L << INT) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassTypContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public ClassTypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classTyp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterClassTyp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitClassTyp(this);
		}
	}

	public final ClassTypContext classTyp() throws RecognitionException {
		ClassTypContext _localctx = new ClassTypContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_classTyp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public BlockStmtContext blockStmt() {
			return getRuleContext(BlockStmtContext.class,0);
		}
		public TerminalNode STATIC() { return getToken(BKOOLParser.STATIC, 0); }
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public ParaListContext paraList() {
			return getRuleContext(ParaListContext.class,0);
		}
		public MethodDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterMethodDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitMethodDecl(this);
		}
	}

	public final MethodDeclContext methodDecl() throws RecognitionException {
		MethodDeclContext _localctx = new MethodDeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_methodDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STATIC) {
				{
				setState(171);
				match(STATIC);
				}
			}

			setState(175);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(174);
				typ();
				}
				break;
			}
			setState(177);
			match(ID);
			setState(178);
			match(LB);
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << FLOAT) | (1L << INT) | (1L << STRING) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				setState(179);
				paraList();
				}
			}

			setState(182);
			match(RB);
			setState(183);
			blockStmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParaListContext extends ParserRuleContext {
		public List<ParaContext> para() {
			return getRuleContexts(ParaContext.class);
		}
		public ParaContext para(int i) {
			return getRuleContext(ParaContext.class,i);
		}
		public List<TerminalNode> SM() { return getTokens(BKOOLParser.SM); }
		public TerminalNode SM(int i) {
			return getToken(BKOOLParser.SM, i);
		}
		public ParaListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paraList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterParaList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitParaList(this);
		}
	}

	public final ParaListContext paraList() throws RecognitionException {
		ParaListContext _localctx = new ParaListContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_paraList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			para();
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SM) {
				{
				{
				setState(186);
				match(SM);
				setState(187);
				para();
				}
				}
				setState(192);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParaContext extends ParserRuleContext {
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(BKOOLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKOOLParser.ID, i);
		}
		public List<TerminalNode> CM() { return getTokens(BKOOLParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKOOLParser.CM, i);
		}
		public ParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterPara(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitPara(this);
		}
	}

	public final ParaContext para() throws RecognitionException {
		ParaContext _localctx = new ParaContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_para);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			typ();
			setState(194);
			match(ID);
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(195);
				match(CM);
				setState(196);
				match(ID);
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayLitContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public List<TerminalNode> CM() { return getTokens(BKOOLParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKOOLParser.CM, i);
		}
		public ArrayLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayLit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterArrayLit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitArrayLit(this);
		}
	}

	public final ArrayLitContext arrayLit() throws RecognitionException {
		ArrayLitContext _localctx = new ArrayLitContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_arrayLit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(LP);
			setState(203);
			literal();
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(204);
				match(CM);
				setState(205);
				literal();
				}
				}
				setState(210);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(211);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public List<EqualeeContext> equalee() {
			return getRuleContexts(EqualeeContext.class);
		}
		public EqualeeContext equalee(int i) {
			return getRuleContext(EqualeeContext.class,i);
		}
		public TerminalNode LESS() { return getToken(BKOOLParser.LESS, 0); }
		public TerminalNode LEQ() { return getToken(BKOOLParser.LEQ, 0); }
		public TerminalNode GREATER() { return getToken(BKOOLParser.GREATER, 0); }
		public TerminalNode GEQ() { return getToken(BKOOLParser.GEQ, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_exp);
		int _la;
		try {
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				equalee();
				setState(214);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << GREATER) | (1L << LEQ) | (1L << GEQ))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(215);
				equalee();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(217);
				equalee();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EqualeeContext extends ParserRuleContext {
		public List<AndOreeContext> andOree() {
			return getRuleContexts(AndOreeContext.class);
		}
		public AndOreeContext andOree(int i) {
			return getRuleContext(AndOreeContext.class,i);
		}
		public TerminalNode EQ() { return getToken(BKOOLParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(BKOOLParser.NEQ, 0); }
		public EqualeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterEqualee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitEqualee(this);
		}
	}

	public final EqualeeContext equalee() throws RecognitionException {
		EqualeeContext _localctx = new EqualeeContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_equalee);
		int _la;
		try {
			setState(225);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(220);
				andOree();
				setState(221);
				_la = _input.LA(1);
				if ( !(_la==NEQ || _la==EQ) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(222);
				andOree();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(224);
				andOree();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AndOreeContext extends ParserRuleContext {
		public AddSubeeContext addSubee() {
			return getRuleContext(AddSubeeContext.class,0);
		}
		public AndOreeContext andOree() {
			return getRuleContext(AndOreeContext.class,0);
		}
		public TerminalNode AND() { return getToken(BKOOLParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKOOLParser.OR, 0); }
		public AndOreeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andOree; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterAndOree(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitAndOree(this);
		}
	}

	public final AndOreeContext andOree() throws RecognitionException {
		AndOreeContext _localctx = new AndOreeContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_andOree);
		int _la;
		try {
			setState(232);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				addSubee(0);
				setState(228);
				_la = _input.LA(1);
				if ( !(_la==OR || _la==AND) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(229);
				andOree();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(231);
				addSubee(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AddSubeeContext extends ParserRuleContext {
		public MulDivModeeContext mulDivModee() {
			return getRuleContext(MulDivModeeContext.class,0);
		}
		public AddSubeeContext addSubee() {
			return getRuleContext(AddSubeeContext.class,0);
		}
		public TerminalNode ADD() { return getToken(BKOOLParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(BKOOLParser.SUB, 0); }
		public AddSubeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addSubee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterAddSubee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitAddSubee(this);
		}
	}

	public final AddSubeeContext addSubee() throws RecognitionException {
		return addSubee(0);
	}

	private AddSubeeContext addSubee(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AddSubeeContext _localctx = new AddSubeeContext(_ctx, _parentState);
		AddSubeeContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_addSubee, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(235);
			mulDivModee(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(242);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new AddSubeeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_addSubee);
					setState(237);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(238);
					_la = _input.LA(1);
					if ( !(_la==ADD || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(239);
					mulDivModee(0);
					}
					} 
				}
				setState(244);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MulDivModeeContext extends ParserRuleContext {
		public ConCateeContext conCatee() {
			return getRuleContext(ConCateeContext.class,0);
		}
		public MulDivModeeContext mulDivModee() {
			return getRuleContext(MulDivModeeContext.class,0);
		}
		public TerminalNode MUL() { return getToken(BKOOLParser.MUL, 0); }
		public TerminalNode INTDIV() { return getToken(BKOOLParser.INTDIV, 0); }
		public TerminalNode FLDIV() { return getToken(BKOOLParser.FLDIV, 0); }
		public TerminalNode MOD() { return getToken(BKOOLParser.MOD, 0); }
		public MulDivModeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulDivModee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterMulDivModee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitMulDivModee(this);
		}
	}

	public final MulDivModeeContext mulDivModee() throws RecognitionException {
		return mulDivModee(0);
	}

	private MulDivModeeContext mulDivModee(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MulDivModeeContext _localctx = new MulDivModeeContext(_ctx, _parentState);
		MulDivModeeContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_mulDivModee, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(246);
			conCatee(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(253);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new MulDivModeeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_mulDivModee);
					setState(248);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(249);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << FLDIV) | (1L << INTDIV) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(250);
					conCatee(0);
					}
					} 
				}
				setState(255);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ConCateeContext extends ParserRuleContext {
		public NoteeContext notee() {
			return getRuleContext(NoteeContext.class,0);
		}
		public ConCateeContext conCatee() {
			return getRuleContext(ConCateeContext.class,0);
		}
		public TerminalNode CONCAT() { return getToken(BKOOLParser.CONCAT, 0); }
		public ConCateeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conCatee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterConCatee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitConCatee(this);
		}
	}

	public final ConCateeContext conCatee() throws RecognitionException {
		return conCatee(0);
	}

	private ConCateeContext conCatee(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ConCateeContext _localctx = new ConCateeContext(_ctx, _parentState);
		ConCateeContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_conCatee, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(257);
			notee();
			}
			_ctx.stop = _input.LT(-1);
			setState(264);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ConCateeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_conCatee);
					setState(259);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(260);
					match(CONCAT);
					}
					setState(261);
					notee();
					}
					} 
				}
				setState(266);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class NoteeContext extends ParserRuleContext {
		public NoteeContext notee() {
			return getRuleContext(NoteeContext.class,0);
		}
		public TerminalNode NOT() { return getToken(BKOOLParser.NOT, 0); }
		public SubAddeeContext subAddee() {
			return getRuleContext(SubAddeeContext.class,0);
		}
		public NoteeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_notee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterNotee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitNotee(this);
		}
	}

	public final NoteeContext notee() throws RecognitionException {
		NoteeContext _localctx = new NoteeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_notee);
		try {
			setState(270);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(267);
				match(NOT);
				}
				setState(268);
				notee();
				}
				break;
			case THIS:
			case TRUE:
			case FALSE:
			case ADD:
			case SUB:
			case NEW:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(269);
				subAddee();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubAddeeContext extends ParserRuleContext {
		public SubAddeeContext subAddee() {
			return getRuleContext(SubAddeeContext.class,0);
		}
		public TerminalNode SUB() { return getToken(BKOOLParser.SUB, 0); }
		public TerminalNode ADD() { return getToken(BKOOLParser.ADD, 0); }
		public IndexeeContext indexee() {
			return getRuleContext(IndexeeContext.class,0);
		}
		public SubAddeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subAddee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterSubAddee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitSubAddee(this);
		}
	}

	public final SubAddeeContext subAddee() throws RecognitionException {
		SubAddeeContext _localctx = new SubAddeeContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_subAddee);
		int _la;
		try {
			setState(275);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
			case SUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(272);
				_la = _input.LA(1);
				if ( !(_la==ADD || _la==SUB) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(273);
				subAddee();
				}
				break;
			case THIS:
			case TRUE:
			case FALSE:
			case NEW:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(274);
				indexee();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IndexeeContext extends ParserRuleContext {
		public MemAccesseeContext memAccessee() {
			return getRuleContext(MemAccesseeContext.class,0);
		}
		public TerminalNode LS() { return getToken(BKOOLParser.LS, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RS() { return getToken(BKOOLParser.RS, 0); }
		public IndexeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_indexee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterIndexee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitIndexee(this);
		}
	}

	public final IndexeeContext indexee() throws RecognitionException {
		IndexeeContext _localctx = new IndexeeContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_indexee);
		try {
			setState(283);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(277);
				memAccessee(0);
				setState(278);
				match(LS);
				setState(279);
				exp();
				setState(280);
				match(RS);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(282);
				memAccessee(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MemAccesseeContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public MemAccesseeContext memAccessee() {
			return getRuleContext(MemAccesseeContext.class,0);
		}
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public ArgLitsContext argLits() {
			return getRuleContext(ArgLitsContext.class,0);
		}
		public MemAccesseeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memAccessee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterMemAccessee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitMemAccessee(this);
		}
	}

	public final MemAccesseeContext memAccessee() throws RecognitionException {
		return memAccessee(0);
	}

	private MemAccesseeContext memAccessee(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MemAccesseeContext _localctx = new MemAccesseeContext(_ctx, _parentState);
		MemAccesseeContext _prevctx = _localctx;
		int _startState = 48;
		enterRecursionRule(_localctx, 48, RULE_memAccessee, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(286);
			atom();
			}
			_ctx.stop = _input.LT(-1);
			setState(301);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(299);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
					case 1:
						{
						_localctx = new MemAccesseeContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_memAccessee);
						setState(288);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(289);
						match(DOT);
						setState(290);
						match(ID);
						}
						break;
					case 2:
						{
						_localctx = new MemAccesseeContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_memAccessee);
						setState(291);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(292);
						match(DOT);
						setState(293);
						match(ID);
						setState(294);
						match(LB);
						setState(296);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << THIS) | (1L << TRUE) | (1L << FALSE) | (1L << ADD) | (1L << SUB) | (1L << NOT) | (1L << NEW) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
							{
							setState(295);
							argLits();
							}
						}

						setState(298);
						match(RB);
						}
						break;
					}
					} 
				}
				setState(303);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode THIS() { return getToken(BKOOLParser.THIS, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public NeweeContext newee() {
			return getRuleContext(NeweeContext.class,0);
		}
		public ArrayLitContext arrayLit() {
			return getRuleContext(ArrayLitContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitAtom(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_atom);
		try {
			setState(309);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case THIS:
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				match(THIS);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(305);
				match(ID);
				}
				break;
			case TRUE:
			case FALSE:
			case INTLIT:
			case FLOATLIT:
			case STRINGLIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(306);
				literal();
				}
				break;
			case NEW:
				enterOuterAlt(_localctx, 4);
				{
				setState(307);
				newee();
				}
				break;
			case LP:
				enterOuterAlt(_localctx, 5);
				{
				setState(308);
				arrayLit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NeweeContext extends ParserRuleContext {
		public TerminalNode NEW() { return getToken(BKOOLParser.NEW, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public ArgLitsContext argLits() {
			return getRuleContext(ArgLitsContext.class,0);
		}
		public NeweeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_newee; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterNewee(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitNewee(this);
		}
	}

	public final NeweeContext newee() throws RecognitionException {
		NeweeContext _localctx = new NeweeContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_newee);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			match(NEW);
			setState(312);
			match(ID);
			setState(313);
			match(LB);
			setState(315);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << THIS) | (1L << TRUE) | (1L << FALSE) | (1L << ADD) | (1L << SUB) | (1L << NOT) | (1L << NEW) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
				{
				setState(314);
				argLits();
				}
			}

			setState(317);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(BKOOLParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(BKOOLParser.FLOATLIT, 0); }
		public TerminalNode STRINGLIT() { return getToken(BKOOLParser.STRINGLIT, 0); }
		public BooleanLitContext booleanLit() {
			return getRuleContext(BooleanLitContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_literal);
		try {
			setState(323);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTLIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(319);
				match(INTLIT);
				}
				break;
			case FLOATLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(320);
				match(FLOATLIT);
				}
				break;
			case STRINGLIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(321);
				match(STRINGLIT);
				}
				break;
			case TRUE:
			case FALSE:
				enterOuterAlt(_localctx, 4);
				{
				setState(322);
				booleanLit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BooleanLitContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(BKOOLParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(BKOOLParser.FALSE, 0); }
		public BooleanLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanLit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterBooleanLit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitBooleanLit(this);
		}
	}

	public final BooleanLitContext booleanLit() throws RecognitionException {
		BooleanLitContext _localctx = new BooleanLitContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_booleanLit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(325);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgLitsContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKOOLParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKOOLParser.CM, i);
		}
		public ArgLitsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argLits; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterArgLits(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitArgLits(this);
		}
	}

	public final ArgLitsContext argLits() throws RecognitionException {
		ArgLitsContext _localctx = new ArgLitsContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_argLits);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			exp();
			setState(332);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(328);
				match(CM);
				setState(329);
				exp();
				}
				}
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public BlockStmtContext blockStmt() {
			return getRuleContext(BlockStmtContext.class,0);
		}
		public AsmStmtContext asmStmt() {
			return getRuleContext(AsmStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public BreakStmtContext breakStmt() {
			return getRuleContext(BreakStmtContext.class,0);
		}
		public ContinueStmtContext continueStmt() {
			return getRuleContext(ContinueStmtContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public AtrbDeclContext atrbDecl() {
			return getRuleContext(AtrbDeclContext.class,0);
		}
		public InvokeStmtContext invokeStmt() {
			return getRuleContext(InvokeStmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_stmt);
		try {
			setState(344);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(335);
				blockStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(336);
				asmStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(337);
				ifStmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(338);
				forStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(339);
				breakStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(340);
				continueStmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(341);
				returnStmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(342);
				atrbDecl();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(343);
				invokeStmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockStmtContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public List<NullAbleDeclListContext> nullAbleDeclList() {
			return getRuleContexts(NullAbleDeclListContext.class);
		}
		public NullAbleDeclListContext nullAbleDeclList(int i) {
			return getRuleContext(NullAbleDeclListContext.class,i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public BlockStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterBlockStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitBlockStmt(this);
		}
	}

	public final BlockStmtContext blockStmt() throws RecognitionException {
		BlockStmtContext _localctx = new BlockStmtContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_blockStmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			match(LP);
			setState(350);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(347);
					nullAbleDeclList();
					}
					} 
				}
				setState(352);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			}
			setState(356);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STATIC) | (1L << FINAL) | (1L << BOOLEAN) | (1L << BREAK) | (1L << CONTINUE) | (1L << FLOAT) | (1L << IF) | (1L << INT) | (1L << STRING) | (1L << FOR) | (1L << THIS) | (1L << RETURN) | (1L << TRUE) | (1L << FALSE) | (1L << VOID) | (1L << NEW) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
				{
				{
				setState(353);
				stmt();
				}
				}
				setState(358);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(359);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NullAbleDeclListContext extends ParserRuleContext {
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(BKOOLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKOOLParser.ID, i);
		}
		public List<AtrbInitContext> atrbInit() {
			return getRuleContexts(AtrbInitContext.class);
		}
		public AtrbInitContext atrbInit(int i) {
			return getRuleContext(AtrbInitContext.class,i);
		}
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public TerminalNode FINAL() { return getToken(BKOOLParser.FINAL, 0); }
		public List<TerminalNode> CM() { return getTokens(BKOOLParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKOOLParser.CM, i);
		}
		public NullAbleDeclListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nullAbleDeclList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterNullAbleDeclList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitNullAbleDeclList(this);
		}
	}

	public final NullAbleDeclListContext nullAbleDeclList() throws RecognitionException {
		NullAbleDeclListContext _localctx = new NullAbleDeclListContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_nullAbleDeclList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FINAL) {
				{
				setState(361);
				match(FINAL);
				}
			}

			setState(364);
			typ();
			setState(365);
			match(ID);
			setState(366);
			atrbInit();
			setState(372);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(367);
				match(CM);
				setState(368);
				match(ID);
				setState(369);
				atrbInit();
				}
				}
				setState(374);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(375);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AsmStmtContext extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKOOLParser.ASSIGN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public AsmStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asmStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterAsmStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitAsmStmt(this);
		}
	}

	public final AsmStmtContext asmStmt() throws RecognitionException {
		AsmStmtContext _localctx = new AsmStmtContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_asmStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(377);
			lhs();
			setState(378);
			match(ASSIGN);
			setState(379);
			exp();
			setState(380);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LhsContext extends ParserRuleContext {
		public IndexeeContext indexee() {
			return getRuleContext(IndexeeContext.class,0);
		}
		public MemAccesseeContext memAccessee() {
			return getRuleContext(MemAccesseeContext.class,0);
		}
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterLhs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitLhs(this);
		}
	}

	public final LhsContext lhs() throws RecognitionException {
		LhsContext _localctx = new LhsContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_lhs);
		try {
			setState(388);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(382);
				indexee();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(383);
				memAccessee(0);
				setState(384);
				match(DOT);
				setState(385);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(387);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKOOLParser.IF, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode THEN() { return getToken(BKOOLParser.THEN, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(BKOOLParser.ELSE, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterIfStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitIfStmt(this);
		}
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_ifStmt);
		try {
			setState(402);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(390);
				match(IF);
				setState(391);
				exp();
				setState(392);
				match(THEN);
				setState(393);
				stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(395);
				match(IF);
				setState(396);
				exp();
				setState(397);
				match(THEN);
				setState(398);
				stmt();
				setState(399);
				match(ELSE);
				setState(400);
				stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForStmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKOOLParser.FOR, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKOOLParser.ASSIGN, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode DO() { return getToken(BKOOLParser.DO, 0); }
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public TerminalNode TO() { return getToken(BKOOLParser.TO, 0); }
		public TerminalNode DOWNTO() { return getToken(BKOOLParser.DOWNTO, 0); }
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterForStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitForStmt(this);
		}
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_forStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(404);
			match(FOR);
			setState(405);
			match(ID);
			setState(406);
			match(ASSIGN);
			setState(407);
			exp();
			setState(408);
			_la = _input.LA(1);
			if ( !(_la==TO || _la==DOWNTO) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(409);
			exp();
			setState(410);
			match(DO);
			setState(411);
			stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BreakStmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKOOLParser.BREAK, 0); }
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public BreakStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterBreakStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitBreakStmt(this);
		}
	}

	public final BreakStmtContext breakStmt() throws RecognitionException {
		BreakStmtContext _localctx = new BreakStmtContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_breakStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(413);
			match(BREAK);
			setState(414);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContinueStmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKOOLParser.CONTINUE, 0); }
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public ContinueStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterContinueStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitContinueStmt(this);
		}
	}

	public final ContinueStmtContext continueStmt() throws RecognitionException {
		ContinueStmtContext _localctx = new ContinueStmtContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_continueStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(416);
			match(CONTINUE);
			setState(417);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKOOLParser.RETURN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterReturnStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitReturnStmt(this);
		}
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_returnStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			match(RETURN);
			setState(420);
			exp();
			setState(421);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InvokeStmtContext extends ParserRuleContext {
		public MemAccesseeContext memAccessee() {
			return getRuleContext(MemAccesseeContext.class,0);
		}
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public TerminalNode SM() { return getToken(BKOOLParser.SM, 0); }
		public ArgLitsContext argLits() {
			return getRuleContext(ArgLitsContext.class,0);
		}
		public InvokeStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_invokeStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).enterInvokeStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKOOLListener ) ((BKOOLListener)listener).exitInvokeStmt(this);
		}
	}

	public final InvokeStmtContext invokeStmt() throws RecognitionException {
		InvokeStmtContext _localctx = new InvokeStmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_invokeStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(423);
			memAccessee(0);
			setState(424);
			match(DOT);
			setState(425);
			match(ID);
			setState(426);
			match(LB);
			setState(428);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << THIS) | (1L << TRUE) | (1L << FALSE) | (1L << ADD) | (1L << SUB) | (1L << NOT) | (1L << NEW) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
				{
				setState(427);
				argLits();
				}
			}

			setState(430);
			match(RB);
			setState(431);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return addSubee_sempred((AddSubeeContext)_localctx, predIndex);
		case 19:
			return mulDivModee_sempred((MulDivModeeContext)_localctx, predIndex);
		case 20:
			return conCatee_sempred((ConCateeContext)_localctx, predIndex);
		case 24:
			return memAccessee_sempred((MemAccesseeContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean addSubee_sempred(AddSubeeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean mulDivModee_sempred(MulDivModeeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean conCatee_sempred(ConCateeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean memAccessee_sempred(MemAccesseeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A\u01b4\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2"+
		"V\n\2\f\2\16\2Y\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3a\n\3\3\3\3\3\7\3e\n\3"+
		"\f\3\16\3h\13\3\3\3\3\3\3\4\3\4\5\4n\n\4\3\5\3\5\5\5r\n\5\3\6\5\6u\n\6"+
		"\3\6\3\6\3\6\5\6z\n\6\3\6\3\6\3\6\5\6\177\n\6\7\6\u0081\n\6\f\6\16\6\u0084"+
		"\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u008d\n\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\7\7\u0095\n\7\f\7\16\7\u0098\13\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3"+
		"\t\5\t\u00a3\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\5\r\u00af\n"+
		"\r\3\r\5\r\u00b2\n\r\3\r\3\r\3\r\5\r\u00b7\n\r\3\r\3\r\3\r\3\16\3\16\3"+
		"\16\7\16\u00bf\n\16\f\16\16\16\u00c2\13\16\3\17\3\17\3\17\3\17\7\17\u00c8"+
		"\n\17\f\17\16\17\u00cb\13\17\3\20\3\20\3\20\3\20\7\20\u00d1\n\20\f\20"+
		"\16\20\u00d4\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00dd\n\21"+
		"\3\22\3\22\3\22\3\22\3\22\5\22\u00e4\n\22\3\23\3\23\3\23\3\23\3\23\5\23"+
		"\u00eb\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00f3\n\24\f\24\16\24\u00f6"+
		"\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00fe\n\25\f\25\16\25\u0101"+
		"\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0109\n\26\f\26\16\26\u010c"+
		"\13\26\3\27\3\27\3\27\5\27\u0111\n\27\3\30\3\30\3\30\5\30\u0116\n\30\3"+
		"\31\3\31\3\31\3\31\3\31\3\31\5\31\u011e\n\31\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u012b\n\32\3\32\7\32\u012e\n\32\f"+
		"\32\16\32\u0131\13\32\3\33\3\33\3\33\3\33\3\33\5\33\u0138\n\33\3\34\3"+
		"\34\3\34\3\34\5\34\u013e\n\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0146"+
		"\n\35\3\36\3\36\3\37\3\37\3\37\7\37\u014d\n\37\f\37\16\37\u0150\13\37"+
		"\3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u015b\n \3!\3!\7!\u015f\n!\f!\16!\u0162"+
		"\13!\3!\7!\u0165\n!\f!\16!\u0168\13!\3!\3!\3\"\5\"\u016d\n\"\3\"\3\"\3"+
		"\"\3\"\3\"\3\"\7\"\u0175\n\"\f\"\16\"\u0178\13\"\3\"\3\"\3#\3#\3#\3#\3"+
		"#\3$\3$\3$\3$\3$\3$\5$\u0187\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5"+
		"%\u0195\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3"+
		")\3*\3*\3*\3*\3*\5*\u01af\n*\3*\3*\3*\3*\2\6&(*\62+\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\n\5\2\n\n\17"+
		"\17\21\22\3\2&)\3\2#$\3\2*+\3\2\35\36\3\2\37\"\3\2\27\30\3\2\33\34\2\u01c5"+
		"\2W\3\2\2\2\4\\\3\2\2\2\6m\3\2\2\2\bq\3\2\2\2\nt\3\2\2\2\f\u008c\3\2\2"+
		"\2\16\u009b\3\2\2\2\20\u00a2\3\2\2\2\22\u00a4\3\2\2\2\24\u00a9\3\2\2\2"+
		"\26\u00ab\3\2\2\2\30\u00ae\3\2\2\2\32\u00bb\3\2\2\2\34\u00c3\3\2\2\2\36"+
		"\u00cc\3\2\2\2 \u00dc\3\2\2\2\"\u00e3\3\2\2\2$\u00ea\3\2\2\2&\u00ec\3"+
		"\2\2\2(\u00f7\3\2\2\2*\u0102\3\2\2\2,\u0110\3\2\2\2.\u0115\3\2\2\2\60"+
		"\u011d\3\2\2\2\62\u011f\3\2\2\2\64\u0137\3\2\2\2\66\u0139\3\2\2\28\u0145"+
		"\3\2\2\2:\u0147\3\2\2\2<\u0149\3\2\2\2>\u015a\3\2\2\2@\u015c\3\2\2\2B"+
		"\u016c\3\2\2\2D\u017b\3\2\2\2F\u0186\3\2\2\2H\u0194\3\2\2\2J\u0196\3\2"+
		"\2\2L\u019f\3\2\2\2N\u01a2\3\2\2\2P\u01a5\3\2\2\2R\u01a9\3\2\2\2TV\5\4"+
		"\3\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\2"+
		"\2\3[\3\3\2\2\2\\]\7\6\2\2]`\7=\2\2^_\7\7\2\2_a\7=\2\2`^\3\2\2\2`a\3\2"+
		"\2\2ab\3\2\2\2bf\7\61\2\2ce\5\6\4\2dc\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3"+
		"\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7\62\2\2j\5\3\2\2\2kn\5\b\5\2ln\5\30\r\2"+
		"mk\3\2\2\2ml\3\2\2\2n\7\3\2\2\2or\5\f\7\2pr\5\n\6\2qo\3\2\2\2qp\3\2\2"+
		"\2r\t\3\2\2\2su\7\b\2\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\5\20\t\2wy\7="+
		"\2\2xz\5\16\b\2yx\3\2\2\2yz\3\2\2\2z\u0082\3\2\2\2{|\7\60\2\2|~\7=\2\2"+
		"}\177\5\16\b\2~}\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080{\3\2\2\2"+
		"\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0085"+
		"\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\7/\2\2\u0086\13\3\2\2\2\u0087"+
		"\u008d\7\t\2\2\u0088\u0089\7\t\2\2\u0089\u008d\7\b\2\2\u008a\u008b\7\b"+
		"\2\2\u008b\u008d\7\t\2\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2\u008c"+
		"\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\5\20"+
		"\t\2\u008f\u0090\7=\2\2\u0090\u0096\5\16\b\2\u0091\u0092\7\60\2\2\u0092"+
		"\u0093\7=\2\2\u0093\u0095\5\16\b\2\u0094\u0091\3\2\2\2\u0095\u0098\3\2"+
		"\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098"+
		"\u0096\3\2\2\2\u0099\u009a\7/\2\2\u009a\r\3\2\2\2\u009b\u009c\7%\2\2\u009c"+
		"\u009d\5 \21\2\u009d\17\3\2\2\2\u009e\u00a3\5\24\13\2\u009f\u00a3\5\26"+
		"\f\2\u00a0\u00a3\7\31\2\2\u00a1\u00a3\5\22\n\2\u00a2\u009e\3\2\2\2\u00a2"+
		"\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\21\3\2\2"+
		"\2\u00a4\u00a5\5\24\13\2\u00a5\u00a6\7\65\2\2\u00a6\u00a7\79\2\2\u00a7"+
		"\u00a8\7\66\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\t\2\2\2\u00aa\25\3\2\2\2"+
		"\u00ab\u00ac\7=\2\2\u00ac\27\3\2\2\2\u00ad\u00af\7\b\2\2\u00ae\u00ad\3"+
		"\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2\5\20\t\2\u00b1"+
		"\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7="+
		"\2\2\u00b4\u00b6\7\63\2\2\u00b5\u00b7\5\32\16\2\u00b6\u00b5\3\2\2\2\u00b6"+
		"\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\7\64\2\2\u00b9\u00ba\5"+
		"@!\2\u00ba\31\3\2\2\2\u00bb\u00c0\5\34\17\2\u00bc\u00bd\7/\2\2\u00bd\u00bf"+
		"\5\34\17\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2"+
		"\u00c0\u00c1\3\2\2\2\u00c1\33\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4"+
		"\5\20\t\2\u00c4\u00c9\7=\2\2\u00c5\u00c6\7\60\2\2\u00c6\u00c8\7=\2\2\u00c7"+
		"\u00c5\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2"+
		"\2\2\u00ca\35\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\7\61\2\2\u00cd\u00d2"+
		"\58\35\2\u00ce\u00cf\7\60\2\2\u00cf\u00d1\58\35\2\u00d0\u00ce\3\2\2\2"+
		"\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5"+
		"\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\7\62\2\2\u00d6\37\3\2\2\2\u00d7"+
		"\u00d8\5\"\22\2\u00d8\u00d9\t\3\2\2\u00d9\u00da\5\"\22\2\u00da\u00dd\3"+
		"\2\2\2\u00db\u00dd\5\"\22\2\u00dc\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd"+
		"!\3\2\2\2\u00de\u00df\5$\23\2\u00df\u00e0\t\4\2\2\u00e0\u00e1\5$\23\2"+
		"\u00e1\u00e4\3\2\2\2\u00e2\u00e4\5$\23\2\u00e3\u00de\3\2\2\2\u00e3\u00e2"+
		"\3\2\2\2\u00e4#\3\2\2\2\u00e5\u00e6\5&\24\2\u00e6\u00e7\t\5\2\2\u00e7"+
		"\u00e8\5$\23\2\u00e8\u00eb\3\2\2\2\u00e9\u00eb\5&\24\2\u00ea\u00e5\3\2"+
		"\2\2\u00ea\u00e9\3\2\2\2\u00eb%\3\2\2\2\u00ec\u00ed\b\24\1\2\u00ed\u00ee"+
		"\5(\25\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0\u00f1\t\6\2\2\u00f1"+
		"\u00f3\5(\25\2\u00f2\u00ef\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2"+
		"\2\2\u00f4\u00f5\3\2\2\2\u00f5\'\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8"+
		"\b\25\1\2\u00f8\u00f9\5*\26\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb\f\4\2\2"+
		"\u00fb\u00fc\t\7\2\2\u00fc\u00fe\5*\26\2\u00fd\u00fa\3\2\2\2\u00fe\u0101"+
		"\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100)\3\2\2\2\u0101"+
		"\u00ff\3\2\2\2\u0102\u0103\b\26\1\2\u0103\u0104\5,\27\2\u0104\u010a\3"+
		"\2\2\2\u0105\u0106\f\4\2\2\u0106\u0107\7-\2\2\u0107\u0109\5,\27\2\u0108"+
		"\u0105\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2"+
		"\2\2\u010b+\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7,\2\2\u010e\u0111"+
		"\5,\27\2\u010f\u0111\5.\30\2\u0110\u010d\3\2\2\2\u0110\u010f\3\2\2\2\u0111"+
		"-\3\2\2\2\u0112\u0113\t\6\2\2\u0113\u0116\5.\30\2\u0114\u0116\5\60\31"+
		"\2\u0115\u0112\3\2\2\2\u0115\u0114\3\2\2\2\u0116/\3\2\2\2\u0117\u0118"+
		"\5\62\32\2\u0118\u0119\7\65\2\2\u0119\u011a\5 \21\2\u011a\u011b\7\66\2"+
		"\2\u011b\u011e\3\2\2\2\u011c\u011e\5\62\32\2\u011d\u0117\3\2\2\2\u011d"+
		"\u011c\3\2\2\2\u011e\61\3\2\2\2\u011f\u0120\b\32\1\2\u0120\u0121\5\64"+
		"\33\2\u0121\u012f\3\2\2\2\u0122\u0123\f\5\2\2\u0123\u0124\78\2\2\u0124"+
		"\u012e\7=\2\2\u0125\u0126\f\4\2\2\u0126\u0127\78\2\2\u0127\u0128\7=\2"+
		"\2\u0128\u012a\7\63\2\2\u0129\u012b\5<\37\2\u012a\u0129\3\2\2\2\u012a"+
		"\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\7\64\2\2\u012d\u0122\3"+
		"\2\2\2\u012d\u0125\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u012f"+
		"\u0130\3\2\2\2\u0130\63\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0138\7\25\2"+
		"\2\u0133\u0138\7=\2\2\u0134\u0138\58\35\2\u0135\u0138\5\66\34\2\u0136"+
		"\u0138\5\36\20\2\u0137\u0132\3\2\2\2\u0137\u0133\3\2\2\2\u0137\u0134\3"+
		"\2\2\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138\65\3\2\2\2\u0139"+
		"\u013a\7.\2\2\u013a\u013b\7=\2\2\u013b\u013d\7\63\2\2\u013c\u013e\5<\37"+
		"\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140"+
		"\7\64\2\2\u0140\67\3\2\2\2\u0141\u0146\79\2\2\u0142\u0146\7:\2\2\u0143"+
		"\u0146\7<\2\2\u0144\u0146\5:\36\2\u0145\u0141\3\2\2\2\u0145\u0142\3\2"+
		"\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u01469\3\2\2\2\u0147\u0148"+
		"\t\b\2\2\u0148;\3\2\2\2\u0149\u014e\5 \21\2\u014a\u014b\7\60\2\2\u014b"+
		"\u014d\5 \21\2\u014c\u014a\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2"+
		"\2\2\u014e\u014f\3\2\2\2\u014f=\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u015b"+
		"\5@!\2\u0152\u015b\5D#\2\u0153\u015b\5H%\2\u0154\u015b\5J&\2\u0155\u015b"+
		"\5L\'\2\u0156\u015b\5N(\2\u0157\u015b\5P)\2\u0158\u015b\5\b\5\2\u0159"+
		"\u015b\5R*\2\u015a\u0151\3\2\2\2\u015a\u0152\3\2\2\2\u015a\u0153\3\2\2"+
		"\2\u015a\u0154\3\2\2\2\u015a\u0155\3\2\2\2\u015a\u0156\3\2\2\2\u015a\u0157"+
		"\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015b?\3\2\2\2\u015c"+
		"\u0160\7\61\2\2\u015d\u015f\5B\"\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2"+
		"\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0166\3\2\2\2\u0162"+
		"\u0160\3\2\2\2\u0163\u0165\5> \2\u0164\u0163\3\2\2\2\u0165\u0168\3\2\2"+
		"\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166"+
		"\3\2\2\2\u0169\u016a\7\62\2\2\u016aA\3\2\2\2\u016b\u016d\7\t\2\2\u016c"+
		"\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\5\20"+
		"\t\2\u016f\u0170\7=\2\2\u0170\u0176\5\16\b\2\u0171\u0172\7\60\2\2\u0172"+
		"\u0173\7=\2\2\u0173\u0175\5\16\b\2\u0174\u0171\3\2\2\2\u0175\u0178\3\2"+
		"\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0179\3\2\2\2\u0178"+
		"\u0176\3\2\2\2\u0179\u017a\7/\2\2\u017aC\3\2\2\2\u017b\u017c\5F$\2\u017c"+
		"\u017d\7\5\2\2\u017d\u017e\5 \21\2\u017e\u017f\7/\2\2\u017fE\3\2\2\2\u0180"+
		"\u0187\5\60\31\2\u0181\u0182\5\62\32\2\u0182\u0183\78\2\2\u0183\u0184"+
		"\7=\2\2\u0184\u0187\3\2\2\2\u0185\u0187\7=\2\2\u0186\u0180\3\2\2\2\u0186"+
		"\u0181\3\2\2\2\u0186\u0185\3\2\2\2\u0187G\3\2\2\2\u0188\u0189\7\20\2\2"+
		"\u0189\u018a\5 \21\2\u018a\u018b\7\23\2\2\u018b\u018c\5> \2\u018c\u0195"+
		"\3\2\2\2\u018d\u018e\7\20\2\2\u018e\u018f\5 \21\2\u018f\u0190\7\23\2\2"+
		"\u0190\u0191\5> \2\u0191\u0192\7\16\2\2\u0192\u0193\5> \2\u0193\u0195"+
		"\3\2\2\2\u0194\u0188\3\2\2\2\u0194\u018d\3\2\2\2\u0195I\3\2\2\2\u0196"+
		"\u0197\7\24\2\2\u0197\u0198\7=\2\2\u0198\u0199\7\5\2\2\u0199\u019a\5 "+
		"\21\2\u019a\u019b\t\t\2\2\u019b\u019c\5 \21\2\u019c\u019d\7\r\2\2\u019d"+
		"\u019e\5> \2\u019eK\3\2\2\2\u019f\u01a0\7\13\2\2\u01a0\u01a1\7/\2\2\u01a1"+
		"M\3\2\2\2\u01a2\u01a3\7\f\2\2\u01a3\u01a4\7/\2\2\u01a4O\3\2\2\2\u01a5"+
		"\u01a6\7\26\2\2\u01a6\u01a7\5 \21\2\u01a7\u01a8\7/\2\2\u01a8Q\3\2\2\2"+
		"\u01a9\u01aa\5\62\32\2\u01aa\u01ab\78\2\2\u01ab\u01ac\7=\2\2\u01ac\u01ae"+
		"\7\63\2\2\u01ad\u01af\5<\37\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2"+
		"\u01af\u01b0\3\2\2\2\u01b0\u01b1\7\64\2\2\u01b1\u01b2\7/\2\2\u01b2S\3"+
		"\2\2\2,W`fmqty~\u0082\u008c\u0096\u00a2\u00ae\u00b1\u00b6\u00c0\u00c9"+
		"\u00d2\u00dc\u00e3\u00ea\u00f4\u00ff\u010a\u0110\u0115\u011d\u012a\u012d"+
		"\u012f\u0137\u013d\u0145\u014e\u015a\u0160\u0166\u016c\u0176\u0186\u0194"+
		"\u01ae";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}