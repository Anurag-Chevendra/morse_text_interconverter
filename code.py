

alphaToMorse_dictionary={
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...',
    'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----','2':'..---','3':'...--',
    '4':'....-','5':'.....','6':'-....', '7':'--...','8':'---..','9':'----.', '0':'-----',', ':'--..--', '.':'.-.-.-',
    '?':'..--..','/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'
}
morseToAlpha_dictionary={
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0','.-.-.-':'.', '..--..':'?', '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')','--..--':',' , "":""

}
def encode(i):
    return alphaToMorse_dictionary[i]
def decode(i):

    return morseToAlpha_dictionary[i]

print("=============================================================")
while(True):
    print("Do you want to 1)Convert text to Morse code ")
    print("               2)Convert Morse code to Text ")
    q1 = input()
    if (q1 == "1"):
        s = input("Enter the sentence to be converted to Morse Code : ")
        s = s.upper()
        ss = ""
        for i in s:
            if (i == ' '):
                ss = ss + '/ '
            else:
                ss = ss + encode(i) + " "

        print(ss)
        print("Do you wish to continue?")
        print("1)Yes")
        print("2)No")
        choice=input()
        if(choice=="1"):continue
        else:break
    elif (q1 == "2"):
        s = input("Enter the Morse code to be converted to normal Text :  ")
        ss = ""
        test = ""
        for i in s:
            if (i != "/"):
                if (i != ' ' or i == ""):
                    test = test + i
                elif (i == ' '):
                    ss = ss + decode(test)
                    test = ""

            elif (i == "/"):
                ss = ss + " "

        print(ss)
        print("Do you wish to continue?")
        print("1)Yes")
        print("2)No")
        choice = input()
        if (choice == "1"):
            continue
        else:
            break


