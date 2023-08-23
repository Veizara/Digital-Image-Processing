clc; clearvars; close all;
pkg load image
img1 = imread('image14.tif')

subplot(2,3,1)
imshow(img1)
title("Original (Noisy) Image")

img2=medfilt2(img1)
subplot(2,3,2)
imshow(img2)
title("Median Filtered Image")

PQ= paddedsize(size(img1))

H1 =notch('btw',PQ(1),PQ(2),5,430,486)
H2 =notch('btw',PQ(1),PQ(2),5,82,28)
H3 =notch('btw',PQ(1),PQ(2),6,14,10)
H4 =notch('btw',PQ(1),PQ(2),6,498,501)
img5=fftshift(H1.*H2.*H3.*H4)
subplot(2,3,5)
imshow(img5)
title("Notch Filters")

img3=fft2(double(img1),PQ(1),PQ(2))
FSimg = img3.*H1.*H2.*H3.*H4
img3=real(ifft2(FSimg))
img3=img3(1:size(img1,1), 1:size(img1,2))

subplot(2,3,3)
imshow(img3,[])
title("Notch Filtered Image")

img4=img1
Ff=fft2(img4)
Fsh=fftshift(Ff)
img4=log(1+abs(Fsh))
subplot(2,3,4)
imshow(img4,[])
title("Fourier Specturum of Noisy Image")

Fcf=fftshift(FSimg)
img6=log(1+abs(Fcf))
subplot(2,3,6)
imshow(img6,[])
title("Fourier Spectrum of Filtered Image")

#########################################
img1 = imread('image23.tif')
figure()
subplot(2,3,1)
imshow(img1)
title("Original (Noisy) Image")

img2=medfilt2(img1)
subplot(2,3,2)
imshow(img2)
title("Median Filtered Image")

PQ= paddedsize(size(img1))

H1 =notch('btw',PQ(1),PQ(2),5,16,82)
H2 =notch('btw',PQ(1),PQ(2),5,16,10)
H3 =notch('btw',PQ(1),PQ(2),6,496,430)
H4 =notch('btw',PQ(1),PQ(2),6,498,504)
img5=fftshift(H1.*H2.*H3.*H4)
subplot(2,3,5)
imshow(img5)
title("Notch Filters")

img3=fft2(double(img1),PQ(1),PQ(2))
FSimg = img3.*H1.*H2.*H3.*H4
img3=real(ifft2(FSimg))
img3=img3(1:size(img1,1), 1:size(img1,2))

subplot(2,3,3)
imshow(img3,[])
title("Notch Filtered Image")

img4=img1
Ff=fft2(img4)
Fsh=fftshift(Ff)
img4=log(1+abs(Fsh))
subplot(2,3,4)
imshow(img4,[])
title("Fourier Specturum of Noisy Image")

Fcf=fftshift(FSimg)
img6=log(1+abs(Fcf))
subplot(2,3,6)
imshow(img6,[])
title("Fourier Spectrum of Filtered Image")

