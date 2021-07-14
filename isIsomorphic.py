'''Given two strings s and t, determine if they are isIsomorphic. Two strings s and t are isIsomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Examples:

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

# U
# Does case sensitivity matters?
# Does spaces matters 
# Does time/space comp matters
# What if it is a null input ? do i just return a null output?

# M
# Input: 
s = "paper"
t = "title"

# dict = { p : t, a : i, p : t, e : l, r : e}
#create dictionary

def isIsomorphic(s,t):
 
  dicti = {}

  if len(s) !=  len(t):
    return False
  for i in range(len(s)):
    key = s[i]
    val = t[i]
    if key in dicti:
      if dicti[key] != val :
        return False
    else:
      dicti[key] = val
  return True

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo","bar"))
print(isIsomorphic("paper","title"))
print(isIsomorphic("","")) # true
print(isIsomorphic("add","dee")) # true
