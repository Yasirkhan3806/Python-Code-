#My first module or you can say package
def main():
  hello("World")
  goodbye("mfs")
def hello(name):
    print("hello " + name)

def goodbye(name):
    print("Goodbye " + name)
if __name__ == "__main__" : #if __name__ == __main__ this means that main will be set to name when we execute the file the main function contain but when we use that file as module the main function will not be called
    main()