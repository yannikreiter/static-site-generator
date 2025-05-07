from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
	text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	html_node = HTMLNode("p", "This is a paragraph", None, { "class": "bold" })
	print(text_node)
	print(html_node)

main()