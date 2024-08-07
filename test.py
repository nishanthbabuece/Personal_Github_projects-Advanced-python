# # Open the file in write mode
with open('india.txt', 'w') as file:
    # Write contents about India
    file.write("India is a country in South Asia.\n")
    file.write("It is the seventh-largest country by land area.\n")
    file.write("India is known for its diverse culture and rich history.\n")
    file.write("The capital of India is New Delhi.\n")
    file.write("India has a population of over 1.3 billion people.\n")
    file.write("It is a federal parliamentary democratic republic.\n")
    file.write("India is famous for its cuisine, festivals, and landmarks like the Taj Mahal.\n")
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def search_strings_in_file(file_path, search_string):
    lines = read_file(file_path)
    for line in lines:
        if search_string in line:
            print(line.strip())

# Example usage
file_path = 'india.txt'
search_string = 'festivals'
search_strings_in_file(file_path, search_string)
