import requests



def signin(login:str, password:str):
    with requests.post("http://103.195.100.145:25595/online/user/login", data={
        "token":"nanoputazo",
        "alias":login,
        "password":password
    }) as a:
        auth_code = a.json()["auth_code"]
        id = a.json()["id"]

        return auth_code, id
def loadLevel(auth_code: str, id:str, level_id:str):
    with requests.post(f'http://103.195.100.145:25595/stage/{level_id}', data={
        "token":"nanoputazo",
        "discord_id":id,
        "auth_code": auth_code
    }) as a:
        return a.json()["result"]["archivo"]

def downloadLevel(link: str):
    with requests.get(link) as a:
        print(a.text)


def loop():
    try:
        print("please sign in! \"login\",\"password\"")

        userData = signin(*input('').split(','))

        downloadLevel(
            loadLevel(*userData, input("level id\n"))
        )
    except:
        return -1
while(1):
    loop()