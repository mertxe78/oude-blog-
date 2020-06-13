import markdown2
from os import listdir
from os.path import isfile, join
path = 'posts'

def generate_index():
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files = sorted(files, reverse=True)
    files.remove('index.md')

    titles = []
    for f in files:
        f = f.replace(".md", "")
        titles.append(f[7:])
    
    posts = zip(files, titles)

    def print_ul(elements):
        html = '<h2>Artikelen</h2>\n<ul>\n'
        for link, title in elements:
            html = html + "<li><a href=\"" + title.lower() + ".html\">" + str(title) + "</a></li>\n"
        html = html + "</ul>\n"
        return html

    blogposts = print_ul(posts)
    

    html = markdown2.markdown_path('posts/index.md')

    with open('header.html', 'r') as file:
        header = file.read()

    with open('footer.html', 'r') as file:
        footer = file.read()

    f = open( 'index.html', 'w' )
    f.write(header + '\n' + html + '\n' + blogposts + '\n' + footer)
    f.close()

def generate_posts():
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files = sorted(files, reverse=True)

    titles = []
    for f in files:
        f = f.replace(".md", "")
        titles.append(f[7:])

    posts = zip(files, titles)

    for file, title in posts:
        html = markdown2.markdown_path('posts/' + file)

        with open('header.html', 'r') as file:
            header = file.read()

        with open('footer.html', 'r') as file:
            footer = file.read()

        f = open( title.lower() + '.html', 'w' )
        f.write(header + '\n' + html + '\n' + footer)
        f.close()

generate_index()
generate_posts()