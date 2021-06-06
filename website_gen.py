#!/usr/bin/env python

"""
	This program generates a website folder for you.
"""
import os


def website_generator(web_name, author_name, script, sheet):

    # Tags to be written to index.html file
    title_tag = f"<title>{web_name}</title>\n"
    meta_tag = f"<meta name='author' content='{author_name}'>"

    # Check if file exists in directory before creating
    if os.path.exists(web_name):
        return "File already exists."
    else:
        os.mkdir(web_name)
        os.chdir(web_name)

    # Create index.html file and write the tags to it
    with open('index.html', "x") as index_page:
        index_page.write(title_tag)
        index_page.write(meta_tag)

    # Create Javascript and/or CSS folder if user wants it
    if script.startswith("y"):
        os.mkdir("js")

    if sheet.startswith("y"):
        os.mkdir("css")

    os.chdir("..")
    # Print files in directory
    for name in os.listdir(web_name):
        full_name = os.path.join(web_name, name)
        print(f"Created {full_name}")

    return ""


# Input information
name = input("Site name: ")
author = input("Author: ")
js_dir = input("Do you want a folder for JavaScript? ").lower()
css_dir = input("Do you want a folder for CSS? ").lower()

# Call function
folder = website_generator(name, author, js_dir, css_dir)

print(folder)
