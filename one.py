import csv
import pandas as pd
with open("data.csv",'r')as file:
   filecontent=csv.reader(file)
   c=0
   gt=[]
   lh=[]
   df_modified = pd.DataFrame()
   df_modified={
       "duration":[],"Pulse":[],"Calories":[]
   }
   for row in filecontent:
        if(c>1):
            for j in range(0,len(row)):
                if(row[j]!=""):
                    row[j]=float(row[j])
                else:
                    row[j]=False

        c=c+1
        if(False in row):
            index=row.index(False)
            mean=sum(row)/len(row)
            row[index]=mean
            print(row)
        #the rows with calories values between 500 and 1000
        if(c>2):
            if(row[3]<=1000 and row[3]>=500):
                gt.append(row)
                #print("the rows with calories values between 500 and 1000",row)
            if(row[3]>500 and row[1]<100):
                lh.append(row)
                #print(" the rows with calories values > 500 and pulse < 100",row)
        df_modified["duration"].append(row[0])
        df_modified["Pulse"].append(row[2])
        df_modified["Calories"].append(row[3])
        row.pop(2)
    print(filecontent)







                


            
