import requests

print("Welcome to Jinda's Email Verification Python Application!")
email = input("Please enter in the email address in its full form (name@example.com): ")
url = "https://email-checker.p.rapidapi.com/verify/v1"

querystring = {"email": email}

headers = {
    'x-rapidapi-host': "email-checker.p.rapidapi.com",
    'x-rapidapi-key': "2c55019311msha703d4f4d477ac6p1b0a95jsn20b3f6f65c02"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response.text.split(",")

print(response.text)













