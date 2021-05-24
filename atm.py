
import pyttsx3

engine=pyttsx3.init()
voices= engine.getProperty('voices')                     # to change voice 
engine.setProperty('voice', voices[len(voices)-2].id)    # female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def main():
	accountHolderName=['Jatin','Ekta', 'Saloni', 'Akshita', 'Anurag']
	accountNumber=['0001','0002','0003', '0004', '0005']
	pinNumber=['7568','9876', '5674', '7328', '9510']
	balance=[1000,200000,145000,76000,10]
    
	flag= False
	for i in range(0,9):
        
		print("""
		
		
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
||                  _____            _____   _____                 _____       ||
||   \          /  |        |       |       |     |    /\  /\     |            ||
||    \        /   |_____   |       |       |     |   /  \/  \    |_____       ||
||     \  /\  /    |        |       |       |     |  /        \   |            ||
||      \/  \/     |_____   |_____  |_____  |_____| /          \  |_____       ||
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
Welcome to atm system
		""")
		speak("Welcome to atm system")	
		speak("please enter your name")
		name= input("enter your name: ").lower()
		pin= 0000
		index=0
		count =0
		for name1 in accountHolderName:
            
            if name1 == name:
                index=count
				speak("please enter your pin code.")
                pin= input("\nenter pin: ")
            count +=1

        if pin==pinNumber[index]:
            flag = True
        else:
            speak("sorry! your pin is invalid.")
            print("invalid pin")
            flag =False
            continue
        if flag==True: 
            speak("Your account number is {}".format(accountNumber[index]))
            print("\nYour account number is: ",accountNumber[index])
            speak("Your account balace is rupees only {}".format(balance[index]))
            print("\nYour account balace is: Rs.",balance[index])
            speak("Do you want to deposit or draw cash.")
            choice= input("\nDo you want to deposit or draw cash (deposit/draw/no):")
            if choice=="draw":
                speak("please Enter the amount you want to darw.")
                amount= input("\nEnter the amount you want to darw: ")
                try:
                    amount=int(amount)
                    if amount>balance[index]:
                        raise
                except:
                        speak("your amount is invalid")
                        print("invalid amount.")
                        continue
                        
                newBalance=balance[index]-amount
                balance.remove(balance[index])
                balance.insert(index,newBalance)
                speak("Your available balance is {} rupees only".format(newBalance))
                print("\nYour available balance is: ", newBalance)
                speak("thankyou for banking.")
            if choice=="deposit":
                speak("Enter the amount you want to deposit")
                amount= input("\nEnter the amount you want to deposit: ")
                try:
                    amount=int(amount)
                    if amount>balance[index]:
                        raise
                except:
                        speak("your amount is invalid")
                        print("invalid amount.")
                        continue
                        
                newBalance=balance[index]+amount
                balance.remove(balance[index])
                balance.insert(index,newBalance)
                speak("Your available balance is {} rupees only".format(newBalance))
                print("\nYour available balance is: ", newBalance)
                speak("thankyou for banking.")
            

              
main()            