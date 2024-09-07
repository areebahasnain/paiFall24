file_name = r'replacement_needed.txt'

try:
    content = ''
    with open(file_name, 'r+') as f:
        content = f.read()
        print("file:", content)
        content = content.replace(input('Enter original character: '), input('Enter a characer to replace with: '))
        f.seek(0)
        f.write(content)
        
except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
except IOError:
        print(f"Error: Unable to read file '{file_name}'.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")