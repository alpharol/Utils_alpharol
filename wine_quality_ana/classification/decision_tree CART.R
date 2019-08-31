library(pROC) #绘制ROC曲线
library(rpart)
library(rpart.plot)


#Cart算法
wine_decisiontree_cart <- rpart(等级 ~  非挥发性酸性   + 挥发性酸性 + 柠檬酸 + 剩余糖分  + 氯化物 + 游离二氧化硫+二氧化硫总量+浓度+pH+硫酸盐+酒精, data = train_data, method="class",parms=list(split="gini"))

#选择使得xerror最小的cp值
printcp(wine_decisiontree_cart)
wine_decisiontree_cart_prune<-prune(wine_decisiontree_cart,cp= 0.010000 )
#画出决策树
rpart.plot(wine_decisiontree_cart_prune,branch=1, fallen.leaves=T,cex=0.6)

#在测试集上预测
pre_decisiontree_cart<-predict(wine_decisiontree_cart_prune,newdata=test_data,type="class")

#将测试集计算所得概率与观测本身取值整合到一起
obs_p_decision_cart = data.frame(prob=pre_decisiontree_cart,obs=test_data$等级)

#输出混淆矩阵
table(test_data$等级,pre_decisiontree_cart,dnn=c("真实值","预测值"))   

#计算Accuracy/Precision/Recall
a_cart=sum(obs_p_decision_cart$prob==0 & obs_p_decision_cart$obs==0)
b_cart=sum(obs_p_decision_cart$prob==1 & obs_p_decision_cart$obs==0)
c_cart=sum(obs_p_decision_cart$prob==0 & obs_p_decision_cart$obs==1)
d_cart=sum(obs_p_decision_cart$prob==1 & obs_p_decision_cart$obs==1)

Accuracy_cart = (a_cart+d_cart)/(a_cart+b_cart+c_cart+d_cart)
Precision_cart= d_cart/(b_cart+d_cart)
Recall_cart = d_cart/(c_cart+d_cart)

#绘制ROC图像
decisiontree_roc_cart <- roc(test_data$等级,as.numeric(pre_decisiontree_cart))
plot(decisiontree_roc_cart, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='Cart算法ROC曲线')
