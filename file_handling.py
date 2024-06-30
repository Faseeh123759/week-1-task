# -*- coding: utf-8 -*-
"""file handling

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MmlED4KWtcq_9kxz8Api8jeTpGb5YE2o
"""

def read_file(filename):
  """Reads data from a file and prints its contents, also counts words.

  Args:
    filename: The name of the file to read.

  Returns:
    The number of words in the file.
  """
  try:
    with open(filename, 'r') as file:
      content = file.read()
      print(content)
      word_count = len(content.split())
      return word_count
  except FileNotFoundError:
    print(f"File '{filename}' not found.")
    return 0
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    return 0

def write_to_file(filename):
  """Takes user input and writes it to a new file.

  Args:
    filename: The name of the file to write to.
  """
  user_input = input("Enter text to write to the file: ")
  try:
    with open(filename, 'w') as file:
      file.write(user_input)
    print(f"Text written to '{filename}' successfully.")
  except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Example usage
word_count = read_file('data.txt')
print(f"Number of words in the file: {word_count}")

write_to_file('output.txt')
read_file('output.txt')