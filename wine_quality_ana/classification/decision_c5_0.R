library(C50)

wine_decisiontree_C50 <-  C5.0(factor(等级) ~  非挥发性酸性   + 挥发性酸性 + 
                                 柠檬酸 + 剩余糖分  + 氯化物 + 游离二氧化硫+
                                 二氧化硫总量+浓度+pH+硫酸盐+酒精, data = train_data,trails=5)
printcp(wine_decisiontree_C50)

pre_decisiontree_C50 <- predict(wine_decisiontree_C50, test_data)
obs_p_decision_c50 = data.frame(prob=pre_decisiontree_C50,obs=test_data$等级)
table(test_data$等级,pre_decisiontree_C50,dnn=c("真实值","预测值"))   

#绘制ROC图像
decisiontree_roc_c50 <- roc(test_data$等级,as.numeric(pre_decisiontree_C50))
plot(decisiontree_roc_c50, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='C5.0 算法ROC曲线')