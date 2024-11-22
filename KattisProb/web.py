import validators

x = input()
print(x)
valid = validators.url(x)
if(valid):
    print(True)
else:
    print(False)
