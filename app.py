
class Bier:
  def __init__(self, bier_name: str, bier_type: str) -> None:
    self.bier_name = bier_name
    self.bier_type = bier_type

class BierMitHerkunft(Bier):
  def __init__(self, bier_name: str, bier_type: str, herkunft: str) -> None:
    super().__init__(bier_name, bier_type)
    self.herkunft = herkunft

def main():
  """Das is Philipp's DocString!"""
  print("ich bin main!")
  b : Bier = Bier("Zipfer", "Marzen")
  print(b.bier_name)

  b2 : BierMitHerkunft = BierMitHerkunft("Gösser", "Martze", "Goess")
  print(b2.bier_name)
  print(b2.herkunft)

def bla():
  return "bla!" + "fasel"

# this is my comment!
main()
print(bla())

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict.keys()))

import datetime

dd:datetime.datetime = datetime.datetime(2023,5, 6)
print(dd)

import json


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 

print(json.dumps((1,"a"))) 
