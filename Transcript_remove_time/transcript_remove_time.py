def remove_timestamp(file):
    '''
    remove_timestamp(file) <-- .txt file
    
    This function removes time stamps in .txt files with time stamps as lines following
    Youtube's format
    '''
    import re
    import string
    try:
        with open(file,'r') as f:
            text_file = f.readlines()
        
        new_f = open(f'{file}_clean.txt','x')

        with open(f'{file}_clean.txt','w') as g:
            for line in text_file:
                test = line.translate(str.maketrans('', '', string.punctuation))
                test = test.replace('\n','')
                alnum_test = [x.isalnum() for x in test.split(' ')]
                num_test = [x.isdigit() for x in test.split(' ')]

                if all(num_test):
                    continue
                if all(alnum_test):
                    g.write(line)
        print('Done')           
    except Exception as e:
        print(f'Failed because: {e}')

file_path = input('input file name from this folder: ')
remove_timestamp(file_path)



