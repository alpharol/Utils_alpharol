library(pROC) #绘制ROC曲线
library(e1071)



train_data$等级 = as.factor(train_data$等级)
test_data$等级 = as.factor(test_data$等级)
#svm
wine_svm<- svm(等级 ~  非挥发性酸性   + 挥发性酸性 + 柠檬酸 + 
                   剩余糖分  + 氯化物 + 游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精, 
                 data = train_data,
                 type = 'C',kernel = 'polynomial' )

#测试集
pre_svm <- predict(wine_svm,newdata = test_data)

obs_p_svm = data.frame(prob=pre_svm,obs=test_data$等级)

table(test_data$等级,pre_svm,dnn=c("真实值","预测值"))

obs_p_svm$prob = as.numeric(obs_p_svm$prob)
obs_p_svm$obs  = as.numeric(obs_p_svm$obs)

a_svm=sum(obs_p_svm$prob==0 & obs_p_svm$obs==0)
b_svm=sum(obs_p_svm$prob==1 & obs_p_svm$obs==0)
c_svm=sum(obs_p_svm$prob==0 & obs_p_svm$obs==1)
d_svm=sum(obs_p_svm$prob==1 & obs_p_svm$obs==1)

Accuracy_svm = (a_svm+d_svm)/(a_svm+b_svm+c_svm+d_svm)
Precision_svm = d_svm/(b_svm+d_svm)
Recall_svm = d_svm/(c_svm+d_svm)


svm_roc <- roc(test_data$等级,as.numeric(pre_svm))
plot(svm_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='SVM模型ROC曲线 kernel = polynomial')