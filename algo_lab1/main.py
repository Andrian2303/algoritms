from timeit import default_timer as timer
from datetime import timedelta
import csv_reader
import print_info
import copy
from heapsort_withdatastruct import *
from sort import *

def main():
    list_of_helicopters = csv_reader.csv_to_helicopters('helicopters.csv')

    print('---------- SELECTION SORT - ASCENDING - BY MAXIMUM LIFTING WEIGHT ----------')

    start_time = timer()
    sorted_helicopters = ascending_selection_sort_weights(copy.deepcopy(list_of_helicopters))
    elapsed_time = timedelta(seconds=timer() - start_time)

    print_info.print_algorithm_info(elapsed_time, 'SELECTION')
    print('-------------------------------------------------------------')
    print_info.print_list(sorted_helicopters)

    print('\n')
    print('---------- HEAP SORT - DESCENDING - BY MAXIMUM HEIGHT ----------')

    start_time = timer()
    sorted_helicopters = Heap.heap_sort(copy.deepcopy(list_of_helicopters))
    elapsed_time = timedelta(seconds=timer() - start_time)

    print_info.print_algorithm_info(elapsed_time, 'HEAP SORT')
    print('-------------------------------------------------------------')
    print_info.print_list(sorted_helicopters)


if __name__ == '__main__':
    main()