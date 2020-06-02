package C06_Collection

/*
 *  컬렉션(Collection) 
 *  - data set
 *  - 수정 여부 , 순서 보장 ( index ) , 중복 허용 등으로 분류
 *  
 *  Array Collection
 *  - 수정 가능 ( muttable)
 *  - index 사용 가능
 *  - 중복 허용
 *  - 동일 type만 저장 가능
 *  형식) var variable : Array[type] = new Array[type](size)
 */

object S01_Array {
  
  def main(args : Array[String]): Unit= {
    //1. new 명령어 객체
    var arr : Array[Int] = new Array[Int](5)
    arr(0) = 10
    arr(1) = 20
    arr(4) = 50
    
    
    
    for ( i <- arr ) print(i+" ")
    println()
     var arr2 = Array(10,20,0,0,50)
     for ( i <- arr2 ) print(i+" ")
     
     // Array 생성 축약형
     var arr3 = new Array[Double](50)
     
     var idx = 0 until 50
     for( i <- idx){
       var r = Math.random()
       arr3(i) = r
     }
     println()
    for( i <- arr3){
      print(i + " ")
    }
    
  }  
}