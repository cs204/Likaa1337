def main():
    greetting = input("Приветствие: ")
    value(greetting)

def value(greeting):
    greetting = greeting.lower()
    if greetting.startswith ("здравствуйте"):
        print ("$0")
    elif greetting.startswith ("з"):
        print ("$20")
    else:
        print ("$100")

if __name__ == "__main__":
   main()

