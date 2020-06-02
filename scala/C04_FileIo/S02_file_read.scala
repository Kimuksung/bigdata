package C04_FileIo

// io pacakge import
import scala.io.Source
import java.io.FileNotFoundException // 예외 처리

object S02_file_read {
  
  //iris.csv => read
  def csv_load( filename : String) : Unit ={
    try{
      val fileRead = Source.fromFile("C:/ITWILL/5_Hadoop_Spark/workspace/Part1_Scala/src/fileDir/" + filename)
      println("file read complete")
      var lines = fileRead.getLines().drop(1) // column명 제거
      for ( line <- lines){
        // ',' 로 토큰 생성 -> 변수 저장
        var cols = line.split(",").map(_.trim())
        println(s"${cols(0)} , ${cols(1)} , ${cols(2)} , ${cols(3)} , ${cols(4)}")
      }
      fileRead.close()
    }catch{
      case ex : FileNotFoundException => println("error : " + ex)
    }
    
  }
  
  def main(args : Array[String]): Unit= {
    /*try{
      val fileRead = Source.fromFile("C:/ITWILL/5_Hadoop_Spark/workspace/Part1_Scala/src/fileDir/scala_object.txt")
      println("file read complete")
      var lines = fileRead.getLines()
      for ( line <- lines){
        println(line)
      }
    }catch{
      case ex : FileNotFoundException => println("error : " + ex)
    }
    */
    csv_load("iris.csv")
  }
}
