import json
def save_contact(contact: dict, filename: str):
    with open(filename, "a") as f:
        json.dump(contact, f)


print("This program saves a Contact in your Contacts List")
name = ("sophie dee")
email = ("gjgjggjgjg")
phone = ("0131316868")
relationship = ("my love")

contact = {
    "name": name,
    "email": email,
    "phone": phone,
    "relationship": relationship
}

save_contact(contact, "contacts.json")