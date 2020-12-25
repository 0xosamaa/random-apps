try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
        print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('You are not allowed to do that.')
except Exception as err:
    print('Some other error occured: ', str(err))