import unittest
from copy import deepcopy

class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        self.tokens = deepcopy(memento)

class Evaluate(unittest.TestCase):
    def test_memento(self):
        tm = TokenMachine()

        token = Token(111)
        print('Made a token with value 111 and kept a reference')

        tm.add_token(token)
        print('Added this token to the list')

        m = tm.add_token_value(222)
        print('Added token 222 and kept a memento')

        print('Changed 111 token\'s value to 333... pay attention!')
        token.value = 333

        tm.revert(m)

        self.assertEqual(2, len(tm.tokens),
                         'At this point, token machine should have exactly 2 tokens, you have ' + str(len(tm.tokens)))

        self.assertEqual(111, tm.tokens[0].value,
                         'You got the tokens[0] value wrong here. Hint: did you init the memento by value?')



if __name__ == "__main__":
    unittest.main()
