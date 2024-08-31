def build_message(**info):
    message = ""
    for key, value in info.items():
        message += f"{key.capitalize()}: {value}\n"
    return message

print(build_message(name="Areeba Hasnain", age=21, city="Karachi"))
print("\n")
print(build_message(name="Hamza", country="USA", occupation="Electrical Engineer"))
