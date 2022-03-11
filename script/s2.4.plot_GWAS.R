#argv[1]:fastGWA path argv[2]:Man_png_path argv[3]:QQ_png_path argv[4]:min_MAF argv[5]:max_MAF
library("qqman")
library("data.table")
argv=commandArgs(T)
print("Loadding data")
data <- fread(argv[1],header = TRUE) #读取数据
# print(data[,c(2,3)])
data1 <- data[,c(2,1,3,13)] #id(rs) CHR POS P
data2 <- na.omit(data1) # 删除含有NA的整行
color_set <- rainbow(9) # 设置颜色集合 建议c("#8DA0CB","#E78AC3","#A6D854","#FFD92F","#E5C494","#66C2A5","#FC8D62")
print("plotting Man")
png(argv[2])
par(cex=0.8) #设置点的大小
colnames(data2) = c("SNP","CHR","BP","P")
color_set <- c("#8DA0CB","#E78AC3","#A6D854","#FFD92F","#E5C494","#66C2A5","#FC8D62")
manhattan(data2,main="Manhattan Plot",col =color_set, suggestiveline = FALSE,annotatePval = 0.01) #suggestiveline = FALSE 更加显著
dev.off() # 保存图片
print("Done")