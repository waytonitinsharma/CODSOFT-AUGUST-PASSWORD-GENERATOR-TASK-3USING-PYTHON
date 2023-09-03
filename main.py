import random

uppercase_latters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_latters= uppercase_latters.lower()
digits="0123456789"
symbols="()[]{},;:.-/\\?+*#"
upper,lower,nums,syms = False,True, False, True

all=""

if upper:
    all +=uppercase_latters
if lower:
    all +=lowercase_latters
if nums:
    all+=digits
if syms:
    all +=symbols
lenght = 25
amount = 10


for x in range(amount):
    password="".join(random.sample(all,lenght))
    print(password)


