#Encode User Name
str= input("Enter Username: ").encode('utf-8')
hex_str = str.hex()
print(f"Encoded Username: {hex_str}")
notes = open("username.txt", 'a')
notes.write(f"{note}")
