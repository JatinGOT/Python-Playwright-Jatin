x = "Please email us at mentor@rahulshettyacademy.com with below template to receive response "
b = x.split("at ")
print(b)
print(b[1])
v = b[1].split(" ")[0]
print(v)
print("-".join(v))