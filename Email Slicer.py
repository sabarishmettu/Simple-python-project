# Python program to fetch username and domain name from an email

# Taking the email as an input
email = input("Enter the email: ")

# Splitting the email into two strings using @ as the divider
username, domain_name = email.split('@')

# Printing the username and domain name
print("Username:", username)
print("Domain name:", domain_name)