import cv2
import numpy as np
import base64
from deepface import DeepFace


def base64_to_image(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def compare_faces(image1, image2):

    img1 = base64_to_image(image1)
    img2 = base64_to_image(image2)

    # cv2.imshow("image 1", img1)
    # cv2.imshow("image 2", img2)
    # cv2.waitKey(0)

    result = DeepFace.verify(img1, img2)

    print(result)

    # print(type(result["verified"]))

    response = np.bool(result["verified"])

    # print(type(response))

    return response
