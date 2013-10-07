dir = '/home/sunnymh/stat157/questionnaire_group7/'

library(vioplot)
library(pheatmap)
library(plotrix)

mydata = read.csv(paste(dir, 'data.csv', sep = ''), colClasses=c("character",rep("numeric",8)))
learing_cats = c('Aural', 'Kinesthetic', 'Read_Write', 'Visual')
class_cats = c('STAT133', 'STAT134', 'STAT135', 'CS')

##################
# Learning Style #
##################

# 1. Distribution of learning style
png(paste(dir, 'hist_style.png', sep = ''), 500, 400)
with(mydata, 
     multhist(list(Aural,Kinesthetic,Read_Write,Visual), 
              main = "Learning style", xlab = "score", ylab = "count", 
              col = c("yellow", "red", "blue", "green")))
legend("topright", learing_cats, fill = c("yellow", "red", "blue", "green"), cex = 0.8)
dev.off()

png(paste(dir, 'violin_style.png', sep = ''), 500, 400)
with(mydata, 
     vioplot(Aural,Kinesthetic,Read_Write,Visual, names = learing_cats, col = "lightblue"))
title("Violin Plots for learning style")
dev.off()

# Conclusions:
# Due to the limit of the size of the data, we can't really say much about the data. 
# Still Aural score seems to be evenly spread out from 0 to 10.
# The other three scores has a larger spread.
# Seems like the scores could fit with a normal distribution.

# 2. Check how good each parameter fits with normal distribution.
check_normal = function(data, name){
  data.norm = (data - mean(data))/sd(data)
  qqnorm(data.norm, xlim = c(-1,1), ylim = c(-1,1),  main = paste("Normal Q-Q Plot for ", name), cex = 0.5, pch = 19)
  abline(0, 1)
}
png(paste(dir, 'normal_style.png', sep = ''), 900, 800)
par(mfrow=c(2,2))
check_normal(mydata$Aural, 'Aural')
check_normal(mydata$Kinesthetic, 'Kinesthetic')
check_normal(mydata$Read_Write, 'Read_Write')
check_normal(mydata$Visual, 'Visual')
dev.off()
# Conclusions:
# Since the data is ordinal, this plot can only be taken as a reference.
# As we can see from violin plot, Aural has big tail for both sides. 
# The other three are approximately normal, but skew to the side.

# 3. Pairsie correlation for learning style
png(paste(dir, 'scatterplot_style.png', sep = ''), 900, 800)
pairs(~Aural+Kinesthetic+Read_Write+Visual, data = mydata, main = 'Scatterplot Matrix for learning style', cex =0.5, pch = 19)
dev.off()

person_cor = matrix(nrow = length(learing_cats), ncol = length(learing_cats), byrow = TRUE, dimnames = list(learing_cats, learing_cats) )
for (var1 in learing_cats){
  for (var2 in learing_cats){
    person_cor[var1, var2] = cor(mydata[[var1]], mydata[[var2]], use = "complete.obs", method = "pearson")
  }
}

png(paste(dir, 'heatmap_style.png', sep = ''), 500, 400)
pheatmap(person_cor, clustering_distance_rows=as.dist((1-person_cor^2)), clustering_distance_cols=as.dist(1-person_cor^2), 
         cluster_rows=T, cluster_cols = T, 
         breaks=seq(-1, 1, 0.1),
         color = colorRampPalette(c("darkblue", "blue", "lightblue", "white", "wheat", "orange", "firebrick"))(20),
         legend = TRUE,
         main = paste("Person's correlation for learning style"), display_numbers = T, fontsize=14)
dev.off()

# Again, since the data is ordinal, Pearson's correlation might not be a accurate prediction.
# Still, we can see that Read_Write is not correlatied with the other three categories.
# For Aural, Kinesthetic, and Visual, if the student score higher in one of them, he is likely to score higher in the other two.

###########
# Classes #
###########

# barplot for distribution of class
png(paste(dir, 'barplot_class.png', sep = ''), 500, 400)
barplot(sapply(mydata[, class_cats], sum), main = "Barplot for people taking each class")
dev.off()

############################
# Learning style & Classes #
############################

# Distribution of students taking STAT and CS classes 
png(paste(dir, 'table_class.png', sep = ''), 500, 400)
stat_group = (mydata$STAT133==1 | mydata$STAT134==1 | mydata$STAT135==1)
cs_group = mydata$CS==1
plot(table(stat_group, cs_group), xlab = "People taking STAT class", ylab = "People taking CS class", main = "Distribution of classes taken")
text(x = c(0.1, 0.6, 0.1, 0.6),y = c(0.05, 0.03, 0.5, 0.5), labels= c(1, 3, 5, 22))
dev.off()

# Hypothesis:
# STAT students with a particualr learning style are more likely to take a CS class.

# Assumptions:
#  Students who have taken at least one of STAT 133, 134, 135 are considered as students with STAT background.

# Method:
# Compare the learning style of students of group STAT & CS and group STAT & NOT CS.

mydata2 = mydata[stat_group,]
cat_CS = mydata2$CS == 1

chisq_test = matrix(nrow = length(learing_cats), ncol = length(learing_cats), byrow = TRUE, dimnames = list(learing_cats, learing_cats) )
for (var1 in learing_cats){
  for (var2 in learing_cats){
    test = mydata2[[var1]] > mydata2[[var2]]
    result = chisq.test(table(cat_CS,test))
    chisq_test[var1, var2] = result$p.value
  }
}

png(paste(dir, 'chisq_class.png', sep = ''), 500, 400)
pheatmap(chisq_test, color = "white", main = paste("P value for Chi-square test"), display_numbers = T, legend= F, cluster_rows=F, cluster_cols = F, fontsize=14)
dev.off()

# Conclusion:
# Due to the size of the sample, chi square test can't tell us anything.