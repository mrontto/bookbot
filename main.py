def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  total_characters = get_character_count(text)
  ordered_list_of_characters = ordered_dict_by_highest(total_characters)
  printed_report(book_path, num_words, ordered_list_of_characters)


def printed_report(book, num_words, ordered_list):
  print(f"---Begin report of {book}---")
  print(f"There are {num_words} words found in the document")
  print()
  for char_dict in ordered_list:
    # Get the first (and only) key from the dictionary
    char = list(char_dict.keys())[0]
    # Get the corresponding value
    count = char_dict[char]
    print(f"The '{char}' character was found {count} times")
  print("---End of Report---")


def sort_on(dict):
  return next(iter(dict.values()))


def ordered_dict_by_highest(character_dict):
  list_of_characters = []
  for pairs in character_dict:
    temp_dict = {}
    if pairs.isalpha() == True:
      temp_dict[pairs] = character_dict[pairs]
      list_of_characters.append(temp_dict)
  list_of_characters.sort(reverse=True, key=sort_on)    
  return list_of_characters


def get_character_count(text):
  dictionary_count = {}
  lowered_string = text.lower()
  for letter in lowered_string:
    if letter in dictionary_count:
     dictionary_count[letter] += 1
    else:
      dictionary_count[letter] = 1     
  return dictionary_count

def get_num_words(text):
  words = text.split()
  return len(words)


def get_book_text(path):
  with open(path) as f:
    return f.read()

main()