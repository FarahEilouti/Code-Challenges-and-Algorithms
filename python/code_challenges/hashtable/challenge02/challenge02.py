# Write here the code challenge solution

def find_first_repeated_word(s):
    ''' 
    function to find the first repeated word in a sentence, 
    where we split the string into a list of words and store it
    in a dictionary
    '''

    # Splitting the string and storing it in a dictionary

    words = s.split()

    word_count = {}

    # loop through the list of words
    for word in words:
        
        if word not in word_count:
            word_count[word] = 1
            
        else:
            word_count[word] += 1

    
    for word in words:
        if word_count[word] > 1:
            return word

    return None


if __name__ == "__main__":

  string1 = "This is a test string with no repeated words"
  print(find_first_repeated_word(string1)) #None

  string2 = "The quick brown fox jumps over the quick dog"
  print(find_first_repeated_word(string2)) # quick

  string3 = "this is a trial to know which is the first repeated word in a sentence"
  print(find_first_repeated_word(string3)) # is

  string4 = "Write a function that will take a string as a parameter and return the first repeated word in that string."
  print(find_first_repeated_word(string4))  # a