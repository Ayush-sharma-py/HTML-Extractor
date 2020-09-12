"""
#Creating the html file
def create_html_doc(name,PIL_open):
    main_tags = ["<html>","<head>","<title>","<body>"]
    additional_tag = ["<p>"]

    with open(name + ".html","a+") as f:
        f.write("<html>")
        f.write("<head><title> Rename </title></head>")

        for i in extract_text(PIL_open).split("\n\n"):
            if "\n" in i:
                continue

        f.write("</html>")
        f.close()
"""


"""
input = images in numpy , text transcribed of images (raw for now maybe list seperated by \n or \n\n) 
output = list or numpy array() of list of pytesseract to find the text data
to find the paragraph in images

"""