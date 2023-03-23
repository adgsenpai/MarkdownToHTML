import markdown
import pdfkit 

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.tables'])

# This is the template for the html file change the template.html to your liking
def CompileMarkdownToHTML(markdown_text,filename):
    html = markdown_to_html(markdown_text)
    with open("template.html", "r") as f:
        template = f.read()
    template = template.replace("{{content}}", html)
    template = template.replace("{{title}}", filename.split(".")[0])
    # save to file
    with open(filename, "w") as f:
        f.write(template)

def HTMLTOPDF(filename):     
    # some weird retarded error pdfkit is giving but it works? thats the purpose of the try and catch 
    try:
        pdfkit.from_file(filename, filename.split(".")[0]+".pdf")
    except:
        pass
    

if __name__ == "__main__":
    # You may run the hello world example here?
    with open("helloworld.md", "r") as f:
        markdown_text = f.read()
    CompileMarkdownToHTML(markdown_text,"helloworld.html")       
    HTMLTOPDF("helloworld.html") 

    
 