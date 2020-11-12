'''
Задача № 8
Даны центры равномерно растущих кругов на плоскости. При столкновении друг
с другом столкнувшиеся круги прекращают свой рост. Найти радиусы кругов, когда
процесс роста остановится полностью.
'''

import math
from matplotlib import pyplot as plt
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

def circles_impact(circles):
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
    '''Вычисление первого столкновения для определённости сисетмы'''
    c1, c2 = None, None
    min_d = max_dist
    for c in circles_r:
        for c_ in circles_r:
            if (c[0] != c_[0]):
                d = dist(c, c_)
                if (d < min_d):
                    c1, c2 = c, c_
                    min_d = d
    for a in circles_r:
        if (a[0] == c1[0]):
            a[1] = min_d/2
        if (a[0] == c2[0]):
            a[1] = min_d/2
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

def autotest():
    test_arr = [(0,0), (0,1), (3,0)]
    test_rads = circles_impact(test_arr)
    if (test_rads[0][1] != 0.5 or test_rads[1][1] != 0.5 or test_rads[2][1] != 2.5):
        print('Error: autotest not passed.\n')
        raise SystemExit(-1)
    print('Autotest passed')
    
autotest()

test = get_centers()
rads = circles_impact(test)
print(rads)
circles = []
for c in rads:
    x = []
    y = []
    for alpha in range(0,629):
        x.append(c[0][0] - c[1]*math.cos(alpha/100))
        y.append(c[0][1] + c[1]*math.sin(alpha/100))
    circles.append((x,y))

fig, axes = plt.subplots()
axes.set_aspect(1)
for r in rads:
    axes.scatter(r[0][0], r[0][1], c = 'purple')
for c in circles:
    axes.plot(c[0], c[1], c = 'purple')
