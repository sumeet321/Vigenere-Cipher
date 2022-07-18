alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new = []

for i in range(26):
  alphabet = alphabet + [alphabet[0]]  # alphabet.append(alphabet[0])  <-- Didn't work
  # updated the alphabet list ^^^^^^^
  alphabet.remove(alphabet[0])
  new.append(alphabet)
  # print(alphabet) worked but was not inside of a list. However, new.append(alphabet) in line 9 did not work with alphabet.append(alphabet[0]) in line 6

key = input("Enter key: ").lower()
plain = input("Enter a message: ").lower()
plain = plain.replace(" ", "")
key = key.replace(" ", "")

encrypt = ""

for i in range(len(plain)):
  if len(key) < len(plain): # adding itself to the key string
      key += key
  if len(plain) > 25: # extending the list more to fit respectively
    new.append(alphabet)
  encrypt += new[new[0].index(key[i])][new[-1].index(plain[i])] #new[i][second index value]
  # new[0] because getting first value of list        new[-1] so first list is [b,c,d,e,f,g,...z]
    
print("\nCipher Text: " + encrypt)