package com.spark.C03_sparkML

/*
 * discrete classfication / multiple classfication
 */
import org.apache.spark.sql.SparkSession // DF
import org.apache.spark.ml.feature.VectorAssembler // Feature
import org.apache.spark.ml.classification.{LogisticRegression , LogisticRegressionModel} // model
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator // model 평가


object S03_LogisticRegression {
  def main(args: Array[String]) = {
      val spark = SparkSession.builder
      .master("local")
      .appName("dataFrameAPI")
      .getOrCreate
      
      // 1. Dataset 생성
      import spark.implicits._
      // train set : 키 / 몸무게 / 나이 / 성별 
      val train = List(( 171 , 68.65 , 29 , 1 ), ( 175 , 74.5 , 35 , 1 ), ( 159 , 58.6 , 29 , 0 )).toDF("height", "weight" , "age" , "gender")
      //train.show()
      
      val test = List(( 169 , 65.12 , 35 , 1 ),( 161 , 52.5 , 29 , 0 ), ( 171 , 70.5 , 25 , 1 ) ).toDF("height", "weight" , "age" , "gender")
      //test.show()
      
      // 2. assembler 생성 : features
      val assemble_train = new VectorAssembler()
                      .setInputCols(Array("height", "weight" , "age"))
                      .setOutputCol("features")
      val trainset = assemble_train.transform(train)
      trainset.show()
      
      // 3. model 생성
      val lr = new LogisticRegression()
               .setMaxIter(10) // 반복 학습 횟수
               .setRegParam(0.01) // 학습률
               .setLabelCol("gender") // Y
               .setFeaturesCol("features") // X
               
      val model = lr.fit(trainset)
      
      // 4. model 평가
      val assemble_test = new VectorAssembler()
                      .setInputCols(Array("height", "weight" , "age"))
                      .setOutputCol("features")
      val testset = assemble_test.transform(test)
      testset.show()
      
      val pred = model.transform(testset)
      //pred.show()
      pred.select("gender" , "prediction").show()
      
      // 이항 다항 분류 평가
      val evaluatoer = new MulticlassClassificationEvaluator()
                        .setLabelCol("gender")
                        .setPredictionCol("prediction")
      
      val acc = evaluatoer.setMetricName("accuracy").evaluate(pred)                  
      val f1 = evaluatoer.setMetricName("f1").evaluate(pred)
      
      println(acc)
      println(f1)
      
      // 5. model save + load
      val path = "C:/hadoop-2.6.0/lrModel"
      model.write.overwrite().save(path)
      println("model save")
      
      // model load
      val new_lrmodel = LogisticRegressionModel.load(path)
      val result = new_lrmodel.transform(trainset)
      result.show()
      
      spark.close()
  }  
}