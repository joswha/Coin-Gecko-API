import requests
import json
import time
from pathlib import Path

#Create favourite.txt
Path('favourite.txt').touch()

def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

while True :

    option = input("Here are your options:\n   1.List all coins. \n   2.List your favourite coins. \n   3.Add a favourite coin. \n   4.Check a coin(by id). \n   5.Exit\n")

    #List all coins
    if int(option) == 1:
        print("\nYou have selected option nr."+option+"! Here you have a list of all the coins available.\n")
        time.sleep(0.2)
        response = requests.get("https://api.coingecko.com/api/v3/coins/list")
        jprint(response.json())

    #List favourite coins
    elif int(option) == 2:
        print("\nYou have selected option nr."+option+"! Here you have a list of all your favourite coins:\n")
        time.sleep(0.2)
        #print("bitcoin\nethereum\nma-ta")
        print(open('favourite.txt').read())

    #Add favourite coins
    elif int(option) == 3:
        print("\nYou have selected option nr."+option+"! You can now add a coin to your favourite list:\n")
        time.sleep(0.2)
        new_favourite = input("Add a coin id: ")
        file = open("favourite.txt", "a")
        file.write(new_favourite + "\n")
        file.close()
        print("\nYou added "+new_favourite+" to your favourite list, would you like to add another coin?\n")
        time.sleep(0.2)
        new_coin = input("Yes/No\n")
        while new_coin == "Yes":
            new_favourite = input("Add a coin id: ")
            file = open("favourite.txt", "a")
            file.write(new_favourite + "\n")
            file.close()
            time.sleep(0.2)
            print("\nYou added "+new_favourite+" to your favourite list, would you like to add another coin?\n")
            another_one = input("Yes/No\n")
            time.sleep(0.2)
            if(another_one) == "No":
                break
        print("Alright... see ya\n")

    #Check a certain coin
    elif int(option) == 4:
        checked_4 = "Yes"
        id_4 = input("\nYou have selected option nr."+option+"! Which coin would you like to check?\n")
        time.sleep(0.2)
        coin_response = requests.get("https://api.coingecko.com/api/v3/coins/"+id_4)
        jprint(coin_response.json())
        
        while checked_4 == "Yes":
            print("\nYou have checked "+id_4+". Would you like to check another coin?\n")
            time.sleep(0.3)
            checked_4 = input("Yes/No\n")
            if checked_4 != "Yes":
                print("Alright... see ya\n")
                time.sleep(0.3)
                break
            id_4 = input("Which coin would you like to check?\n")
            time.sleep(0.3)
            coin_response = requests.get("https://api.coingecko.com/api/v3/coins/"+id_4)
            jprint(coin_response.json())
    
    #Exit
    elif int(option) == 5:
        print("\nSee ya!\n")
        break     
    
    else: print("\nOut of bounds\n")