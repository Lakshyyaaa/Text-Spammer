# Define the message and the number of times it should be repeated
message =input("Enter the text you want to Spam")# Replace this with your desired message
num_repeats = int(input("Enter the number of times you want to spam"))

# Open a file in write mode
with open("spamfile.txt", "w") as file:
    # Write the message to the file the specified number of times
    for _ in range(num_repeats):
        file.write(message + "\n")

print(f"Message written {num_repeats} times to output.txt")
