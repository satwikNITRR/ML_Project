# Open the requirements.txt file
with open('requirements.txt', 'r') as file:
# Read all lines, strip whitespace, and ignore empty lines
    packages = [line.strip() for line in file if line.strip()]

# Print the list of package names
print(packages)