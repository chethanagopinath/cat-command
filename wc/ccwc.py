#!/usr/bin/env python
import sys

def ccwc():
    ccwc_input = []
    allowed_arg_list = {'-c', '-l', '-w', '-m'}

    for arg in sys.argv:
        ccwc_input.append(arg)

    # command will always be in this format: ccwc allowed_arg_list[n] filename.extension

    if len(ccwc_input) == 0 or len(ccwc_input) > 5:
        print("Incorrect number of arguments, please re-check")
        return
    
    result = ''

    # we should be able to do provide 1, 2 or all 3 options and ccwc should work
    options = ''

    for arg in ccwc_input:
        if '-' in arg:
            if arg not in allowed_arg_list:
                print("Invalid argument, please re-check")
                return
            
            else:
                options += arg

    if len(options) == 0:
        options = '-l -w -c'


    file_name = ccwc_input[-1]
    # can also add error handling around invalid file, where we cant find the txt file at this path
    if '.txt' not in file_name:
        print("Only .txt files are supported, please re-check")
        return


    for option in options.split():
        if option == '-l':
            with open(file_name) as reader_l:
                result += str(len(reader_l.readlines())) + " "

        if option == '-w':
            with open(file_name) as reader_w:
                file_contents = reader_w.read()
            
            result += str(len(file_contents.split())) + " "

        if option == '-c':
            '''
            This code opens the file in binary mode ('rb'), reads its contents, and then converts the contents into a memoryview using getbuffer(). 
            The len function is then used to find the number of bytes in the file. 
            Note that this method reads the entire file into memory, so it may not be suitable for very large files.
            '''
            with open(file_name, 'rb') as reader_c:
                file_contents = reader_c.read()
            
            buffer = memoryview(file_contents)
            result += str(len(buffer.tobytes())) + " "

        if option == '-m':
            # my count shows 342190
            # wc -m gives me 339292
            # this is weird, going to take a look later
            with open(file_name) as reader_m:
                file_contents = reader_m.read()

            char_count = 0
            chars = {}
            for char in file_contents:
                char_count += 1
                if char not in chars:
                    chars[char] = 1
                else:
                    chars[char] += 1

            result = str(char_count)
            print(chars)



    print(result.strip() + " " + file_name)

    return





    



if __name__ == "__main__":
    ccwc()