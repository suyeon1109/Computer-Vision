import cv2

#1. 이미지 파일을 화면에 표시
# #path of the image
# img_file = "/Users/mac/Documents/GitHub/computer-vision/지코12.jpg"
# img= cv2.imread(img_file) 

# cv2.imshow('zico',img) 
# cv2.waitKey() 
# cv2.destroyAllWindows() 


#2. 이미지 파일을 그레이스케일로 변환
# img_file = "/Users/mac/Documents/GitHub/computer-vision/지코12.jpg"
# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

# #print(img)
# cv2. imshow('IMG', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# """
#  [[255 240 255]
#   [255 235 255]
#   [255 231 255]
#   ...
#   [212 201 221]
#   [198 187 207]
#   [189 177 199]]]
#   """


#3. 이미지 파일을 그레이스케일로 저장
# img_file = "/Users/mac/Documents/GitHub/computer-vision/지코12.jpg"
# save_file = "/Users/mac/Desktop/grayscale.jpg"

# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
# cv2.imshow("zico", img)
# cv2.imwrite(save_file, img)
# cv2.waitKey()
# cv2.destroyAllWindows()

for i in range(1,25):
    img_file = f"/Users/mac/Documents/GitHub/computer-vision/지코/지코{i}.jpg"
    save_file = f"/Users/mac/Desktop/grayscale{i}.jpg"

    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(save_file, img)

#4.동영상 및 카메라 프레임 읽기
video_file="/Users/mac/Documents/GitHub/computer-vision/test.mp4"
cap = cv2.VideoCapture(video_file)

while True:
    ret, img = cap.read() #return ret=true/false,img=3d array
    cv2.imshow("video", img)
    cv2.waitKey(25) #25ms 대기

cv2.release()
cv2.destroyAllWindows()
