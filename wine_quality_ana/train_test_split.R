library(openxlsx)
wine = read.xlsx("C:/Users/Mr.Reliable/Desktop/classification/winequality-red.xlsx") 
#将数据集分为训练集和测试集,比例为7:3
train_sub = sample(nrow(wine),7/10*nrow(wine))
train_data = wine[train_sub,]
test_data = wine[-train_sub,]



