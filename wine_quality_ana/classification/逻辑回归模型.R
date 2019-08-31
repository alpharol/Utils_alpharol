#逻辑回归方法
library(pROC) #绘制ROC曲线

#对训练集进行逻辑回归
wine_logistic <- glm(等级 ~  挥发性酸性+氯化物+游离二氧化硫+二氧化硫总量
                  +硫酸盐+酒精, data = train_data, family = "binomial")
wine_logistic <- glm(等级 ~  非挥发性酸性   + 挥发性酸性 + 
                         柠檬酸 + 剩余糖分  + 氯化物 + 
                         游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精,
                       data = train_data, family = "binomial")
#对逻辑回归结果进行汇总
summary(wine_logistic)

#对测试集进行预测
pre_logistic<-as.numeric(predict(wine_logistic,newdata=test_data,type="response")>0.5)
#将测试集计算所得概率与观测本身取值整合到一起
obs_p_logistic = data.frame(prob=pre_logistic,obs=test_data$等级)

#输出混淆矩阵
table(test_data$等级,pre_logistic,dnn=c("真实值","预测值"))   

#计算Accuracy/Precision/Recall
a_logi=sum(obs_p_logistic$prob<0.5 & obs_p_logistic$obs==0)
b_logi=sum(obs_p_logistic$prob>0.5 & obs_p_logistic$obs==0)
c_logi=sum(obs_p_logistic$prob<0.5 & obs_p_logistic$obs==1)
d_logi=sum(obs_p_logistic$prob>0.5 & obs_p_logistic$obs==1)

Accuracy_logistic = (a_logi+d_logi)/(a_logi+b_logi+c_logi+d_logi)
Precision_logistic = d_logi/(b_logi+d_logi)
Recall_logistic = d_logi/(c_logi+d_logi)

#绘制ROC曲线
logistic_roc <- roc(test_data$等级,pre_logistic)
plot(logistic_roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='逻辑回归ROC曲线')
