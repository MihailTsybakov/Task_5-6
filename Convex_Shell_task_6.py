'''
Задача № 9
Дано множество точек на плоскости. Построить выпуклую оболочку этого множества.
'''
import math
import random
from matplotlib import pyplot as plt
def get_points():
    points_number = int(input('Enter number of dots: '))
    status = str(input('Want to generate random set? Y/N: '))
    if (status != 'Y' and status != 'N'):
        print('Error: unknown answer')
        return 0
    if (points_number <= 0):
        print('Error: incorrect dots number.')
        return 0
    if (status == 'N'):
        points = [(float(input('Dot {}: enter X: '.format(i+1))), float(input('Dot {}: enter Y: '.format(i+1)))) for i in range(0, points_number)]
        for i,p in enumerate(points):
            for i_, p_ in enumerate(points):
                if (p == p_ and i != i_):
                    print('Error: two different dots have the same locations.')
                    return 0
    else:
        points = [(random.randint(-20, 20), random.randint(-20,20)) for i in range(0, points_number)]
        for i,p in enumerate(points):
            for i_, p_ in enumerate(points):
                if (p == p_ and i != i_):
                    points.remove(p_)
    return points

def convex_shell(points):
    if (len(points) == 1 or len(points) == 2):
        return points
    def dist(point_1, point_2):
        return math.sqrt(sum(list(map(lambda x,y: (x-y)**2, point_1, point_2))))
    def check_borderness(point_1, point_2):
        def point_atleft(p):
            v1 = [point_2[0] - point_1[0], point_2[1] - point_1[1]]
            v2 = [p[0] - point_1[0], p[1] - point_1[1]]
            vectmul = v1[0]*v2[1] - v1[1]*v2[0]
            if (vectmul >= 0):
                return True
            return False
        for p_ in points:
            if (p_ != point_1 and p_ != point_2):
                if (point_atleft(p_) == False):
                    return False
        return True
    start_dot = sorted([(p, p[0]) for p in points], key = lambda x:x[1])[0][0]
    mass_center = [sum([p[0] for p in points])/len(points), sum([p[1] for p in points])/len(points)]
    points_d = sorted([(p, dist(p, mass_center)) for p in points], reverse = True)
    convex_shell = [start_dot]
    while True:
        curr_dot = convex_shell[len(convex_shell) - 1]
        flag = False
        tmp = []
        for p_ in points_d:
            if (p_[0] not in convex_shell):
                if (check_borderness(curr_dot, p_[0]) == True):
                    flag = True
                    tmp.append(p_[0])
        if (flag != False):
            tmp_d = sorted([(o, dist(o, curr_dot)) for o in tmp], key = lambda x: x[1])
            convex_shell.append(tmp_d[0][0])
        if (flag == False):
            break
    return convex_shell, mass_center

def autotest():
    test_points = [(0,0), (3,3), (6,-3), (1,0)]
    test_convex_shell = convex_shell(test_points)
    if (test_convex_shell[0] != [(0,0), (6,-3), (3,3)]):
        print('Error: autotest not passed.\n')
        raise SystemExit(-1)
    print('Autotest passed')
    
autotest()

test = get_points()
conv, mass_center = convex_shell(test)
print(conv)
fig, axes = plt.subplots()
axes.set_aspect(1)
for p in test:
    if p not in conv:
        axes.scatter(p[0], p[1], c = 'orange')
for c in conv:
    axes.scatter(c[0], c[1], c = 'maroon')
for i in range(0, len(conv) - 1):
    x = [conv[i][0], conv[i+1][0]]
    y = [conv[i][1], conv[i+1][1]]
    axes.plot(x, y, c = 'salmon', linestyle = 'dashed')
x = [conv[len(conv) - 1][0], conv[0][0]]
y = [conv[len(conv) - 1][1], conv[0][1]]
axes.plot(x, y, c = 'salmon', linestyle = 'dashed')
axes.scatter(mass_center[0], mass_center[1], c = 'cyan')
