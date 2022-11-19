import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {} """
        input = """class a{int main() {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test2(self):
        """More complex program"""
        input = """class Example1 {
        int factorial(int n){
        if n == 0 then return 1; else return n * this.factorial(n - 1);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2))
    
    def test3(self):
        """Miss ) int main( {}"""
        input = """class a{int main() {}}"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,203))

    def test4(self):
        input = """class Shape {
        float length,width;
        float getArea() {}
        Shape(float length,width){
        this.length := length;
        this.width := width;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test5(self):
        input = """class Rectangle extends Shape {
        float getArea(){
        return this.length*this.width;
        }
        }
        class Triangle extends Shape {
        float getArea(){
        return this.length*this.width / 2;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test6(self):
        input = """class Example2 {
        void main(){
        Shape s;
        s := new Rectangle(3,4);
        io.writeFloatLn(s.getArea());
        s := new Triangle(3,4);
        io.writeFloatLn(s.getArea());
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test7(self):
        input = """class a {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test8(self):
        input = """class a {
            int[5] a = {1,2};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test9(self):
        input = """class a {
            final int a = 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test10(self):
        input = """class a {
            int foo(){a.foo(b);}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test11(self):
        input = """class a {
            void foo(int a; float b) {
                int[5] a;
                int[4] b;
                b[5]:=5;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test12(self):
        input = """class a {
            int a = {1,2};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test13(self):
        input = """class a {
            int a = 5*7+3/3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test14(self):
        input = """class a {
            string a_ () {
                int a;
                return a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test15(self):
        input = """class a {
            # du thanh dat
            /*du thanh dat */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test16(self):
        input = """class a {
            float a = 12.3e3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test17(self):
        input = """class a {
            int[3] a = {1,2,3,4};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test18(self):
        input = """class a {
            float a(){a[3+x.foo(2)] := a[b[2]] +3;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test19(self):
        input = """class a {
            float b(int a) {x.b[2] := x.m()[3];}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test20(self):
        input = """class a {
            float a () {
                int a = new a();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test21(self):
        input = """class a {
            float a () {
                this.a := a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test22(self):
        input = """class a {
            int a = 4*3/3*3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test23(self):
        input = """class a {
            int a = 4+3/3*3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test24(self):
        input = """class a {
           boolean a= TRUE || FALSE;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,24))

    def test25(self):
        input = """class a {
           int aaaaa = 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    
    def test26(self):
        input = """class a {
           float a() {
            if TRUE then a := 2;
           }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    
    def test27(self):
        input = """class a {
           float a() {
            if TRUE then a := 2; else for a:=2 to 3 do a:=2;
           }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    
    def test28(self):
        input = """class a {
           c;
        }
        """
        expect = "Error on line 2 col 12: ;"
        self.assertTrue(TestParser.test(input,expect,228))
    
    def test29(self):
        input = """class a {
           int a = 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    
    def test30(self):
        input = """class a {
           int[4] a= 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    
    def test31(self):
        input = """class a {
           float a() {
                s.Shape();
           }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    
    def test32(self):
        input = """class a {
           float a() {
                s.Shape(2,a,3);
           }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    
    def test33(self):
        input = """class a {
           float a(int a; string b) {}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    
    def test34(self):
        input = """class asd {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    
    def test35(self):
        input = """class awererw {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    
    def test36(self):
        input = """class a {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    
    def test37(self):
        input = """class qwwqe {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    
    def test38(self):
        input = """class a {
           int a = 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    
    def test39(self):
        input = """class a {
           float b(int a) {x.b[2] := x.m()[a];}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test40(self):
        input = """class a {
           float b(int a) {x.b[2] := x.m()[asd];}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test41(self):
        input = """class a {
           float b(int b) {x.b[2] := x.m()[3];}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test42(self):
        input = """class a {
           float b(int a) {x.a[2] := x.m()[3];}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test43(self):
        input = """class asddsa {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test44(self):
        input = """class aasda {
           float b(int a) {if false || true then a:= 5;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test45(self):
        input = """class a {
           float b(int a) {x.b[2] := x.m()[89];}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test46(self):
        input = """class a {
           string a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test47(self):
        input = """class b {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test48(self):
        input = """class c {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test49(self):
        input = """class d {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test50(self):
        input = """class f {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test51(self):
        input = """class g {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test52(self):
        input = """class h {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test53(self):
        input = """class a {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test54(self):
        input = """class i {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test55(self):
        input = """class k {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test56(self):
        input = """class l {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test57(self):
        input = """class m {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def test58(self):
        input = """class n {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test59(self):
        input = """class o {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def test60(self):
        input = """class p {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test61(self):
        input = """class q{
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test62(self):
        input = """class a {
           
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,262))

    def test63(self):
        input = """class r {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test64(self):
        input = """class s {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test65(self):
        input = """class t {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test66(self):
        input = """class u {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test67(self):
        input = """class v 
           
        }
        """
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.test(input,expect,267))

    def test68(self):
        input = """class w {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test69(self):
        input = """class x {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test70(self):
        input = """class y {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test71(self):
        input = """class z {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test72(self):
        input = """class a_ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test73(self):
        input = """class a__ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test74(self):
        input = """class a____ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test75(self):
        input = """class a_____ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test76(self):
        input = """class a______ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test77(self):
        input = """class a_______ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test78(self):
        input = """class a________ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test79(self):
        input = """class a________ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test80(self):
        input = """class bb {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test81(self):
        input = """class b_ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test82(self):
        input = """class a {
           int a[;
        }
        """
        expect = "Error on line 2 col 16: ["
        self.assertTrue(TestParser.test(input,expect,282))

    def test83(self):
        input = """class a {
           void main() {this.a[0];}
        }
        """
        expect = "Error on line 2 col 33: ;"
        self.assertTrue(TestParser.test(input,expect,283))

    def test84(self):
        input = """class b____ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test85(self):
        input = """class b_____ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test86(self):
        input = """class b______ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test87(self):
        input = """class b_______ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test88(self):
        input = """class b________ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test89(self):
        input = """class b_________ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test90(self):
        input = """class cc {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test91(self):
        input = """class c_ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test92(self):
        input = """class c__ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test93(self):
        input = """class c___ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test94(self):
        input = """class c____ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test95(self):
        input = """class c_____ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test96(self):
        input = """class c______ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test97(self):
        input = """class c_______ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test98(self):
        input = """class c________ {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test99(self):
        input = """class aasasadwerw {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test100(self):
        input = """class aasadasadswer {
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

    
    
    
    