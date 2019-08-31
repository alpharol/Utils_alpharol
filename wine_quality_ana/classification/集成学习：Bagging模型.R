library(pROC) #绘制ROC曲线
library(adabag)
#数据预处理
train_data$等级 = factor(train_data$等级)
test_data$等级 = factor(test_data$等级)
#bagging算法
wine_bagging <- bagging(等级 ~  非挥发性酸性   + 挥发性酸性 + 柠檬酸 + 剩余糖分  + 氯化物 + 游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精, data = train_data,mfinal=500 )


#测试集
pre_decisiontree_bag <- as.numeric(predict(wine_bagging,newdata = test_data)$class)
#将测试集计算所得概率与观测本身取值整合到一起
obs_p_decision_bag= data.frame(prob=pre_decisiontree_bag,obs=test_data$等级)
#输出混淆矩阵
table(test_data$等级,pre_decisiontree_bag,dnn=c("真实值","预测值"))

#计算Accuracy/Precision/Recall
a_bag=sum(obs_p_decision_bag$prob==0 & obs_p_decision_bag$obs==0)
b_bag=sum(obs_p_decision_bag$prob==1 & obs_p_decision_bag$obs==0)
c_bag=sum(obs_p_decision_bag$prob==0 & obs_p_decision_bag$obs==1)
d_bag=sum(obs_p_decision_bag$prob==1 & obs_p_decision_bag$obs==1)

Accuracy_bag = (a_bag+d_bag)/(a_bag+b_bag+c_bag+d_bag)
Precision_bag= d_bag/(b_bag+d_bag)
Recall_bag = d_bag/(c_bag+d_bag)

#绘制ROC曲线
decisiontree_roc_bag <- roc(test_data$等级,pre_decisiontree_bag)
plot(decisiontree_roc_bag, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='Bagging算法ROC曲线')

plot(decisiontree_roc_ada, col="black")  
plot.roc(decisiontree_roc_bag, add=TRUE, col="red") 
legend("bottomright", legend=c("Adaboost", "Bagging"), col=c("1", "2"), lwd=2)