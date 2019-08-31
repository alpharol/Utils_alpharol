library("xgboost")
library('pROC')
library(Matrix)



traindata1 <- data.matrix(train_data[,c(1:11)]) # 将自变量转化为矩阵
traindata2 <- Matrix(traindata1,sparse=T) # 利用Matrix函数，将sparse参数设置为TRUE，转化为稀疏矩阵
traindata3 <- as.numeric(as.character(train_data[,13]))
traindata4 <- list(data=traindata2,label=traindata3) # 将自变量和因变量拼接为list
dtrain <- xgb.DMatrix(data = traindata4$data, label = traindata4$label) # 构造模型需要的xgb.DMatrix对象，处理对象为稀疏矩阵

testset1 <- data.matrix(test_data[,c(1:11)]) # 将自变量转化为矩阵
testset2 <- Matrix(testset1,sparse=T) # 利用Matrix函数，将sparse参数设置为TRUE，转化为稀疏矩阵
testset3 <- as.numeric(as.factor(test_data[,13])) # 将因变量转化为numeric
testset4 <- list(data=testset2,label=testset3) # 将自变量和因变量拼接为list
dtest <- xgb.DMatrix(data = testset4$data, label = testset4$label) # 构造模型需要的xgb.DMatrix对象，处理对象为稀疏矩阵


xgb <- xgboost(data = dtrain,max_depth=6, eta=0.5,  objective='binary:logistic', nround=100)

pre_xgb = round(predict(xgb,newdata = dtest))

table(test_data$等级,pre_xgb,dnn=c("真实值","预测值"))


xgboost_roc <- roc(test_data$等级,as.numeric(pre_xgb))
plot(xgboost_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='xgboost模型ROC曲线')

