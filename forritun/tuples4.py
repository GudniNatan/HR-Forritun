def get_emails():
    address_list = list()
    email = input("Email address: ")
    while email != "q":
        address_list.append(email)
        email = input("Email address: ")
    return address_list

def get_names_and_domains(email_list):
    return [tuple(x.split("@")) for x in email_list]

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)