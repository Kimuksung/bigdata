package C01_Variable

object S03_datatype {
  def main(args : Array[String]): Unit= {
    val cal : Int = 100*4/3
    //val cal2 : Int = Int(100*0.25/3)
    println(cal)
    val cal_re : Float = 100*4/3
    println(cal_re)
    val cal_re2 = 100*2.5/3
    println(cal_re2.getClass())
    
    //실수형 변수
    val x: Double = 2.4
    val a : Float = 0.5f
    val b : Float = 1.0f
    
    val y_pred = x*a+b
    println(y_pred)
    
    //논리형 변수 선언
    var bool_re : Boolean = 2.5f == y_pred
    println(bool_re)
    
    var strVar : String = "우리나라 대한민국"
    var charVar : Char = '우'
    
    println(strVar)
    println(charVar , charVar.getClass())
    
    println(cal_re2)
    printf("%.5f" , cal_re2)
    println()
    val cal_long :Long = 1000000*2
    
    println(cal_long)
  }  
}