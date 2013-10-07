# dir = '/home/sunnymh/stat157/questionnaire_group7/'
dir = 
  
data = read.csv(paste(dir, 'data.csv', sep = ''), colClasses=c("character",rep("numeric",8)))
  
# t tests to determine if the distribution of each learning style is significantly different #

t.test(data$Aural, data$Kinesthetic, paired=TRUE)

# data:  data$Aural and data$Kinesthetic 
# t = -0.7727, df = 30, p-value = 0.4457
# alternative hypothesis: true difference in means is not equal to 0 
# 95 percent confidence interval:
# -1.6452310  0.7420052 
# sample estimates:
# mean of the differences 
#             -0.4516129 

t.test(data$Aural, data$Read, paired=TRUE)

# data:  data$Aural and data$Read 
# t = -0.2606, df = 30, p-value = 0.7962
# alternative hypothesis: true difference in means is not equal to 0 
# 95 percent confidence interval:
#  -1.710119  1.323022 
# sample estimates:
# mean of the differences 
#              -0.1935484 

t.test(data$Aural, data$Visual, paired=TRUE)

# data:  data$Kinesthetic and data$Read 
# t = 0.3356, df = 30, p-value = 0.7395
# alternative hypothesis: true difference in means is not equal to 0 
# 95 percent confidence interval:
#  -1.312400  1.828529 
# sample estimates:
# mean of the differences 
#               0.2580645 

t.test(data$Kinesthetic, data$Read, paired=TRUE)

# data:  data$Kinesthetic and data$Read 
# t = 0.3356, df = 30, p-value = 0.7395
# alternative hypothesis: true difference in means is not equal to 0 
# 95 percent confidence interval:
#  -1.312400  1.828529 
# sample estimates:
# mean of the differences 
#               0.2580645 

t.test(data$Kinesthetic, data$Visual, paired=TRUE)
 
# data:  data$Kinesthetic and data$Visual 
# t = 0.0558, df = 30, p-value = 0.9559
# alternative hypothesis: true difference in means is not equal to 0 
# 95 percent confidence interval:
#  -1.148687  1.213204 
# sample estimates:
# mean of the differences 
#              0.03225806 

t.test(data$Read, data$Visual, paired=TRUE)

# data:  data$Read and data$Visual 
# t = -0.2702, df = 30, p-value = 0.7888
# alternative hypothesis: true difference in means is not equal to 0 
# 95 percent confidence interval:
#  -1.932419  1.480806 
# sample estimates:
# mean of the differences 
#              -0.2258065 