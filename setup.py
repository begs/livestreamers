from configparser import ConfigParser

def runSetup():
    config_object = ConfigParser()
    accessToken = input("Enter your access token: ")
    clientId = input("Enter your client id: ")
    userId = input("Enter your user id: ")

    config_object["config"] = {
        "accessToken": accessToken,
        "clientId": clientId,
        "userId": userId
    }

    with open('config.ini', 'w') as conf:
        config_object.write(conf);
