import cv2
import os

########################################################################
# SETTINGS #
SHOW_REAL_VIDEO = False  # Set this to True to get real camera video from cv2

########################################################################

# 17-long
# ORDER = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')
# L = len(ORDER)

# # 9-long
# ORDER = (' ', "'", ':', 'c', 'x', 'k', 'd', '0', 'N')
# L = len(ORDER)

# 5-long
ORDER = (' ', ':', 'x', 'd', 'N')
L = len(ORDER)


# # 3-long
# ORDER = (' ', 'x', 'N')
# L = len(ORDER)

# # https://stackoverflow.com/a/67780964
# ORDER = tuple([x for x in '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]])
# L = len(ORDER)

# # https://stackoverflow.com/a/74186686
# ORDER = tuple([x for x in ''' `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@'''][::8])
# L = len(ORDER)


def convert_row_to_ascii(row):
    return tuple(ORDER[int(x / (255 / L))] for x in row)[::-1]


def convert_to_ascii(input_grays):
    return tuple(convert_row_to_ascii(row) for row in input_grays)


def print_array(input_ascii_array):
    os.system("clear")
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')


cap = cv2.VideoCapture(0)
try:
    while cv2.waitKey(1) & 0xFF != ord('q'):
        # Get screensize for reduction
        screen_height, screen_width = os.popen('stty size', 'r').read().split()

        # Get image data
        ret, frame = cap.read()

        # Convert data to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Reduce grayscale array to proper resolution
        reduced = cv2.resize(gray, (int(screen_width), int(screen_height)))

        # Plug in reduced resolution numpy array for ascii converter func
        converted = convert_to_ascii(reduced)
        print_array(converted)

        # Display the resulting frame
        if SHOW_REAL_VIDEO:
            cv2.imshow('frame', reduced)
except KeyboardInterrupt:
    pass

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
