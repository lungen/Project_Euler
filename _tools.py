def remove_files(file_names):
    """ removes files  """

    import os, glob

    list_files= glob.glob(file_names + '*')

    try:
        for f in list_files:
            os.remove(f)
        print('FILES REMOVED')
    except:
        print('FAIL TO REMOVE FILES')


def save_it(data, file_name):
    """ save list: data, filename """

    def timeStamped(fname, fmt='{fname}_%Y-%m-%d-%H-%M-%S.txt'):
        import datetime
        return datetime.datetime.now().strftime(fmt).format(fname=fname)

    try:
        with open(timeStamped(file_name), "w") as f:
            f.write('\n'.join(str(line) for line in data))

        print("DATA SAVED")

    except:
        print("FAIL TO SAVE DATA")


def load_it(file_name):

    try:
        with open(file_name, 'r') as f:
            data = f.read()
    except:
        print("FAIL to READ DATA!")

    data_list = [number for number in data.split("\n")]
    print(file_name, "LOADED ")
    return(data_list)
