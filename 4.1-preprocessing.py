import cv2
import matplotlib.pyplot as plt
import numpy as np


# img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코1.jpg")

# #region of interest = roi (관심영역)
# x = 20; y = 50; w =50; h=50
# roi = img[y:y+h, x:x+w]

# print(roi.shape)
# #(50, 0, 3) 50 = 50가지의 디멘션 3d 안에서도 2d의 개수가 50개

# cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
# cv2.imshow("img", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#thresholding
"""
흑백사진의 정의 : binary image (0,255) 
일케 표현하는 ㅣㅇ유: 이미지에서 원하는 피사체의 모양을 좀 더 정확히 판단하기 위함.
종이에서 글씨를 분리, 배경에서 전경을 분리하는 작업 등

thresholding: 여러 점수를 커트라인 기준으로 합격 불합격으로 나누는 것처럼
여러 값을 경계점을 기준으로 두 가지로 분류로 나눈 것이다. 이렇게 나눠진 두가지
색 즉 흑,백이 바이너리 이미지를 만드는 가장 대표적인 방법이다.
"""

# import matplotlib.pylab as plt
# img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코6.jpg", cv2.IMREAD_GRAYSCALE)

# print(img)

# #numpy로 바이너리 이미지 만들어보기
# thresh_np = np.zeros_like(img)
# #print(thresh_np)
# thresh_np[img>127] = 255   #0=black, 255=white

# #openCV로 바이너리 이미지 만들어보기
# ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# imgs = {"Original": img, "Numpy": thresh_np, "OpenCV": thresh_cv}

# # for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(1,3,i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([]) #없어도 됨
# plt.show()




# img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코1.jpg", cv2.IMREAD_GRAYSCALE)

# _, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# _, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# _, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# _, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# _, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# imgs = {"Original": img, "binary": t_bin, "bininv": t_bininv, "truc": t_truc, "t_2zr" : t_2zr, "2zrinv": t_2zrinv}

# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(2,3,i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([]) #없어도 됨
# plt.show()




#자동으로 이미지에 맞게 threshold 적용해주는 알고리즘
"""
Otsu -> Nobuyuki Otsu 가 만든 오츠 알고리즘
-> 유동적으로 사진에 맞는 threshold를 결정하기 위해 사용됨
"""

# _, t_130 = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
# t, t_otsu = cv2.threshold(img,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# print('otsu threshold:', t)

# imgs = {"Original": img, "t_130": t_130, "otsu": t_otsu}

# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(1,3,i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([]) #없어도 됨
# plt.show()





"""
적응형 threshold 적용
# """
# blk_size = 9 
# C = 5 #바뀌지 않을 상수는 대문자로
# img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코1.jpg", cv2.IMREAD_GRAYSCALE)

# #오츠알고리즘으로 단일 경계값을 전체 이미지에 적용
# ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(th1)

# #adaptive threshold : 평균, 가우시안 분포로 각각 적용
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

# imgs = {'Original': img, 'Otsu': th1, 'Adaptive-Mean': th2, 'Adaptive-Gaussian': th3}
# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(2,2,i+1)
#     plt.title(key)
#     plt.imshow(value,'gray')
#     plt.xticks([])
#     plt.yticks([])

# plt.show()





# 합성 alpha blending
# img1 = cv2.imread("/Users/mac/Documents/GitHub/crawling/몬스타엑스기현/몬스타엑스기현11.jpg")
# img2 = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코1.jpg")
# img1 = cv2.resize(img1, (255,183))
# img2 = cv2.resize(img2, (255,183))

# img3 = img1 + img2   # 같은 쉐잎일때
# img4 = cv2.add(img1,img2)

# imgs={'img1': img1, 'img2': img2, 'img3': img3, 'img4': img4}
# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(2,2,i+1)
#     plt.imshow(value[:,:,::-1])
#     plt.title(key)
#     plt.xticks([])
#     plt.yticks([])

# plt.show()




"""
alpha blending: 가중치를 줘서 이미지 합성을 그럴싸하게
"""
# alpha = 0.9 #합성에 사용할 가중치 50%

# img1 = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/KakaoTalk_Photo_2022-06-10-20-48-22 001.jpeg")
# img2 = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/KakaoTalk_Photo_2022-06-10-20-48-22 002.jpeg")
# img1 = cv2.resize(img1, (1328,2000))
# img2 = cv2.resize(img2, (1328,2000))

# blended = img1*alpha + img2*(1-alpha)
# blended = blended.astype(np.uint8) #uint8 = usigned integer
# # signed integer = integer = 정수: 음수, 양수, 0 -> int16 -> -255,0,255
# # unsigned integer = 정수 오로지 양수와 0만 취급하는 정수 어차피 양수만 나옴 (256까지의 숫자만 사용 가능 0~255 = 256개)
# #cv2.imshow('blended', blended)

# des = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)

# cv2.imshow('cv2.addWeighted', des)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# alpha = 0.9 #합성에 사용할 가중치 50%

# img1 = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/KakaoTalk_Photo_2022-06-10-20-48-22 001.jpeg")
# img2 = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/KakaoTalk_Photo_2022-06-10-20-48-22 002.jpeg")
# img1 = cv2.resize(img1, (1328,2000))
# img2 = cv2.resize(img2, (1328,2000))

# """
# 트랙바로 알파 블렌딩하기
# """

# win_name = "Alpha Blending"
# trackbar_name = "fade"

# def onChange(x):
#     alpha = x/100
#     dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
#     cv2.imshow(win_name, dst)

# cv2.imshow(win_name, img1)
# cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





"""
이미지를 분석하자 -> 히스토그램!!!
"""

img1 = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/KakaoTalk_Photo_2022-06-10-20-48-22 001.jpeg")
cv2.imshow('img', img1)

#cv2.calHist(img, channel, mask, histSize, ranges)
colors = ('b','g','r')
channels = cv2.split(img1)

for (ch, color) in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
plt.show()