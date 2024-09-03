a = {
    "name" : "Ash",
    "contact" : [
        {
            "papa" : 896426151612,
            "maa" : 45698221336,
            "brother" : 5469823552,
        }
    ]

}

#aim is to fetch the "maa" key value
#this is a bit noob way
contacts = a.get("contact")
contacts = contacts[0]
print(contacts.get("maa"))



#this is intermediate way
for numbers in a["contact"]:
    print(numbers)
    print(numbers["maa"]) #here we fetched the key "maa"



#in case of multiple dict inside list
b = {
    "name" : "Ashish",
    "contact" : [
        {"papa" : 896426151612, "gmail" : "papa@gmail.com"},
        {"maa" : 45698221336, "gmail" : "maa@gmail.com"},
        {"brother" : 5469823552, "gmail" : "bro@gmail.com"},
    ]

}
#we want to fetch all the gmails
print()
for mails in b["contact"]:
    print(mails)
    print(mails["gmail"])
