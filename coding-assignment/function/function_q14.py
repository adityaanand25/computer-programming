Convert markdown text into HTML format.
import markdown
def convert_markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)
md_text = "# Hello World\nThis is markdown text."
html_output = convert_markdown_to_html(md_text)
print(html_output)
