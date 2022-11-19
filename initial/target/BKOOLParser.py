# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01ba\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3a\n\3\3\3\3\3\7\3e\n\3\f")
        buf.write("\3\16\3h\13\3\3\3\3\3\3\4\3\4\5\4n\n\4\3\5\3\5\5\5r\n")
        buf.write("\5\3\6\5\6u\n\6\3\6\3\6\3\6\5\6z\n\6\3\6\3\6\3\6\5\6\177")
        buf.write("\n\6\7\6\u0081\n\6\f\6\16\6\u0084\13\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u008d\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7")
        buf.write("\u0095\n\7\f\7\16\7\u0098\13\7\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u00a3\n\t\3\n\3\n\5\n\u00a7\n\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\5\r\u00b2\n\r\3\r\5\r")
        buf.write("\u00b5\n\r\3\r\3\r\3\r\5\r\u00ba\n\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\7\16\u00c2\n\16\f\16\16\16\u00c5\13\16\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00cb\n\17\f\17\16\17\u00ce\13\17")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u00d4\n\20\f\20\16\20\u00d7")
        buf.write("\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00e0\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\5\22\u00e7\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00ee\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\7\24\u00f6\n\24\f\24\16\24\u00f9\13\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\7\25\u0101\n\25\f\25\16\25\u0104")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u010c\n\26\f")
        buf.write("\26\16\26\u010f\13\26\3\27\3\27\3\27\5\27\u0114\n\27\3")
        buf.write("\30\3\30\3\30\5\30\u0119\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0121\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u012e\n\32\3\32\7\32\u0131")
        buf.write("\n\32\f\32\16\32\u0134\13\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u013b\n\33\3\34\3\34\3\34\3\34\5\34\u0141\n\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\5\35\u0149\n\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\7\37\u0150\n\37\f\37\16\37\u0153\13\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \5 \u015d\n \3!\3!\7!\u0161\n")
        buf.write("!\f!\16!\u0164\13!\3!\7!\u0167\n!\f!\16!\u016a\13!\3!")
        buf.write("\3!\3\"\5\"\u016f\n\"\3\"\3\"\3\"\5\"\u0174\n\"\3\"\3")
        buf.write("\"\3\"\5\"\u0179\n\"\7\"\u017b\n\"\f\"\16\"\u017e\13\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\5$\u018d\n$")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u019b\n%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\5*\u01b5\n*\3*\3*\3*\3*\2\6&(*\62+\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPR\2\n\5\2\n\n\17\17\21\22\3\2&)\3\2#$")
        buf.write("\3\2*+\3\2\35\36\3\2\37\"\3\2\27\30\3\2\33\34\2\u01cc")
        buf.write("\2W\3\2\2\2\4\\\3\2\2\2\6m\3\2\2\2\bq\3\2\2\2\nt\3\2\2")
        buf.write("\2\f\u008c\3\2\2\2\16\u009b\3\2\2\2\20\u00a2\3\2\2\2\22")
        buf.write("\u00a6\3\2\2\2\24\u00ac\3\2\2\2\26\u00ae\3\2\2\2\30\u00b1")
        buf.write("\3\2\2\2\32\u00be\3\2\2\2\34\u00c6\3\2\2\2\36\u00cf\3")
        buf.write("\2\2\2 \u00df\3\2\2\2\"\u00e6\3\2\2\2$\u00ed\3\2\2\2&")
        buf.write("\u00ef\3\2\2\2(\u00fa\3\2\2\2*\u0105\3\2\2\2,\u0113\3")
        buf.write("\2\2\2.\u0118\3\2\2\2\60\u0120\3\2\2\2\62\u0122\3\2\2")
        buf.write("\2\64\u013a\3\2\2\2\66\u013c\3\2\2\28\u0148\3\2\2\2:\u014a")
        buf.write("\3\2\2\2<\u014c\3\2\2\2>\u015c\3\2\2\2@\u015e\3\2\2\2")
        buf.write("B\u016e\3\2\2\2D\u0181\3\2\2\2F\u018c\3\2\2\2H\u019a\3")
        buf.write("\2\2\2J\u019c\3\2\2\2L\u01a5\3\2\2\2N\u01a8\3\2\2\2P\u01ab")
        buf.write("\3\2\2\2R\u01af\3\2\2\2TV\5\4\3\2UT\3\2\2\2VY\3\2\2\2")
        buf.write("WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\2\2\3[\3")
        buf.write("\3\2\2\2\\]\7\6\2\2]`\7=\2\2^_\7\7\2\2_a\7=\2\2`^\3\2")
        buf.write("\2\2`a\3\2\2\2ab\3\2\2\2bf\7\61\2\2ce\5\6\4\2dc\3\2\2")
        buf.write("\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2i")
        buf.write("j\7\62\2\2j\5\3\2\2\2kn\5\b\5\2ln\5\30\r\2mk\3\2\2\2m")
        buf.write("l\3\2\2\2n\7\3\2\2\2or\5\f\7\2pr\5\n\6\2qo\3\2\2\2qp\3")
        buf.write("\2\2\2r\t\3\2\2\2su\7\b\2\2ts\3\2\2\2tu\3\2\2\2uv\3\2")
        buf.write("\2\2vw\5\20\t\2wy\7=\2\2xz\5\16\b\2yx\3\2\2\2yz\3\2\2")
        buf.write("\2z\u0082\3\2\2\2{|\7\60\2\2|~\7=\2\2}\177\5\16\b\2~}")
        buf.write("\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080{\3\2\2\2")
        buf.write("\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3")
        buf.write("\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086")
        buf.write("\7/\2\2\u0086\13\3\2\2\2\u0087\u008d\7\t\2\2\u0088\u0089")
        buf.write("\7\t\2\2\u0089\u008d\7\b\2\2\u008a\u008b\7\b\2\2\u008b")
        buf.write("\u008d\7\t\2\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2")
        buf.write("\u008c\u008a\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\5")
        buf.write("\20\t\2\u008f\u0090\7=\2\2\u0090\u0096\5\16\b\2\u0091")
        buf.write("\u0092\7\60\2\2\u0092\u0093\7=\2\2\u0093\u0095\5\16\b")
        buf.write("\2\u0094\u0091\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0099\u009a\7/\2\2\u009a\r\3\2\2\2\u009b")
        buf.write("\u009c\7%\2\2\u009c\u009d\5 \21\2\u009d\17\3\2\2\2\u009e")
        buf.write("\u00a3\5\24\13\2\u009f\u00a3\5\26\f\2\u00a0\u00a3\7\31")
        buf.write("\2\2\u00a1\u00a3\5\22\n\2\u00a2\u009e\3\2\2\2\u00a2\u009f")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\21\3\2\2\2\u00a4\u00a7\5\24\13\2\u00a5\u00a7\5\26\f\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3")
        buf.write("\2\2\2\u00a8\u00a9\7\65\2\2\u00a9\u00aa\79\2\2\u00aa\u00ab")
        buf.write("\7\66\2\2\u00ab\23\3\2\2\2\u00ac\u00ad\t\2\2\2\u00ad\25")
        buf.write("\3\2\2\2\u00ae\u00af\7=\2\2\u00af\27\3\2\2\2\u00b0\u00b2")
        buf.write("\7\b\2\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00b5\5\20\t\2\u00b4\u00b3\3\2\2")
        buf.write("\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7")
        buf.write("\7=\2\2\u00b7\u00b9\7\63\2\2\u00b8\u00ba\5\32\16\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\7\64\2\2\u00bc\u00bd\5@!\2\u00bd\31\3\2\2")
        buf.write("\2\u00be\u00c3\5\34\17\2\u00bf\u00c0\7/\2\2\u00c0\u00c2")
        buf.write("\5\34\17\2\u00c1\u00bf\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\33\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00c7\5\20\t\2\u00c7\u00cc\7=\2\2")
        buf.write("\u00c8\u00c9\7\60\2\2\u00c9\u00cb\7=\2\2\u00ca\u00c8\3")
        buf.write("\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\35\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0")
        buf.write("\7\61\2\2\u00d0\u00d5\58\35\2\u00d1\u00d2\7\60\2\2\u00d2")
        buf.write("\u00d4\58\35\2\u00d3\u00d1\3\2\2\2\u00d4\u00d7\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7\62\2\2\u00d9")
        buf.write("\37\3\2\2\2\u00da\u00db\5\"\22\2\u00db\u00dc\t\3\2\2\u00dc")
        buf.write("\u00dd\5\"\22\2\u00dd\u00e0\3\2\2\2\u00de\u00e0\5\"\22")
        buf.write("\2\u00df\u00da\3\2\2\2\u00df\u00de\3\2\2\2\u00e0!\3\2")
        buf.write("\2\2\u00e1\u00e2\5$\23\2\u00e2\u00e3\t\4\2\2\u00e3\u00e4")
        buf.write("\5$\23\2\u00e4\u00e7\3\2\2\2\u00e5\u00e7\5$\23\2\u00e6")
        buf.write("\u00e1\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7#\3\2\2\2\u00e8")
        buf.write("\u00e9\5&\24\2\u00e9\u00ea\t\5\2\2\u00ea\u00eb\5$\23\2")
        buf.write("\u00eb\u00ee\3\2\2\2\u00ec\u00ee\5&\24\2\u00ed\u00e8\3")
        buf.write("\2\2\2\u00ed\u00ec\3\2\2\2\u00ee%\3\2\2\2\u00ef\u00f0")
        buf.write("\b\24\1\2\u00f0\u00f1\5(\25\2\u00f1\u00f7\3\2\2\2\u00f2")
        buf.write("\u00f3\f\4\2\2\u00f3\u00f4\t\6\2\2\u00f4\u00f6\5(\25\2")
        buf.write("\u00f5\u00f2\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\'\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fb\b\25\1\2\u00fb\u00fc\5*\26\2\u00fc")
        buf.write("\u0102\3\2\2\2\u00fd\u00fe\f\4\2\2\u00fe\u00ff\t\7\2\2")
        buf.write("\u00ff\u0101\5*\26\2\u0100\u00fd\3\2\2\2\u0101\u0104\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103)")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\b\26\1\2\u0106")
        buf.write("\u0107\5,\27\2\u0107\u010d\3\2\2\2\u0108\u0109\f\4\2\2")
        buf.write("\u0109\u010a\7-\2\2\u010a\u010c\5,\27\2\u010b\u0108\3")
        buf.write("\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e+\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111")
        buf.write("\7,\2\2\u0111\u0114\5,\27\2\u0112\u0114\5.\30\2\u0113")
        buf.write("\u0110\3\2\2\2\u0113\u0112\3\2\2\2\u0114-\3\2\2\2\u0115")
        buf.write("\u0116\t\6\2\2\u0116\u0119\5.\30\2\u0117\u0119\5\60\31")
        buf.write("\2\u0118\u0115\3\2\2\2\u0118\u0117\3\2\2\2\u0119/\3\2")
        buf.write("\2\2\u011a\u011b\5\62\32\2\u011b\u011c\7\65\2\2\u011c")
        buf.write("\u011d\5 \21\2\u011d\u011e\7\66\2\2\u011e\u0121\3\2\2")
        buf.write("\2\u011f\u0121\5\62\32\2\u0120\u011a\3\2\2\2\u0120\u011f")
        buf.write("\3\2\2\2\u0121\61\3\2\2\2\u0122\u0123\b\32\1\2\u0123\u0124")
        buf.write("\5\64\33\2\u0124\u0132\3\2\2\2\u0125\u0126\f\5\2\2\u0126")
        buf.write("\u0127\78\2\2\u0127\u0131\7=\2\2\u0128\u0129\f\4\2\2\u0129")
        buf.write("\u012a\78\2\2\u012a\u012b\7=\2\2\u012b\u012d\7\63\2\2")
        buf.write("\u012c\u012e\5<\37\2\u012d\u012c\3\2\2\2\u012d\u012e\3")
        buf.write("\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131\7\64\2\2\u0130")
        buf.write("\u0125\3\2\2\2\u0130\u0128\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\63\3\2")
        buf.write("\2\2\u0134\u0132\3\2\2\2\u0135\u013b\7\25\2\2\u0136\u013b")
        buf.write("\7=\2\2\u0137\u013b\58\35\2\u0138\u013b\5\66\34\2\u0139")
        buf.write("\u013b\5\36\20\2\u013a\u0135\3\2\2\2\u013a\u0136\3\2\2")
        buf.write("\2\u013a\u0137\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u0139")
        buf.write("\3\2\2\2\u013b\65\3\2\2\2\u013c\u013d\7.\2\2\u013d\u013e")
        buf.write("\7=\2\2\u013e\u0140\7\63\2\2\u013f\u0141\5<\37\2\u0140")
        buf.write("\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0143\7\64\2\2\u0143\67\3\2\2\2\u0144\u0149\79")
        buf.write("\2\2\u0145\u0149\7:\2\2\u0146\u0149\7<\2\2\u0147\u0149")
        buf.write("\5:\36\2\u0148\u0144\3\2\2\2\u0148\u0145\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u01499\3\2\2\2\u014a")
        buf.write("\u014b\t\b\2\2\u014b;\3\2\2\2\u014c\u0151\5 \21\2\u014d")
        buf.write("\u014e\7\60\2\2\u014e\u0150\5 \21\2\u014f\u014d\3\2\2")
        buf.write("\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152=\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u015d")
        buf.write("\5@!\2\u0155\u015d\5D#\2\u0156\u015d\5H%\2\u0157\u015d")
        buf.write("\5J&\2\u0158\u015d\5L\'\2\u0159\u015d\5N(\2\u015a\u015d")
        buf.write("\5P)\2\u015b\u015d\5R*\2\u015c\u0154\3\2\2\2\u015c\u0155")
        buf.write("\3\2\2\2\u015c\u0156\3\2\2\2\u015c\u0157\3\2\2\2\u015c")
        buf.write("\u0158\3\2\2\2\u015c\u0159\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015c\u015b\3\2\2\2\u015d?\3\2\2\2\u015e\u0162\7\61\2")
        buf.write("\2\u015f\u0161\5B\"\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0168\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0167\5> \2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3")
        buf.write("\2\2\2\u016b\u016c\7\62\2\2\u016cA\3\2\2\2\u016d\u016f")
        buf.write("\7\t\2\2\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0171\5\20\t\2\u0171\u0173\7=\2\2")
        buf.write("\u0172\u0174\5\16\b\2\u0173\u0172\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u017c\3\2\2\2\u0175\u0176\7\60\2\2\u0176")
        buf.write("\u0178\7=\2\2\u0177\u0179\5\16\b\2\u0178\u0177\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0175\3")
        buf.write("\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017f")
        buf.write("\u0180\7/\2\2\u0180C\3\2\2\2\u0181\u0182\5F$\2\u0182\u0183")
        buf.write("\7\5\2\2\u0183\u0184\5 \21\2\u0184\u0185\7/\2\2\u0185")
        buf.write("E\3\2\2\2\u0186\u018d\5\60\31\2\u0187\u0188\5\62\32\2")
        buf.write("\u0188\u0189\78\2\2\u0189\u018a\7=\2\2\u018a\u018d\3\2")
        buf.write("\2\2\u018b\u018d\7=\2\2\u018c\u0186\3\2\2\2\u018c\u0187")
        buf.write("\3\2\2\2\u018c\u018b\3\2\2\2\u018dG\3\2\2\2\u018e\u018f")
        buf.write("\7\20\2\2\u018f\u0190\5 \21\2\u0190\u0191\7\23\2\2\u0191")
        buf.write("\u0192\5> \2\u0192\u019b\3\2\2\2\u0193\u0194\7\20\2\2")
        buf.write("\u0194\u0195\5 \21\2\u0195\u0196\7\23\2\2\u0196\u0197")
        buf.write("\5> \2\u0197\u0198\7\16\2\2\u0198\u0199\5> \2\u0199\u019b")
        buf.write("\3\2\2\2\u019a\u018e\3\2\2\2\u019a\u0193\3\2\2\2\u019b")
        buf.write("I\3\2\2\2\u019c\u019d\7\24\2\2\u019d\u019e\7=\2\2\u019e")
        buf.write("\u019f\7\5\2\2\u019f\u01a0\5 \21\2\u01a0\u01a1\t\t\2\2")
        buf.write("\u01a1\u01a2\5 \21\2\u01a2\u01a3\7\r\2\2\u01a3\u01a4\5")
        buf.write("> \2\u01a4K\3\2\2\2\u01a5\u01a6\7\13\2\2\u01a6\u01a7\7")
        buf.write("/\2\2\u01a7M\3\2\2\2\u01a8\u01a9\7\f\2\2\u01a9\u01aa\7")
        buf.write("/\2\2\u01aaO\3\2\2\2\u01ab\u01ac\7\26\2\2\u01ac\u01ad")
        buf.write("\5 \21\2\u01ad\u01ae\7/\2\2\u01aeQ\3\2\2\2\u01af\u01b0")
        buf.write("\5\62\32\2\u01b0\u01b1\78\2\2\u01b1\u01b2\7=\2\2\u01b2")
        buf.write("\u01b4\7\63\2\2\u01b3\u01b5\5<\37\2\u01b4\u01b3\3\2\2")
        buf.write("\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7")
        buf.write("\7\64\2\2\u01b7\u01b8\7/\2\2\u01b8S\3\2\2\2/W`fmqty~\u0082")
        buf.write("\u008c\u0096\u00a2\u00a6\u00b1\u00b4\u00b9\u00c3\u00cc")
        buf.write("\u00d5\u00df\u00e6\u00ed\u00f7\u0102\u010d\u0113\u0118")
        buf.write("\u0120\u012d\u0130\u0132\u013a\u0140\u0148\u0151\u015c")
        buf.write("\u0162\u0168\u016e\u0173\u0178\u017c\u018c\u019a\u01b4")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "':='", "'class'", 
                     "'extends'", "'static'", "'final'", "'boolean'", "'break'", 
                     "'continue'", "'do'", "'else'", "'float'", "'if'", 
                     "'int'", "'string'", "'then'", "'for'", "'this'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'='", "'<'", "'>'", "'<='", "'>='", "'||'", 
                     "'&&'", "'!'", "'^'", "'new'", "';'", "','", "'{'", 
                     "'}'", "'('", "')'", "'['", "']'", "':'", "'.'" ]

    symbolicNames = [ "<INVALID>", "CMTLINE", "CMTBLOCK", "ASSIGN", "CLASS", 
                      "EXTENDS", "STATIC", "FINAL", "BOOLEAN", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "FLOAT", "IF", "INT", "STRING", 
                      "THEN", "FOR", "THIS", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
                      "FLDIV", "INTDIV", "MOD", "NEQ", "EQ", "EQQ", "LESS", 
                      "GREATER", "LEQ", "GEQ", "OR", "AND", "NOT", "CONCAT", 
                      "NEW", "SM", "CM", "LP", "RP", "LB", "RB", "LS", "RS", 
                      "CL", "DOT", "INTLIT", "FLOATLIT", "INFL", "STRINGLIT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDecl = 1
    RULE_member = 2
    RULE_atrbDecl = 3
    RULE_mutDecl = 4
    RULE_immutDecl = 5
    RULE_atrbInit = 6
    RULE_typ = 7
    RULE_arrayTyp = 8
    RULE_priTyp = 9
    RULE_classTyp = 10
    RULE_methodDecl = 11
    RULE_paraList = 12
    RULE_para = 13
    RULE_arrayLit = 14
    RULE_exp = 15
    RULE_equalee = 16
    RULE_andOree = 17
    RULE_addSubee = 18
    RULE_mulDivModee = 19
    RULE_conCatee = 20
    RULE_notee = 21
    RULE_subAddee = 22
    RULE_indexee = 23
    RULE_memAccessee = 24
    RULE_atom = 25
    RULE_newee = 26
    RULE_literal = 27
    RULE_booleanLit = 28
    RULE_argLits = 29
    RULE_stmt = 30
    RULE_blockStmt = 31
    RULE_nullAbleDeclList = 32
    RULE_asmStmt = 33
    RULE_lhs = 34
    RULE_ifStmt = 35
    RULE_forStmt = 36
    RULE_breakStmt = 37
    RULE_continueStmt = 38
    RULE_returnStmt = 39
    RULE_invokeStmt = 40

    ruleNames =  [ "program", "classDecl", "member", "atrbDecl", "mutDecl", 
                   "immutDecl", "atrbInit", "typ", "arrayTyp", "priTyp", 
                   "classTyp", "methodDecl", "paraList", "para", "arrayLit", 
                   "exp", "equalee", "andOree", "addSubee", "mulDivModee", 
                   "conCatee", "notee", "subAddee", "indexee", "memAccessee", 
                   "atom", "newee", "literal", "booleanLit", "argLits", 
                   "stmt", "blockStmt", "nullAbleDeclList", "asmStmt", "lhs", 
                   "ifStmt", "forStmt", "breakStmt", "continueStmt", "returnStmt", 
                   "invokeStmt" ]

    EOF = Token.EOF
    CMTLINE=1
    CMTBLOCK=2
    ASSIGN=3
    CLASS=4
    EXTENDS=5
    STATIC=6
    FINAL=7
    BOOLEAN=8
    BREAK=9
    CONTINUE=10
    DO=11
    ELSE=12
    FLOAT=13
    IF=14
    INT=15
    STRING=16
    THEN=17
    FOR=18
    THIS=19
    RETURN=20
    TRUE=21
    FALSE=22
    VOID=23
    NIL=24
    TO=25
    DOWNTO=26
    ADD=27
    SUB=28
    MUL=29
    FLDIV=30
    INTDIV=31
    MOD=32
    NEQ=33
    EQ=34
    EQQ=35
    LESS=36
    GREATER=37
    LEQ=38
    GEQ=39
    OR=40
    AND=41
    NOT=42
    CONCAT=43
    NEW=44
    SM=45
    CM=46
    LP=47
    RP=48
    LB=49
    RB=50
    LS=51
    RS=52
    CL=53
    DOT=54
    INTLIT=55
    FLOATLIT=56
    INFL=57
    STRINGLIT=58
    ID=59
    WS=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 82
                self.classDecl()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemberContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemberContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BKOOLParser.CLASS)
            self.state = 91
            self.match(BKOOLParser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 92
                self.match(BKOOLParser.EXTENDS)
                self.state = 93
                self.match(BKOOLParser.ID)


            self.state = 96
            self.match(BKOOLParser.LP)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 97
                self.member()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atrbDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AtrbDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.atrbDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtrbDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutDeclContext,0)


        def mutDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MutDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_atrbDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtrbDecl" ):
                return visitor.visitAtrbDecl(self)
            else:
                return visitor.visitChildren(self)




    def atrbDecl(self):

        localctx = BKOOLParser.AtrbDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atrbDecl)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.immutDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.mutDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def atrbInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AtrbInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AtrbInitContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutDecl" ):
                return visitor.visitMutDecl(self)
            else:
                return visitor.visitChildren(self)




    def mutDecl(self):

        localctx = BKOOLParser.MutDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mutDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 113
                self.match(BKOOLParser.STATIC)


            self.state = 116
            self.typ()
            self.state = 117
            self.match(BKOOLParser.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQQ:
                self.state = 118
                self.atrbInit()


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 121
                self.match(BKOOLParser.CM)
                self.state = 122
                self.match(BKOOLParser.ID)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQQ:
                    self.state = 123
                    self.atrbInit()


                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def atrbInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AtrbInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AtrbInitContext,i)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutDecl" ):
                return visitor.visitImmutDecl(self)
            else:
                return visitor.visitChildren(self)




    def immutDecl(self):

        localctx = BKOOLParser.ImmutDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 133
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 134
                self.match(BKOOLParser.FINAL)
                self.state = 135
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.state = 136
                self.match(BKOOLParser.STATIC)
                self.state = 137
                self.match(BKOOLParser.FINAL)
                pass


            self.state = 140
            self.typ()
            self.state = 141
            self.match(BKOOLParser.ID)
            self.state = 142
            self.atrbInit()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 143
                self.match(BKOOLParser.CM)
                self.state = 144
                self.match(BKOOLParser.ID)
                self.state = 145
                self.atrbInit()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtrbInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQQ(self):
            return self.getToken(BKOOLParser.EQQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_atrbInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtrbInit" ):
                return visitor.visitAtrbInit(self)
            else:
                return visitor.visitChildren(self)




    def atrbInit(self):

        localctx = BKOOLParser.AtrbInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atrbInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BKOOLParser.EQQ)
            self.state = 154
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def priTyp(self):
            return self.getTypedRuleContext(BKOOLParser.PriTypContext,0)


        def classTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ClassTypContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def arrayTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayTypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typ)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.priTyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.classTyp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(BKOOLParser.VOID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.arrayTyp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def priTyp(self):
            return self.getTypedRuleContext(BKOOLParser.PriTypContext,0)


        def classTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ClassTypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayTyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayTyp" ):
                return visitor.visitArrayTyp(self)
            else:
                return visitor.visitChildren(self)




    def arrayTyp(self):

        localctx = BKOOLParser.ArrayTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING]:
                self.state = 162
                self.priTyp()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 163
                self.classTyp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 166
            self.match(BKOOLParser.LS)
            self.state = 167
            self.match(BKOOLParser.INTLIT)
            self.state = 168
            self.match(BKOOLParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PriTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_priTyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriTyp" ):
                return visitor.visitPriTyp(self)
            else:
                return visitor.visitChildren(self)




    def priTyp(self):

        localctx = BKOOLParser.PriTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_priTyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classTyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassTyp" ):
                return visitor.visitClassTyp(self)
            else:
                return visitor.visitChildren(self)




    def classTyp(self):

        localctx = BKOOLParser.ClassTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_classTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def paraList(self):
            return self.getTypedRuleContext(BKOOLParser.ParaListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 174
                self.match(BKOOLParser.STATIC)


            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 177
                self.typ()


            self.state = 180
            self.match(BKOOLParser.ID)
            self.state = 181
            self.match(BKOOLParser.LB)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 182
                self.paraList()


            self.state = 185
            self.match(BKOOLParser.RB)
            self.state = 186
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParaContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParaContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SM)
            else:
                return self.getToken(BKOOLParser.SM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paraList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaList" ):
                return visitor.visitParaList(self)
            else:
                return visitor.visitChildren(self)




    def paraList(self):

        localctx = BKOOLParser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.para()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SM:
                self.state = 189
                self.match(BKOOLParser.SM)
                self.state = 190
                self.para()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = BKOOLParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.typ()
            self.state = 197
            self.match(BKOOLParser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 198
                self.match(BKOOLParser.CM)
                self.state = 199
                self.match(BKOOLParser.ID)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrayLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(BKOOLParser.LP)
            self.state = 206
            self.literal()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 207
                self.match(BKOOLParser.CM)
                self.state = 208
                self.literal()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalee(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.EqualeeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.EqualeeContext,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def LEQ(self):
            return self.getToken(BKOOLParser.LEQ, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def GEQ(self):
            return self.getToken(BKOOLParser.GEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.equalee()
                self.state = 217
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 218
                self.equalee()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.equalee()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andOree(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AndOreeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AndOreeContext,i)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equalee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualee" ):
                return visitor.visitEqualee(self)
            else:
                return visitor.visitChildren(self)




    def equalee(self):

        localctx = BKOOLParser.EqualeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_equalee)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.andOree()
                self.state = 224
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                self.andOree()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.andOree()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndOreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addSubee(self):
            return self.getTypedRuleContext(BKOOLParser.AddSubeeContext,0)


        def andOree(self):
            return self.getTypedRuleContext(BKOOLParser.AndOreeContext,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_andOree

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOree" ):
                return visitor.visitAndOree(self)
            else:
                return visitor.visitChildren(self)




    def andOree(self):

        localctx = BKOOLParser.AndOreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_andOree)
        self._la = 0 # Token type
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.addSubee(0)
                self.state = 231
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.andOree()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.addSubee(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddSubeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulDivModee(self):
            return self.getTypedRuleContext(BKOOLParser.MulDivModeeContext,0)


        def addSubee(self):
            return self.getTypedRuleContext(BKOOLParser.AddSubeeContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_addSubee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubee" ):
                return visitor.visitAddSubee(self)
            else:
                return visitor.visitChildren(self)



    def addSubee(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.AddSubeeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_addSubee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.mulDivModee(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.AddSubeeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addSubee)
                    self.state = 240
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 241
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 242
                    self.mulDivModee(0) 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulDivModeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conCatee(self):
            return self.getTypedRuleContext(BKOOLParser.ConCateeContext,0)


        def mulDivModee(self):
            return self.getTypedRuleContext(BKOOLParser.MulDivModeeContext,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def INTDIV(self):
            return self.getToken(BKOOLParser.INTDIV, 0)

        def FLDIV(self):
            return self.getToken(BKOOLParser.FLDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mulDivModee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivModee" ):
                return visitor.visitMulDivModee(self)
            else:
                return visitor.visitChildren(self)



    def mulDivModee(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.MulDivModeeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_mulDivModee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.conCatee(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.MulDivModeeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulDivModee)
                    self.state = 251
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 252
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 253
                    self.conCatee(0) 
                self.state = 258
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConCateeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notee(self):
            return self.getTypedRuleContext(BKOOLParser.NoteeContext,0)


        def conCatee(self):
            return self.getTypedRuleContext(BKOOLParser.ConCateeContext,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_conCatee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConCatee" ):
                return visitor.visitConCatee(self)
            else:
                return visitor.visitChildren(self)



    def conCatee(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ConCateeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_conCatee, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.notee()
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ConCateeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conCatee)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 263
                    self.match(BKOOLParser.CONCAT)
                    self.state = 264
                    self.notee() 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NoteeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notee(self):
            return self.getTypedRuleContext(BKOOLParser.NoteeContext,0)


        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def subAddee(self):
            return self.getTypedRuleContext(BKOOLParser.SubAddeeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_notee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotee" ):
                return visitor.visitNotee(self)
            else:
                return visitor.visitChildren(self)




    def notee(self):

        localctx = BKOOLParser.NoteeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_notee)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(BKOOLParser.NOT)
                self.state = 271
                self.notee()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NEW, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.subAddee()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubAddeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subAddee(self):
            return self.getTypedRuleContext(BKOOLParser.SubAddeeContext,0)


        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def indexee(self):
            return self.getTypedRuleContext(BKOOLParser.IndexeeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subAddee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubAddee" ):
                return visitor.visitSubAddee(self)
            else:
                return visitor.visitChildren(self)




    def subAddee(self):

        localctx = BKOOLParser.SubAddeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_subAddee)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 276
                self.subAddee()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.indexee()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memAccessee(self):
            return self.getTypedRuleContext(BKOOLParser.MemAccesseeContext,0)


        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_indexee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexee" ):
                return visitor.visitIndexee(self)
            else:
                return visitor.visitChildren(self)




    def indexee(self):

        localctx = BKOOLParser.IndexeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_indexee)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.memAccessee(0)
                self.state = 281
                self.match(BKOOLParser.LS)
                self.state = 282
                self.exp()
                self.state = 283
                self.match(BKOOLParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.memAccessee(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemAccesseeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BKOOLParser.AtomContext,0)


        def memAccessee(self):
            return self.getTypedRuleContext(BKOOLParser.MemAccesseeContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def argLits(self):
            return self.getTypedRuleContext(BKOOLParser.ArgLitsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memAccessee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemAccessee" ):
                return visitor.visitMemAccessee(self)
            else:
                return visitor.visitChildren(self)



    def memAccessee(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.MemAccesseeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_memAccessee, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 302
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.MemAccesseeContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_memAccessee)
                        self.state = 291
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 292
                        self.match(BKOOLParser.DOT)
                        self.state = 293
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.MemAccesseeContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_memAccessee)
                        self.state = 294
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 295
                        self.match(BKOOLParser.DOT)
                        self.state = 296
                        self.match(BKOOLParser.ID)
                        self.state = 297
                        self.match(BKOOLParser.LB)
                        self.state = 299
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 298
                            self.argLits()


                        self.state = 301
                        self.match(BKOOLParser.RB)
                        pass

             
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def newee(self):
            return self.getTypedRuleContext(BKOOLParser.NeweeContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BKOOLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_atom)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.literal()
                pass
            elif token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.newee()
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 311
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NeweeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def argLits(self):
            return self.getTypedRuleContext(BKOOLParser.ArgLitsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_newee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewee" ):
                return visitor.visitNewee(self)
            else:
                return visitor.visitChildren(self)




    def newee(self):

        localctx = BKOOLParser.NeweeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_newee)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(BKOOLParser.NEW)
            self.state = 315
            self.match(BKOOLParser.ID)
            self.state = 316
            self.match(BKOOLParser.LB)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 317
                self.argLits()


            self.state = 320
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def booleanLit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanLitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.booleanLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_booleanLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLit" ):
                return visitor.visitBooleanLit(self)
            else:
                return visitor.visitChildren(self)




    def booleanLit(self):

        localctx = BKOOLParser.BooleanLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_booleanLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_argLits

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLits" ):
                return visitor.visitArgLits(self)
            else:
                return visitor.visitChildren(self)




    def argLits(self):

        localctx = BKOOLParser.ArgLitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argLits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.exp()
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 331
                self.match(BKOOLParser.CM)
                self.state = 332
                self.exp()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def asmStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AsmStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def invokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvokeStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.asmStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 340
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 341
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 342
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 343
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 344
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 345
                self.invokeStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def nullAbleDeclList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.NullAbleDeclListContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.NullAbleDeclListContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKOOLParser.LP)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 349
                    self.nullAbleDeclList() 
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 355
                self.stmt()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 361
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullAbleDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def atrbInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AtrbInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AtrbInitContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_nullAbleDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullAbleDeclList" ):
                return visitor.visitNullAbleDeclList(self)
            else:
                return visitor.visitChildren(self)




    def nullAbleDeclList(self):

        localctx = BKOOLParser.NullAbleDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_nullAbleDeclList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 363
                self.match(BKOOLParser.FINAL)


            self.state = 366
            self.typ()
            self.state = 367
            self.match(BKOOLParser.ID)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQQ:
                self.state = 368
                self.atrbInit()


            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 371
                self.match(BKOOLParser.CM)
                self.state = 372
                self.match(BKOOLParser.ID)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQQ:
                    self.state = 373
                    self.atrbInit()


                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 381
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_asmStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsmStmt" ):
                return visitor.visitAsmStmt(self)
            else:
                return visitor.visitChildren(self)




    def asmStmt(self):

        localctx = BKOOLParser.AsmStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_asmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.lhs()
            self.state = 384
            self.match(BKOOLParser.ASSIGN)
            self.state = 385
            self.exp()
            self.state = 386
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexee(self):
            return self.getTypedRuleContext(BKOOLParser.IndexeeContext,0)


        def memAccessee(self):
            return self.getTypedRuleContext(BKOOLParser.MemAccesseeContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_lhs)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.indexee()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.memAccessee(0)
                self.state = 390
                self.match(BKOOLParser.DOT)
                self.state = 391
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStmt)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(BKOOLParser.IF)
                self.state = 397
                self.exp()
                self.state = 398
                self.match(BKOOLParser.THEN)
                self.state = 399
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(BKOOLParser.IF)
                self.state = 402
                self.exp()
                self.state = 403
                self.match(BKOOLParser.THEN)
                self.state = 404
                self.stmt()
                self.state = 405
                self.match(BKOOLParser.ELSE)
                self.state = 406
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(BKOOLParser.FOR)
            self.state = 411
            self.match(BKOOLParser.ID)
            self.state = 412
            self.match(BKOOLParser.ASSIGN)
            self.state = 413
            self.exp()
            self.state = 414
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 415
            self.exp()
            self.state = 416
            self.match(BKOOLParser.DO)
            self.state = 417
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(BKOOLParser.BREAK)
            self.state = 420
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(BKOOLParser.CONTINUE)
            self.state = 423
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(BKOOLParser.RETURN)
            self.state = 426
            self.exp()
            self.state = 427
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memAccessee(self):
            return self.getTypedRuleContext(BKOOLParser.MemAccesseeContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def argLits(self):
            return self.getTypedRuleContext(BKOOLParser.ArgLitsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invokeStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvokeStmt" ):
                return visitor.visitInvokeStmt(self)
            else:
                return visitor.visitChildren(self)




    def invokeStmt(self):

        localctx = BKOOLParser.InvokeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_invokeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.memAccessee(0)
            self.state = 430
            self.match(BKOOLParser.DOT)
            self.state = 431
            self.match(BKOOLParser.ID)
            self.state = 432
            self.match(BKOOLParser.LB)
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 433
                self.argLits()


            self.state = 436
            self.match(BKOOLParser.RB)
            self.state = 437
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.addSubee_sempred
        self._predicates[19] = self.mulDivModee_sempred
        self._predicates[20] = self.conCatee_sempred
        self._predicates[24] = self.memAccessee_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def addSubee_sempred(self, localctx:AddSubeeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def mulDivModee_sempred(self, localctx:MulDivModeeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def conCatee_sempred(self, localctx:ConCateeContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def memAccessee_sempred(self, localctx:MemAccesseeContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




