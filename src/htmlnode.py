class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        props_html = ""
        for k, v in self.props.items():
            props_html += f" {k}={v}"

        return props_html

    def __repr__(self) -> str:
        children_repr = ""
        if self.children is not None:
            children_repr = self.children.__repr__()

        return f"<{self.tag}{self.props_to_html()}>{children_repr}</{self.tag}>"
