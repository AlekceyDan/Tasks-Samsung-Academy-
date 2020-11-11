import sys


def get_size(x, level=0, print_res = True):
    if print_res:
        print('\t' * level, f'type {x.__class__}, size={sys.getsizeof(x)}, object= {x}')
    total_size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                total_size += get_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                total_size += get_size(xx, level + 1)

    return total_size
print(i)

mas = [int(input()) for i in range(15)]

id_max= mas.index(max(mas))
id_min= mas.index(min(mas))

sum_mas = sum([i for i in mas[min(id_min,id_max)+1:max(id_max,id_min)]])


ttl_size = get_size(sum_mas)+get_size(id_min)+get_size(id_max)+get_size(mas)+get_size(len(mas))
+get_size(len(mas[min(id_min,id_max)+1:max(id_max,id_min)]))


print(ttl_size)
