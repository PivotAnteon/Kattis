import validators

x = input()
valid = validators.url(x)
print(valid)
