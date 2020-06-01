package C01_Variable

/*
 * Scala 상수 선언(값 수정 불가능)
 * val 변수명 : 자료형 = 값
 * - 초기화 이후 수정이 불가능
 */
object S01_val {
  def main(args : Array[String]): Unit= {
    val numVal : Int = 100
    val numVal2 = 105.41
    
    println(numVal)
    println(numVal2)
    println(numVal.getClass())
    println(numVal2.getClass())
    
    var tmp = numVal*2
    println(tmp)
  }
}