#################################
## <제9장-2 연습문제>
################################# 


# 01. 트럼프 연설문(trump.txt)과 오바마 연설문(obama.txt)을 대상으로 빈도수가 2회 이상 단어를 대상으로 단어구름 시각화하시오.
trump <- file(file.choose(), encoding="UTF-8")
trump_data <- readLines(trump) # 줄 단위 TEXT FILE 읽기 
str(trump_data)
str(VectorSource(trump_data))
myCorpus <- Corpus(VectorSource(trump_data))

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) # 수치 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) # 소문자 변경
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english'))
inspect(myCorpusPrepro[1:5])

myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(1,100)))
myCorpusPrepro_term
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]

myName <- names(wordResult)
word.df <- data.frame(word=myName, freq=wordResult) 
head(word.df)
str(word.df)

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))
wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")

obama <- file(file.choose(), encoding="UTF-8")
obama_data  = readLines(obama)

obama_nouns <- sapply(obama_data, exNouns)

myCorpus <- Corpus(VectorSource(obama_nouns))

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) # 수치 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, tolower) # 소문자 변경
myCorpusPrepro <-tm_map(myCorpusPrepro, removeWords, stopwords('english'))
inspect(myCorpusPrepro[1])

myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(1,100)))

myCorpusPrepro_term
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]

myName <- names(wordResult)
word.df <- data.frame(word=myName, freq=wordResult) 
head(word.df)
str(word.df)

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))
wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=2, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")
# 02. 공공데이터 사이트에서 관심분야 데이터 셋을 다운로드 받아서 빈도수가 5회 이상 단어를 이용하여 
#      단어 구름으로 시각화 하시오.
# 공공데이터 사이트 : www.data.go.kr
library(rJava)
library(KoNLP) 
library(tm) 
library(wordcloud) 
temp <- read.csv(file.choose())
str(temp)
myCorpus <- Corpus(VectorSource(temp$제목))
inspect(myCorpus)

exNouns <- function(x) { 
  paste(extractNoun(as.character(x)), collapse=" ")
}
temp_nouns <- sapply(myCorpus, exNouns) 

myCorpus <- Corpus(VectorSource(temp_nouns))

myCorpusPrepro <- tm_map(myCorpus, removePunctuation) # 문장부호 제거
myCorpusPrepro <- tm_map(myCorpusPrepro, removeNumbers) # 수치 제거

inspect(myCorpusPrepro[1])
myCorpusPrepro_term <- TermDocumentMatrix(myCorpusPrepro, 
                                          control=list(wordLengths=c(2,Inf)))
myTerm_df <- as.data.frame(as.matrix(myCorpusPrepro_term)) 
wordResult <- sort(rowSums(myTerm_df), decreasing=TRUE) 
wordResult[1:10]

myName <- names(wordResult)
word.df <- data.frame(word=myName, freq=wordResult)
head(word.df)
str(word.df)

pal <- brewer.pal(12,"Paired")
windowsFonts(malgun=windowsFont("맑은 고딕"))
wordcloud(word.df$word, word.df$freq, 
          scale=c(5,1), min.freq=5, random.order=F, 
          rot.per=.1, colors=pal, family="malgun")
