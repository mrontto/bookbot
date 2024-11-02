def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  print(f"there are {num_words} in the document")
  total_characters = get_character_count(text)
  print(total_characters)


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