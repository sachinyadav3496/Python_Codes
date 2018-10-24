def hello(*args):
    c = 1
    for var in args : 
        print(f"arg[{c}] = {var}")
        c = c + 1



if __name__ == "__main__" : 

    import sys
    args = sys.argv

    hello(*args)
