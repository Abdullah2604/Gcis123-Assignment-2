'''This is our GCIS Assignment 2 made by Group 6 - Zafar Shaikh, Adnan Sedaghat, Iqram Haider, Abdullah Nassem'''
'''The function of this program is to pack as many words in to the each line to make it justified to given max width'''

'''Defining function named, "read_text_file", adding a parameter named "filename", whose function includes opening the file in read modea and splitting and stripping the lines of file into a list'''
def read_text_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


'''Defining the function named, "justify_text" which includes justification of the text line by line and adding the appropriate amount of spaces to meet the value of max width'''
def justify_text(words, max_width):
    lines = []
    current_line = []
    current_width = 0
    
    for word in words:
        if current_width + len(current_line) + len(word) > max_width:
            lines.append(current_line)
            current_line = []
            current_width = 0
            
        current_line.append(word)
        current_width += len(word)
        
    if current_line:
        lines.append(current_line)
        
    result = []
    for i, line in enumerate(lines):
        line_width = sum(len(word) for word in line)
        num_spaces = max_width - line_width
        num_words = len(line)
        if num_words == 1:
            result.append(line[0] + ' ' * num_spaces)
        else:
            space_per_gap = num_spaces // (num_words - 1)
            extra_spaces = num_spaces % (num_words - 1)
            justified_line = ''
            for j in range(num_words - 1):
                justified_line += line[j]
                if j < extra_spaces:
                    justified_line += ' ' * (space_per_gap + 1)
                else:
                    justified_line += ' ' * space_per_gap
            justified_line += line[-1]
            result.append(justified_line)
    
    return result


'''Defining the main function which allows the user to input the filename and maxwidth and calling the functions to justify the text and displaying the result by using for loop line by line'''
def main():
    filename = input("Enter the name of the input file: ")
    max_width = int(input("Enter the maximum line width: "))
    
    lines = read_text_file(filename)
    words = [word for line in lines for word in line.split()]
    justified_lines = justify_text(words, max_width)
    
    for line in justified_lines:
        print(line)

'''Calling the main function'''    
main()