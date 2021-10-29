import unittest

class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def traverse_preorder(self):
    yield(self.value)
    for child in [self.left, self.right]:
        if child:
            yield from child.traverse_preorder()


class Evaluate(unittest.TestCase):
    def test_traverse_preorder(self):
        root = Node(
            1,
            Node(2),
            Node(3)
        )
        assert list(root.traverse_preorder()) == [1, 2, 3]

        node = Node('a',
                    Node('b',
                         Node('c'),
                         Node('d')),
                    Node('e'))
        self.assertEqual(
          'abcde',
          ''.join([x for x in node.traverse_preorder()])
        )


if __name__ == "__main__":
    unittest.main()
