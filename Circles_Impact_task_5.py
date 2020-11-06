'''
Задача №8
Даны центры равномерно растущих кругов на плоскости. При столкновении друг
с другом столкнувшиеся круги прекращают свой рост. Найти радиусы кругов, когда
процесс роста остановится полностью.
'''

import math
def get_centers():
    circles_number = int(input('Enter circles number: '))
    if (circles_number <= 1):
        print('Error: incorrect circles number: {}'.format(circles_number))
        return 0
    centers = [(float(input('Circle {}: enter X of center: '.format(i+1))), float(input('Circle {}: enter Y of center: '.format(i+1)))) for i in range (0, circles_number)]
    for i,c in enumerate(centers):
        for i_,c_ in enumerate(centers):
            if (c == c_ and i != i_):
                print('Error: you entered two different circles with the same center.')
                return 0
    return centers

def calc_rads(circles):
    circles_r = [[circle, 0] for circle in circles]
    '''Евклидово расстояние'''
    def dist(circle_1, circle_2):
        return math.sqrt(sum(list(map(lambda x,y: (x-y)**2, circle_1[0], circle_2[0]))))
    '''Максимальное расстояние между кругами для дальнейшего сравнения'''
    max_dist = 0
    for c in circles_r:
        for c_ in circles_r:
            d = dist(c, c_)
            if (d > max_dist):
                max_dist = d
    '''Нахождение для текущего круга соседа, столкновение с которым наиболее близко'''
    def closest_impact(circle):
        min_d = max_dist
        nn = None #nearest neighbour
        for c in circles_r:
            if (c != circle):
                if (c[1] == 0):
                    d = dist(c, circle)/2
                else:
                    d = dist(c, circle) - c[1]
                if (d <= min_d):
                    min_d = d
                    nn = c
        return nn
    for circle in circles_r:
        if (circle[1] != 0):
            continue
        nearest_neighbour = closest_impact(circle)
        if (nearest_neighbour[1] == 0):
            d = dist(nearest_neighbour, circle)/2
            circle[1] = d
            for n in circles_r:
                if n == nearest_neighbour:
                    n[1] = d
        else:
            d = dist(nearest_neighbour, circle) - nearest_neighbour[1]
            circle[1] = d
    return circles_r
            
test = get_centers()
print(calc_rads(test))