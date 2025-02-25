# Given a string , the task is to convert string into integer
# Example A:
# input : "Three hundred thousand"
# output : 300,000

# Example B:
# input : "Five hundred million"
# output : 300,000

def words_to_number(s):
    # Define the mappings for numbers
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, 
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, 
        "fourteen": 14, "fifteen": 15, "sixteen": 16, 
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }
    
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, 
        "fifty": 50, "sixty": 60, "seventy": 70, 
        "eighty": 80, "ninety": 90
    }
    
    scales = {
        "hundred": 100, "thousand": 1000, 
        "million": 1000000, "billion": 1000000000
    }
    
    # Split the input string into words
    words = s.lower().replace('-', ' ').split()
    
    # Initialize current and result to accumulate the number
    current = result = 0
    
    # Iterate through each word
    for word in words:
        # If the word is in units, add its value to current
        if word in units:
            current += units[word]
        
        # If the word is in tens, add its value to current
        elif word in tens:
            current += tens[word]
        
        # If the word is "hundred", multiply current by 100
        elif word == "hundred":
            current *= scales[word]
        
        # If the word is in scales, scale the current value and add to result
        elif word in scales:
            result += current * scales[word]
            current = 0
            
    # Return the final result by adding any remaining value in current
    return result + current

print(words_to_number("Three hundred thousand"))
print(words_to_number("Five hundred million"))