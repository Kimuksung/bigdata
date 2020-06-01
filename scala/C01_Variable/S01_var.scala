package C01_Variable

/*
 * Scala 변수 / 상수 선언
 * - var : 값을 수정하는 변수 선언
 * - var num : Int = 5
 * - 자료형 생략 시 추론
 */
object S01_var {
    def main(args : Array[String]): Unit= {
      var num1 : Int = 1000 // type 명시
      var num2 =2000
      println(num1)
      println(num2)
      
      var str1 : String = "우리나라, 대한민국"
      println(str1)
      
      var str2 = "korean"
      print(str2)
    }
}