from htmlnode import HTMLNode
from textnode import TextNode

if __name__ == "__main__":
    print(TextNode(text="This is a text node", text_type="bold", url="https://www.boot.dev"))
    p_node = HTMLNode(tag="p", value="hi", children=None, props={"class": "test", "id": "wew"})
    print(p_node)
