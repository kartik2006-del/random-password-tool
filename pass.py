import random
import string
print('******** welcome to the random password generator ********'.title().center(120))
length=int(input('enter the length of password : '))

all_chars=string.ascii_letters+string.punctuation+string.digits

password="".join(random.choices(all_chars,k=length))

print('your random password is : ', password)