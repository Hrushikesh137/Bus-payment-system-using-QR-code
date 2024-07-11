import qrcode

def generate_qr_code(content):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    return img


def main():
    you = input("Enter your current loction : ")
    youDict={"Loni":"a","Sangammner":"b","Sinner":"c","Kolhar":"d","Rahuri":"e","Nashik":"f"}
    Location=input("Enter your Destination loction : ")
    locDict={"Loni":"a","Sangammner":"b","Sinner":"c","Kolhar":"d","Rahuri":"e","Nashik":"f"}
    choice=youDict[you]
    computer=locDict[Location]
    if(you== Location):
        print("You are at current loaction")
    else:
        print(f"your Location is from {you} to {Location} ")
        if choice == 'f' and computer=="c":
            content = "You have to pay 30 rupees"
        elif choice == "f" and computer=="b":
            content="You Have to pay 50 rupees"
        elif choice == "f" and computer=="a":
            content="You Have to pay 70 rupees"
        elif choice == "f" and computer=="d":
            content="You Have to pay 100 rupees"
        elif choice == "f" and computer=="e":
            content="You Have to pay 120 rupees"
        elif choice == "c" and computer=="b":
            content="You Have to pay 30 rupees"
        elif choice == "c" and computer=="a":
            content="You Have to pay 60 rupees"
        elif choice == "c" and computer=="d":
            content="You Have to pay 80 rupees"
        elif choice == "c" and computer=="e":
            content="You Have to pay 100 rupees"
        elif choice == "b" and computer=="a":
            content="You Have to pay 40 rupees"
        elif choice == "b" and computer=="d":
            content="You Have to pay 60 rupees"
        elif choice == "b" and computer=="e":
            content="You Have to pay 80 rupees"
        elif choice == "a" and computer=="d":
            content = "You Have to pay 20 rupees "
        elif choice == "a" and computer=="e" :
            content = "You Have to pay 40 rupees "
        elif choice == "d" and computer=="e":
            content = "You Have to pay 30 rupees "
        else:
            print("Invalid choice")
            return
        
    
    qr_code = generate_qr_code(content)
    
    
    qr_code.save("qrcode.png")  
    qr_code.show() 

if __name__ == "__main__":
    main()
