
def train_data():
    print('In training function')
#    my_file_handle = open("/Users/nir/remtst/data.txt")
    my_file_handle = open("/v3io/users/admin/nir/data.txt")
    data = my_file_handle.read()

    print(data)

