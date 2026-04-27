import emoji

name = input("")

output = emoji.emojize(name, language='alias')
print(f"{output}")