class Token:
    pass

class Scanner:
    def __init__(self, input_stream):
        self._input_stream = input_stream
    def __del__(self):
        pass
    def scan(self):
        return Token()

class Parser:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def parse(self, scanner, program_node_builder):
        pass

class ProgramNode:
    pass

class ProgramNodeBuilder:
    def __init__(self):
        self._node = None
    def new_variable(self, variable_name: str) -> ProgramNode:
        return ProgramNode()
    def new_assignment(self, variable: ProgramNode, expression: ProgramNode) -> ProgramNode:
        return ProgramNode()
    def new_return_statement(self, value: ProgramNode) -> ProgramNode:
        return ProgramNode()
    def new_condition(self, condition: ProgramNode, true_part: ProgramNode, false_part: ProgramNode) -> ProgramNode:
        return ProgramNode()
    def get_root_node(self) -> ProgramNode:
        return self._node

class ProgramNode:
    def __init__(self):
        pass
    def get_source_position(self, line: int, index: int):
        pass
    def add(self, node):
        pass
    def remove(self, node):
        pass
    def traverse(self, code_generator):
        pass

class CodeGenerator:
    def __init__(self, bytecode_stream):
        self._output = bytecode_stream
    def visit_statement_node(self, statement_node):
        pass
    def visit_expression_node(self, expression_node):
        pass

class ExpressionNode:
    def __init__(self):
        self._children = []
    def traverse(self, code_generator):
        code_generator.visit_expression_node(self)
        for child in self._children:
            child.traverse(code_generator)

class ListIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0
    def first(self):
        self._index = 0
    def is_done(self):
        return self._index >= len(self._items)
    def next(self):
        self._index += 1
    def current_item(self):
        if not self.is_done():
            return self._items[self._index]
        return None

class Compiler:
    def __init__(self):
        pass
    def compile(self, input_stream, bytecode_stream):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()
        parser.parse(scanner, builder)
        generator = RISCCodeGenerator(bytecode_stream)
        parse_tree = builder.get_root_node()
        parse_tree.traverse(generator)

class Scanner:
    def __init__(self, input_stream):
        self._input_stream = input_stream

class ProgramNodeBuilder:
    def __init__(self):
        self._node = None
    def get_root_node(self):
        return self._node

class Parser:
    def __init__(self):
        pass
    def parse(self, scanner, builder):
        pass

class RISCCodeGenerator:
    def __init__(self, bytecode_stream):
        self._output = bytecode_stream
    def visit_expression_node(self, node):
        pass

