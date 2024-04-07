import cv2 
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("C:/Users/Emre/Pictures/taskimage/trk.jpg")
    
hist,bins=np.histogram(img.flatten(),256,[0,256])
#verilen görüntünün histogramı burada hesaplanır. 
#hist= histogramdaki değerlerin sayılarnı içerir.   bins= histogramın kenarlarını belirler.
cdf=hist.cumsum()
#CDF hesaplamak için kullanılır.Histogramdaki belirli bir değerin olasılığını hesaplamak için kullanılır.
cdf_normalized=cdf*float(hist.max())/cdf.max()
#Hesaplanan kümülatif dağılım fonksiyonunu CDF normalize etmek için kullanılır.
#hist.max= Histogramdaki en büyük değeri,CDF deki en büyük deperi temsil eder.CDF de olabilecek max piksel sayısını belirtir.
#cdf.max= CDFnin max değerini verir.
 
plt.plot(cdf_normalized,color = 'b')
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()