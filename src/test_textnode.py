import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a test node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)

    def test_repr(self):
        node5 = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node6 = TextNode(
            "This is a text node",
            TextType.LINK,
            "https://www.vecteezy.com/free-photos/image",
        )
        node7 = TextNode("This is a text node", TextType.TEXT)

        self.assertEqual(
            repr(node5), "TextNode(This is a text node, link, https://www.boot.dev)"
        )

        self.assertEqual(
            repr(node6),
            "TextNode(This is a text node, link, https://www.vecteezy.com/free-photos/image)",
        )

        self.assertEqual(repr(node7), "TextNode(This is a text node, text, None)")


if __name__ == "__main__":
    unittest.main()
