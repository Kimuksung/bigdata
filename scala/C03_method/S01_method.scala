package C03_method

/*
 *  method : class or object function
 *  function : independent function
 *  
 *  형식) 
 *  def 함수명(매개변수 : type) : return type = {
 *  		~~~~~
 *  }
 *  
 *  반환값이 없는 경우 : Unit
 */

object S01_method {
  // max method
  def max( x : Int , y :Int) : Int = {
    if( x> y) x else y
  }
  
  def adder( x: Float , y: Float) : Float ={
    val add = x+y
    return add
  }
  
  def getPI() : Double = {
    val PI = 3.14159 // default : double
    return PI
  }
  
  def getPI2 : Double = 3.14159
  
  // 시작점 : main method
  def main(args : Array[String]): Unit= {
    val x=20
    val y=15
    println(max(x,y))
    
    println(adder(x,y))
    
    println(getPI()) 
  }
}