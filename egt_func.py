import cv2
import numpy as np
import random
import time
import dlib
import sys
from math import hypot

# # ------------------------------------ Inputs
ratio_blinking = 5.7
dict_color = {'green': (0,255,0),
              'blue':(255,0,0),
              'red': (0,0,255),
              'yellow': (0,255,255),
              'white': (255, 255, 255),
              'black': (0,0,0)}
# # ------------------------------------


# -----   Initialize camera
def init_camera(camera_ID):
    camera = cv2.VideoCapture(0)
    return camera
# --------------------------------------------------

def make_black_page(size):
    page = (np.zeros((int(size[0]), int(size[1]), 3))).astype('uint8')
    return page


def make_white_page(size):
    page = (np.zeros((int(size[0]), int(size[1]), 3)) + 255).astype('uint8')
    return page


def adjust_frame(frame):
    # frame = cv2.rotate(frame, cv2.ROTATE_180)
    frame = cv2.flip(frame, 1)
    return frame



def shut_off(camera):
    camera.release()
    cv2.destroyAllWindows()


def show_window(title_window, window):
    cv2.namedWindow(title_window)
    cv2.imshow(title_window,window)


def display_box_around_face(img, box, color, size):
    x_left, y_top, x_right, y_bottom = box[0], box[1], box[2], box[3]
    cv2.rectangle(img, (x_left-size[0], y_top-size[1]), (x_right+size[0], y_bottom+size[1]),
                 dict_color[color], 5)

def half_point(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


def get_eye_coordinates(landmarks, points):

    x_left = (landmarks.part(points[0]).x, landmarks.part(points[0]).y)
    x_right = (landmarks.part(points[3]).x, landmarks.part(points[3]).y)

    y_top = half_point(landmarks.part(points[1]), landmarks.part(points[2]))
    y_bottom = half_point(landmarks.part(points[5]), landmarks.part(points[4]))

    return x_left, x_right, y_top, y_bottom



def display_eye_lines(img, coordinates, color):
    cv2.line(img, coordinates[0], coordinates[1], dict_color[color], 2)
    cv2.line(img, coordinates[2], coordinates[3], dict_color[color], 2)



def display_face_points(img, landmarks, points_to_draw, color):
    for point in range(points_to_draw[0], points_to_draw[1]):
        x = landmarks.part(point).x
        y = landmarks.part(point).y
        cv2.circle(img, (x, y), 4, dict_color[color], 2)



def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


def is_blinking(eye_coordinates):
    blinking = False

    major_axis = np.sqrt((eye_coordinates[1][0]-eye_coordinates[0][0])**2 + (eye_coordinates[1][1]-eye_coordinates[0][1])**2)
    minor_axis = np.sqrt((eye_coordinates[3][0]-eye_coordinates[2][0])**2 + (eye_coordinates[3][1]-eye_coordinates[2][1])**2)

    ratio = major_axis/minor_axis

    if ratio > 5.7: blinking = True

    return blinking



def find_cut_limits(calibration_cut):
    x_cut_max = np.transpose(np.array(calibration_cut))[0].max()
    x_cut_min = np.transpose(np.array(calibration_cut))[0].min()
    y_cut_max = np.transpose(np.array(calibration_cut))[1].max()
    y_cut_min = np.transpose(np.array(calibration_cut))[1].min()

    return x_cut_min, x_cut_max, y_cut_min, y_cut_max


def pupil_on_cut_valid(pupil_on_cut, cut_frame):
    in_frame_cut = False
    condition_x = ((pupil_on_cut[0] > 0) & (pupil_on_cut[0] < cut_frame.shape[1]))
    condition_y = ((pupil_on_cut[1] > 0) & (pupil_on_cut[1] < cut_frame.shape[0]))
    if condition_x and condition_y:
        in_frame_cut = True

    return in_frame_cut


def project_on_page(img_from, img_to, point):

    scale = (np.array(img_to.shape) / np.array(img_from.shape))  #.astype('int')

    projected_point = (point * scale).astype('int')
    return projected_point


def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    ratio = hor_line_lenght / ver_line_lenght
    return ratio


def dysplay_keyboard(img, keys):

    color_board = (255, 250, 100)
    for key in keys:
        x1,x2=map(int,key[1])
        x3,x4=map(int, key[2])
        x5,x6=map(int,key[3])
        cv2.putText(img,   key[0], (x1,x2), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 100),3)
        cv2.rectangle(img, (x3,x4), (x5,x6), color_board,4)



def identify_key(key_points, coordinate_X, coordinate_Y):
    pressed_key = False

    for key in range(0, len(key_points)):
        condition_1 = np.mean(np.array([coordinate_Y, coordinate_X]) > np.array(key_points[key][2]))
        condition_2 = np.mean(np.array([coordinate_Y, coordinate_X]) < np.array(key_points[key][3]))

        if (int(condition_1 + condition_2) == 2):
            pressed_key = key_points[key][0]
            break
    return pressed_key


def take_radius_eye(eye_coordinates):
    radius = np.sqrt((eye_coordinates[3][0]-eye_coordinates[2][0])**2 + (eye_coordinates[3][1]-eye_coordinates[2][1])**2)
    return int(radius)

