import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = """class main {
            int a;
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("main"),
                                [
                                    AttributeDecl(
                                        Instance(), VarDecl(Id("a"), IntType())
                                    )
                                ],
                            )
                        ]
                    )
                ),
                301,
            )
        )

    def test_302(self):
        input = """class A302 {
            static int a;
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A302"),
                                [AttributeDecl(Static(), VarDecl(Id("a"), IntType()))],
                            )
                        ]
                    )
                ),
                302,
            )
        )

    def test_303(self):
        input = """class A303 {
            static final int a;
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A303"),
                                [
                                    AttributeDecl(
                                        Static(), ConstDecl(Id("a"), IntType(), None)
                                    )
                                ],
                            )
                        ]
                    )
                ),
                303,
            )
        )

    def test_304(self):
        input = """class A304 {
            final static int a = 10;    
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A304"),
                                [
                                    AttributeDecl(
                                        Static(),
                                        ConstDecl(Id("a"), IntType(), IntLiteral(10)),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                304,
            )
        )

    def test_305(self):
        input = """class A305 {
            final int a, b, c = 10;
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A305"),
                                [
                                    AttributeDecl(
                                        Instance(), ConstDecl(Id("a"), IntType(), None)
                                    ),
                                    AttributeDecl(
                                        Instance(), ConstDecl(Id("b"), IntType(), None)
                                    ),
                                    AttributeDecl(
                                        Instance(),
                                        ConstDecl(Id("c"), IntType(), IntLiteral(10)),
                                    ),
                                ],
                            )
                        ]
                    )
                ),
                305,
            )
        )

    def test_306(self):
        input = """class A306 {
            final int a = 10, b, c = 4;
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A306"),
                                [
                                    AttributeDecl(
                                        Instance(),
                                        ConstDecl(Id("a"), IntType(), IntLiteral(10)),
                                    ),
                                    AttributeDecl(
                                        Instance(), ConstDecl(Id("b"), IntType(), None)
                                    ),
                                    AttributeDecl(
                                        Instance(),
                                        ConstDecl(Id("c"), IntType(), IntLiteral(4)),
                                    ),
                                ],
                            )
                        ]
                    )
                ),
                306,
            )
        )

    def test_307(self):
        input = """class A307 {
            int main() {

            }
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A307"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("main"),
                                        [],
                                        IntType(),
                                        Block([], []),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                307,
            )
        )

    def test_308(self):
        input = """class A308 {
            int me(int a) {

            }
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A308"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("me"),
                                        [VarDecl(Id("a"), IntType())],
                                        IntType(),
                                        Block([], []),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                308,
            )
        )

    def test_309(self):
        input = """class A309 {
            int me(int a,b) {

            }
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A309"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("me"),
                                        [
                                            VarDecl(Id("a"), IntType()),
                                            VarDecl(Id("b"), IntType()),
                                        ],
                                        IntType(),
                                        Block([], []),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                309,
            )
        )

    def test_310(self):
        input = """class A310 {
            int me(int a,b; float c) {

            }
        }"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("A310"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("me"),
                                        [
                                            VarDecl(Id("a"), IntType()),
                                            VarDecl(Id("b"), IntType()),
                                            VarDecl(Id("c"), FloatType()),
                                        ],
                                        IntType(),
                                        Block([], []),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                310,
            )
        )

    def test_311(self):
        input = """class Example1 {
        int factorial(int n){
        if n == 0 then return 1; else return n * this.factorial(n - 1);
        }}"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("Example1"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("factorial"),
                                        [VarDecl(Id("n"), IntType())],
                                        IntType(),
                                        Block(
                                            [],
                                            [
                                                If(
                                                    BinaryOp(
                                                        "==", Id("n"), IntLiteral(0)
                                                    ),
                                                    Return(IntLiteral(1)),
                                                    Return(
                                                        BinaryOp(
                                                            "*",
                                                            Id("n"),
                                                            CallExpr(
                                                                SelfLiteral(),
                                                                Id("factorial"),
                                                                [
                                                                    BinaryOp(
                                                                        "-",
                                                                        Id("n"),
                                                                        IntLiteral(1),
                                                                    )
                                                                ],
                                                            ),
                                                        )
                                                    ),
                                                )
                                            ],
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                311,
            )
        )

    def test_312(self):
        input = """class Shape {
        float length,width;
        float getArea() {}
        Shape(float length,width){
        this.length := length;
        this.width := width;
        }}"""
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("Shape"),
                                [
                                    AttributeDecl(
                                        Instance(), VarDecl(Id("length"), FloatType())
                                    ),
                                    AttributeDecl(
                                        Instance(), VarDecl(Id("width"), FloatType())
                                    ),
                                    MethodDecl(
                                        Instance(),
                                        Id("getArea"),
                                        [],
                                        FloatType(),
                                        Block([], []),
                                    ),
                                    MethodDecl(
                                        Instance(),
                                        Id("Shape"),
                                        [
                                            VarDecl(Id("length"), FloatType()),
                                            VarDecl(Id("width"), FloatType()),
                                        ],
                                        None,
                                        Block(
                                            [],
                                            [
                                                Assign(
                                                    FieldAccess(
                                                        SelfLiteral(), Id("length")
                                                    ),
                                                    Id("length"),
                                                ),
                                                Assign(
                                                    FieldAccess(
                                                        SelfLiteral(), Id("width")
                                                    ),
                                                    Id("width"),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            )
                        ]
                    )
                ),
                312,
            )
        )

    def test_313(self):
        input = "class A313 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A313"), [], None)])), 313)
        )

    def test_314(self):
        input = """class A314 {
            # abc
            /* dat dep trai 10 diem ppl2 */
        }"""
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A314"), [], None)])), 314)
        )

    def test_315(self):
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
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("Rectangle"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("getArea"),
                                        [],
                                        FloatType(),
                                        Block(
                                            [],
                                            [
                                                Return(
                                                    BinaryOp(
                                                        "*",
                                                        FieldAccess(
                                                            SelfLiteral(), Id("length")
                                                        ),
                                                        FieldAccess(
                                                            SelfLiteral(), Id("width")
                                                        ),
                                                    )
                                                )
                                            ],
                                        ),
                                    )
                                ],
                                Id("Shape"),
                            ),
                            ClassDecl(
                                Id("Triangle"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("getArea"),
                                        [],
                                        FloatType(),
                                        Block(
                                            [],
                                            [
                                                Return(
                                                    BinaryOp(
                                                        "\\",
                                                        BinaryOp(
                                                            "*",
                                                            FieldAccess(
                                                                SelfLiteral(),
                                                                Id("length"),
                                                            ),
                                                            FieldAccess(
                                                                SelfLiteral(),
                                                                Id("width"),
                                                            ),
                                                        ),
                                                        IntLiteral(2),
                                                    )
                                                )
                                            ],
                                        ),
                                    )
                                ],
                                Id("Shape"),
                            ),
                        ]
                    )
                ),
                315,
            )
        )

    def test_316(self):
        input = """class Example2 {
            void main() {
                Shape s;
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
            }
        }
        """
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("Example2"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("main"),
                                        [],
                                        VoidType(),
                                        Block(
                                            [
                                                VarDecl(
                                                    Id("s"),
                                                    ClassType(Id("Shape")),
                                                )
                                            ],
                                            [
                                                Assign(
                                                    Id("s"),
                                                    NewExpr(
                                                        Id("Rectangle"),
                                                        [IntLiteral(3), IntLiteral(4)],
                                                    ),
                                                ),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeFloatLn"),
                                                    [
                                                        CallExpr(
                                                            Id("s"), Id("getArea"), []
                                                        )
                                                    ],
                                                ),
                                                Assign(
                                                    Id("s"),
                                                    NewExpr(
                                                        Id("Triangle"),
                                                        [IntLiteral(3), IntLiteral(4)],
                                                    ),
                                                ),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeFloatLn"),
                                                    [
                                                        CallExpr(
                                                            Id("s"), Id("getArea"), []
                                                        )
                                                    ],
                                                ),
                                            ],
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                316,
            )
        )

    def test_317(self):
        input = """class a {
            int[5] a = {1,2};
        }
        """
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("a"),
                                [
                                    AttributeDecl(
                                        Instance(),
                                        VarDecl(
                                            Id("a"),
                                            ArrayType(5, IntType()),
                                            ArrayLiteral(
                                                [IntLiteral(1), IntLiteral(2)]
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                317,
            )
        )

    def test_318(self):
        input = """class a {
            int a = {1,2};
        }
        """
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("a"),
                                [
                                    AttributeDecl(
                                        Instance(),
                                        VarDecl(
                                            Id("a"),
                                            IntType(),
                                            ArrayLiteral(
                                                [IntLiteral(1), IntLiteral(2)]
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                318,
            )
        )

    def test_319(self):
        input = """class a {
            int a = 5*7+3/3;
        }
        """
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("a"),
                                [
                                    AttributeDecl(
                                        Instance(),
                                        VarDecl(
                                            Id("a"),
                                            IntType(),
                                            BinaryOp(
                                                "+",
                                                BinaryOp(
                                                    "*", IntLiteral(5), IntLiteral(7)
                                                ),
                                                BinaryOp(
                                                    "\\", IntLiteral(3), IntLiteral(3)
                                                ),
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                319,
            )
        )

    def test_320(self):
        input = """class a {
            string a_ () {
                int a;
                return a;
            }
        }
        """
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("a"),
                                [
                                    MethodDecl(
                                        Instance(),
                                        Id("a_"),
                                        [],
                                        StringType(),
                                        Block(
                                            [VarDecl(Id("a"), IntType())],
                                            [Return(Id("a"))],
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                320,
            )
        )

    def test_321(self):
        input = """class a {
            # du thanh dat
            /*du thanh dat */
        }
        """
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("a"), [])])), 321)
        )

    def test_322(self):
        input = """class a {
            float a = 12.3e3;
        }
        """
        self.assertTrue(
            TestAST.test(
                input,
                str(
                    Program(
                        [
                            ClassDecl(
                                Id("a"),
                                [
                                    AttributeDecl(
                                        Instance(),
                                        VarDecl(Id("a"), FloatType(), FloatLiteral(12.3e3)),
                                    )
                                ],
                            )
                        ]
                    )
                ),
                322,
            )
        )

    def test_323(self):
        input = "class A323 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A323"), [], None)])), 323)
        )

    def test_324(self):
        input = "class A324 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A324"), [], None)])), 324)
        )

    def test_325(self):
        input = "class A325 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A325"), [], None)])), 325)
        )

    def test_326(self):
        input = "class A326 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A326"), [], None)])), 326)
        )

    def test_327(self):
        input = "class A327 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A327"), [], None)])), 327)
        )

    def test_328(self):
        input = "class A328 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A328"), [], None)])), 328)
        )

    def test_329(self):
        input = "class A329 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A329"), [], None)])), 329)
        )

    def test_330(self):
        input = "class A330 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A330"), [], None)])), 330)
        )

    def test_331(self):
        input = "class A331 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A331"), [], None)])), 331)
        )

    def test_332(self):
        input = "class A332 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A332"), [], None)])), 332)
        )

    def test_333(self):
        input = "class A333 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A333"), [], None)])), 333)
        )

    def test_334(self):
        input = "class A334 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A334"), [], None)])), 334)
        )

    def test_335(self):
        input = "class A335 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A335"), [], None)])), 335)
        )

    def test_336(self):
        input = "class A336 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A336"), [], None)])), 336)
        )

    def test_337(self):
        input = "class A337 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A337"), [], None)])), 337)
        )

    def test_338(self):
        input = "class A338 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A338"), [], None)])), 338)
        )

    def test_339(self):
        input = "class A339 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A339"), [], None)])), 339)
        )

    def test_340(self):
        input = "class A340 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A340"), [], None)])), 340)
        )

    def test_341(self):
        input = "class A341 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A341"), [], None)])), 341)
        )

    def test_342(self):
        input = "class A342 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A342"), [], None)])), 342)
        )

    def test_343(self):
        input = "class A343 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A343"), [], None)])), 343)
        )

    def test_344(self):
        input = "class A344 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A344"), [], None)])), 344)
        )

    def test_345(self):
        input = "class A345 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A345"), [], None)])), 345)
        )

    def test_346(self):
        input = "class A346 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A346"), [], None)])), 346)
        )

    def test_347(self):
        input = "class A347 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A347"), [], None)])), 347)
        )

    def test_348(self):
        input = "class A348 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A348"), [], None)])), 348)
        )

    def test_349(self):
        input = "class A349 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A349"), [], None)])), 349)
        )

    def test_350(self):
        input = "class A350 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A350"), [], None)])), 350)
        )

    def test_351(self):
        input = "class A351 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A351"), [], None)])), 351)
        )

    def test_352(self):
        input = "class A352 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A352"), [], None)])), 352)
        )

    def test_353(self):
        input = "class A353 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A353"), [], None)])), 353)
        )

    def test_354(self):
        input = "class A354 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A354"), [], None)])), 354)
        )

    def test_355(self):
        input = "class A355 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A355"), [], None)])), 355)
        )

    def test_356(self):
        input = "class A356 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A356"), [], None)])), 356)
        )

    def test_357(self):
        input = "class A357 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A357"), [], None)])), 357)
        )

    def test_358(self):
        input = "class A358 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A358"), [], None)])), 358)
        )

    def test_359(self):
        input = "class A359 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A359"), [], None)])), 359)
        )

    def test_360(self):
        input = "class A360 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A360"), [], None)])), 360)
        )

    def test_361(self):
        input = "class A361 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A361"), [], None)])), 361)
        )

    def test_362(self):
        input = "class A362 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A362"), [], None)])), 362)
        )

    def test_363(self):
        input = "class A363 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A363"), [], None)])), 363)
        )

    def test_364(self):
        input = "class A364 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A364"), [], None)])), 364)
        )

    def test_365(self):
        input = "class A365 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A365"), [], None)])), 365)
        )

    def test_366(self):
        input = "class A366 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A366"), [], None)])), 366)
        )

    def test_367(self):
        input = "class A367 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A367"), [], None)])), 367)
        )

    def test_368(self):
        input = "class A368 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A368"), [], None)])), 368)
        )

    def test_369(self):
        input = "class A369 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A369"), [], None)])), 369)
        )

    def test_370(self):
        input = "class A370 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A370"), [], None)])), 370)
        )

    def test_371(self):
        input = "class A371 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A371"), [], None)])), 371)
        )

    def test_372(self):
        input = "class A372 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A372"), [], None)])), 372)
        )

    def test_373(self):
        input = "class A373 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A373"), [], None)])), 373)
        )

    def test_374(self):
        input = "class A374 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A374"), [], None)])), 374)
        )

    def test_375(self):
        input = "class A375 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A375"), [], None)])), 375)
        )

    def test_376(self):
        input = "class A376 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A376"), [], None)])), 376)
        )

    def test_377(self):
        input = "class A377 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A377"), [], None)])), 377)
        )

    def test_378(self):
        input = "class A378 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A378"), [], None)])), 378)
        )

    def test_379(self):
        input = "class A379 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A379"), [], None)])), 379)
        )

    def test_380(self):
        input = "class A380 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A380"), [], None)])), 380)
        )

    def test_381(self):
        input = "class A381 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A381"), [], None)])), 381)
        )

    def test_382(self):
        input = "class A382 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A382"), [], None)])), 382)
        )

    def test_383(self):
        input = "class A383 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A383"), [], None)])), 383)
        )

    def test_384(self):
        input = "class A384 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A384"), [], None)])), 384)
        )

    def test_385(self):
        input = "class A385 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A385"), [], None)])), 385)
        )

    def test_386(self):
        input = "class A386 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A386"), [], None)])), 386)
        )

    def test_387(self):
        input = "class A387 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A387"), [], None)])), 387)
        )

    def test_388(self):
        input = "class A388 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A388"), [], None)])), 388)
        )

    def test_389(self):
        input = "class A389 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A389"), [], None)])), 389)
        )

    def test_390(self):
        input = "class A390 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A390"), [], None)])), 390)
        )

    def test_391(self):
        input = "class A391 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A391"), [], None)])), 391)
        )

    def test_392(self):
        input = "class A392 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A392"), [], None)])), 392)
        )

    def test_393(self):
        input = "class A393 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A393"), [], None)])), 393)
        )

    def test_394(self):
        input = "class A394 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A394"), [], None)])), 394)
        )

    def test_395(self):
        input = "class A395 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A395"), [], None)])), 395)
        )

    def test_396(self):
        input = "class A396 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A396"), [], None)])), 396)
        )

    def test_397(self):
        input = "class A397 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A397"), [], None)])), 397)
        )

    def test_398(self):
        input = "class A398 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A398"), [], None)])), 398)
        )

    def test_399(self):
        input = "class A399 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A399"), [], None)])), 399)
        )

    def test_400(self):
        input = "class A400 {}"
        self.assertTrue(
            TestAST.test(input, str(Program([ClassDecl(Id("A400"), [], None)])), 400)
        )
