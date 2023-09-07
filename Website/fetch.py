import requests

def login(username, password):
    login_url = 'https://lootx.com/login'  # Replace with the actual login URL of the website

    # Form data to be sent as part of the login request
    data = {
        'username': username,
        'password': password
    }

    # Perform the login POST request
    response = requests.post(login_url, data=data)

    # Check if the login was successful (you may need to adjust this based on the website's response)
    if response.status_code == 200:
        print("Login successful!")
        # You can now proceed to perform other actions after successful login
    else:
        print("Login failed. Status code:", response.status_code)

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with your actual login credentials
    username = 'SuperNova3D'
    password = 'jalil2024'
    login(username, password)

def giveaway(hourly):
    giveaway_url = 'https://lootx.com/giveaways/hourly'

    hourly = button

    responseGiveAway = requests.post(giveaway_url)
    if responseGiveAway.status_code == 200:
        print("Giveaway entered!")
    else:
        print("Captcha verification failed :(")
if __name__ == "__main__":
    giveaway(hourly)
