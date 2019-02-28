#!/usr/bin/env python3

from PIL import Image,ImageFilter

def foo_image():
    im = Image.open('pillow_test.jpg')
    w,h=im.size
    print('Original image size: %s * %s' % (w,h))
    im.thumbnail((w//2,h//2))
    im.save('thumbnail.jpg','jpeg')

def foo_filter():
    im = Image.open('pillow_test.jpg')
    im2=im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg','jpeg')

if __name__=="__main__":
    #foo_image()
    foo_filter()