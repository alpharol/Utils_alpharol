library(pROC) #����ROC����
library(rpart)
library(rpart.plot)


#ID3�㷨
wine_decisiontree_ID3 <- rpart(�ȼ� ~  �ǻӷ������� 
                                 + �ӷ������� + ������ + ʣ���Ƿ� 
                                 + �Ȼ��� + �����������+������������+
                                   Ũ��+pH+������+�ƾ�, data = train_data,
                                 method="class",parms=list(split="information"))

#���ļ�֦�ж�
printcp(wine_decisiontree_ID3)
#���ļ�֦��ѡ��ʹ��xerror��С��cpֵ
wine_decisiontree_ID3_prune<-prune(wine_decisiontree_ID3,cp= 0.010000)
#��ͼ
rpart.plot(wine_decisiontree_ID3_prune,branch=1, fallen.leaves=T,cex=0.6)

#�ڲ��Լ���Ԥ��
pre_decisiontree_ID3<-predict(wine_decisiontree_ID3_prune,newdata=test_data,type="class")

#�����Լ��������ø�����۲Ȿ��ȡֵ���ϵ�һ��
obs_p_decision_ID3 = data.frame(prob=pre_decisiontree_ID3,obs=test_data$�ȼ�)

#�����������
table(test_data$�ȼ�,pre_decisiontree_ID3,dnn=c("��ʵֵ","Ԥ��ֵ"))    

#����Accuracy/Precision/Recall
a_ID3=sum(obs_p_decision_ID3$prob==0 & obs_p_decision_ID3$obs==0)
b_ID3=sum(obs_p_decision_ID3$prob==1 & obs_p_decision_ID3$obs==0)
c_ID3=sum(obs_p_decision_ID3$prob==0 & obs_p_decision_ID3$obs==1)
d_ID3=sum(obs_p_decision_ID3$prob==1 & obs_p_decision_ID3$obs==1)

Accuracy_ID3 = (a_ID3+d_ID3)/(a_ID3+b_ID3+c_ID3+d_ID3)
Precision_ID3 = d_ID3/(b_ID3+d_ID3)
Recall_ID3 = d_ID3/(c_ID3+d_ID3)

#����ROC����
decisiontree_roc_ID3 <- roc(test_data$�ȼ�,as.numeric(pre_decisiontree_ID3))
plot(decisiontree_roc_ID3, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='ID3�㷨ROC����')






