package com.spark.C03_sparkML

/*
 * Tree model + confusion matrix
 */

import org.apache.spark.sql.SparkSession // DF
import org.apache.spark.ml.classification.{DecisionTreeClassifier} // model
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.mllib.evaluation.MulticlassMetrics

/*
 * ml vs mllib
 * ml : Dataframe model
 * mllib : Rdd model
 */

object S06_Classification {
    def main(args: Array[String]) = {
    val spark = SparkSession.builder
    .master("local")
    .appName("dataFrameAPI")
    .getOrCreate
    
    val df = spark.read.format("libsvm").load("src/main/resources/iris_libsvm.txt")
    df.show()
    
    // split
    val Array(train , test ) = df.randomSplit(Array(0.7 , 0.3))
    // dataset memory load
    train.cache()
    test.cache()
    
    // Tree model
    val dt = new DecisionTreeClassifier().setLabelCol("label").setFeaturesCol("features")
    val model = dt.fit(train)
    
    println(model.featureImportances)
    
    val pred = model.transform(test)
    pred.show()
    
    // model 평가
    val evaluate = new MulticlassClassificationEvaluator().setLabelCol("label").setPredictionCol("prediction")
    val acc = evaluate.setMetricName("accuracy").evaluate(pred)
    val f1 = evaluate.setMetricName("f1").evaluate(pred)
    
    println(s"acc : ${acc} , f1 : ${f1}")
    
    // 교차 분할표
    import spark.implicits._
    val predRDD = pred.select("label" , "prediction").as[(Double,Double)].rdd
    val confusion = new MulticlassMetrics(predRDD) //RDD data
    
    println(confusion.confusionMatrix)
    
    spark.close()
    
  }
}