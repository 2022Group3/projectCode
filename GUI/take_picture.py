import cv2


def capture():

    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    if result:
        path_img=r"D:\bootcamp\AMAT\project\cam.png"
        cv2.imwrite(path_img, image)
        return path_img

    else:
        return None
#
# if __name__ == '__main__':
#     print(capture())