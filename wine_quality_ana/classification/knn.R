library(pROC) #����ROC����
library(kknn)

train_data$�ȼ� = factor(train_data$�ȼ�)
test_data$�ȼ� = factor(test_data$�ȼ�)

wine_knn <- kknn(�ȼ� ~  �ǻӷ�������   + �ӷ������� + ������ + ʣ���Ƿ�  
                   + �Ȼ��� + �����������+������������+Ũ��+pH+������+�ƾ�,
                   train_data,test_data,  k=7,distance = 2,kernel = 'rectangular')

pre_knn <- fitted(wine_knn)

table(test_data$�ȼ�, pre_knn,dnn=c("��ʵֵ","Ԥ��ֵ"))

knn_roc <- roc(test_data$�ȼ�,as.numeric(pre_knn))
plot(knn_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='knn�㷨ROC����')