def checklist(thelist):
    if isinstance(thelist, list):
        for item in thelist:
            checklist(item)
    else:
        print(thelist)


print('helo!')
print('BOTAFOGO!')
