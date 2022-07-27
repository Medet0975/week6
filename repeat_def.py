def yell(text: str):
    return text.upper() + "!"

# print(yell("hello"))

# shout = yell
# print(shout.__name__)
# print(yell.__name__)
# del yell
# print(shout('hey, vernis!!!'))

def greet(func):
    result = func("hello")
    return result
# print(greet(yell))

# def speak(text):
#     def whisper():
#         return text.lower() + "..."
#     return whisper()
# result = speak("HELLO")
# print(result())
# print(speak("HELLO"))

# def speak(volume):
#     def whisper(text):
#         return text.lower()
#     def shout(text):
#         return text.upper()
#     if volume > 5:
#         return shout
#     else:
#         return whisper
#
# result = speak(3)
# print(result("hey, this is a text"))

def make_adder(x):
    def add(n):
        x = 0
        for n in range(1,2**5):
            x += n
        return x
    return add

plus_3 = make_adder(3)
print(plus_3(23))
