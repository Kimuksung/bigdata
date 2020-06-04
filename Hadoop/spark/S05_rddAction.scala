package com.spark.C01_rdd

/*
 * RDD Action : load & save
 * 1. collect() : rdd resource extract -> vector type
 * 2. textfile() : text file to rdd object create
 * 3. saveAsTextfile() : rdd object file save
 */

import org.apache.spark.{SparkConf, SparkContext}

object S05_rddAction {
    def main(args: Array[String]) = {
        // 1. SparkContext object 생성
        val conf = new SparkConf()
        .setAppName("SparkTest")
        .setMaster("local")  // Spark 환경 객체
        
        // rdd data 생성
        val sc = new SparkContext(conf)  // 분산 파일 읽기
        
        // collect
        val rdd = sc.parallelize(1 to 100 ,5)
        println(rdd.collect.mkString(" "))
        println(rdd.first)
        println(rdd.take(10).mkString(" "))
        
        // textfile
        val rdd2 = sc.textFile("C:/hadoop-2.6.0/README.txt")
        println(rdd2.count())
        println(rdd2.take(20).mkString("\n"))
        
        // save
        //rdd.saveAsTextFile("C:/hadoop-2.6.0/output")
        //rdd2.saveAsTextFile("C:/hadoop-2.6.0/output2")
        
        //println("success")
        
        //HDFS file load & HDFS file save
        val hdfs_rdd = sc.textFile("hdfs://localhost:9000/test/README.txt" , 5)
        
        hdfs_rdd.saveAsTextFile("hdfs://localhost:9000/output")
        
        println("success")
        sc.stop
  }
}