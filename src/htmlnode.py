class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props == None:
            return ""

        html_string = ""
        for property in self.props.keys():
            html_string += f' {property}="{self.props[property]}"'

        return html_string

    def __repr__(self) -> str:
        return f"HTMLNode:\n\tTag: {self.tag}\n\tValue: {self.value}\n\tChildren: {self.children}\n\tProps: {self.props}"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ):
        super(LeafNode, self).__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        prop_string = super().props_to_html()
        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode:\n\tTag: {self.tag}\n\tValue: {self.value}\n\tProps: {self.props}"


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None
    ):
        super(ParentNode, self).__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        if self.children is None:
            raise ValueError("No children given.")

        html_string = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string
