# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = "Hello!!!, he said (!---and went."

# To take input from the user
# str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)