from htmlnode import HTMLNode
from textnode import TextNode

if __name__ == "__main__":
    print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    print(HTMLNode("p", "hi", None, {"class": "test"}))
