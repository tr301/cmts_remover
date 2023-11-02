
#import libraries :
import argparse
import os

#-------------------------------------------------------------------------------------------------------------------------------------

#definition of the remove_single_line_comments function :
def remove_single_line_comments(input_file, output_file):       #has 2 parameters, input_file and output_file
    #open input_file as read and output_file as write :
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:     #check every lines to see if there is a comments 
            stripped_line = line.split('//')[0]  # Remove comments
            outfile.write(stripped_line)        #write the new line, without the comments, to the output file 

#-------------------------------------------------------------------------------------------------------------------------------------

#definition of the process_directory function that will go through a folder to remove comments from every files that ends with .c
def process_directory(input_dir, output_dir):       #has 2 parameters, input_dir and output_dir
    
    if not os.path.exists(output_dir):      #if the sepcified folder does not exists, create it 
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:      #search for files in the folder that ends with .c
            if file.endswith(".c"):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_dir)
                output_file = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                remove_single_line_comments(input_file, output_file)        ##if there is a file that match, send it to the remove_single_line_comments function 

#-------------------------------------------------------------------------------------------------------------------------------------


#main function :
if __name__ == '__main__':
    #get the arguments of the command :
    parser = argparse.ArgumentParser(description='Remove single-line comments from C files.')
    parser.add_argument('-i', '--input', help='Input file or directory', required=True)
    parser.add_argument('-o', '--output', help='Output file or directory', required=True)
    args = parser.parse_args()

    #store the args in variables 
    input_path = args.input
    output_path = args.output

    #if the input file or folder does not exists, print an error :
    if os.path.isfile(input_path):
        remove_single_line_comments(input_path, output_path)
    elif os.path.isdir(input_path):
        process_directory(input_path, output_path)
    else:
        print("Input must be a valid file or directory.")
