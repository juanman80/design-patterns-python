# pylint: disable=C0114, C0115, C0116, R0903, R0201, W0622, R0912

from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        VARIABLE = 3

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return '`%s`' % {self.text}

    @property
    def is_op(self):
        return self.type in (Token.Type.PLUS, Token.Type.MINUS)


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value

        if self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value

        return 0

    def add_item(self, value):
        if self.left is None:
            self.left = value
        elif self.right is None:
            self.right = value

    @property
    def is_full(self):
        return self.left is not None and self.right is not None


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def lex(self, input):
        result = []

        i = 0
        while i < len(input):
            if input[i] == '+':
                result.append(Token(Token.Type.PLUS, '+'))
            elif input[i] == '-':
                result.append(Token(Token.Type.MINUS, '-'))
            elif input[i].isalpha():
                variable = [input[i]]
                for j in range(i + 1, len(input)):
                    if input[j].isalpha():
                        variable.append(input[j])
                        i += 1
                    else:
                        break
                if len(variable) > 1:
                    result.append(Token(Token.Type.INTEGER, 0))
                else:
                    result.append(Token(Token.Type.VARIABLE, ''.join(variable)))

            else:  # must be a number
                digits = [input[i]]
                for j in range(i + 1, len(input)):
                    if input[j].isdigit():
                        digits.append(input[j])
                        i += 1
                    else:
                        break

                result.append(Token(Token.Type.INTEGER,''.join(digits)))
            i += 1

        return result

    def parse(self, tokens):
        result = BinaryOperation()
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.is_op and result.is_full:
                new = BinaryOperation()
                new.add_item(result)
                result = new

            if token.type == Token.Type.INTEGER:
                result.add_item(Integer(int(token.text)))
            elif token.type == Token.Type.PLUS:
                result.type = BinaryOperation.Type.ADDITION
            elif token.type == Token.Type.MINUS:
                result.type = BinaryOperation.Type.SUBTRACTION
            elif token.type == Token.Type.VARIABLE:
                value = self.variables.get(token.text, 0)
                result.add_item(Integer(int(value)))

            i += 1
        return result

    def calculate(self, expression):
        tokens = self.lex(expression)
        print(' '.join(map(str, tokens)))

        parsed = self.parse(tokens)
        print('%s = %d' % (expression, parsed.value))


if __name__ == '__main__':
    ep = ExpressionProcessor()
    ep.calculate("1+2+3")
    ep.calculate("1+2+xy")
    ep.variables['x'] = 3
    ep.calculate("10-2-x")
