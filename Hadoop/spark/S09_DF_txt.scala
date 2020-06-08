package com.spark.dataFrame_SQL

/*
 * text file -> DataFrame
 * 문자열 처리 함수
 */

import org.apache.spark.sql.SparkSession

object S06_DF_txt {
      def main(args: Array[String]) = {
      val spark = SparkSession.builder
      .master("local")
      .appName("dataFrameAPI")
      .getOrCreate
      
      // text file -> DF
      val path = "src/main/resources/"
      val df= spark.read.text(path + "input.txt")
      df.show(false)
      
      // column 사용을 위한 표준 내장 함수
      import org.apache.spark.sql.functions._
      // 형식) df.select(column 내장 함수)
      /*
      df.select(col("value")).show()
      df.select(split(col("value")," ").as("words")).show(false)
      df.select(explode(split(col("value")," ")).as("words")).show(false)
      */
      //sentence -> words
      
      val words = df.select(explode(split(col("value")," ")).as("words"))
      //words.show()
      
      //word count
      words.groupBy("words").count().show()
      
      spark.close()
  }
}