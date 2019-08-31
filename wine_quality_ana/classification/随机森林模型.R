#randonForest方法
library(pROC) #绘制ROC曲线
library(randomForest)

train_data$等级 = as.factor(train_data$等级)
test_data$等级 = as.factor(test_data$等级)

#randomforest
wine_randomforest <- randomForest(等级 ~  非挥发性酸性   + 挥发性酸性 + 柠檬酸 + 剩余糖分  + 氯化物 + 游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精,data = train_data,mtry=3,importance=TRUE ,proximity=TRUE)

#查看变量的重要性
wine_randomforest$importance
varImpPlot(wine_randomforest, main = "variable importance")


#测试集
pre_ran <- predict(wine_randomforest,newdata=test_data)

obs_p_ran = data.frame(prob=pre_ran,obs=test_data$等级)

table(test_data$等级,pre_ran,dnn=c("真实值","预测值"))

a_ran=sum(obs_p_ran$prob==0 & obs_p_ran$obs==0)
b_ran=sum(obs_p_ran$prob==1 & obs_p_ran$obs==0)
c_ran=sum(obs_p_ran$prob==0 & obs_p_ran$obs==1)
d_ran=sum(obs_p_ran$prob==1 & obs_p_ran$obs==1)

Accuracy_ran = (a_ran+d_ran)/(a_ran+b_ran+c_ran+d_ran)
Precision_ran = d_ran/(b_ran+d_ran)
Recall_ran = d_ran/(c_ran+d_ran)

ran_roc <- roc(test_data$等级,as.numeric(pre_ran))
plot(ran_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='随机森林模型ROC曲线')