def convert_url():
    user_input = input("Enter your URL: ")

    parts = user_input.split("http://www.")
    if len(parts) > 1:
        user_url = parts.pop()  
        converted_url = user_url + ".com"  
        return converted_url
    else:
        return "Invalid URL format. Please ensure it starts with 'http://www.'"

result = convert_url()
print("Converted URL: " + result)
