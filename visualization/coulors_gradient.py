from PIL import Image


def convert_to_rgb(minval, maxval, val, colors):
    max_index = len(colors)-1
    v = float(val-minval) / float(maxval-minval) * max_index
    i1, i2 = int(v), min(int(v)+1, max_index)
    (r1, g1, b1), (r2, g2, b2) = colors[i1], colors[i2]
    f = v - i1
    return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))

if __name__ == '__main__':
    # minval, maxval = 1, 3
    # steps = 10
    # delta = float(maxval-minval) / steps
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # [BLUE, GREEN, RED]
    # print('  Val       R    G    B')
    # for i in range(steps+1):
    #     val = minval + float(i) * delta
    #     r, g, b = convert_to_rgb(minval, maxval, val, colors)
    #     print('{:.3f} -> ({:3d}, {:3d}, {:3d})'.format(val, r, g, b))

    colors = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]  # [BLUE, GREEN, RED]
    steps = 256
    im = Image.new('RGB', (steps, 62))
    ld = im.load()
    minval, maxval = 1, 5
    delta = float(maxval-minval) / steps
    for x in range(steps):
        val = minval + float(x) * delta
        r, g, b = convert_to_rgb(minval, maxval, val, colors)
        print('({:3d}, {:3d}, {:3d}),'.format(r, g, b))
        for y in range(im.size[1]):
            ld[x, y] = (r, g, b)

    im.show()
