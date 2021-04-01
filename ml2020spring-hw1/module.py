import csv

# 開啟 CSV 檔案
with open('train.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  
  data=[]
  features=[]
  count=0
  w=[0.1]*19 #為"權重"
  # 以迴圈輸出每一列
  for row in rows:
    if count<=18:
        features.append(row[2])
        count+=1
        
    if row[2]=="RAINFALL":
        for i,element in enumerate(row):
            if element=="NR":
                row[i]=0

    data.append(row)
pm2_5=[];pm2_5_pointer=10 #pm2_5為真實數值 pm_2_5_pointer輔助收集pm2.5

pm2_5_prediction=[] #pm2.5的預測值
while pm2_5_pointer<len(data): #pm2.5 連續值
    for i in data[pm2_5_pointer][3:]:
        pm2_5.append(float(i))
        pm2_5_pointer+=18 
print(data[1][2])
pm2_5_prediction.append(float(pm2_5[0])) #initial pm2.5預測值


def gradient(w,pm2_5,pm2_5_prediction,index,feature):
    learning_rate=0.01
    residual=(pm2_5[index]-pm2_5_prediction[index]) #殘差
    print("residual=",residual)
    
    #loss=residual**2
    count=0
    while count<=10:
        for i,element in enumerate(w):
            if i==0:
                w[i]=w[i]-learning_rate*(2*residual)*(-1)
            else:
                w[i]=w[i]-learning_rate*(2*residual)*(-1*feature[i-1])
        pm2_5_prediction[index]=w[0]
        for i,element in enumerate(w[1:]):
            pm2_5_prediction[index]+=element*feature[i]
        residual=(pm2_5[index]-pm2_5_prediction[index]) #殘差    
        count+=1
        print(w)
    print(feature)

def predict():
    global w,pm2_5,data,pm2_5_prediction
    temp=0
    day=0
    pm2_5_index=1
    feature=[]
    count=1#test
    while (day+1)*18*24<len(data):
        for j in range(3,27): #每進一格表過一個小時
            temp+=w[0]
            for i in range(1,19):
                
                temp+=w[i]*float(data[i+18*day][j]) #init data[1][3],data[2][3]...
                feature.append(float(data[i+18*day][j]))
            pm2_5_prediction.append(temp) #將每個小時的預測值收納
            if count<=1: #test
                gradient(w,pm2_5,pm2_5_prediction,pm2_5_index,feature)
                
            count+=1 #test 
            feature=[]
            pm2_5_index+=1
            temp=0
        day+=1 #表示資料掃過一天
    print(day)   
predict()       
        
 