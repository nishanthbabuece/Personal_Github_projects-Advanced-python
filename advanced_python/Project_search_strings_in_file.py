def search_strings_in_file(file_path, search_string):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if search_string in line:
            print(line.strip())

# Example usage
file_path = 'india.txt'
search_string = 'Temple'
search_strings_in_file(file_path, search_string)