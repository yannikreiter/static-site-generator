import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "Some text")])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_children(self):
        children = [
            LeafNode("div", "Some unstyled text"),
            LeafNode("div", "Some styled text", {"class": "bold"})
        ]
        self.assertEqual(
            ParentNode("div", children).to_html(),
            '<div><div>Some unstyled text</div><div class="bold">Some styled text</div></div>'
        )

    def test_to_html_with_grandchildren(self):
        grand_children = [
            LeafNode("p", "Some unstyled text"),
            LeafNode("p", "Some styled text", {"class": "bold"})
        ]
        children = [
            ParentNode("div", grand_children),
            LeafNode("i", "Some italic text")
        ]
        self.assertEqual(
            ParentNode("div", children).to_html(),
            '<div><div><p>Some unstyled text</p><p class="bold">Some styled text</p></div><i>Some italic text</i></div>'
        )


if __name__ == "__main__":
    unittest.main()
