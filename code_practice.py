def isVowel(character): # function to check whether input character is a vowel
  character = character.lower() # convert character to lower case so upper cases can also be handled
  vowels = "aeiou" # string containing all vowels

  if character in vowels: # check if given character is in vowels
    return 1
  else:
      return 0

def countVowels(string): # function that returns the count of vowels
	count = 0
	for i in range(len(string)): 
		if isVowel(string[i]) : # check if character is vowel 
			count += 1
	return count 

# Driver code 
string = "Educative"
print(countVowels(string)) 