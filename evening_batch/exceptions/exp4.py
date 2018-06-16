def main():
    try :
        path = input("Enter your path ")
        fp = open(path)
    except FileNotFoundError as error:
        print("Ther is an Error!!",error)
        print("Check your path it should be valid")
        main()
    else:
        print(fp.read())

if __name__ == "__main__" :
    main()
