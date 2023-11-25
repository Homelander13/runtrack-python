def draw_triangle(height):
    for i in range(height - 1):
        print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

 
    print('/' + '_' * (2 * (height - 1)) + '\\')


draw_triangle(5)
