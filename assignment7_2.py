
def fileread():
    while True:
        data_filename = input('What is the name of the file you would like to process?')
        try:
            data_file = open(data_filename, "r")
            break
        except:
            print("not valid")

    return (data_file)

