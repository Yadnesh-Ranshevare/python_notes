import markdown
from markdown import extensions

def convert_md_to_txt():
    # Read the markdown file
    with open('example.md', 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert markdown content to HTML (using markdown module)
    html_content = markdown.markdown(md_content)

    # You can strip HTML tags here if you need just plain text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    plain_text = soup.get_text()

    # Write the plain text to a .txt file
    with open('output.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(plain_text)

    print(f"Converted MD to TXT and saved to")

convert_md_to_txt()

# f = open("sample.txt",'r')
# data = f.read()
# print(data)
