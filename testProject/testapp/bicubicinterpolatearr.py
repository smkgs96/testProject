import math
import numpy as np
from scipy.interpolate import griddata
from colour import Color

data = [26, 26, 26, 26, 26, 26, 27, 27, 26, 26, 26, 26, 26, 27, 27, 27, 26, 26, 26, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 25, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 27, 27, 26, 25, 25, 26, 25, 26, 26, 27]
def do_color(ifcamlist):
    result_arr = []
    COLORDEPTH = 1024
    MINTEMP = 26
    MAXTEMP = 80

    points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
    grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

    blue = Color("indigo")
    colors = list(blue.range_to(Color("red"), COLORDEPTH))

    colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))

    def map(x, in_min, in_max, out_min, out_max):
      return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    pixels = data
    pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
    for j,row in enumerate(bicubic):
        for i,pixel in enumerate(row):
            result_arr.append(colors[constrain(int(pixel), 0, COLORDEPTH- 1)])
    
    return result_arr


if __name__ == "__main__":
    a = do_color(data)
    print(a)
    print(len(a))