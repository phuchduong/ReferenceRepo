Article = c(0, 0, 0, 1, 1)
Mention = c("John", "California", "Los Angeles", "Microsoft", "Boston")
Offset = c(0, 29, 79, 0, 133)
Length = c(4, 10, 11, 9, 6)
Type = c("PER", "LOC", "LOG", "ORG", "LOC")
dataset1 <- data.frame(Article, Mention, Offset, Length, Type)
a <- paste(dataset1[,2], dataset1[,5], sep =", ")
len <- length(a)
b <- ""
for(i in 1:len){
	if(nchar(b)>0){
		b <- paste(b, a[i], sep=", ")
	} else {
		b <- a[i]
	}
}
c <- data.frame(b)