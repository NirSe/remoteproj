
from folder1.my_data1 import find_car1


def load_data1(car: str = 'Toyota'):
    print ('in loading function')
#    my_file_handle = open("/Users/nir/remtst/data.txt", 'w')
    my_file_handle = open("data.txt", 'w')
    car = find_car1()
    my_file_handle.write(car)
