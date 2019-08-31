library("xgboost")
library('pROC')
library(Matrix)



traindata1 <- data.matrix(train_data[,c(1:11)]) # ���Ա���ת��Ϊ����
traindata2 <- Matrix(traindata1,sparse=T) # ����Matrix��������sparse��������ΪTRUE��ת��Ϊϡ�����
traindata3 <- as.numeric(as.character(train_data[,13]))
traindata4 <- list(data=traindata2,label=traindata3) # ���Ա����������ƴ��Ϊlist
dtrain <- xgb.DMatrix(data = traindata4$data, label = traindata4$label) # ����ģ����Ҫ��xgb.DMatrix���󣬴�������Ϊϡ�����

testset1 <- data.matrix(test_data[,c(1:11)]) # ���Ա���ת��Ϊ����
testset2 <- Matrix(testset1,sparse=T) # ����Matrix��������sparse��������ΪTRUE��ת��Ϊϡ�����
testset3 <- as.numeric(as.factor(test_data[,13])) # �������ת��Ϊnumeric
testset4 <- list(data=testset2,label=testset3) # ���Ա����������ƴ��Ϊlist
dtest <- xgb.DMatrix(data = testset4$data, label = testset4$label) # ����ģ����Ҫ��xgb.DMatrix���󣬴�������Ϊϡ�����


xgb <- xgboost(data = dtrain,max_depth=6, eta=0.5,  objective='binary:logistic', nround=100)

pre_xgb = round(predict(xgb,newdata = dtest))

table(test_data$�ȼ�,pre_xgb,dnn=c("��ʵֵ","Ԥ��ֵ"))


xgboost_roc <- roc(test_data$�ȼ�,as.numeric(pre_xgb))
plot(xgboost_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='xgboostģ��ROC����')
