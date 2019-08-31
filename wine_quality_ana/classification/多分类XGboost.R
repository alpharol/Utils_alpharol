library("xgboost")



traindata1 <- data.matrix(train_data[,c(7:17)]) # 将自变量转化为矩阵
library(Matrix)
traindata2 <- Matrix(traindata1,sparse=T) # 利用Matrix函数，将sparse参数设置为TRUE，转化为稀疏矩阵
traindata3 <- as.numeric(as.character(train_data[,18]))
traindata4 <- list(data=traindata2,label=traindata3) # 将自变量和因变量拼接为list
dtrain <- xgb.DMatrix(data = traindata4$data, label = traindata4$label) # 构造模型需要的xgb.DMatrix对象，处理对象为稀疏矩阵

testset1 <- data.matrix(test_data[,c(7:17)]) # 将自变量转化为矩阵
testset2 <- Matrix(testset1,sparse=T) # 利用Matrix函数，将sparse参数设置为TRUE，转化为稀疏矩阵
testset3 <- as.numeric(as.factor(test_data[,18])) # 将因变量转化为numeric
testset4 <- list(data=testset2,label=testset3) # 将自变量和因变量拼接为list
dtest <- xgb.DMatrix(data = testset4$data, label = testset4$label) # 构造模型需要的xgb.DMatrix对象，处理对象为稀疏矩阵

param <- list(max_depth=2, eta=1, silent=1, objective='binary:logistic') # 定义模型参数
nround = 4

xgb <- xgboost(data = dtrain, nround=25)

pre_xgb = round(predict(xgb,newdata = dtest))

table(test_data$quality,pre_xgb,dnn=c("真实值","预测值"))

N=0
for (i in c(1:1470)){
  N =N + abs(test_data$quality[i]-pre_xgb[i])
}
MAD=N/1470
MAD

multiclass.roc(test_data$quality,as.numeric(pre_xgb),percent=TRUE)



traindata1 <- data.matrix(train_data[,c(2:5)]) # 将自变量转化为矩阵
library(Matrix)
traindata2 <- Matrix(traindata1,sparse=T) # 利用Matrix函数，将sparse参数设置为TRUE，转化为稀疏矩阵
traindata3 <- as.numeric(as.character(train_data[,18])) # 将因变量转化为numeric
traindata4 <- list(data=traindata2,label=traindata3) # 将自变量和因变量拼接为list
dtrain <- xgb.DMatrix(data = traindata4$data, label = traindata4$label) # 构造模型需要的xgb.DMatrix对象，处理对象为稀疏矩阵

testset1 <- data.matrix(test_data[,c(2:5)]) # 将自变量转化为矩阵
testset2 <- Matrix(testset1,sparse=T) # 利用Matrix函数，将sparse参数设置为TRUE，转化为稀疏矩阵
testset3 <- as.numeric(as.character(test_data[,18])) # 将因变量转化为numeric
testset4 <- list(data=testset2,label=testset3) # 将自变量和因变量拼接为list
dtest <- xgb.DMatrix(data = testset4$data, label = testset4$label) # 构造模型需要的xgb.DMatrix对象，处理对象为稀疏矩阵

param <- list(max_depth=2, eta=1, silent=1, objective='binary:logistic') # 定义模型参数
nround = 4

xgb <- xgboost(data = dtrain, nround=25)

pre_xgb = round(predict(xgb,newdata = dtest))


table(test_data$quality,pre_xgb,dnn=c("真实值","预测值"))

multiclass.roc(test_data$quality,as.numeric(pre_xgb),percent=TRUE)

N=0
for (i in c(1:1470)){
  N =N + abs(test_data$quality[i]-pre_xgb[i])
}
MAD=N/1470
MAD
