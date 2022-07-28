import cv2

def capture():
    '''
    func to open camera and take a picture
    :return: path to the capture image
    '''
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("capture")

    img_name=""
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("capture", frame)


        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = r"cam.png"
            cv2.imwrite(img_name, frame)
            break
    cam.release()
    cv2.destroyAllWindows()
    return img_name