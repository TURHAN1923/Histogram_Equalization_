Histogram Equalization,
Görüntü işelme alanında kullanılan bir tekniktir.Görüntünün kontrastını arttırmakn için kullanılır.Bu işlem görüntünün histogramını kullanarak görüntünün piksel dağılımını dengeler ve daha iyi kontrast elde etmeyi sağlar.

Genellikle, bir görüntünün histogramı, görüntüdeki farklı piksel değerlerinin (genellikle 0 ile 255 arasında) görülme sıklığını gösterir. 

Eğer bir görüntünün histogramı geniş bir aralıkta homojen olarak dağılmışsa, görüntünün kontrastı yüksektir ve detaylar daha iyi görülebilir. Ancak, eğer histogram belirli bir aralıkta yoğunlaşmışsa, görüntünün kontrastı düşük olabilir ve detaylar belirsizleşebilir.

Histogram daha homojen dağılmayı sağlar.Temel olarak, bir görüntünün kümülatif dağılım fonksiyonu (CDF) hesaplanır ve bu fonksiyon kullanılarak piksel değerleri yeniden düzenlenir. Sonuç olarak, görüntüdeki piksel değerleri daha geniş bir aralığa dağılır ve kontrast artar.
Bazı durumlarda aşırı eşitleme yapılması sonucunda görüntüdeki detayların kaybolabileceği veya istenmeyen artefaktların oluşabileceği unutulmamalıdır. 
*******************************

Histogram Equalization,
It is a technique used in the field of image processing. It is used to increase the contrast of the image. This process balances the pixel distribution of the image by using the histogram of the image and provides better contrast.

Generally, the histogram of an image shows the frequency of occurrence of different pixel values ​​(usually between 0 and 255) in the image.

If the histogram of an image is homogeneously distributed over a wide range, the contrast of the image is high and details can be seen better. However, if the histogram is concentrated in a certain range, the contrast of the image may be low and details may be blurred.

Histogram provides more homogeneous distribution. Basically, the cumulative distribution function (CDF) of an image is calculated and pixel values ​​are rearranged using this function. As a result, pixel values ​​in the image are distributed over a wider range and contrast increases.
It should be kept in mind that in some cases, as a result of excessive equalization, details in the image may be lost or unwanted artifacts may occur.


***************************

import cv2
import numpy as np

def histogram_equalization(image):
    # Histogram eşitleme işlemi
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

# Örnek bir görüntü yükleme (grayscale)
image = cv2.imread("example_image.jpg", cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme uygulama
equalized_image = histogram_equalization(image)

# Görüntüyü gösterme
cv2.imshow("Original Image", image)
cv2.imshow("Equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


***************************
