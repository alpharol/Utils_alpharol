library(pROC) #����ROC����
library(rpart)
library(rpart.plot)


#Cart�㷨
wine_decisiontree_cart <- rpart(�ȼ� ~  �ǻӷ�������   + �ӷ������� + ������ + ʣ���Ƿ�  + �Ȼ��� + �����������+������������+Ũ��+pH+������+�ƾ�, data = train_data, method="class",parms=list(split="gini"))

#ѡ��ʹ��xerror��С��cpֵ
printcp(wine_decisiontree_cart)
wine_decisiontree_cart_prune<-prune(wine_decisiontree_cart,cp= 0.010000 )
#����������
rpart.plot(wine_decisiontree_cart_prune,branch=1, fallen.leaves=T,cex=0.6)

#�ڲ��Լ���Ԥ��
pre_decisiontree_cart<-predict(wine_decisiontree_cart_prune,newdata=test_data,type="class")

#�����Լ��������ø�����۲Ȿ��ȡֵ���ϵ�һ��
obs_p_decision_cart = data.frame(prob=pre_decisiontree_cart,obs=test_data$�ȼ�)

#�����������
table(test_data$�ȼ�,pre_decisiontree_cart,dnn=c("��ʵֵ","Ԥ��ֵ"))   

#����Accuracy/Precision/Recall
a_cart=sum(obs_p_decision_cart$prob==0 & obs_p_decision_cart$obs==0)
b_cart=sum(obs_p_decision_cart$prob==1 & obs_p_decision_cart$obs==0)
c_cart=sum(obs_p_decision_cart$prob==0 & obs_p_decision_cart$obs==1)
d_cart=sum(obs_p_decision_cart$prob==1 & obs_p_decision_cart$obs==1)

Accuracy_cart = (a_cart+d_cart)/(a_cart+b_cart+c_cart+d_cart)
Precision_cart= d_cart/(b_cart+d_cart)
Recall_cart = d_cart/(c_cart+d_cart)

#����ROCͼ��
decisiontree_roc_cart <- roc(test_data$�ȼ�,as.numeric(pre_decisiontree_cart))
plot(decisiontree_roc_cart, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='Cart�㷨ROC����')