package com.spark.C03_sparkML

/*
 * Logistic Regression + Pipeline 
 */
import org.apache.spark.sql.SparkSession // DF
import org.apache.spark.ml.feature.VectorAssembler // Feature
import org.apache.spark.ml.classification.{LogisticRegression , LogisticRegressionModel} // model
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator // model 평가
import org.apache.spark.ml.{Pipeline , PipelineModel}

object S04_Logistic_Pipeline {
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
      val assembler = new VectorAssembler()
                      .setInputCols(Array("height", "weight" , "age"))
                      .setOutputCol("features")
      
      // 3. model 생성
      val lr_obj = new LogisticRegression()
               .setMaxIter(10) // 반복 학습 횟수
               .setRegParam(0.01) // 학습률
               .setLabelCol("gender") // Y
               .setFeaturesCol("features") // X
               
      // 4. Pipeline model
      val pipeline = new Pipeline().setStages(Array(assembler , lr_obj))    
      val pipelineModel = pipeline.fit(train)
      
      val pred = pipelineModel.transform(test)
      pred.show()
      
      // 5. Pipeline model save / load
      val path = "C:/hadoop-2.6.0/pipeModel"
      pipelineModel.write.overwrite().save(path)
      println("save complete")
      
      val new_pipeModel =  PipelineModel.load(path)
      val new_pred = new_pipeModel.transform(train)
      new_pred.show()
      spark.close()
  }   
}