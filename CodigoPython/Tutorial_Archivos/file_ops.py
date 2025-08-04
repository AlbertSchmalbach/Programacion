def read_file(file_name):
    with open(file_name, 'r') as file:
        file_read = file.read()
        print(file_read)
        return file_read

def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
       
    with open(output_filename, 'w') as file_out:
        file_out.write(first_line)

def read_even_numbered_lines(file_name):
   
    ### WRITE SOLUTION HERE
    with  open(file_name) as file:
        file_lines = file.readlines()
        lineas_pares = []
        for index, lines in enumerate(file_lines):
            if index % 2 != 0:
                lineas_pares.append(file_lines[index])
            
                

        return lineas_pares

    raise NotImplementedError()

def main():
    file_contents = read_file("sampletext.txt")
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))

if __name__ == "__main__":
    main()
