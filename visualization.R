dir = '/home/sunnymh/stat157/questionnaire_group7/'

library(pheatmap)

mydata = read.csv(paste(dir, 'data.csv', sep = ''), colClasses=c("character",rep("numeric",8)))

learing_cats = c('Aural', 'Kinesthetic', 'Read_Write', 'Visual')

# Distribution of learning style
png(paste(dir, 'violin.png', sep = ''), 1200, 900)
library(vioplot)
with(mydata, 
     vioplot(Aural,Kinesthetic,Read_Write,Visual, names = learing_cats, col = "lightblue"))
title("Violin Plots for learning style")
dev.off()

# Pairsie correlation for learning style
png(paste(dir, 'scatterplot.png', sep = ''), 1200, 900)
pairs(~Aural+Kinesthetic+Read_Write+Visual, data = mydata, main = 'Scatterplot Matrix for learning style', cex =0.5, pch = 19)
dev.off()
png(paste(dir, 'heatmap.png', sep = ''), 1200, 900)
person_cor = matrix(nrow = length(learing_cats), ncol = length(learing_cats), byrow = TRUE, dimnames = list(learing_cats, learing_cats) )
for (var1 in learing_cats){
  for (var2 in learing_cats){
    person_cor[var1, var2] = cor(mydata[[var1]], mydata[[var2]], use = "complete.obs", method = "pearson")
  }
}
pheatmap(person_cor, clustering_distance_rows=as.dist((1-person_cor^2)), clustering_distance_cols=as.dist(1-person_cor^2), 
         cluster_rows=T, cluster_cols = T, 
         breaks=seq(-1, 1, 0.1),
         color = colorRampPalette(c("darkblue", "blue", "lightblue", "white", "wheat", "orange", "firebrick"))(20),
         legend = TRUE,
         main = paste("Person's correlation for learning style"), display_numbers = T, fontsize=14)
dev.off()

a = sapply(mydata[, c("STAT133","STAT134", "STAT135", "CS")], sum)
barplot(a)


hist(factor(mydata$STAT133)
     