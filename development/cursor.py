"""
This script includes a function that can compile cursor data from an image.

-Sean McKiernan
"""

import os
import pygame as pg


def cursor_from_image(image,size,hotspot,location=(0,0),flip=False):
    """
    This function's return value is of the form accepted by
    pg.mouse.set_cursor() (passed using the *args syntax). The argument image
    is an already loaded image surface containing your desired cursor; size is
    a single integer corresponding to the width of the cursor (must be a
    multiple of 8); hotspot is a 2-tuple representing the exact point in your
    cursor that will represent the mouse position; location is a 2-tuple for
    where your cursor is located on the passed in image. Setting flip to True
    will create the cursor with colors opposite to the source image.

    Color in image to color in cursor defaults:
        Black (  0,   0,   0) ---> Black
        White (255, 255, 255) ---> White
        Cyan  (  0, 255, 255) ---> Xor (only available on certain systems)
        Any Other Color ---------> Transparent
    """
    if size%8:
        raise ValueError("Size must be a multiple of 8.")
    compile_args = (".", "X", "o") if flip else ("X", ".", "o")
    colors = {(  0,  0,  0,255) : ".",
              (255,255,255,255) : "X",
              (  0,255,255,255) : "o"}
    cursor_string = []
    for j in range(size):
        this_row = []
        for i in range(size):
            where = (i+location[0], j+location[1])
            pixel = tuple(image.get_at(where))
            this_row.append(colors.get(pixel, " "))
        cursor_string.append("".join(this_row))
    xors,ands = pg.cursors.compile(cursor_string, *compile_args)
    size = size, size
    return size, hotspot, xors, ands

"""
Cursors dict.

-Rodrigo de Oliveira
"""

cursor_image1 = pg.image.load(os.path.join('data', 'images', 'cursors', 'hand.png'))
cursor_data1 = cursor_from_image(cursor_image1, 16, (5, 1), (0, 0))

cursor_image2 = pg.image.load(os.path.join('data', 'images', 'cursors', 'hand2.png'))
cursor_data2 = cursor_from_image(cursor_image2, 16, (5, 1), (0, 0))

cursors_dict = {'Hand'    : cursor_data1,
                'Hand2'   : cursor_data2,
                'Default' : pg.cursors.arrow}
