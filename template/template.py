from abc import ABC
import unittest

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        c1vsc2 = self.hit(self.creatures[c1_index], self.creatures[c2_index])
        c2vsc1 = self.hit(self.creatures[c2_index], self.creatures[c1_index])
        if c1vsc2 and c2vsc1:
            return -1
        if not c1vsc2 and not c2vsc1:
            return -1
        if c1vsc2:
            return c1_index
        if c2vsc1:
            return c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        if attacker.attack >= defender.health:
            return True
        return False


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        if attacker.attack >= defender.health:
            return True
        defender.health -= attacker.attack
        return False


class Evaluate(unittest.TestCase):
    def test_impasse(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')
        self.assertEqual(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')

    def test_temporary_murder(self):
        c1 = Creature(1, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(1, game.combat(0, 1))

    def test_double_murder(self):
        c1 = Creature(2, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1))

    def test_permanent_damage_death(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 3)
        game = PermanentDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), 'Nobody should win this battle.')
        self.assertEqual(1, c1.health)
        self.assertEqual(2, c2.health)
        self.assertEqual(1, game.combat(0, 1), 'Creature at index 1 should win this')



if __name__ == "__main__":
    unittest.main()