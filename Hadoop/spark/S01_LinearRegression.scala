package com.spark.C03_sparkML

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.regression.LinearRegression //model 생성

/*
 * libsvm file + linear regression model
 * - libsvm : label , features
 */

object S01_LinearRegression {
    def main(args: Array[String]) = {
      val spark = SparkSession.builder
      .master("local")
      .appName("dataFrameAPI")
      .getOrCreate
      
      // 1. dataset load
      val dataset = spark.read.format("libsvm").load("src/main/resources/iris_libsvm.txt")
      
      dataset.show(false)
      
      // 2. model 생성
      val lr = new LinearRegression() // model 객체 생성
      
      val model = lr.fit(dataset) //model 생성 
      
      // 3. model 평가
      println(model.coefficients) // 기울기
      println(model.intercept) // 절편
      val model_summary = model.summary
      //잔차
      model_summary.residuals.show()
      
      //mse r2 score
      println (model_summary.r2) //비정규화
      println(model_summary.meanSquaredError) // 정규화
          
      spark.close()
  }  
}