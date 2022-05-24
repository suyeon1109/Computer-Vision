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

# for i in range(1,25):
#     img_file = f"/Users/mac/Documents/GitHub/computer-vision/지코/지코{i}.jpg"
#     save_file = f"/Users/mac/Desktop/grayscale{i}.jpg"

#     img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
#     cv2.imwrite(save_file, img)

# #4.동영상 및 카메라 프레임 읽기
# video_file="/Users/mac/Documents/GitHub/computer-vision/test.mp4"
# cap = cv2.VideoCapture(video_file)

# while True:
#     ret, img = cap.read() #return ret=true/false,img=3d array
#     cv2.imshow("video", img)
#     cv2.waitKey(25) #25ms 대기

# cv2.release()
# cv2.destroyAllWindows()

# #5.동영상 프레임 읽기
# cap = cv2.VideoCapture(0) #0번 카메라 장치 연결

# while True:
#     ret, img = cap.read()
#     cv2.imshow('camera', img)
#     if cv2.waitKey(1) != -1: #아무키나 누르면
#         break
# cap.releas()
# cv2.destroyAllWindows()

# #6. 카메라로 사진찍기
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('camera', frame)
#     if cv2.waitKey(1) != -1:
#         cv2.imwrite('/Users/mac/Documents/GitHub/computer-vision/photo.jpg', frame)
#         break
# cap.release()
# cv2.destroyAllWindows()

#7. 카메라로 녹화하기
cap = cv2.VideoCapture(0)
file_path = "/Users/mac/Documents/GitHub/computer-vision/record.mp4"
fps = 25.40
fourcc = cv2.VideoWriter_fourcc(*'DIVX')   #인코딩 방식
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
size = (int(width), int(height))
out = cv2.VideoWriter(file_path, fourcc,fps,size)

while True:
    ret, frame= cap.read()
    cv2.imshow('camera', frame)
    out.write(frame) #파일저장
    if cv2.waitKey(1)!=-1:
        break

out.released()
cap.release()
cv2.destroyAllWindows()

