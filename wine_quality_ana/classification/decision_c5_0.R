library(C50)

wine_decisiontree_C50 <-  C5.0(factor(�ȼ�) ~  �ǻӷ�������   + �ӷ������� + 
                                 ������ + ʣ���Ƿ�  + �Ȼ��� + �����������+
                                 ������������+Ũ��+pH+������+�ƾ�, data = train_data,trails=5)
printcp(wine_decisiontree_C50)

pre_decisiontree_C50 <- predict(wine_decisiontree_C50, test_data)
obs_p_decision_c50 = data.frame(prob=pre_decisiontree_C50,obs=test_data$�ȼ�)
table(test_data$�ȼ�,pre_decisiontree_C50,dnn=c("��ʵֵ","Ԥ��ֵ"))   

#����ROCͼ��
decisiontree_roc_c50 <- roc(test_data$�ȼ�,as.numeric(pre_decisiontree_C50))
plot(decisiontree_roc_c50, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='C5.0 �㷨ROC����')