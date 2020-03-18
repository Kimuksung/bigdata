#https://media.daum.net/

#1. 패키지 설치
install.packages('httr') # remote url request
library(httr)
install.packages('XML') # tag-> html parsing
library(XML)

#2. url request
url = "https://media.daum.net/"
web = GET(url)
web

#3. parsing
html = htmlTreeParse(web,useInternalNodes = T, trim = T , encoding="utf-8")
root_node = xmlRoot(html)

# 4. Tag 자료 수집   "//tag[@속성='값']"
news = xpathSApply(root_node , "//a[@class='link_txt']", xmlValue)
news2 = news[1:59]
news2

# 5. news data refinement
news_sent = gsub('[[\n\r\t]]', '', news2)
news_sent = gsub('[[:punct:]]', '', news_sent)
news_sent = gsub('[[:cntrl:]]', '', news_sent) 
news_sent = gsub('[[a-zA-Z]]', '', news_sent) 
news_sent = gsub('\\s+', ' ', news_sent) 
news_sent

# 6. file save
setwd("C:/ITWILL/2_Rwork/output")
write.csv(news_sent,'news_data.csv' , row.names = T ,quote=F)

news_data = read.csv('news_data.csv')
news_data
colnames(news_data)= c('no','news_text')
class(news_data)

news_text = news_data$news_text
news_text

# 7. 토픽 분석
library(rJava)
library(KoNLP)
library(tm)
library(wordcloud) 

user_dic <- data.frame(term=c("코로나19","펜데믹","타다"), tag='ncn')
buildDictionary(ext_dic='sejong', user_dic = user_dic)

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}

news_nouns <- sapply(news_text, exNouns) 
news_nouns[1]
myCorpus <- Corpus(VectorSource(news_nouns))
inspect(myCorpus[1])

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거
inspect(myCorpusPrepro[1])
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(4,16)))
inspect(myCorpusPrepro)
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term))
myTerm_df[c(1:10), 1]

wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]
myName <- names(wordResult)
word.df <- data.frame(word=myName, freq=wordResult) 

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))
wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")


