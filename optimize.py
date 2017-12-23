import sys
from Optimizer import Optimizer

if __name__ == '__main__':
    selection_num = int(sys.argv[1])

    start = ['111111', '110011', '000111']
    optimizer_obj = Optimizer(start)

    print('START')
    print(optimizer_obj.get_current())
    for i in range(selection_num):
        print('')
        print('SELECTION: %s' % (i + 1))
        print(optimizer_obj.get_current_scores())
        optimizer_obj.go_to_next_generation()
        print(optimizer_obj.get_current())
