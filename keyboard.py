import cv2
import numpy as np



def get_keyboard(width_keyboard , height_keyboard, offset_keyboard):
    column = np.arange(0, width_keyboard, width_keyboard/ 10, dtype=int) + offset_keyboard[0]
    row = np.arange(0, height_keyboard, height_keyboard/ 4, dtype=int) + offset_keyboard[1]

    box = int(width_keyboard / 10)

    color_board = (0, 100, 250)

    key_points = []
                    # key   center               upper-left                      bottom-right
    key_points.append(['1', (column[0], row[0]), (column[0]-box/2, row[0]-box/2), (column[0]+box/2, row[0]+box/2)])
    key_points.append(['2', (column[1], row[0]), (column[1]-box/2, row[0]-box/2), (column[1]+box/2, row[0]+box/2)])
    key_points.append(['3', (column[2], row[0]), (column[2]-box/2, row[0]-box/2), (column[2]+box/2, row[0]+box/2)])
    key_points.append(['4', (column[3], row[0]), (column[3]-box/2, row[0]-box/2), (column[3]+box/2, row[0]+box/2)])
    key_points.append(['5', (column[4], row[0]), (column[4]-box/2, row[0]-box/2), (column[4]+box/2, row[0]+box/2)])
    key_points.append(['6', (column[5], row[0]), (column[5]-box/2, row[0]-box/2), (column[5]+box/2, row[0]+box/2)])
    key_points.append(['7', (column[6], row[0]), (column[6]-box/2, row[0]-box/2), (column[6]+box/2, row[0]+box/2)])
    key_points.append(['8', (column[7], row[0]), (column[7]-box/2, row[0]-box/2), (column[7]+box/2, row[0]+box/2)])
    key_points.append(['9', (column[8], row[0]), (column[8]-box/2, row[0]-box/2), (column[8]+box/2, row[0]+box/2)])
    key_points.append(['0', (column[9], row[0]), (column[9]-box/2, row[0]-box/2), (column[9]+box/2, row[0]+box/2)])

    key_points.append(['Q', (column[0], row[1]), (column[0]-box/2, row[1]-box/2), (column[0]+box/2, row[1]+box/2)])
    key_points.append(['W', (column[1], row[1]), (column[1]-box/2, row[1]-box/2), (column[1]+box/2, row[1]+box/2)])
    key_points.append(['E', (column[2], row[1]), (column[2]-box/2, row[1]-box/2), (column[2]+box/2, row[1]+box/2)])
    key_points.append(['R', (column[3], row[1]), (column[3]-box/2, row[1]-box/2), (column[3]+box/2, row[1]+box/2)])
    key_points.append(['T', (column[4], row[1]), (column[4]-box/2, row[1]-box/2), (column[4]+box/2, row[1]+box/2)])
    key_points.append(['Y', (column[5], row[1]), (column[5]-box/2, row[1]-box/2), (column[5]+box/2, row[1]+box/2)])
    key_points.append(['U', (column[6], row[1]), (column[6]-box/2, row[1]-box/2), (column[6]+box/2, row[1]+box/2)])
    key_points.append(['I', (column[7], row[1]), (column[7]-box/2, row[1]-box/2), (column[7]+box/2, row[1]+box/2)])
    key_points.append(['O', (column[8], row[1]), (column[8]-box/2, row[1]-box/2), (column[8]+box/2, row[1]+box/2)])
    key_points.append(['P', (column[9], row[1]), (column[9]-box/2, row[1]-box/2), (column[9]+box/2, row[1]+box/2)])

    key_points.append(['A', (column[0]+ box/3, row[2]), (column[0]+ box/3-box/2, row[2]-box/2), (column[0]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['S', (column[1]+ box/3, row[2]), (column[1]+ box/3-box/2, row[2]-box/2), (column[1]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['D', (column[2]+ box/3, row[2]), (column[2]+ box/3-box/2, row[2]-box/2), (column[2]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['F', (column[3]+ box/3, row[2]), (column[3]+ box/3-box/2, row[2]-box/2), (column[3]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['G', (column[4]+ box/3, row[2]), (column[4]+ box/3-box/2, row[2]-box/2), (column[4]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['H', (column[5]+ box/3, row[2]), (column[5]+ box/3-box/2, row[2]-box/2), (column[5]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['J', (column[6]+ box/3, row[2]), (column[6]+ box/3-box/2, row[2]-box/2), (column[6]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['K', (column[7]+ box/3, row[2]), (column[7]+ box/3-box/2, row[2]-box/2), (column[7]+ box/3+box/2, row[2]+box/2)])
    key_points.append(['L', (column[8]+ box/3, row[2]), (column[8]+ box/3-box/2, row[2]-box/2), (column[8]+ box/3+box/2, row[2]+box/2)])

    key_points.append(['del',(column[0]+ box*2/3, row[3]), (column[0]+ box*2/3-box/2, row[3]-box/2), (column[0]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['Z', (column[1]+ box*2/3, row[3]), (column[1]+ box*2/3-box/2, row[3]-box/2), (column[1]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['X', (column[2]+ box*2/3, row[3]), (column[2]+ box*2/3-box/2, row[3]-box/2), (column[2]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['C', (column[3]+ box*2/3, row[3]), (column[3]+ box*2/3-box/2, row[3]-box/2), (column[3]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['V', (column[4]+ box*2/3, row[3]), (column[4]+ box*2/3-box/2, row[3]-box/2), (column[4]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['B', (column[5]+ box*2/3, row[3]), (column[5]+ box*2/3-box/2, row[3]-box/2), (column[5]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['N', (column[6]+ box*2/3, row[3]), (column[6]+ box*2/3-box/2, row[3]-box/2), (column[6]+ box*2/3+box/2, row[3]+box/2)])
    key_points.append(['M', (column[7]+ box*2/3, row[3]), (column[7]+ box*2/3-box/2, row[3]-box/2), (column[7]+ box*2/3+box/2, row[3]+box/2)])

    return key_points
