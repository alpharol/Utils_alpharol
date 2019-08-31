library(pROC) #绘制ROC曲线
library(adabag)


#数据预处理
train_data$等级 = as.factor(train_data$等级)
test_data$等级 = as.factor(test_data$等级)

#Adaboost算法
wine_adaboost = boosting(等级~非挥发性酸性+挥发性酸性+柠檬酸+剩余糖分+氯化物+游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精, data = train_data,boos=TRUE, mfinal=500 )

#测试集
pre_decisiontree_ada <- predict(wine_adaboost,newdata = test_data)$class

#将测试集计算所得概率与观测本身取值整合到一起
obs_p_decision_ada= data.frame(prob=pre_decisiontree_ada,obs=test_data$等级)

table(test_data$等级,pre_decisiontree_ada,dnn=c("真实值","预测值"))

#计算Accuracy/Precision/Recall
a_ada=sum(obs_p_decision_ada$prob==0 & obs_p_decision_ada$obs==0)
b_ada=sum(obs_p_decision_ada$prob==1 & obs_p_decision_ada$obs==0)
c_ada=sum(obs_p_decision_ada$prob==0 & obs_p_decision_ada$obs==1)
d_ada=sum(obs_p_decision_ada$prob==1 & obs_p_decision_ada$obs==1)

Accuracy_ada = (a_ada+d_ada)/(a_ada+b_ada+c_ada+d_ada)
Precision_ada= d_ada/(b_ada+d_ada)
Recall_ada = d_ada/(c_ada+d_ada)

#绘制ROC图像
decisiontree_roc_ada <- roc(test_data$等级,as.numeric(pre_decisiontree_ada))
plot(decisiontree_roc_ada, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='Adaboost算法ROC曲线')