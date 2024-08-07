class LogFileIterator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            if "Error" in line or "Exception" in line:
                return line.strip()

# Usage
log_file_path = 'large_log_file.txt'
log_iterator = LogFileIterator(log_file_path)

for line in log_iterator:
    print(line)  # Process each line containing "Error" or "Exception"