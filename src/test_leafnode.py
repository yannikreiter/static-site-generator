import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
	def test_to_html_div(self):
		leaf_node = LeafNode("div", "Hello, world!", { "href": "https://boot.dev", "class": "greeting" })
		self.assertEqual(
			leaf_node.to_html(),
			'<div href="https://boot.dev" class="greeting">Hello, world!</div>'
		)

	def test_to_html_no_tag(self):
		leaf_node = LeafNode(None, "Hello, world!", { "href": "https://boot.dev", "class": "greeting" })
		self.assertEqual(
			leaf_node.to_html(),
			"Hello, world!"
		)

	def test_to_html_no_value(self):
		leaf_node = LeafNode("p", None)
		self.assertRaises(ValueError, leaf_node.to_html)

if __name__ == "__main__":
	unittest.main()
