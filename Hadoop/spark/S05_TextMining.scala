package com.spark.C03_sparkML

import org.apache.spark.sql.SparkSession // DF
import org.apache.spark.ml.feature.StringIndexer // string -> discrete value(0,1)
import org.apache.spark.ml.feature.VectorAssembler // Feature
import org.apache.spark.ml.classification.{LogisticRegression} // model
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator // model 평가

//textmining
import org.apache.spark.ml.feature.{RegexTokenizer , StopWordsRemover , CountVectorizer , IDF} // token , 불용어 처리 , 고유 번호 , 가중치

object S05_TextMining {
def main(args: Array[String]) = {
      val spark = SparkSession.builder
      .master("local")
      .appName("dataFrameAPI")
      .getOrCreate
      
       val df= spark.read
          .format("csv")
          .option("header","false")
          .option("delimiter",",")
          .option("inferSchema","true")
          .load("src/main/resources/sms_spam_data.csv")
            
       df.show(false)
       
       // data preprocessing - 1. dummy 2. word sparse matrix
       // 1. dummy
       val idx = new StringIndexer().setInputCol("_c0").setOutputCol("label")
       val sms_data_label = idx.fit(df).transform(df)
       sms_data_label.show()
       
       //token 정규 표현식을 이용한 토큰 생성기
       val tokenizer = new RegexTokenizer().setInputCol("_c1").setOutputCol("words").setPattern("\\W+")
       val tokenizered = tokenizer.transform(sms_data_label)      
       
       // 2. stop words remover
       val stopWords  = new StopWordsRemover().setInputCol("words").setOutputCol("terms")
       val newData = stopWords.transform(tokenizered)
       
       //newData.select("words","terms").show()
       
       // 3. CountVectorizer ( 단어마다 고유 번호 , 길이 제한 )
       val countVec = new CountVectorizer().setInputCol("terms").setOutputCol("countVec").setVocabSize(4000)       
       val newDataCont = countVec.fit(newData).transform(newData)
      //newDataCont.show()
        
      val tfidf = new IDF().setInputCol("countVec").setOutputCol("tfidfVec")

      val tfidf_data = tfidf.fit(newDataCont).transform(newDataCont)
      //tfidf_data.show()
      tfidf_data.select("label", "tfidfVec").show(false)
      
      
      // 4. feature 생성
      val assemble = new VectorAssembler()
                .setInputCols(Array("tfidfVec"))
                .setOutputCol("features")
                
      val data = assemble.transform(tfidf_data)
      data.show()
      
      val Array(train , test) = data.randomSplit(Array(0.8,0.2))
      
      // 5. model 생성
      val lr = new LogisticRegression().setMaxIter(10).setRegParam(0.01).setLabelCol("label").setFeaturesCol("features")
      val model = lr.fit(train)
      val pred = model.transform(test)
      pred.select("label" , "prediction").show(1000)
      
      // 6. model 평가
      val evaluator = new MulticlassClassificationEvaluator().setLabelCol("label").setPredictionCol("prediction")
      val acc = evaluator.setMetricName("accuracy").evaluate(pred)
      val f1 = evaluator.setMetricName("f1").evaluate(pred)
      println(acc)
      println(f1)
      spark.close()
  }
}