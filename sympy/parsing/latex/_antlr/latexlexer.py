
# encoding: utf-8

# *** GENERATED BY `setup.py antlr`, DO NOT EDIT BY HAND ***
#
# Generated from ../LaTeX.g4, derived from latex2sympy
#     latex2sympy is licensed under the MIT license
#     https://github.com/augustt198/latex2sympy/blob/master/LICENSE.txt
#
# Generated with antlr4
#    antlr4 is licensed under the BSD-3-Clause License
#    https://github.com/antlr/antlr4/blob/master/LICENSE.txt
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"K\u02af\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\t")
        buf.write(u"J\4K\tK\4L\tL\3\2\3\2\3\3\6\3\u009d\n\3\r\3\16\3\u009e")
        buf.write(u"\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\5\4\u00af\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\5\5\u00be\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00cf\n")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00f3\n\t\3\t")
        buf.write(u"\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write(u"\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write(u"\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3")
        buf.write(u"\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write(u"\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0180\n")
        buf.write(u"\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write(u"!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write(u"$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*")
        buf.write(u"\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write(u",\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3")
        buf.write(u"\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write(u"\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3")
        buf.write(u"\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\3")
        buf.write(u"9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;")
        buf.write(u"\3;\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write(u">\3>\3?\3?\3@\3@\3A\3A\3B\3B\7B\u025f\nB\fB\16B\u0262")
        buf.write(u"\13B\3B\3B\3B\6B\u0267\nB\rB\16B\u0268\5B\u026b\nB\3")
        buf.write(u"C\3C\3D\3D\3E\6E\u0272\nE\rE\16E\u0273\3E\3E\3E\3E\3")
        buf.write(u"E\7E\u027b\nE\fE\16E\u027e\13E\3E\7E\u0281\nE\fE\16E")
        buf.write(u"\u0284\13E\3E\3E\3E\3E\3E\7E\u028b\nE\fE\16E\u028e\13")
        buf.write(u"E\3E\3E\6E\u0292\nE\rE\16E\u0293\5E\u0296\nE\3F\3F\3")
        buf.write(u"G\3G\3H\3H\3H\3H\3H\3I\3I\3J\3J\3J\3J\3J\3K\3K\3L\3L")
        buf.write(u"\6L\u02ac\nL\rL\16L\u02ad\3\u0260\2M\3\3\5\4\7\5\t\6")
        buf.write(u"\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write(u"\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write(u"\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]")
        buf.write(u"\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write(u"A\u0081\2\u0083B\u0085C\u0087\2\u0089D\u008bE\u008dF")
        buf.write(u"\u008fG\u0091H\u0093I\u0095J\u0097K\3\2\5\5\2\13\f\17")
        buf.write(u"\17\"\"\4\2C\\c|\3\2\62;\2\u02bf\2\3\3\2\2\2\2\5\3\2")
        buf.write(u"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write(u"\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write(u"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write(u"\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write(u"\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write(u"\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write(u"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write(u"\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write(u"\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write(u"\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write(u"\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write(u"i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write(u"\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write(u"\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3")
        buf.write(u"\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write(u"\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2")
        buf.write(u"\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009c")
        buf.write(u"\3\2\2\2\7\u00ae\3\2\2\2\t\u00bd\3\2\2\2\13\u00ce\3\2")
        buf.write(u"\2\2\r\u00d2\3\2\2\2\17\u00da\3\2\2\2\21\u00f2\3\2\2")
        buf.write(u"\2\23\u00f6\3\2\2\2\25\u0105\3\2\2\2\27\u0116\3\2\2\2")
        buf.write(u"\31\u0118\3\2\2\2\33\u011a\3\2\2\2\35\u011c\3\2\2\2\37")
        buf.write(u"\u011e\3\2\2\2!\u0120\3\2\2\2#\u0122\3\2\2\2%\u0124\3")
        buf.write(u"\2\2\2\'\u0126\3\2\2\2)\u0129\3\2\2\2+\u012c\3\2\2\2")
        buf.write(u"-\u012e\3\2\2\2/\u0130\3\2\2\2\61\u0138\3\2\2\2\63\u0141")
        buf.write(u"\3\2\2\2\65\u0143\3\2\2\2\67\u017f\3\2\2\29\u0181\3\2")
        buf.write(u"\2\2;\u0186\3\2\2\2=\u018b\3\2\2\2?\u0191\3\2\2\2A\u0196")
        buf.write(u"\3\2\2\2C\u019b\3\2\2\2E\u019f\3\2\2\2G\u01a4\3\2\2\2")
        buf.write(u"I\u01a9\3\2\2\2K\u01ae\3\2\2\2M\u01b3\3\2\2\2O\u01b8")
        buf.write(u"\3\2\2\2Q\u01bd\3\2\2\2S\u01c5\3\2\2\2U\u01cd\3\2\2\2")
        buf.write(u"W\u01d5\3\2\2\2Y\u01dd\3\2\2\2[\u01e5\3\2\2\2]\u01ed")
        buf.write(u"\3\2\2\2_\u01f3\3\2\2\2a\u01f9\3\2\2\2c\u01ff\3\2\2\2")
        buf.write(u"e\u0207\3\2\2\2g\u020f\3\2\2\2i\u0217\3\2\2\2k\u021d")
        buf.write(u"\3\2\2\2m\u0224\3\2\2\2o\u022a\3\2\2\2q\u022f\3\2\2\2")
        buf.write(u"s\u0235\3\2\2\2u\u023c\3\2\2\2w\u0244\3\2\2\2y\u024c")
        buf.write(u"\3\2\2\2{\u0254\3\2\2\2}\u0256\3\2\2\2\177\u0258\3\2")
        buf.write(u"\2\2\u0081\u025a\3\2\2\2\u0083\u025c\3\2\2\2\u0085\u026c")
        buf.write(u"\3\2\2\2\u0087\u026e\3\2\2\2\u0089\u0295\3\2\2\2\u008b")
        buf.write(u"\u0297\3\2\2\2\u008d\u0299\3\2\2\2\u008f\u029b\3\2\2")
        buf.write(u"\2\u0091\u02a0\3\2\2\2\u0093\u02a2\3\2\2\2\u0095\u02a7")
        buf.write(u"\3\2\2\2\u0097\u02a9\3\2\2\2\u0099\u009a\7.\2\2\u009a")
        buf.write(u"\4\3\2\2\2\u009b\u009d\t\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write(u"\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2")
        buf.write(u"\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\b\3\2\2\u00a1\6\3")
        buf.write(u"\2\2\2\u00a2\u00a3\7^\2\2\u00a3\u00af\7.\2\2\u00a4\u00a5")
        buf.write(u"\7^\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7j\2\2\u00a7\u00a8")
        buf.write(u"\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab")
        buf.write(u"\7r\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7e\2\2\u00ad\u00af")
        buf.write(u"\7g\2\2\u00ae\u00a2\3\2\2\2\u00ae\u00a4\3\2\2\2\u00af")
        buf.write(u"\u00b0\3\2\2\2\u00b0\u00b1\b\4\2\2\u00b1\b\3\2\2\2\u00b2")
        buf.write(u"\u00b3\7^\2\2\u00b3\u00be\7<\2\2\u00b4\u00b5\7^\2\2\u00b5")
        buf.write(u"\u00b6\7o\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7f\2\2\u00b8")
        buf.write(u"\u00b9\7u\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7c\2\2\u00bb")
        buf.write(u"\u00bc\7e\2\2\u00bc\u00be\7g\2\2\u00bd\u00b2\3\2\2\2")
        buf.write(u"\u00bd\u00b4\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0")
        buf.write(u"\b\5\2\2\u00c0\n\3\2\2\2\u00c1\u00c2\7^\2\2\u00c2\u00cf")
        buf.write(u"\7=\2\2\u00c3\u00c4\7^\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write(u"\7j\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9")
        buf.write(u"\7m\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7r\2\2\u00cb\u00cc")
        buf.write(u"\7c\2\2\u00cc\u00cd\7e\2\2\u00cd\u00cf\7g\2\2\u00ce\u00c1")
        buf.write(u"\3\2\2\2\u00ce\u00c3\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write(u"\u00d1\b\6\2\2\u00d1\f\3\2\2\2\u00d2\u00d3\7^\2\2\u00d3")
        buf.write(u"\u00d4\7s\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7c\2\2\u00d6")
        buf.write(u"\u00d7\7f\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\b\7\2\2")
        buf.write(u"\u00d9\16\3\2\2\2\u00da\u00db\7^\2\2\u00db\u00dc\7s\2")
        buf.write(u"\2\u00dc\u00dd\7s\2\2\u00dd\u00de\7w\2\2\u00de\u00df")
        buf.write(u"\7c\2\2\u00df\u00e0\7f\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write(u"\u00e2\b\b\2\2\u00e2\20\3\2\2\2\u00e3\u00e4\7^\2\2\u00e4")
        buf.write(u"\u00f3\7#\2\2\u00e5\u00e6\7^\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write(u"\u00e8\7g\2\2\u00e8\u00e9\7i\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write(u"\u00eb\7j\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write(u"\u00ee\7u\2\2\u00ee\u00ef\7r\2\2\u00ef\u00f0\7c\2\2\u00f0")
        buf.write(u"\u00f1\7e\2\2\u00f1\u00f3\7g\2\2\u00f2\u00e3\3\2\2\2")
        buf.write(u"\u00f2\u00e5\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5")
        buf.write(u"\b\t\2\2\u00f5\22\3\2\2\2\u00f6\u00f7\7^\2\2\u00f7\u00f8")
        buf.write(u"\7p\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7i\2\2\u00fa\u00fb")
        buf.write(u"\7o\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7f\2\2\u00fd\u00fe")
        buf.write(u"\7u\2\2\u00fe\u00ff\7r\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write(u"\7e\2\2\u0101\u0102\7g\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write(u"\u0104\b\n\2\2\u0104\24\3\2\2\2\u0105\u0106\7^\2\2\u0106")
        buf.write(u"\u0107\7p\2\2\u0107\u0108\7g\2\2\u0108\u0109\7i\2\2\u0109")
        buf.write(u"\u010a\7v\2\2\u010a\u010b\7j\2\2\u010b\u010c\7k\2\2\u010c")
        buf.write(u"\u010d\7e\2\2\u010d\u010e\7m\2\2\u010e\u010f\7u\2\2\u010f")
        buf.write(u"\u0110\7r\2\2\u0110\u0111\7c\2\2\u0111\u0112\7e\2\2\u0112")
        buf.write(u"\u0113\7g\2\2\u0113\u0114\3\2\2\2\u0114\u0115\b\13\2")
        buf.write(u"\2\u0115\26\3\2\2\2\u0116\u0117\7-\2\2\u0117\30\3\2\2")
        buf.write(u"\2\u0118\u0119\7/\2\2\u0119\32\3\2\2\2\u011a\u011b\7")
        buf.write(u",\2\2\u011b\34\3\2\2\2\u011c\u011d\7\61\2\2\u011d\36")
        buf.write(u"\3\2\2\2\u011e\u011f\7*\2\2\u011f \3\2\2\2\u0120\u0121")
        buf.write(u"\7+\2\2\u0121\"\3\2\2\2\u0122\u0123\7}\2\2\u0123$\3\2")
        buf.write(u"\2\2\u0124\u0125\7\177\2\2\u0125&\3\2\2\2\u0126\u0127")
        buf.write(u"\7^\2\2\u0127\u0128\7}\2\2\u0128(\3\2\2\2\u0129\u012a")
        buf.write(u"\7^\2\2\u012a\u012b\7\177\2\2\u012b*\3\2\2\2\u012c\u012d")
        buf.write(u"\7]\2\2\u012d,\3\2\2\2\u012e\u012f\7_\2\2\u012f.\3\2")
        buf.write(u"\2\2\u0130\u0131\7^\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write(u"\7g\2\2\u0133\u0134\7h\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write(u"\3\2\2\2\u0136\u0137\b\30\2\2\u0137\60\3\2\2\2\u0138")
        buf.write(u"\u0139\7^\2\2\u0139\u013a\7t\2\2\u013a\u013b\7k\2\2\u013b")
        buf.write(u"\u013c\7i\2\2\u013c\u013d\7j\2\2\u013d\u013e\7v\2\2\u013e")
        buf.write(u"\u013f\3\2\2\2\u013f\u0140\b\31\2\2\u0140\62\3\2\2\2")
        buf.write(u"\u0141\u0142\7~\2\2\u0142\64\3\2\2\2\u0143\u0144\7^\2")
        buf.write(u"\2\u0144\u0145\7n\2\2\u0145\u0146\7k\2\2\u0146\u0147")
        buf.write(u"\7o\2\2\u0147\66\3\2\2\2\u0148\u0149\7^\2\2\u0149\u014a")
        buf.write(u"\7v\2\2\u014a\u0180\7q\2\2\u014b\u014c\7^\2\2\u014c\u014d")
        buf.write(u"\7t\2\2\u014d\u014e\7k\2\2\u014e\u014f\7i\2\2\u014f\u0150")
        buf.write(u"\7j\2\2\u0150\u0151\7v\2\2\u0151\u0152\7c\2\2\u0152\u0153")
        buf.write(u"\7t\2\2\u0153\u0154\7t\2\2\u0154\u0155\7q\2\2\u0155\u0180")
        buf.write(u"\7y\2\2\u0156\u0157\7^\2\2\u0157\u0158\7T\2\2\u0158\u0159")
        buf.write(u"\7k\2\2\u0159\u015a\7i\2\2\u015a\u015b\7j\2\2\u015b\u015c")
        buf.write(u"\7v\2\2\u015c\u015d\7c\2\2\u015d\u015e\7t\2\2\u015e\u015f")
        buf.write(u"\7t\2\2\u015f\u0160\7q\2\2\u0160\u0180\7y\2\2\u0161\u0162")
        buf.write(u"\7^\2\2\u0162\u0163\7n\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write(u"\7p\2\2\u0165\u0166\7i\2\2\u0166\u0167\7t\2\2\u0167\u0168")
        buf.write(u"\7k\2\2\u0168\u0169\7i\2\2\u0169\u016a\7j\2\2\u016a\u016b")
        buf.write(u"\7v\2\2\u016b\u016c\7c\2\2\u016c\u016d\7t\2\2\u016d\u016e")
        buf.write(u"\7t\2\2\u016e\u016f\7q\2\2\u016f\u0180\7y\2\2\u0170\u0171")
        buf.write(u"\7^\2\2\u0171\u0172\7N\2\2\u0172\u0173\7q\2\2\u0173\u0174")
        buf.write(u"\7p\2\2\u0174\u0175\7i\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write(u"\7k\2\2\u0177\u0178\7i\2\2\u0178\u0179\7j\2\2\u0179\u017a")
        buf.write(u"\7v\2\2\u017a\u017b\7c\2\2\u017b\u017c\7t\2\2\u017c\u017d")
        buf.write(u"\7t\2\2\u017d\u017e\7q\2\2\u017e\u0180\7y\2\2\u017f\u0148")
        buf.write(u"\3\2\2\2\u017f\u014b\3\2\2\2\u017f\u0156\3\2\2\2\u017f")
        buf.write(u"\u0161\3\2\2\2\u017f\u0170\3\2\2\2\u01808\3\2\2\2\u0181")
        buf.write(u"\u0182\7^\2\2\u0182\u0183\7k\2\2\u0183\u0184\7p\2\2\u0184")
        buf.write(u"\u0185\7v\2\2\u0185:\3\2\2\2\u0186\u0187\7^\2\2\u0187")
        buf.write(u"\u0188\7u\2\2\u0188\u0189\7w\2\2\u0189\u018a\7o\2\2\u018a")
        buf.write(u"<\3\2\2\2\u018b\u018c\7^\2\2\u018c\u018d\7r\2\2\u018d")
        buf.write(u"\u018e\7t\2\2\u018e\u018f\7q\2\2\u018f\u0190\7f\2\2\u0190")
        buf.write(u">\3\2\2\2\u0191\u0192\7^\2\2\u0192\u0193\7g\2\2\u0193")
        buf.write(u"\u0194\7z\2\2\u0194\u0195\7r\2\2\u0195@\3\2\2\2\u0196")
        buf.write(u"\u0197\7^\2\2\u0197\u0198\7n\2\2\u0198\u0199\7q\2\2\u0199")
        buf.write(u"\u019a\7i\2\2\u019aB\3\2\2\2\u019b\u019c\7^\2\2\u019c")
        buf.write(u"\u019d\7n\2\2\u019d\u019e\7p\2\2\u019eD\3\2\2\2\u019f")
        buf.write(u"\u01a0\7^\2\2\u01a0\u01a1\7u\2\2\u01a1\u01a2\7k\2\2\u01a2")
        buf.write(u"\u01a3\7p\2\2\u01a3F\3\2\2\2\u01a4\u01a5\7^\2\2\u01a5")
        buf.write(u"\u01a6\7e\2\2\u01a6\u01a7\7q\2\2\u01a7\u01a8\7u\2\2\u01a8")
        buf.write(u"H\3\2\2\2\u01a9\u01aa\7^\2\2\u01aa\u01ab\7v\2\2\u01ab")
        buf.write(u"\u01ac\7c\2\2\u01ac\u01ad\7p\2\2\u01adJ\3\2\2\2\u01ae")
        buf.write(u"\u01af\7^\2\2\u01af\u01b0\7e\2\2\u01b0\u01b1\7u\2\2\u01b1")
        buf.write(u"\u01b2\7e\2\2\u01b2L\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4")
        buf.write(u"\u01b5\7u\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7\7e\2\2\u01b7")
        buf.write(u"N\3\2\2\2\u01b8\u01b9\7^\2\2\u01b9\u01ba\7e\2\2\u01ba")
        buf.write(u"\u01bb\7q\2\2\u01bb\u01bc\7v\2\2\u01bcP\3\2\2\2\u01bd")
        buf.write(u"\u01be\7^\2\2\u01be\u01bf\7c\2\2\u01bf\u01c0\7t\2\2\u01c0")
        buf.write(u"\u01c1\7e\2\2\u01c1\u01c2\7u\2\2\u01c2\u01c3\7k\2\2\u01c3")
        buf.write(u"\u01c4\7p\2\2\u01c4R\3\2\2\2\u01c5\u01c6\7^\2\2\u01c6")
        buf.write(u"\u01c7\7c\2\2\u01c7\u01c8\7t\2\2\u01c8\u01c9\7e\2\2\u01c9")
        buf.write(u"\u01ca\7e\2\2\u01ca\u01cb\7q\2\2\u01cb\u01cc\7u\2\2\u01cc")
        buf.write(u"T\3\2\2\2\u01cd\u01ce\7^\2\2\u01ce\u01cf\7c\2\2\u01cf")
        buf.write(u"\u01d0\7t\2\2\u01d0\u01d1\7e\2\2\u01d1\u01d2\7v\2\2\u01d2")
        buf.write(u"\u01d3\7c\2\2\u01d3\u01d4\7p\2\2\u01d4V\3\2\2\2\u01d5")
        buf.write(u"\u01d6\7^\2\2\u01d6\u01d7\7c\2\2\u01d7\u01d8\7t\2\2\u01d8")
        buf.write(u"\u01d9\7e\2\2\u01d9\u01da\7e\2\2\u01da\u01db\7u\2\2\u01db")
        buf.write(u"\u01dc\7e\2\2\u01dcX\3\2\2\2\u01dd\u01de\7^\2\2\u01de")
        buf.write(u"\u01df\7c\2\2\u01df\u01e0\7t\2\2\u01e0\u01e1\7e\2\2\u01e1")
        buf.write(u"\u01e2\7u\2\2\u01e2\u01e3\7g\2\2\u01e3\u01e4\7e\2\2\u01e4")
        buf.write(u"Z\3\2\2\2\u01e5\u01e6\7^\2\2\u01e6\u01e7\7c\2\2\u01e7")
        buf.write(u"\u01e8\7t\2\2\u01e8\u01e9\7e\2\2\u01e9\u01ea\7e\2\2\u01ea")
        buf.write(u"\u01eb\7q\2\2\u01eb\u01ec\7v\2\2\u01ec\\\3\2\2\2\u01ed")
        buf.write(u"\u01ee\7^\2\2\u01ee\u01ef\7u\2\2\u01ef\u01f0\7k\2\2\u01f0")
        buf.write(u"\u01f1\7p\2\2\u01f1\u01f2\7j\2\2\u01f2^\3\2\2\2\u01f3")
        buf.write(u"\u01f4\7^\2\2\u01f4\u01f5\7e\2\2\u01f5\u01f6\7q\2\2\u01f6")
        buf.write(u"\u01f7\7u\2\2\u01f7\u01f8\7j\2\2\u01f8`\3\2\2\2\u01f9")
        buf.write(u"\u01fa\7^\2\2\u01fa\u01fb\7v\2\2\u01fb\u01fc\7c\2\2\u01fc")
        buf.write(u"\u01fd\7p\2\2\u01fd\u01fe\7j\2\2\u01feb\3\2\2\2\u01ff")
        buf.write(u"\u0200\7^\2\2\u0200\u0201\7c\2\2\u0201\u0202\7t\2\2\u0202")
        buf.write(u"\u0203\7u\2\2\u0203\u0204\7k\2\2\u0204\u0205\7p\2\2\u0205")
        buf.write(u"\u0206\7j\2\2\u0206d\3\2\2\2\u0207\u0208\7^\2\2\u0208")
        buf.write(u"\u0209\7c\2\2\u0209\u020a\7t\2\2\u020a\u020b\7e\2\2\u020b")
        buf.write(u"\u020c\7q\2\2\u020c\u020d\7u\2\2\u020d\u020e\7j\2\2\u020e")
        buf.write(u"f\3\2\2\2\u020f\u0210\7^\2\2\u0210\u0211\7c\2\2\u0211")
        buf.write(u"\u0212\7t\2\2\u0212\u0213\7v\2\2\u0213\u0214\7c\2\2\u0214")
        buf.write(u"\u0215\7p\2\2\u0215\u0216\7j\2\2\u0216h\3\2\2\2\u0217")
        buf.write(u"\u0218\7^\2\2\u0218\u0219\7u\2\2\u0219\u021a\7s\2\2\u021a")
        buf.write(u"\u021b\7t\2\2\u021b\u021c\7v\2\2\u021cj\3\2\2\2\u021d")
        buf.write(u"\u021e\7^\2\2\u021e\u021f\7v\2\2\u021f\u0220\7k\2\2\u0220")
        buf.write(u"\u0221\7o\2\2\u0221\u0222\7g\2\2\u0222\u0223\7u\2\2\u0223")
        buf.write(u"l\3\2\2\2\u0224\u0225\7^\2\2\u0225\u0226\7e\2\2\u0226")
        buf.write(u"\u0227\7f\2\2\u0227\u0228\7q\2\2\u0228\u0229\7v\2\2\u0229")
        buf.write(u"n\3\2\2\2\u022a\u022b\7^\2\2\u022b\u022c\7f\2\2\u022c")
        buf.write(u"\u022d\7k\2\2\u022d\u022e\7x\2\2\u022ep\3\2\2\2\u022f")
        buf.write(u"\u0230\7^\2\2\u0230\u0231\7h\2\2\u0231\u0232\7t\2\2\u0232")
        buf.write(u"\u0233\7c\2\2\u0233\u0234\7e\2\2\u0234r\3\2\2\2\u0235")
        buf.write(u"\u0236\7^\2\2\u0236\u0237\7d\2\2\u0237\u0238\7k\2\2\u0238")
        buf.write(u"\u0239\7p\2\2\u0239\u023a\7q\2\2\u023a\u023b\7o\2\2\u023b")
        buf.write(u"t\3\2\2\2\u023c\u023d\7^\2\2\u023d\u023e\7f\2\2\u023e")
        buf.write(u"\u023f\7d\2\2\u023f\u0240\7k\2\2\u0240\u0241\7p\2\2\u0241")
        buf.write(u"\u0242\7q\2\2\u0242\u0243\7o\2\2\u0243v\3\2\2\2\u0244")
        buf.write(u"\u0245\7^\2\2\u0245\u0246\7v\2\2\u0246\u0247\7d\2\2\u0247")
        buf.write(u"\u0248\7k\2\2\u0248\u0249\7p\2\2\u0249\u024a\7q\2\2\u024a")
        buf.write(u"\u024b\7o\2\2\u024bx\3\2\2\2\u024c\u024d\7^\2\2\u024d")
        buf.write(u"\u024e\7o\2\2\u024e\u024f\7c\2\2\u024f\u0250\7v\2\2\u0250")
        buf.write(u"\u0251\7j\2\2\u0251\u0252\7k\2\2\u0252\u0253\7v\2\2\u0253")
        buf.write(u"z\3\2\2\2\u0254\u0255\7a\2\2\u0255|\3\2\2\2\u0256\u0257")
        buf.write(u"\7`\2\2\u0257~\3\2\2\2\u0258\u0259\7<\2\2\u0259\u0080")
        buf.write(u"\3\2\2\2\u025a\u025b\t\2\2\2\u025b\u0082\3\2\2\2\u025c")
        buf.write(u"\u0260\7f\2\2\u025d\u025f\5\u0081A\2\u025e\u025d\3\2")
        buf.write(u"\2\2\u025f\u0262\3\2\2\2\u0260\u0261\3\2\2\2\u0260\u025e")
        buf.write(u"\3\2\2\2\u0261\u026a\3\2\2\2\u0262\u0260\3\2\2\2\u0263")
        buf.write(u"\u026b\t\3\2\2\u0264\u0266\7^\2\2\u0265\u0267\t\3\2\2")
        buf.write(u"\u0266\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u0266")
        buf.write(u"\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026b\3\2\2\2\u026a")
        buf.write(u"\u0263\3\2\2\2\u026a\u0264\3\2\2\2\u026b\u0084\3\2\2")
        buf.write(u"\2\u026c\u026d\t\3\2\2\u026d\u0086\3\2\2\2\u026e\u026f")
        buf.write(u"\t\4\2\2\u026f\u0088\3\2\2\2\u0270\u0272\5\u0087D\2\u0271")
        buf.write(u"\u0270\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0271\3\2\2")
        buf.write(u"\2\u0273\u0274\3\2\2\2\u0274\u027c\3\2\2\2\u0275\u0276")
        buf.write(u"\7.\2\2\u0276\u0277\5\u0087D\2\u0277\u0278\5\u0087D\2")
        buf.write(u"\u0278\u0279\5\u0087D\2\u0279\u027b\3\2\2\2\u027a\u0275")
        buf.write(u"\3\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2\u027c")
        buf.write(u"\u027d\3\2\2\2\u027d\u0296\3\2\2\2\u027e\u027c\3\2\2")
        buf.write(u"\2\u027f\u0281\5\u0087D\2\u0280\u027f\3\2\2\2\u0281\u0284")
        buf.write(u"\3\2\2\2\u0282\u0280\3\2\2\2\u0282\u0283\3\2\2\2\u0283")
        buf.write(u"\u028c\3\2\2\2\u0284\u0282\3\2\2\2\u0285\u0286\7.\2\2")
        buf.write(u"\u0286\u0287\5\u0087D\2\u0287\u0288\5\u0087D\2\u0288")
        buf.write(u"\u0289\5\u0087D\2\u0289\u028b\3\2\2\2\u028a\u0285\3\2")
        buf.write(u"\2\2\u028b\u028e\3\2\2\2\u028c\u028a\3\2\2\2\u028c\u028d")
        buf.write(u"\3\2\2\2\u028d\u028f\3\2\2\2\u028e\u028c\3\2\2\2\u028f")
        buf.write(u"\u0291\7\60\2\2\u0290\u0292\5\u0087D\2\u0291\u0290\3")
        buf.write(u"\2\2\2\u0292\u0293\3\2\2\2\u0293\u0291\3\2\2\2\u0293")
        buf.write(u"\u0294\3\2\2\2\u0294\u0296\3\2\2\2\u0295\u0271\3\2\2")
        buf.write(u"\2\u0295\u0282\3\2\2\2\u0296\u008a\3\2\2\2\u0297\u0298")
        buf.write(u"\7?\2\2\u0298\u008c\3\2\2\2\u0299\u029a\7>\2\2\u029a")
        buf.write(u"\u008e\3\2\2\2\u029b\u029c\7^\2\2\u029c\u029d\7n\2\2")
        buf.write(u"\u029d\u029e\7g\2\2\u029e\u029f\7s\2\2\u029f\u0090\3")
        buf.write(u"\2\2\2\u02a0\u02a1\7@\2\2\u02a1\u0092\3\2\2\2\u02a2\u02a3")
        buf.write(u"\7^\2\2\u02a3\u02a4\7i\2\2\u02a4\u02a5\7g\2\2\u02a5\u02a6")
        buf.write(u"\7s\2\2\u02a6\u0094\3\2\2\2\u02a7\u02a8\7#\2\2\u02a8")
        buf.write(u"\u0096\3\2\2\2\u02a9\u02ab\7^\2\2\u02aa\u02ac\t\3\2\2")
        buf.write(u"\u02ab\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ab")
        buf.write(u"\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u0098\3\2\2\2\23\2")
        buf.write(u"\u009e\u00ae\u00bd\u00ce\u00f2\u017f\u0260\u0268\u026a")
        buf.write(u"\u0273\u027c\u0282\u028c\u0293\u0295\u02ad\3\b\2\2")
        return buf.getvalue()


class LaTeXLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    THINSPACE = 3
    MEDSPACE = 4
    THICKSPACE = 5
    QUAD = 6
    QQUAD = 7
    NEGTHINSPACE = 8
    NEGMEDSPACE = 9
    NEGTHICKSPACE = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    L_PAREN = 15
    R_PAREN = 16
    L_BRACE = 17
    R_BRACE = 18
    L_BRACE_LITERAL = 19
    R_BRACE_LITERAL = 20
    L_BRACKET = 21
    R_BRACKET = 22
    CMD_LEFT = 23
    CMD_RIGHT = 24
    BAR = 25
    FUNC_LIM = 26
    LIM_APPROACH_SYM = 27
    FUNC_INT = 28
    FUNC_SUM = 29
    FUNC_PROD = 30
    FUNC_EXP = 31
    FUNC_LOG = 32
    FUNC_LN = 33
    FUNC_SIN = 34
    FUNC_COS = 35
    FUNC_TAN = 36
    FUNC_CSC = 37
    FUNC_SEC = 38
    FUNC_COT = 39
    FUNC_ARCSIN = 40
    FUNC_ARCCOS = 41
    FUNC_ARCTAN = 42
    FUNC_ARCCSC = 43
    FUNC_ARCSEC = 44
    FUNC_ARCCOT = 45
    FUNC_SINH = 46
    FUNC_COSH = 47
    FUNC_TANH = 48
    FUNC_ARSINH = 49
    FUNC_ARCOSH = 50
    FUNC_ARTANH = 51
    FUNC_SQRT = 52
    CMD_TIMES = 53
    CMD_CDOT = 54
    CMD_DIV = 55
    CMD_FRAC = 56
    CMD_BINOM = 57
    CMD_DBINOM = 58
    CMD_TBINOM = 59
    CMD_MATHIT = 60
    UNDERSCORE = 61
    CARET = 62
    COLON = 63
    DIFFERENTIAL = 64
    LETTER = 65
    NUMBER = 66
    EQUAL = 67
    LT = 68
    LTE = 69
    GT = 70
    GTE = 71
    BANG = 72
    SYMBOL = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'\\quad'", u"'\\qquad'", u"'\\negmedspace'", u"'\\negthickspace'",
            u"'+'", u"'-'", u"'*'", u"'/'", u"'('", u"')'", u"'{'", u"'}'",
            u"'\\{'", u"'\\}'", u"'['", u"']'", u"'\\left'", u"'\\right'",
            u"'|'", u"'\\lim'", u"'\\int'", u"'\\sum'", u"'\\prod'", u"'\\exp'",
            u"'\\log'", u"'\\ln'", u"'\\sin'", u"'\\cos'", u"'\\tan'", u"'\\csc'",
            u"'\\sec'", u"'\\cot'", u"'\\arcsin'", u"'\\arccos'", u"'\\arctan'",
            u"'\\arccsc'", u"'\\arcsec'", u"'\\arccot'", u"'\\sinh'", u"'\\cosh'",
            u"'\\tanh'", u"'\\arsinh'", u"'\\arcosh'", u"'\\artanh'", u"'\\sqrt'",
            u"'\\times'", u"'\\cdot'", u"'\\div'", u"'\\frac'", u"'\\binom'",
            u"'\\dbinom'", u"'\\tbinom'", u"'\\mathit'", u"'_'", u"'^'",
            u"':'", u"'='", u"'<'", u"'\\leq'", u"'>'", u"'\\geq'", u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"WS", u"THINSPACE", u"MEDSPACE", u"THICKSPACE", u"QUAD", u"QQUAD",
            u"NEGTHINSPACE", u"NEGMEDSPACE", u"NEGTHICKSPACE", u"ADD", u"SUB",
            u"MUL", u"DIV", u"L_PAREN", u"R_PAREN", u"L_BRACE", u"R_BRACE",
            u"L_BRACE_LITERAL", u"R_BRACE_LITERAL", u"L_BRACKET", u"R_BRACKET",
            u"CMD_LEFT", u"CMD_RIGHT", u"BAR", u"FUNC_LIM", u"LIM_APPROACH_SYM",
            u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", u"FUNC_EXP", u"FUNC_LOG",
            u"FUNC_LN", u"FUNC_SIN", u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC",
            u"FUNC_SEC", u"FUNC_COT", u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN",
            u"FUNC_ARCCSC", u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH",
            u"FUNC_COSH", u"FUNC_TANH", u"FUNC_ARSINH", u"FUNC_ARCOSH",
            u"FUNC_ARTANH", u"FUNC_SQRT", u"CMD_TIMES", u"CMD_CDOT", u"CMD_DIV",
            u"CMD_FRAC", u"CMD_BINOM", u"CMD_DBINOM", u"CMD_TBINOM", u"CMD_MATHIT",
            u"UNDERSCORE", u"CARET", u"COLON", u"DIFFERENTIAL", u"LETTER",
            u"NUMBER", u"EQUAL", u"LT", u"LTE", u"GT", u"GTE", u"BANG",
            u"SYMBOL" ]

    ruleNames = [ u"T__0", u"WS", u"THINSPACE", u"MEDSPACE", u"THICKSPACE",
                  u"QUAD", u"QQUAD", u"NEGTHINSPACE", u"NEGMEDSPACE", u"NEGTHICKSPACE",
                  u"ADD", u"SUB", u"MUL", u"DIV", u"L_PAREN", u"R_PAREN",
                  u"L_BRACE", u"R_BRACE", u"L_BRACE_LITERAL", u"R_BRACE_LITERAL",
                  u"L_BRACKET", u"R_BRACKET", u"CMD_LEFT", u"CMD_RIGHT",
                  u"BAR", u"FUNC_LIM", u"LIM_APPROACH_SYM", u"FUNC_INT",
                  u"FUNC_SUM", u"FUNC_PROD", u"FUNC_EXP", u"FUNC_LOG", u"FUNC_LN",
                  u"FUNC_SIN", u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC",
                  u"FUNC_COT", u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN",
                  u"FUNC_ARCCSC", u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH",
                  u"FUNC_COSH", u"FUNC_TANH", u"FUNC_ARSINH", u"FUNC_ARCOSH",
                  u"FUNC_ARTANH", u"FUNC_SQRT", u"CMD_TIMES", u"CMD_CDOT",
                  u"CMD_DIV", u"CMD_FRAC", u"CMD_BINOM", u"CMD_DBINOM",
                  u"CMD_TBINOM", u"CMD_MATHIT", u"UNDERSCORE", u"CARET",
                  u"COLON", u"WS_CHAR", u"DIFFERENTIAL", u"LETTER", u"DIGIT",
                  u"NUMBER", u"EQUAL", u"LT", u"LTE", u"GT", u"GTE", u"BANG",
                  u"SYMBOL" ]

    grammarFileName = u"LaTeX.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(LaTeXLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


