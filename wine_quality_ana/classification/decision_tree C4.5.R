Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jdk1.8.0_191\\jre')
library(rJava)
library(RWeka)
library(pROC) #����ROC����


#C4.5�㷨
wine_decisiontree_C4_5 <- J48(factor(�ȼ�) ~  �ǻӷ�������  
                                + �ӷ������� + ������ + ʣ���Ƿ�  
                                + �Ȼ��� + �����������+������������+Ũ��
                                +pH+������+�ƾ�, data = train_data,
                                control = Weka_control(U = FALSE , R= TRUE, M=2,B=FALSE))
summary(wine_decisiontree_C4_5)
print(wine_decisiontree_C4_5)
plot(wine_decisiontree_C4_5,type = 'simpple') 


#�ڲ��Լ���Ԥ��
pre_decisiontree_C4_5<-predict(wine_decisiontree_C4_5,newdata=test_data)

#�����Լ��������ø�����۲Ȿ��ȡֵ���ϵ�һ��
obs_p_decision_c4_5 = data.frame(prob=pre_decisiontree_C4_5,obs=test_data$�ȼ�)

#�����������
table(test_data$�ȼ�,pre_decisiontree_C4_5,dnn=c("��ʵֵ","Ԥ��ֵ"))   

#����Accuracy/Precision/Recall
a_c4_5=sum(obs_p_decision_c4_5$prob==0 & obs_p_decision_c4_5$obs==0)
b_c4_5=sum(obs_p_decision_c4_5$prob==1 & obs_p_decision_c4_5$obs==0)
c_c4_5=sum(obs_p_decision_c4_5$prob==0 & obs_p_decision_c4_5$obs==1)
d_c4_5=sum(obs_p_decision_c4_5$prob==1 & obs_p_decision_c4_5$obs==1)

Accuracy_c4_5 = (a_c4_5+d_c4_5)/(a_c4_5+b_c4_5+c_c4_5+d_c4_5)
Precision_c4_5= d_c4_5/(b_c4_5+d_c4_5)
Recall_c4_5 = d_c4_5/(c_c4_5+d_c4_5)

#����ROCͼ��
decisiontree_roc_C4_5 <- roc(test_data$�ȼ�,as.numeric(pre_decisiontree_C4_5))
plot(decisiontree_roc_C4_5, print.auc=TRUE, auc.polygon=TRUE, max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='C4.5�㷨ROCͼ��')













