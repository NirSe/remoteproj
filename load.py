
from my_data import find_car


def load_data(car: str = 'Toyota'):
    print ('in loading function')
#    my_file_handle = open("/Users/nir/remtst/data.txt", 'w')
    my_file_handle = open("/v3io/users/admin/nir/data.txt", 'w')
    car = find_car()
    my_file_handle.write(car)
