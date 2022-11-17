# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0099\n\3\f\3\16\3\u009c")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\78\u0169\n8\f8\168\u016c\138\38\58\u016f")
        buf.write("\n8\39\39\59\u0173\n9\39\39\39\39\39\59\u017a\n9\59\u017c")
        buf.write("\n9\3:\3:\7:\u0180\n:\f:\16:\u0183\13:\3;\3;\5;\u0187")
        buf.write("\n;\3;\3;\7;\u018b\n;\f;\16;\u018e\13;\3<\3<\5<\u0192")
        buf.write("\n<\3=\3=\7=\u0196\n=\f=\16=\u0199\13=\3=\3=\3>\3>\5>")
        buf.write("\u019f\n>\3?\3?\3?\3@\3@\3@\5@\u01a7\n@\3A\3A\7A\u01ab")
        buf.write("\nA\fA\16A\u01ae\13A\3B\6B\u01b1\nB\rB\16B\u01b2\3B\3")
        buf.write("B\3C\3C\7C\u01b9\nC\fC\16C\u01bc\13C\3C\3C\5C\u01c0\n")
        buf.write("C\3C\3C\3D\3D\7D\u01c6\nD\fD\16D\u01c9\13D\3D\3D\3D\3")
        buf.write("E\3E\3E\3\u009a\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q:s\2u\2w;y<{\2}\2\177\2\u0081=\u0083>")
        buf.write("\u0085?\u0087@\u0089A\3\2\20\4\2\f\f\17\17\3\2\63;\3\2")
        buf.write("\62;\3\2\62\62\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2$")
        buf.write("$^^ddhhppttvv\3\2^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\16\17\"\"\6\2\f\f\17\17GHQQ\3\2$$\2\u01dd\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b")
        buf.write("\3\2\2\2\5\u0094\3\2\2\2\7\u00a2\3\2\2\2\t\u00a5\3\2\2")
        buf.write("\2\13\u00ab\3\2\2\2\r\u00b3\3\2\2\2\17\u00ba\3\2\2\2\21")
        buf.write("\u00c0\3\2\2\2\23\u00c8\3\2\2\2\25\u00ce\3\2\2\2\27\u00d7")
        buf.write("\3\2\2\2\31\u00da\3\2\2\2\33\u00df\3\2\2\2\35\u00e5\3")
        buf.write("\2\2\2\37\u00e8\3\2\2\2!\u00ec\3\2\2\2#\u00f3\3\2\2\2")
        buf.write("%\u00f8\3\2\2\2\'\u00fc\3\2\2\2)\u0101\3\2\2\2+\u0108")
        buf.write("\3\2\2\2-\u010d\3\2\2\2/\u0113\3\2\2\2\61\u0118\3\2\2")
        buf.write("\2\63\u011c\3\2\2\2\65\u011f\3\2\2\2\67\u0126\3\2\2\2")
        buf.write("9\u0128\3\2\2\2;\u012a\3\2\2\2=\u012c\3\2\2\2?\u012e\3")
        buf.write("\2\2\2A\u0130\3\2\2\2C\u0132\3\2\2\2E\u0135\3\2\2\2G\u0138")
        buf.write("\3\2\2\2I\u013a\3\2\2\2K\u013c\3\2\2\2M\u013e\3\2\2\2")
        buf.write("O\u0141\3\2\2\2Q\u0144\3\2\2\2S\u0147\3\2\2\2U\u014a\3")
        buf.write("\2\2\2W\u014c\3\2\2\2Y\u014e\3\2\2\2[\u0152\3\2\2\2]\u0154")
        buf.write("\3\2\2\2_\u0156\3\2\2\2a\u0158\3\2\2\2c\u015a\3\2\2\2")
        buf.write("e\u015c\3\2\2\2g\u015e\3\2\2\2i\u0160\3\2\2\2k\u0162\3")
        buf.write("\2\2\2m\u0164\3\2\2\2o\u016e\3\2\2\2q\u017b\3\2\2\2s\u017d")
        buf.write("\3\2\2\2u\u0184\3\2\2\2w\u0191\3\2\2\2y\u0193\3\2\2\2")
        buf.write("{\u019e\3\2\2\2}\u01a0\3\2\2\2\177\u01a6\3\2\2\2\u0081")
        buf.write("\u01a8\3\2\2\2\u0083\u01b0\3\2\2\2\u0085\u01b6\3\2\2\2")
        buf.write("\u0087\u01c3\3\2\2\2\u0089\u01cd\3\2\2\2\u008b\u008f\7")
        buf.write("%\2\2\u008c\u008e\n\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\b\2\2\2")
        buf.write("\u0093\4\3\2\2\2\u0094\u0095\7\61\2\2\u0095\u0096\7,\2")
        buf.write("\2\u0096\u009a\3\2\2\2\u0097\u0099\13\2\2\2\u0098\u0097")
        buf.write("\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u009b\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3\2\2\2")
        buf.write("\u009d\u009e\7,\2\2\u009e\u009f\7\61\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u00a1\b\3\2\2\u00a1\6\3\2\2\2\u00a2\u00a3")
        buf.write("\7<\2\2\u00a3\u00a4\7?\2\2\u00a4\b\3\2\2\2\u00a5\u00a6")
        buf.write("\7e\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9")
        buf.write("\7u\2\2\u00a9\u00aa\7u\2\2\u00aa\n\3\2\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7z\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7f\2\2\u00b1\u00b2")
        buf.write("\7u\2\2\u00b2\f\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7e\2\2\u00b9\16\3\2\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7c\2\2\u00be\u00bf\7n\2\2\u00bf\20\3\2\2\2\u00c0\u00c1")
        buf.write("\7d\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7n\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\22\3\2\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7m\2\2\u00cd\24\3\2\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\26\3\2\2\2\u00d7\u00d8\7f\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\30\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de\32")
        buf.write("\3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7v\2\2\u00e4\34")
        buf.write("\3\2\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7h\2\2\u00e7\36")
        buf.write("\3\2\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb \3\2\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7i\2\2\u00f2\"\3\2\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4\u00f5\7j\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7p\2\2\u00f7$\3\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7t\2\2\u00fb&\3\2\2\2\u00fc\u00fd")
        buf.write("\7v\2\2\u00fd\u00fe\7j\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7u\2\2\u0100(\3\2\2\2\u0101\u0102\7t\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7v\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7p\2\2\u0107*\3\2\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7t\2\2\u010a\u010b\7w\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c,\3\2\2\2\u010d\u010e\7h\2\2\u010e\u010f")
        buf.write("\7c\2\2\u010f\u0110\7n\2\2\u0110\u0111\7u\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112.\3\2\2\2\u0113\u0114\7x\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7k\2\2\u0116\u0117\7f\2\2\u0117\60")
        buf.write("\3\2\2\2\u0118\u0119\7p\2\2\u0119\u011a\7k\2\2\u011a\u011b")
        buf.write("\7n\2\2\u011b\62\3\2\2\2\u011c\u011d\7v\2\2\u011d\u011e")
        buf.write("\7q\2\2\u011e\64\3\2\2\2\u011f\u0120\7f\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\u0122\7y\2\2\u0122\u0123\7p\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7q\2\2\u0125\66\3\2\2\2\u0126\u0127")
        buf.write("\7-\2\2\u01278\3\2\2\2\u0128\u0129\7/\2\2\u0129:\3\2\2")
        buf.write("\2\u012a\u012b\7,\2\2\u012b<\3\2\2\2\u012c\u012d\7\61")
        buf.write("\2\2\u012d>\3\2\2\2\u012e\u012f\7^\2\2\u012f@\3\2\2\2")
        buf.write("\u0130\u0131\7\'\2\2\u0131B\3\2\2\2\u0132\u0133\7#\2\2")
        buf.write("\u0133\u0134\7?\2\2\u0134D\3\2\2\2\u0135\u0136\7?\2\2")
        buf.write("\u0136\u0137\7?\2\2\u0137F\3\2\2\2\u0138\u0139\7?\2\2")
        buf.write("\u0139H\3\2\2\2\u013a\u013b\7>\2\2\u013bJ\3\2\2\2\u013c")
        buf.write("\u013d\7@\2\2\u013dL\3\2\2\2\u013e\u013f\7>\2\2\u013f")
        buf.write("\u0140\7?\2\2\u0140N\3\2\2\2\u0141\u0142\7@\2\2\u0142")
        buf.write("\u0143\7?\2\2\u0143P\3\2\2\2\u0144\u0145\7~\2\2\u0145")
        buf.write("\u0146\7~\2\2\u0146R\3\2\2\2\u0147\u0148\7(\2\2\u0148")
        buf.write("\u0149\7(\2\2\u0149T\3\2\2\2\u014a\u014b\7#\2\2\u014b")
        buf.write("V\3\2\2\2\u014c\u014d\7`\2\2\u014dX\3\2\2\2\u014e\u014f")
        buf.write("\7p\2\2\u014f\u0150\7g\2\2\u0150\u0151\7y\2\2\u0151Z\3")
        buf.write("\2\2\2\u0152\u0153\7=\2\2\u0153\\\3\2\2\2\u0154\u0155")
        buf.write("\7.\2\2\u0155^\3\2\2\2\u0156\u0157\7}\2\2\u0157`\3\2\2")
        buf.write("\2\u0158\u0159\7\177\2\2\u0159b\3\2\2\2\u015a\u015b\7")
        buf.write("*\2\2\u015bd\3\2\2\2\u015c\u015d\7+\2\2\u015df\3\2\2\2")
        buf.write("\u015e\u015f\7]\2\2\u015fh\3\2\2\2\u0160\u0161\7_\2\2")
        buf.write("\u0161j\3\2\2\2\u0162\u0163\7<\2\2\u0163l\3\2\2\2\u0164")
        buf.write("\u0165\7\60\2\2\u0165n\3\2\2\2\u0166\u016a\t\3\2\2\u0167")
        buf.write("\u0169\t\4\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016f\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016d\u016f\t\5\2\2\u016e\u0166")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016fp\3\2\2\2\u0170\u0172")
        buf.write("\5o8\2\u0171\u0173\5s:\2\u0172\u0171\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\5u;\2\u0175\u017c")
        buf.write("\3\2\2\2\u0176\u0177\5o8\2\u0177\u0179\5s:\2\u0178\u017a")
        buf.write("\5u;\2\u0179\u0178\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c")
        buf.write("\3\2\2\2\u017b\u0170\3\2\2\2\u017b\u0176\3\2\2\2\u017c")
        buf.write("r\3\2\2\2\u017d\u0181\5m\67\2\u017e\u0180\t\4\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182t\3\2\2\2\u0183\u0181\3\2\2")
        buf.write("\2\u0184\u0186\t\6\2\2\u0185\u0187\t\7\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u018c\t\3\2\2\u0189\u018b\t\4\2\2\u018a\u0189\3\2\2\2")
        buf.write("\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018dv\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0192")
        buf.write("\5o8\2\u0190\u0192\5q9\2\u0191\u018f\3\2\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192x\3\2\2\2\u0193\u0197\7$\2\2\u0194\u0196")
        buf.write("\5{>\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019a\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u019b\7$\2\2\u019bz\3\2\2\2\u019c")
        buf.write("\u019f\5}?\2\u019d\u019f\n\b\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f|\3\2\2\2\u01a0\u01a1\7^\2\2\u01a1")
        buf.write("\u01a2\t\t\2\2\u01a2~\3\2\2\2\u01a3\u01a4\7^\2\2\u01a4")
        buf.write("\u01a7\n\t\2\2\u01a5\u01a7\n\n\2\2\u01a6\u01a3\3\2\2\2")
        buf.write("\u01a6\u01a5\3\2\2\2\u01a7\u0080\3\2\2\2\u01a8\u01ac\t")
        buf.write("\13\2\2\u01a9\u01ab\t\f\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u0082\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1\t")
        buf.write("\r\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b5\bB\2\2\u01b5\u0084\3\2\2\2\u01b6\u01ba\7$\2\2\u01b7")
        buf.write("\u01b9\5{>\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bf\3\2\2\2")
        buf.write("\u01bc\u01ba\3\2\2\2\u01bd\u01c0\t\16\2\2\u01be\u01c0")
        buf.write("\n\17\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c1\u01c2\bC\3\2\u01c2\u0086\3\2\2\2")
        buf.write("\u01c3\u01c7\7$\2\2\u01c4\u01c6\5{>\2\u01c5\u01c4\3\2")
        buf.write("\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca")
        buf.write("\u01cb\5\177@\2\u01cb\u01cc\bD\4\2\u01cc\u0088\3\2\2\2")
        buf.write("\u01cd\u01ce\13\2\2\2\u01ce\u01cf\bE\5\2\u01cf\u008a\3")
        buf.write("\2\2\2\26\2\u008f\u009a\u016a\u016e\u0172\u0179\u017b")
        buf.write("\u0181\u0186\u018c\u0191\u0197\u019e\u01a6\u01ac\u01b2")
        buf.write("\u01ba\u01bf\u01c7\6\b\2\2\3C\2\3D\3\3E\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CMTLINE = 1
    CMTBLOCK = 2
    ASSIGN = 3
    CLASS = 4
    EXTENDS = 5
    STATIC = 6
    FINAL = 7
    BOOLEAN = 8
    BREAK = 9
    CONTINUE = 10
    DO = 11
    ELSE = 12
    FLOAT = 13
    IF = 14
    INT = 15
    STRING = 16
    THEN = 17
    FOR = 18
    THIS = 19
    RETURN = 20
    TRUE = 21
    FALSE = 22
    VOID = 23
    NIL = 24
    TO = 25
    DOWNTO = 26
    ADD = 27
    SUB = 28
    MUL = 29
    FLDIV = 30
    INTDIV = 31
    MOD = 32
    NEQ = 33
    EQ = 34
    EQQ = 35
    LESS = 36
    GREATER = 37
    LEQ = 38
    GEQ = 39
    OR = 40
    AND = 41
    NOT = 42
    CONCAT = 43
    NEW = 44
    SM = 45
    CM = 46
    LP = 47
    RP = 48
    LB = 49
    RB = 50
    LS = 51
    RS = 52
    CL = 53
    DOT = 54
    INTLIT = 55
    FLOATLIT = 56
    INFL = 57
    STRINGLIT = 58
    ID = 59
    WS = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'class'", "'extends'", "'static'", "'final'", "'boolean'", 
            "'break'", "'continue'", "'do'", "'else'", "'float'", "'if'", 
            "'int'", "'string'", "'then'", "'for'", "'this'", "'return'", 
            "'true'", "'false'", "'void'", "'nil'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'='", 
            "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", 
            "'new'", "';'", "','", "'{'", "'}'", "'('", "')'", "'['", "']'", 
            "':'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "CMTLINE", "CMTBLOCK", "ASSIGN", "CLASS", "EXTENDS", "STATIC", 
            "FINAL", "BOOLEAN", "BREAK", "CONTINUE", "DO", "ELSE", "FLOAT", 
            "IF", "INT", "STRING", "THEN", "FOR", "THIS", "RETURN", "TRUE", 
            "FALSE", "VOID", "NIL", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
            "FLDIV", "INTDIV", "MOD", "NEQ", "EQ", "EQQ", "LESS", "GREATER", 
            "LEQ", "GEQ", "OR", "AND", "NOT", "CONCAT", "NEW", "SM", "CM", 
            "LP", "RP", "LB", "RB", "LS", "RS", "CL", "DOT", "INTLIT", "FLOATLIT", 
            "INFL", "STRINGLIT", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "CMTLINE", "CMTBLOCK", "ASSIGN", "CLASS", "EXTENDS", "STATIC", 
                  "FINAL", "BOOLEAN", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "FLOAT", "IF", "INT", "STRING", "THEN", "FOR", "THIS", 
                  "RETURN", "TRUE", "FALSE", "VOID", "NIL", "TO", "DOWNTO", 
                  "ADD", "SUB", "MUL", "FLDIV", "INTDIV", "MOD", "NEQ", 
                  "EQ", "EQQ", "LESS", "GREATER", "LEQ", "GEQ", "OR", "AND", 
                  "NOT", "CONCAT", "NEW", "SM", "CM", "LP", "RP", "LB", 
                  "RB", "LS", "RS", "CL", "DOT", "INTLIT", "FLOATLIT", "DECIMAL", 
                  "EXPONENT", "INFL", "STRINGLIT", "CHAR", "ESC", "ILL_ESC", 
                  "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise ErrorToken(self.text)

     


