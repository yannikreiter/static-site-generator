from leafnode import LeafNode
from parentnode import ParentNode


def main():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("div", [
                LeafNode("a", "https://boot.dev", {"class": "website"}),
                LeafNode("p", "Some paragraph text")
            ])
        ],
    )
    html = node.to_html()
    print(html)


main()
