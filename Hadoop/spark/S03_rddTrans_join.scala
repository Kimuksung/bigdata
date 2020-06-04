package com.spark.C01_rdd

/*
 *  RDD TRansformation : join method
 *  
 */
import org.apache.spark.{SparkConf, SparkContext}

object S03_rddTrans_join {
  
  def zip(sc : SparkContext) : Unit = {
    val rdd1 = sc.parallelize(Seq("a","b","c"))
    val rdd2 = sc.parallelize(List (1,2,3))
    val zip_re = rdd1.zip(rdd2)
  }
  
  def reduceByKey(sc : SparkContext) : Unit ={
    val lst = List("data" , "text" , "word" , "data" , "word" , "data")
    val rdd = sc.parallelize(lst)
    
    val new_rdd = rdd.map((_,1))
    println(new_rdd.collect.mkString(","))
    
    new_rdd.reduceByKey(_+_).foreach(println)
  }
  
  def main(args: Array[String]) = {
        // 1. SparkContext object 생성
        val conf = new SparkConf()
        .setAppName("SparkTest")
        .setMaster("local")  // Spark 환경 객체
        
        // rdd data 생성
        val sc = new SparkContext(conf)  // 분산 파일 읽기
        
        // 1. join : 동일한 키를 기준으로 원소 묶는다. 길이는 서로 다름
        val rdd1 = sc.parallelize(Seq("kim","lee","park","choi")).map((_,1))
        println(rdd1.collect().mkString(" "))
        val rdd2 = sc.parallelize(List("lee" , "choi")).map((_,2))
        println(rdd2.collect().mkString(" "))
        
        val join_re = rdd1.join(rdd2) //same key is join
        println(join_re.collect().mkString("_,1"))
        
        // 2. zip : 원소의 순서대로 원소 묶음 : 길이 동일
        reduceByKey(sc)
    }
}