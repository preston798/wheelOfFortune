# Final Project
# Preston Hancock
# This will be a wheel of fortune game. The program will select a category that has a list attached to it with the correct word. The program will create a new list that shows only a couple of the characters and the rest blank. 
# The user will guess a constonant. If it is in the hidden list, they will appear on the actual list and money will be added to the user's account. The user can also buy a vowel. There will be another box where they can guess the entire word or phrase.
# The user will "spin" a wheel in the background to get money added to their account if they choose a letter correctly. 
# 
# The program will first initilize the GUI and select a a category from the dictionary. The dictionary will be stored in a .txt file.   

from tkinter.constants import COMMAND
from breezypythongui import EasyFrame, EasyFrame
import random


class WheelOfF(EasyFrame):
    
    def __init__(self): ##This creates the GUI for the programm and initilizes the wallet object and wheel object for use
        self.wheel = Wheel()
        self.wallet = Wallet(0)
        EasyFrame.__init__(self, title="Wheel of Fortune", width=1000, height=800)
        self.guessingPanel = self.addPanel(row = 0, column= 0, background = "red")
        inputPanel = self.addPanel(row = 1, column= 0, background = "blue")
        inputPanel.addLabel(text = "Spin the wheel", row = 0, column= 0, background = "gray")
        self.wheelOutput = inputPanel.addTextField(text = "", row = 0, column= 2, width = 50, state= "readonly")
        self.walletOutput = inputPanel.addTextField(text = str(self.wallet), row = 0, column= 3, state="readonly")
        inputPanel.addButton(row = 0, column = 1, text = "click here to spin wheel", command = self.spinW())
        inputPanel.addLabel(text="Enter a vowel to buy for $250", row = 1, column= 0) 
        self.inputVowel = inputPanel.addTextField(text = "", row = 1, column= 1)
        inputPanel.addButton(text="Purchase vowel", row =1, column=2,command= self.buyVowel())
        inputPanel.addLabel(text="Enter a constonant to try", row= 2, column=0)
        inputPanel.addTextField(text = "", row=2, column=1)
        inputPanel.addLabel(text = "Guess the entire phrase", row=3, column=0)
        inputPanel.addTextField(text = "", row=3, column=1)
        
    def spinW(self): ##This function spins the wheel and adds the money to the wallet. it sets the text in the corresponding boxes to what the user rolls and how much is in the wallet

        value = self.wheel.spin()
        self.wallet.addMoney(value)
        self.walletOutput.setText(self.wallet.getAmount())
        self.wheelOutput.setText(str(self.wheel))
        self.messageBox(title="Wheel", message="You spun the wheel")

    def buyVowel(self): #this function checks the box for a vowel and ensures the wallet has more then $250 to purchase one. IT subtracts the balance and updates the wallet
        if self.inputVowel.getText() in ["a", "e", "i" ,"o", "u"] and self.wallet.getAmount() > 250:
            self.wallet.minusMoney(250)
            self.walletOutput.setText(self.wallet.getAmount())
        else:
            return
    
    
    
class Wheel(object):  ##This is the object for the virtual wheel the user will spin, it has an upper bound and lower bound
    def __init__(self):
        self.lowerBound = 100
        self.upperBound = 2500
        self.increment = 100
        self.value = 0
    
    def spin(self): ##This function spinds the wheel by selecting a random integer in the lower and upper bound
        self.value = random.randint(self.lowerBound, self.upperBound)
        return self.value

    def __str__(self): ##The str function on this object returns the value
        return str(self.value)


    

class Wallet(object): #The wallet object is wehre the users money is stored
    def __init__(self, amount = 0): 
        self.amount = amount
    def addMoney(self, cash): #Mutator function to add money
        self.amount = self.amount - cash
    def minusMoney(self, cash): #mutator function to subtract money
        self.amount =- cash
    def getAmount(self): #accessor function to view the money
        return self.amount
    def __str__(self): #returns the str for the amount
        return str(self.amount)


class Phrase(object):  #This object handles extracting the phrases and hints from a text file to be used in comparing and outputing in the GUI
    def __init__(self, filename):
        self.filename = filename
   
   
    def importFile(self): #This functions imports the file and selects a random line
        choose = random.randint(1, 6)
        count = 1
        f = open(self.filename, 'r')
        for line in f:
            count += 1
            if count == choose:
                return line 









def main():
    
    
    WheelOfF().mainloop()
    

if __name__ == "__main__":
    main()

