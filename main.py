from replit import clear
from art import logo,winner
print(logo)

#HINT: You can call clear() to clear the output in the console.
dict = {}
# def add_new_bidder(name, bid):
def bit_me(names,bits):
    new = {}
    new[names] = bits
    dict.update(new)
#hihest biter 
def high_bit(dict):
  high = 0
  winner = list(dict.keys())[0]
  for key in dict:
    if dict[key]>high:
      high = dict[key]
      winner = key
  print(f"winner is {winner} with {high}")

bool = 1
while bool == 1:
  name = input("what is your name?")
  bit= int(input("what is your bit?"))
  bit_me(name,bit)
  choise = input("do you  want to continue? y/n")
  if choise == 'n':
    bool = 0
  else:
    clear()

print(dict)
print(winner)
high_bit(dict)
