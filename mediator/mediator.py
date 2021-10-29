import unittest

class Mediator(list):
    def join(self, participant):
        self.append(participant)

    def broadcast(self, source, value):
        for p in self:
            if p != source:
                p.value = value

class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.join(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


class Evaluate(unittest.TestCase):
    def test_mediator(self):
        mediator = Mediator()
        p1 = Participant(mediator)
        p2 = Participant(mediator)
        p1.say(3)
        assert p1.value == 0
        assert p2.value == 3
        p2.say(2)
        assert p1.value == 2
        assert p2.value == 3


if __name__ == "__main__":
    unittest.main()
