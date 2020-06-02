package C04_FileIo

/*
 * Except : 실행 시점에서 오류 처리
 * try{
 * 	예외 발생 가능
 * }
 * catch{
 * 	예외 처리 코드
 * }
 * 
 */
object S01_try_catch {
  
  def main(args : Array[String]): Unit= {
   var lst = List(10,20,30,40,50)
   var size = lst.size
   println(size)
   println(lst(0))
   
   for ( i <- lst ) {
     println(i)
   }
   try{
     for ( i <- 0 until 6 ) 
       print(lst(i) + " ")
   }
   catch{
     case ex : IndexOutOfBoundsException => println( ex)
   }
   println("program end")
  }
}