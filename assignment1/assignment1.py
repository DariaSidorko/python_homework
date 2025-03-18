# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

# Examples:
print(hello())


# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Examples:
print(greet("Sam"))


#Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation."
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"   

# Examples:
print(calc(10, 25))  
print(calc(150, 0, "multiply"))  
print(calc("String", 5))  

# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return "Invalid data type requested."
    except ValueError:
        return f"You can't convert {value} into a {data_type}."   

# Examples:
print(data_type_conversion("325", "int"))
print(data_type_conversion("111", "string"))
print(data_type_conversion("String", "float"))

#Task 5: Grading System, Using *args
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        average = sum(args) / len(args)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    except (TypeError, ValueError):
        return "Invalid data was provided."

# Examples:
print(grade(90, 85, 88))  
print(grade(70, 75, 80))  
print(grade("90", 85))   


#Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Examples:
print(repeat("Hello", 5)) 
print(repeat("Thanks", 2))    


#Task 7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs):
    try:
        if not kwargs:
            return "No student data provided."  

        if mode == "best":
            return max(kwargs, key=kwargs.get) 
        elif mode == "mean":
            return sum(kwargs.values()) / len(kwargs) 
        else:
            return "Invalid mode. Use 'best' or 'mean'."
    except (TypeError, ValueError):
        return "Invalid data was provided."

# Examples:
print(student_scores("best", Dan=66, Sam=25, Nik=33))  
print(student_scores("mean", Dan=66, Sam=25, Nik=33))  
print(student_scores("best"))  
print(student_scores("mean", Sam="C", Nik=55))  


#Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

    words = text.split()  # Split text into a list of words
    if not words:  
        return ""  # Return an empty string if input is empty

    # Capitalize the first and last word, and apply rules to others
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)  # Join the words back into a string

# Examples:
print(titleize("raleigh is the best city")) 
print(titleize("the lion king"))  
print(titleize("i see the cat"))  
print(titleize(""))  




# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    # Create the result string by checking each letter in the secret
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Examples:
print(hangman("apple", "ab"))   
print(hangman("home", "eph"))  


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = 'aeiou'
    words = text.split()
    result = []

    for word in words:
        if word.startswith(('qu')):  
            result.append(word[2:] + 'quay')
        elif word[0] in vowels:
            result.append(word + 'ay')
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                index += 1
            result.append(word[index:] + word[:index] + 'ay')
    
    return ' '.join(result)

print(pig_latin("apple"))          
print(pig_latin("banana"))  
print(pig_latin("quick brown fox"))
print(pig_latin("elephant queue"))
print(pig_latin("square"))