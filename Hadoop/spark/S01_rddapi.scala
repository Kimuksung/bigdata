package com.spark.C01_rdd

import org.apache.spark.{SparkConf, SparkContext}

object S01_rddapi {
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
  }
}