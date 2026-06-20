from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main():
    test = ParentNode(
        "h1",
        [
            LeafNode("p", "text"),
            LeafNode("b", "bold"),
            LeafNode(
                "a", "link", {"href": "https://www.youtube.com", "target": "_blind"}
            ),
        ],
        {"href": "https://www.boot.dev"},
    ).to_html()
    print(test)


if __name__ == "__main__":
    main()
