
from collections import Counter

def count_character_frequency(input_string):
  char_frequency = Counter(input_string)
  return char_frequency

input_string = input("Enter a string: ")

frequency_dict = count_character_frequency(input_string)

print("Character frequencies:")
for char, freq in frequency_dict.items():
    print(f"{char}: {freq}")

