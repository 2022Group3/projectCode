import cv2

def capture():
    print("fjj")
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    if result:
        path_img=r"cam.png"
        print(image.shape)
        image = image[0:480, 80:560]#capture a square image

        cv2.imwrite(path_img, image)
        return path_img
    else:
        return None
