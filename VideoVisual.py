from lib2to3.fixer_util import p1
import matplotlib.pyplot as plt

from VideoProcessing import VideoProcessing


class VideoVisual:
    p1=VideoProcessing
    data=p1.videoprocess()
    def plotting(self,datas):
        plt.figure(figsize=(10,10))
        for i in range(0,25):
            plt.subplot(5,5,i)
            plt.imshow(datas[i], cmap=plt.cm.binary)
            plt.xticks([])
            plt.yticks([])
            plt.show()
    plotting(data)
