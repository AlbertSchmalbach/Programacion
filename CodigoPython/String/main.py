import string
from string import Template

# Constantes
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.octdigits)
print(string.hexdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)


# Plnatillas
tmpl = Template('$lang is the best programming language in the $place!')
tmpl.substitute(lang="Python", place="World")
print(tmpl)

urlbase = Template('https://python.org/3/library/$module.html')

for module in ('string', 're', 'difflib'):
    url = urlbase.substitute(module=module)
    print(url)