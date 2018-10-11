print("\t\tmodule name = ",__name__)
if __name__ == "__main__" : 
    name = input("Enter your name : " )
    age = input("Enter your age : ")
    country = input("Enter your country : ")
    language = input("Enter your language : ")

    info = { 
            'name'  : name,
            'age' : age,
            'country' : country,
            'language' : language,
            }

    print("Here is your info dictionary : ")

    print(info)
