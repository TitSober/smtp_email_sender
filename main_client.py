from smtp_client import send_email
import json

f = open("emails.json", "r")

e_list = json.loads(f.read())
f.close()

print(e_list)
address = ""
y_n = int(input("vnesi številko v imeniku za email ali pritisni 0 za ročno vnašanje: "))
if y_n == 0:
    address = input("Prosim vnesi e-mail naslov na katerega hočeš poslati: ")
else:
    address = e_list.get(str(y_n))
    print(address)

    



#Formatira sporočilo in zadevo
message = 'Subject: {}\n\n{}'.format(input("Prosim vnesite zadevo: "), input("Prosim vnesite sporočilo: "))



#Preverja če je email ze v imeniku
#popravi preverjanje

try:
    for i in range(len(e_list)):
        x = str(i+1)
        if address == e_list[x]:
            print("Email naslov je ze v imeniku:")
            send_email(message, e_list[x])
            break
        elif address != e_list[x] and int(x) == len(e_list):
            print("Tega naslova ni v imeniku! Dodajam...")
            e_list[len(e_list)+1] = address
            print("Dodano.")
            send_email(message, address)
except RuntimeError or UnicodeEncodeError:
    err = "runtime error or uniEror"
    print(err)

#ToDo popravi pisanje v .txt file
d = open('emails.json', 'w')
json.dump(e_list, d)	
d.close()


