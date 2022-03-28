titlee = input()
content = input()

title_output = f"""<h1>
    {titlee}
</h1>"""
print(title_output)
content_output = f"""<article>
    {content}
</article>"""
print(content_output)
comment = input()
while not comment == "end of comments":
    comment_output = f"""<div>
    {comment}
</div>"""
    print(comment_output)
    comment = input()