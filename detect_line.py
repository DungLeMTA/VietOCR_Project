#!/usr/bin/python3
# 2018.01.16 01:11:49 CST
# 2018.01.16 01:55:01 CST
import cv2
import numpy as np

def line_cut(img):
    ## (1) read - doc anh, convert anh ve dang thuoc xam
    # img = cv2.imread("mm.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('0',gray)
    # cv2.waitKey(0)

    ## (2) threshold - dat nguong gi  a tri cua anh
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    # cv2.imwrite("rr1.png", threshed)

    cv2.imshow('1',threshed)
    cv2.waitKey(0)


    ## (3) minAreaRect on the nozeros
    # ma tran cac diem khac 0
    pts = cv2.findNonZero(gray)
    # tra ve cac thong so cua hinh chu nhat quay co dien tich nho nhat
    ret = cv2.minAreaRect(pts)
    (cx,cy), (w,h), ang = ret
    print('w: ',img.shape[1],'h: ',img.shape[0])
    print('w1: ', w,'h2: ',h)

    # neu w > h thi quay them 90'
    if img.shape[1]<img.shape[0] and w>h:
        print('run1')
        w,h = h,w
        ang -= 90

    if img.shape[1]>img.shape[0] and w<h:
        print('run2')
        w,h = h,w
        ang -= 90

    ## (4) Find rotated matrix, do rotation
    # truyen tham so ve tam, goc quay va ti le cua hinh de thuc hien quay ma tran
    M = cv2.getRotationMatrix2D((cx,cy), ang, 1.0)
    # truyen anh, ma tran bien doi M va kich thuoc anh de quay, tra ve anh da duoc quay
    rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))

    ## (5) find and draw the upper and lower boundary of each lines
    # giam chieu ma tran 2D ve 1D, sau do reshape ma tran voi so chieu va so kenh khac
    hist = cv2.reduce(rotated,1, cv2.REDUCE_AVG).reshape(-1)

    thresh = 0
    # kich thuoc anh
    H,W = img.shape[:2]

    # luu lai hang pixel co su thay doi ve gia tri mau sac
    # danh dau dong ke tren
    uppers_y = [y for y in range(H-1) if hist[y]<=thresh and hist[y+1]>thresh]
    # danh dau dong ke duoi
    lowers_y = [y for y in range(H-1) if hist[y]>thresh and hist[y+1]<=thresh]

    # right_x = [x for x in range(W-1) if hist[x]<=thresh and hist[x+1]>thresh]
    #
    # left_x = [x for x in range(W-1) if hist[x]>thresh and hist[x+1]<=thresh]


    # convert anh tu dang thuoc xam sang anh mau
    rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
    # cv2.imwrite("rr2.png", rotated)
    # cv2.imshow('2',rotated)
    # cv2.waitKey(0)

    if uppers_y[0] > lowers_y[0]:
        uppers_y.insert(0,0)

    if uppers_y[len(uppers_y)-1] > lowers_y[len(lowers_y)-1]:
        lowers_y.append(H)

    # ve duong gioi han tren
    # for y in range(0,len(uppers_y)):
    #     right_x = [x for x in range(uppers_y[y],lowers_y[y]) if hist[x] <= thresh and hist[x + 1] > thresh]
    #     left_x = [x for x in range(uppers_y[y],lowers_y[y]) if hist[x] > thresh and hist[x + 1] <= thresh]

        # vẽ bounding box
        # print(right_x)
        # print(left_x)
        # for r in range(0,len(right_x)):
        #     cv2.rectangle(img=rotated,pt1=(right_x[r],uppers_y[y]),pt2=(left_x[r],lowers_y[y]),color=(200,0,0),
        #                   thickness=1,lineType=cv2.LINE_AA,shift=0)
        #     cv2.imshow('result', rotated)
        #     cv2.waitKey(0)

    re = int(H/180)
    min = 10
    for y in range(0,len(uppers_y)):
        if lowers_y[y] - uppers_y[y] <= min :
            # if y != len(uppers_y)-1:
            #     uppers_y[y+1] = uppers_y[y]
                # lowers_y[y+1] = uppers_y[y+1]
            pass
        else:
            cv2.line(rotated, (0,uppers_y[y]-re), (W,uppers_y[y]-re), (255,0,0), 1)
            cv2.line(rotated, (0,lowers_y[y]+re), (W,lowers_y[y]+re), (0, 255, 0), 1)
            crop_img = img[uppers_y[y]-re:lowers_y[y]+re, 0:W]
            cv2.imshow("cropped", crop_img)
            cv2.waitKey(0)
            cv2.imwrite('./result_linecut/crop_'+str(y)+'.png',crop_img)

    # ve duong gioi han duoi
    # for l_y in lowers_y:
    #     cv2.line(rotated, (0,l_y), (W, l_y), (0,255,0), 1)

    # for r_x in right_x:
    #     cv2.line(rotated, (r_x,0), (r_x,H), (255,0,0), 1)
    #
    # for l_x in left_x:
    #     cv2.line(rotated, (l_x,0), (l_x,H), (0,255,0), 1)


    # tao anh
    # cv2.imwrite("rr3.png", rotated)
    # cv2.imshow('3',rotated)
    # cv2.waitKey(0)

    return rotated

if __name__ == '__main__':


    img = './test/vanban1.jpg'

    a = cv2.imread(img)
    # cv2.imshow('1',a)
    # cv2.waitKey(0)

    image1 = line_cut(a)
    # cv2.imshow('result',image1)
    #     # cv2.waitKey(0)
    #     # cv2.imwrite('',image1)