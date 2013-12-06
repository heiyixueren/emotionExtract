#-*- coding: utf-8 -*-
import tms

if __name__ == '__main__':
    tms.tms_train("../twitterData/emotion/emotionTrain.txt",main_save_path="./",seg=1)
    #tms.tms_segment("../twitterData/emotion/twitterTestData.txt",[1],"../twitterData/emotion/twitterTestData1.txt","^","\t",1)
    #tms.tms_predict("../twitterData/emotion/twitterTestData1.txt","./model/tms.config",result_save_path="../twitterData/emotion/tms.result")
