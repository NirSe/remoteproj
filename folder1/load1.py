
from my_data1 import find_car


def load_data1(car: str = 'Toyota'):
    print ('in loading function')
#    my_file_handle = open("/Users/nir/remtst/data.txt", 'w')
    my_file_handle = open("/v3io/users/nir/remote/data.txt", 'w')
    car = find_car()
    my_file_handle.write(car)
