import random

def isim_olusturucu():
    first_name = ["Hatice","Umut","Simge","Melek"]
    last_name = ["Adiguzel","Ozdemir","Yılmaz","Or"]
    return "{} {}".format(random.choice(first_name),random.choice(last_name))

for i in range(10):
    print(isim_olusturucu())