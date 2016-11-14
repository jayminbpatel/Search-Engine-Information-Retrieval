def write_html(file_content, hashCode):
    filename = 'storage/' + hashCode + ".html"
    Html_file = open(filename, "w")
    Html_file.write(file_content)
    Html_file.close()