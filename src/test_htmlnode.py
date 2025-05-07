import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		node = HTMLNode("div", "Hello, world!", None, props={"href": "https://boot.dev", "class": "greeting"})
		self.assertEqual(node.props_to_html(), ' href="https://boot.dev" class="greeting"')

	def test_values(self):
		node = HTMLNode("div", "Hello, world!")
		self.assertEqual(node.tag, "div")
		self.assertEqual(node.value, "Hello, world!")
		self.assertEqual(node.children, None)
		self.assertEqual(node.props, None)

	def test_repr(self):
		node = HTMLNode("div", "Hello, world!", None, props={"href": "https://boot.dev", "class": "greeting"})
		self.assertEqual(
			node.__repr__(),
			"HTMLNode(tag: div, value: Hello, world!, children: None, props: {'href': 'https://boot.dev', 'class': 'greeting'})"
		)

if __name__ == "__main__":
	unittest.main()
