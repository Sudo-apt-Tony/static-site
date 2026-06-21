import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        test_cases = [
            (None, ""),
            (
                {"href": "https://www.boot.dev", "target": "_blank"},
                ' href="https://www.boot.dev" target="_blank"',
            ),
            ({}, ""),
        ]
        for props, expected in test_cases:
            node = HTMLNode(props=props)
            self.assertEqual(node.props_to_html(), expected)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        test_cases = [
            (
                "p",
                "The dog jumped over the crimson moon, seeking tales of slaughter.",
                None,
                "<p>The dog jumped over the crimson moon, seeking tales of slaughter.</p>",
            ),
            (None, None, None, ValueError),
            (None, "Tag, you're it!", None, "Tag, you're it!"),
            (
                "a",
                "Click Here",
                {"href": "https://www.boot.dev", "target": "_blind"},
                '<a href="https://www.boot.dev" target="_blind">Click Here</a>',
            ),
        ]

        for tag, value, props, expected in test_cases:
            if value is None:
                # Value is none for this test case to ensure enforcement on method. Suppressing LSP error
                with self.assertRaises(ValueError):
                    LeafNode(tag, value, props).to_html()  # pyright: ignore[reportArgumentType]
            else:
                node = LeafNode(tag, value, props)
                self.assertEqual(node.to_html(), expected)


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        test_cases = [
            ("h1", [], None, "<h1></h1>"),
            (None, None, None, ValueError),
            ("", [], {}, ValueError),
            (
                "p",
                [
                    LeafNode("p", "text"),
                    LeafNode("b", "bold"),
                    LeafNode(
                        "a",
                        "link",
                        {"href": "https://www.youtube.com", "target": "_blind"},
                    ),
                ],
                None,
                '<p><p>text</p><b>bold</b><a href="https://www.youtube.com" target="_blind">link</a></p>',
            ),
        ]

        for tag, children, props, expected in test_cases:
            if children is None or not tag:
                with self.assertRaises(ValueError):
                    ParentNode(tag, children, props).to_html()  # pyright: ignore[reportArgumentType]
            else:
                node = ParentNode(tag, children, props)
                self.assertEqual(node.to_html(), expected)
