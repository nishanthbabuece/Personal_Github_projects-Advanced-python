def log_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if "Error" in line or "Exception" in line:
                yield line.strip()

# Usage
log_file_path = 'large_log_file.txt'
for line in log_file_generator(log_file_path):
    print(line)  # Process each line containing "Error" or "Exception"