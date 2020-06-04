package com.spark.C01_rdd

import org.apache.spark.{SparkConf, SparkContext}

object S01_rdd_create {
  def main(args: Array[String]) = {
        // 1. SparkContext object 생성
        val conf = new SparkConf()
        .setAppName("SparkTest")
        .setMaster("local")  // Spark 환경 객체
        
        /*
         * 방법1) setMaster("local")
         * -> 현재 Master의 단일머신에서 작업(클러스터 사용 X)
         * 
         * 방법2) setMaster("yarn-cluster")
         * -> 클러스터 환경에서 작업(클러스터 사용 O)
         */
        
        // rdd data 생성
        val sc = new SparkContext(conf)  // 분산 파일 읽기
  
        val rdd1 = sc.parallelize(1 to 100, 5) 
        println(rdd1)
        
        rdd1.foreach((x:Int) => println(x))
        
        val rdd2 = sc.parallelize(List("a" , "b" , "c" , "d" , "e" ,"e")) // data = List 컬렉션
        
        println(rdd2)
        
        rdd2.foreach((x:String)=> print(x + " "))
        
        val rdd3 = sc.textFile("file:/C:/hadoop-2.6.0/NOTICE.txt")
        
        //text file 한줄 -> RDD 1개 원소
        println("0"*30)
        println(rdd3.collect().mkString("\n")) 
        sc.stop
  }  
}