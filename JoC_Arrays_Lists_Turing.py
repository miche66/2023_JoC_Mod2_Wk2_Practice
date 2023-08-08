# JoC_Mod2_Wk2 | Arrays and Files - Turing Test
# M.Angelini

# Create a list, open the Turing file and read each line into the list. Make sure each line is
# less than 80 characters including spaces, and don't split words between lines
# Print the first and last two elements of the list, and the number of lines in the file.

with open("Turing.txt", "r") as file:
    lines = []
    current_line = ""
    count = 0

    for line in file:
        # adds line to list if length <= 80 char
        if len(line) <= 80:
            lines.append(line[:-1])
            count += 1
        else:
            # splits line into words
            words = line.split()

            # loop iterates through each word in line
            for word in words:
                # adds word to current line if line length <= 80
                if len(current_line + word) <= 80:
                    current_line += word + " "
                else:
                    # adds current line to list if length > 0
                    if len(current_line) > 0:
                        lines.append(current_line[:-1])
                        count += 1
                    current_line = word + " "

            # # adds current line to the list if length > 0  AND no new line character at end
            if len(current_line) > 0:
                lines.append(current_line[:-1])
                count += 1
            current_line = ""

# Prints each string in the lines list on a new line
for line in lines:
    print(line)
print()

# Prints the first two and last two elements in the lines list
print("First two elements: ")
print(lines[0], lines[1])
print()
print("Last two elements: ")
print(lines[-2], lines[-1])
print("Line Count: ", count)

