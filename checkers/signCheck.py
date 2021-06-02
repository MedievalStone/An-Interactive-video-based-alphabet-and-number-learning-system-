

import cv2

img=cv2.imread('ColorGameImg.jpg')
img = cv2.line(img, (100,50), (120,70), (0,0,0), 2)
img=cv2.line(img,(100,70),(120,50),(0,0,0), 2)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
