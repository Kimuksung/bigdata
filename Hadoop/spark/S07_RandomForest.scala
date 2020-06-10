package com.spark.C03_sparkML

/*
 * 
 */
import org.apache.spark.sql.SparkSession // DF
import org.apache.spark.ml.feature.StringIndexer // label , feature
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.classification.RandomForestClassifier // model
import org.apache.spark.ml.classification.RandomForestClassificationModel
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.mllib.evaluation.MulticlassMetrics

object S07_RandomForest {
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
      .load("src/main/resources/weather.csv")       
      
      df.show()
      df.printSchema() // column type
      
      //label 생성 Raintomorrow -> dummy
       val sIndexer = new StringIndexer().setInputCol("RainTomorrow").setOutputCol("label")
      
       val sIndexerDF = sIndexer.fit(df).transform(df)
       sIndexerDF.show()
       
       // features 생성
       val assembler = new VectorAssembler()
                      .setInputCols(Array("Sunshine", "WindGustSpeed" , "Humidity" , "Pressure"))
                      .setOutputCol("features")
       
       val weather_set = assembler.transform(sIndexerDF)
       weather_set.show()
       
       // train / test
       val Array(train , test) = weather_set.randomSplit(Array(0.7 , 0.3))
       
       // model 생성
       
       val rf = new RandomForestClassifier().setLabelCol("label").setFeaturesCol("features").setNumTrees(10)
       val model =  rf.fit(train)
       
       val pred = model.transform(test)
       pred.show()
       
       pred.select("label","prediction","features").show()
       
       // model 평가
       // 1) accuarcy
       val evaluator = new MulticlassClassificationEvaluator().setLabelCol("label").setPredictionCol("prediction")
       val acc = evaluator.setMetricName("accuracy").evaluate(pred)
       
       val f1 = evaluator.setMetricName("f1").evaluate(pred)
       println(s"acc : ${acc} / f1 : ${f1}")
       
       // 2) confusion matrix
       import spark.implicits._ // DF -> RDD
       val pred_rdd = pred.select("label" , "prediction").as[(Double,Double)].rdd
       val con_max = new MulticlassMetrics(pred_rdd)
       println(con_max.confusionMatrix)
       
       // model save load
       val path = "C:/hadoop-2.6.0/rdModel"
       model.write.overwrite().save(path)
       println("model saved")
       
       val rmModel = RandomForestClassificationModel.load(path)
       rmModel.transform(test).show()
       
       spark.close()
  }
}