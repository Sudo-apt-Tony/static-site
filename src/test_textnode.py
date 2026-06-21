import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        test_cases = [
            ("foo", TextType.TEXT, None, LeafNode(None, "foo")),  # TEXT
            ("bar", TextType.BOLD, None, LeafNode("b", "bar")),  # BOLD
            (
                "fizz",
                TextType.LINK,
                "https://www.github.com",
                LeafNode("a", "fizz", {"href": "https://www.github.com"}),
            ),  # LINK
            (
                "Image",
                TextType.IMAGE,
                "https://www.imgur.com",
                LeafNode("img", "", {"src": "https://www.imgur.com", "alt": "Image"}),
            ),  # IMG
            (None, None, None, None),  # Exception
        ]

        for text, text_type, url, expected in test_cases:
            if expected is None:
                with self.assertRaises(Exception):
                    text_node_to_html_node(TextNode(text, text_type, url))
                continue
            self.assertEqual(
                text_node_to_html_node(TextNode(text, text_type, url)).value,
                expected.value,
            )


if __name__ == "__main__":
    unittest.main()
