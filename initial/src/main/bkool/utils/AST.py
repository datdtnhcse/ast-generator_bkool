from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Tuple

from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = "visit{}".format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass


class Expr(AST):
    __metaclass__ = ABCMeta
    pass


class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


class Type(AST):
    __metaclass__ = ABCMeta
    pass


class MemDecl(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Id(LHS):
    name: str

    def __str__(self):
        return f'Id("{self.name}")'


# used for binary expression
@dataclass
class BinaryOp(Expr):
    op: str
    left: Expr
    right: Expr

    def __str__(self):
        return f'BinaryOp("{self.op}",{self.left},{self.right})'


# used for unary expression with orerand like !,+,-
@dataclass
class UnaryOp(Expr):
    op: str
    body: Expr

    def __str__(self):
        return f'UnaryOp("{self.op}",{self.body})'


@dataclass
class CallExpr(Expr):
    obj: Expr
    method: Id
    param: List[Expr]

    def __str__(self):
        params = ",".join(str(i) for i in self.param)
        return f"CallExpr({self.obj},{self.method},[{params}])"


@dataclass
class NewExpr(Expr):
    classname: Id
    param: List[Expr]

    def __str__(self):
        params = ",".join(str(i) for i in self.param)
        return f"NewExpr({self.classname},[{params}])"


@dataclass
class ArrayCell(LHS):
    arr: Expr
    idx: Expr

    def __str__(self):
        return f"ArrayCell({self.arr},{self.idx})"


@dataclass
class FieldAccess(LHS):
    obj: Expr
    fieldname: Id

    def __str__(self):
        return f"FieldAccess({self.obj},{self.fieldname})"


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass


@dataclass
class IntLiteral(Literal):
    value: int

    def __str__(self):
        return f"IntLiteral({self.value})"


@dataclass
class FloatLiteral(Literal):
    value: float

    def __str__(self):
        return f"FloatLiteral({self.value})"


@dataclass
class StringLiteral(Literal):
    value: str

    def __str__(self):
        return f"StringLiteral('''{self.value}''')"


@dataclass
class BooleanLiteral(Literal):
    value: bool

    def __str__(self):
        return f"BooleanLiteral({self.value})"


class NullLiteral(Literal):
    def __str__(self):
        return "NullLiteral()"


class SelfLiteral(Literal):
    def __str__(self):
        return "SelfLiteral()"


@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]

    def __str__(self):
        values = ",".join(map(str, self.value))
        return f"ArrayLiteral([{values}])"


class Decl(AST):
    __metaclass__ = ABCMeta
    pass


class StoreDecl(Decl):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Assign(Stmt):
    lhs: Expr
    exp: Expr

    def __str__(self):
        return f"Assign({self.lhs},{self.exp})"


@dataclass
class If(Stmt):
    expr: Expr
    thenStmt: Stmt
    elseStmt: Optional[Stmt] = None  # None if there is no else branch

    def __str__(self):
        return f"If({self.expr},{self.thenStmt},{self.elseStmt})"


@dataclass
class For(Stmt):
    id: Id
    expr1: Expr
    expr2: Expr
    up: bool  # True => increase; False => decrease
    loop: Stmt

    def __str__(self):
        return f"For({self.id},{self.expr1},{self.expr2},{self.up},{self.loop})"


class Break(Stmt):
    def __str__(self):
        return "Break()"


class Continue(Stmt):
    def __str__(self):
        return "Continue()"


@dataclass
class Return(Stmt):
    expr: Expr

    def __str__(self):
        return f"Return({self.expr})"


@dataclass
class CallStmt(Stmt):
    obj: Expr
    method: Id
    param: List[Expr]

    def __str__(self):
        exprs = ",".join(map(str, self.param))
        return f"CallStmt({self.obj},{self.method},[{exprs}])"


# used for local variable or parameter declaration
@dataclass
class VarDecl(StoreDecl):
    variable: Id
    varType: Type
    varInit: Optional[Expr] = None  # None if there is no initial

    def __str__(self):
        return f"VarDecl({self.variable},{self.varType},{self.varInit})"

    def toParam(self):
        return "param(" + str(self.variable) + "," + str(self.varType) + ")"


@dataclass
class Block(Stmt):
    decl: List[StoreDecl]
    stmt: List[Stmt]

    def __str__(self):
        decls = ",".join(str(i) for i in self.decl)
        stmts = ",".join(str(i) for i in self.stmt)
        return f"Block([{decls}],[{stmts}])"


# used for local constant declaration
@dataclass
class ConstDecl(StoreDecl):
    constant: Id
    constType: Type
    value: Optional[Expr]

    def __str__(self):
        return f"ConstDecl({self.constant},{self.constType},{self.value})"


# used for a class declaration
@dataclass
class ClassDecl(Decl):
    classname: Id
    memlist: List[MemDecl]
    parentname: Optional[Id] = None  # None if there is no parent

    def __str__(self):
        memdecls = ",".join(map(str, self.memlist))
        return f"ClassDecl({self.classname},[{memdecls}],{self.parentname})"


class SIKind(AST):
    __metaclass__ = ABCMeta


# used for instance member
class Instance(SIKind):
    def __str__(self):
        return "Instance()"


# used for static member
class Static(SIKind):
    def __str__(self):
        return "Static()"


# used for a normal or special method declaration.
# In the case of special method declaration,the name will be Id("<init>")
# and the return type is VoidType().
# In the case of normal method declaration, the name and the return type are from the declaration.
@dataclass
class MethodDecl(MemDecl):
    kind: SIKind
    name: Id
    param: List[VarDecl]
    returnType: Optional[Type]  # None for constructor
    body: Block

    def __str__(self):
        params = ",".join(map(str, self.param))
        return f"MethodDecl({self.kind},{self.name},[{params}],{self.returnType},{self.body})"


# used for mutable (variable) or immutable (constant) declaration
@dataclass
class AttributeDecl(MemDecl):
    kind: SIKind  # Instance or Static
    decl: StoreDecl  # VarDecl for mutable or ConstDecl for immutable

    def __str__(self):
        return f"AttributeDecl({self.kind},{self.decl})"


class IntType(Type):
    def __str__(self):
        return "IntType()"


class FloatType(Type):
    def __str__(self):
        return "FloatType()"


class BoolType(Type):
    def __str__(self):
        return "BoolType()"


class StringType(Type):
    def __str__(self):
        return "StringType()"


@dataclass
class ArrayType(Type):
    size: int
    eleType: Type

    def __str__(self):
        return f"ArrayType({self.size},{self.eleType})"


@dataclass
class ClassType(Type):
    classname: Id

    def __str__(self):
        return f"ClassType({self.classname})"


class VoidType(Type):
    def __str__(self):
        return "VoidType()"


# used for whole program
@dataclass
class Program(AST):
    decl: List[ClassDecl]

    def __str__(self):
        decls = ",".join(map(str, self.decl))
        return f"Program([{decls}])"