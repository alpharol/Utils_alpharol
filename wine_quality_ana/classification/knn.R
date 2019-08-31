library(pROC) #绘制ROC曲线
library(kknn)

train_data$等级 = factor(train_data$等级)
test_data$等级 = factor(test_data$等级)

wine_knn <- kknn(等级 ~  非挥发性酸性   + 挥发性酸性 + 柠檬酸 + 剩余糖分  
                   + 氯化物 + 游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精,
                   train_data,test_data,  k=7,distance = 2,kernel = 'rectangular')

pre_knn <- fitted(wine_knn)

table(test_data$等级, pre_knn,dnn=c("真实值","预测值"))

knn_roc <- roc(test_data$等级,as.numeric(pre_knn))
plot(knn_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='knn算法ROC曲线')