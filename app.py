import markdown

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.tables'])

def CompileMarkdownToHTML(markdown_text,filename):
    html = markdown_to_html(markdown_text)
    with open("template.html", "r") as f:
        template = f.read()
    template = template.replace("{{content}}", html)
    template = template.replace("{{title}}", filename.split(".")[0])
    # save to file
    with open(filename, "w") as f:
        f.write(template)

if __name__ == "__main__":
    with open("helloworld.md", "r") as f:
        markdown_text = f.read()
    CompileMarkdownToHTML(markdown_text,"helloworld.html")    
