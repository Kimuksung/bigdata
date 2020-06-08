package com.spark.C03_sparkML

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.regression.LinearRegression 
import org.apache.spark.ml.feature.VectorAssembler // x , y 변수 선택
import org.apache.spark.ml.evaluation.RegressionEvaluator // model 평가

object S02_LinearRegression {
    def main(args: Array[String]) = {
      val spark = SparkSession.builder
      .master("local")
      .appName("dataFrameAPI")
      .getOrCreate
           
       val df= spark.read
      .format("csv")
      .option("header","true")
      .option("delimiter",",")
      .option("inferSchema","true")
      .load("src/main/resources/iris.csv")       
      
      df.show()
      
      val colNames = Seq("Sepal_Length","Sepal_Width","Petal_Length","Petal_Width" , "Species")
      //old DF -> New
      val iris_df =  df.toDF(colNames: _*)
      //iris_df.show()
      
      // y = Sepal_Length x = 나머지 3개
      val iris_xy = iris_df.drop("Species")
      iris_xy.show()
      
      
      //label , features 생성 : VectorAssembler
      val assemble = new VectorAssembler()
                      .setInputCols(Array("Sepal_Width" , "Petal_Length" , "Petal_Width"))
                      .setOutputCol("features") // x 변수 -> features 지정
                      
      val data = assemble.transform(iris_xy)
      //data.show(false)
      
      data.select("Sepal_Length","features" ).show(false)
      
      // 3. train / test split ( 70 / 30 )
      val Array(train , test) = data.randomSplit(Array(0.7 , 0.3) , seed = 123)
      
      // 4. model 생성
      val lr = new LinearRegression()
                .setMaxIter(10)
                .setFeaturesCol("features")
                .setLabelCol("Sepal_Length")
      val model = lr.fit(train)
      println(model.coefficients)
      println(model.intercept)
      println(model.summary.meanSquaredError)
      println(model.summary.r2)
      
      // 5. model 평가
      val pred = model.transform(test)
      pred.show()
      
      val evaluater = new RegressionEvaluator()
      evaluater.setLabelCol("Sepal_Length").setPredictionCol("prediction")
      val rmse = evaluater.setMetricName("rmse").evaluate(pred) // root mse
      val mse = evaluater.setMetricName("mse").evaluate(pred) // 평균 제곱 오차
      val mae = evaluater.setMetricName("mae").evaluate(pred) // 평균 절대값 오차
      val r2_score = evaluater.setMetricName("r2").evaluate(pred) 
      
      println("-"*20)
      println(rmse)
      println(mse)
      println(mae)
      println(r2_score)
      spark.close()
  }  
}