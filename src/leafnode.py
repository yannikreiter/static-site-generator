from htmlnode import HTMLNode


class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value == None:
			raise ValueError("All leaf nodes must have a value")

		if self.tag == None:
			return self.value

		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

		def __repr__(self):
			return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"
