#!python
print("content-type: text/html")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, Python'
print('''<!doctype html>
<html>
<head>
    <title>Coding Diary</title>
    <meta charset="UTF-8">
</head>

<body>
    <h1><a href="index.py">kyu</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" 
        placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>'''.format(title=pageId, desc=description, listStr=view.getList()))