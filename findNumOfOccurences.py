'''Implement a method to find the number of occurrences of any given word in a book. A word is represented as a string and a book is represented as an array / list of strings.
Optimize the method to be called multiple times.

Book: [" The", "dog", "jumped", "in", "the", "dog", "house" ...]
Word: "dog"  →  Occurrences: 2
'''

book = [" The", "dog", "jumped", "in", "the", "dog", "house"]
word = "dog"

# U
# Does spaces in the word matters
# Does lower case upper case matter
# what if input is null
# does space matters or time constraint

# M
# simple for loop to check the word in list T = O(N) S= O(1)

#using dictionary to keep travh of counter as value if key is aready in the dictionary than count++


# P
#initializing dictionary : words to their counts
# create a dictionary 

# loop through array
#   check if current word is in dictionary 
#     if it is 
#       increase counter by 1
#.     else
#       put it in dict 


#I

def initializeCounters(book):
  # create a dictionary 
  dict ={}

  # loop through array
  for currWord in book:
  #   check if current word is in dictionary 
    currWord = currWord.strip().lower()
    if currWord in dict:
  #     if it is 
      dict[currWord] += 1
  #       increase counter by 1
    else:
      dict[currWord] = 1
  return dict

def returnCount(dictNew, string):
  return dictNew[string.strip().lower()]



dictNew = initializeCounters(book)
ans = returnCount(dictNew, "dog")

print(ans)
print(returnCount(dictNew,"The"))

try:
  print(returnCount(dictNew,"them"))
except:
  print("Invalid word")

print(returnCount(dictNew,"The"))
