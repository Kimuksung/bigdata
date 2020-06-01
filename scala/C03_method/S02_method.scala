package C03_method

/*
 *  1. 익명 함수 : 함수 이름 없음
 *  python lambda
 *  (인수 : type , 인수 : type) => return value
 *  (x , y) => x+y
 *  
 *  2. Collection 인수
 *  ex) Array , List
 *  Array[type]
 */



object S02_method {
  // 익명 함수
  var any_func = ( x : Int ) => x*x
  println((( x : Int ) => x*x)(10))
  
  // collecion function
  def textPro( texts : Array[String] ) :Unit ={
    for(txt <- texts if(txt.contains("한국"))){
       println(txt)
    }
  }
  
  def main(args : Array[String]): Unit= {
    println(any_func(10))
    
    var textArr = Array("홍길동-한국", "존-미국","강감찬-한국","마이클-호주")
    textPro(textArr)
  }
}