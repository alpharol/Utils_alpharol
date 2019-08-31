library(pROC) #绘制ROC曲线
library(rpart)
library(rpart.plot)


#ID3算法
wine_decisiontree_ID3 <- rpart(等级 ~  非挥发性酸性 
                                 + 挥发性酸性 + 柠檬酸 + 剩余糖分 
                                 + 氯化物 + 游离二氧化硫+二氧化硫总量+
                                   浓度+pH+硫酸盐+酒精, data = train_data,
                                 method="class",parms=list(split="information"))

#树的剪枝判断
printcp(wine_decisiontree_ID3)
#树的剪枝，选择使得xerror最小的cp值
wine_decisiontree_ID3_prune<-prune(wine_decisiontree_ID3,cp= 0.010000)
#树图
rpart.plot(wine_decisiontree_ID3_prune,branch=1, fallen.leaves=T,cex=0.6)

#在测试集上预测
pre_decisiontree_ID3<-predict(wine_decisiontree_ID3_prune,newdata=test_data,type="class")

#将测试集计算所得概率与观测本身取值整合到一起
obs_p_decision_ID3 = data.frame(prob=pre_decisiontree_ID3,obs=test_data$等级)

#输出混淆矩阵
table(test_data$等级,pre_decisiontree_ID3,dnn=c("真实值","预测值"))    

#计算Accuracy/Precision/Recall
a_ID3=sum(obs_p_decision_ID3$prob==0 & obs_p_decision_ID3$obs==0)
b_ID3=sum(obs_p_decision_ID3$prob==1 & obs_p_decision_ID3$obs==0)
c_ID3=sum(obs_p_decision_ID3$prob==0 & obs_p_decision_ID3$obs==1)
d_ID3=sum(obs_p_decision_ID3$prob==1 & obs_p_decision_ID3$obs==1)

Accuracy_ID3 = (a_ID3+d_ID3)/(a_ID3+b_ID3+c_ID3+d_ID3)
Precision_ID3 = d_ID3/(b_ID3+d_ID3)
Recall_ID3 = d_ID3/(c_ID3+d_ID3)

#绘制ROC曲线
decisiontree_roc_ID3 <- roc(test_data$等级,as.numeric(pre_decisiontree_ID3))
plot(decisiontree_roc_ID3, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='ID3算法ROC曲线')







