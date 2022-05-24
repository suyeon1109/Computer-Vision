import cv2
import numpy as np

img = cv2.imread('/Users/mac/Documents/GitHub/computer-vision/White_full.png')
# # cv2.line(img, (50,50), (150,50), (255,0,0)) #파란색 1픽셀짜리 선

# # cv2.line(img,(100,100), (400,100), (255,255,0),10)

# # cv2.line(img,(100,350), (400,400), (0,0,255), 20, cv2.LINE_4)
# # cv2.line(img,(100,450), (400,500), (0,0,255), 20, cv2.LINE_AA)

# cv2.rectangle(img,(50,50), (300,150), (255,0,0),10)
# cv2.rectangle(img,(50,250), (300,150), (255,0,0),-1) #-1: 안을 채우기

# img = cv2.imread('/Users/mac/Documents/GitHub/computer-vision/몬스타엑스기현6.jpg')
# cv2.rectangle(img, (70,25), (150, 100), (255,0,0),5)
# cv2.imshow('lines', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#다각형 그리기
#번개모양 선 좌표
pts1=np.array([[50,50], [150,150], [100,140],[200, 240]], dtype = np.int32)
pts2 = np.array([[350,250], [450,350],[400,450],[300,450],[250,350]], dtype = np.int32)
pts3 = np.array([[500,300], [550,400],[450,550]], dtype = np.int32)

#parameter : img, points, isClosed, color, thickness, lineType
cv2.polylines(img,[pts1], True, (255,0,0))
cv2.polylines(img,[pts2], True, (0,0,0), 5, cv2.LINE_AA)
cv2.polylines(img,[pts3], True, (0,0,0), 5, cv2.LINE_AA)


cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
