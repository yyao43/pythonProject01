import requests
response = requests.get("https://api.github.com/users/octocat")
print("login: ",response.json()["login"])

def main():
    print("Hello from py-venv-proj1, created by UV ! from main()")


if __name__ == "__main__":
    main()
