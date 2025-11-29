def chatbot():
    print("Hi i am himaAI! how can i assist you?🤖")
    while True:
        user=input("you:")
        if user in ["hi","hello","hey"]:
            print("HIMAAI: HI! how can i help you?")
        elif user =="how r u?":
            print("HIMAAI:  I am fine,tq i hope your doing great 👩‍💻")
        elif user=="who are you?":
            print("HIMAAI: i am a chatbot will help you and guide you😊🤖")
        elif user=="what is python?":
            print("HIMAAI: python is object oreinted programming languge with easy syntax and dynamic semantics")
        elif user=="who invented python?":
            print("HIMAAI:  python was invented by guido von rassum in 1991")
        elif user=="what is the weather report":
            celsius=int(input("enter temperature: "))
            fahrenheit=(celsius*9/5)+32
            if 32 <= fahrenheit < 50:
                 print("HIMAAI: Weather is: Cold / Autumn")
            elif 50 <= fahrenheit < 70:
                print("HIMAAI: Weather is: Cloudy")
            elif 70 <= fahrenheit < 90:
                print("HIMAAI: Weather is: Hot")
            elif fahrenheit >= 90:
                print("HIMAAI: Weather is: Very Hot / Summer")
            else:
                print("HIMAAI: Weather is: Freezing / Snowy")
        elif user=="give the harrypotter movie sequence names in order":
                print("HIMAAI: Harry Potter and the Philosopher’s Stone, Harry Potter and the Chamber of Secrets, Harry Potter and the Prisoner of Azkaban, Harry Potter and the Goblet of Fire, Harry Potter and the Order of the Phoenix, Harry Potter and the Half-Blood Prince, Harry Potter and the Deathly Hallows – Part 1, Harry Potter and the Deathly Hallows – Part 2.")
        elif user=="could u suggest the best one among this?":
            print("HIMAAI: If you want the best emotional ending: 👉 Harry Potter and the Deathly Hallows Part 2")
        elif user=="bye":
            print("HIMAAI: Chatbot:bye! Have a great day 😊")
            break
        
        else:
            print("HIMAAI: keyboard smash⌨️")
            
chatbot()
            
   
            
