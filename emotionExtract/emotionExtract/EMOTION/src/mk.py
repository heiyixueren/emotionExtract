import tms
tms.tms_train("../data/Traindata_noseg.txt",main_save_path="./",seg=1)
tms.tms_predict("../data/Testdata.txt","./model/tms.config",result_save_path="./tms.result")
