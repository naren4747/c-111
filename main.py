from os import read, stat
import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv(r"data.csv")
readData=df["reading_time"].tolist()

mean1=statistics.mean(readData)

def random_Set_Of_Mean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(readData)-1)
        value=readData[randomIndex]
        dataSet.append(value)

    mean=statistics.mean(dataSet)
    return mean

meanList=[]

for i in range(0,1000):
    setOfMeans=random_Set_Of_Mean(100)
    meanList.append(setOfMeans)

sd=statistics.stdev(meanList)
mean=statistics.mean(meanList)
print("mean of sampling distubution :",mean)


sd1Start,sd1End=mean-sd,mean+sd
sd2Start,sd2End=mean-(2*sd),mean+(2*sd)
sd3Start,sd3End=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([meanList],["reading time mean"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean of 1000 means"))
fig.add_trace(go.Scatter(x=[sd1Start,sd1Start],y=[0,1],mode="lines",name="SD 1 start"))
fig.add_trace(go.Scatter(x=[sd1End,sd1End],y=[0,1],mode="lines",name="SD 1 end"))
fig.add_trace(go.Scatter(x=[sd2Start,sd2Start],y=[0,1],mode="lines",name="SD 2 start"))
fig.add_trace(go.Scatter(x=[sd2End,sd2End],y=[0,1],mode="lines",name="SD 2 end"))
fig.add_trace(go.Scatter(x=[sd3Start,sd3Start],y=[0,1],mode="lines",name="SD 3 start"))
fig.add_trace(go.Scatter(x=[sd3End,sd3End],y=[0,1],mode="lines",name="SD 3 end"))

fig.show()

zscore=(mean-mean1)/sd

print(zscore)