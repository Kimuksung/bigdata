package com.spark.C01_rdd

import org.apache.spark.{SparkConf, SparkContext}

/*
 * RDD Transformation : map 관련 메서드
 * 1. map
 * 2. flatMap
 * 3. filter
 */

object S02_rddTrans_map {
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
        
        // 1. mapping : rdd resource를 순서대로 받아서 연산 수행
        val rdd = sc.parallelize(List("a" , "b" , "c"))
        val map_re = rdd.map((_,1)) // (a,1) (b,1) (c,1)
        map_re.foreach(println)
        
        val rdd2 = sc.parallelize(1 to 10)
        val map_re2 =rdd2.map(_+1)
        //rdd2 원소 추출 -> 구분자 원소 출력
        println(map_re2.collect().mkString(","))
        println(map_re2.collect())
        
        // 2. flatmap(매핑 연산자) : rdd 원소를 순서대로 받아 연산 수행 ( 1: N )
        val names = sc.parallelize(List("이순신 , 강호동" , "홍길동 , 강감찬"  , "유관순 , 이순신 , 강감찬 "))
        val flatmat_re = names.flatMap(_.split(","))
        println(flatmat_re.collect().mkString(","))
        println("size : " + flatmat_re.count())
        
        // 3. fileter(조건식) : rdd 원소를 순서대로 받아서 조건이 참이 원소 반환
        val filter_re = names.filter(_.size >10)
        println(filter_re.collect().mkString("\t"))
  }
}






