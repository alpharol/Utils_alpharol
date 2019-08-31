Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jdk1.8.0_191\\jre')
library(rJava)
library(RWeka)
library(pROC) #绘制ROC曲线


#C4.5算法
wine_decisiontree_C4_5 <- J48(factor(等级) ~  非挥发性酸性  
                                + 挥发性酸性 + 柠檬酸 + 剩余糖分  
                                + 氯化物 + 游离二氧化硫+二氧化硫总量+浓度
                                +pH+硫酸盐+酒精, data = train_data,
                                control = Weka_control(U = FALSE , R= TRUE, M=2,B=FALSE))
summary(wine_decisiontree_C4_5)
print(wine_decisiontree_C4_5)
plot(wine_decisiontree_C4_5,type = 'simpple') 


#在测试集上预测
pre_decisiontree_C4_5<-predict(wine_decisiontree_C4_5,newdata=test_data)

#将测试集计算所得概率与观测本身取值整合到一起
obs_p_decision_c4_5 = data.frame(prob=pre_decisiontree_C4_5,obs=test_data$等级)

#输出混淆矩阵
table(test_data$等级,pre_decisiontree_C4_5,dnn=c("真实值","预测值"))   

#计算Accuracy/Precision/Recall
a_c4_5=sum(obs_p_decision_c4_5$prob==0 & obs_p_decision_c4_5$obs==0)
b_c4_5=sum(obs_p_decision_c4_5$prob==1 & obs_p_decision_c4_5$obs==0)
c_c4_5=sum(obs_p_decision_c4_5$prob==0 & obs_p_decision_c4_5$obs==1)
d_c4_5=sum(obs_p_decision_c4_5$prob==1 & obs_p_decision_c4_5$obs==1)

Accuracy_c4_5 = (a_c4_5+d_c4_5)/(a_c4_5+b_c4_5+c_c4_5+d_c4_5)
Precision_c4_5= d_c4_5/(b_c4_5+d_c4_5)
Recall_c4_5 = d_c4_5/(c_c4_5+d_c4_5)

#绘制ROC图像
decisiontree_roc_C4_5 <- roc(test_data$等级,as.numeric(pre_decisiontree_C4_5))
plot(decisiontree_roc_C4_5, print.auc=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='C4.5算法ROC图像')














