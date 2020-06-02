package C06_Collection

/*
 * List Collection
 * - 수정 불가( immutable )
 * - 순서 존재(index)
 * - 중복 허용
 * - 동일 자료형 저장
 * - 형식) List()
 * 
 *  Tuple Collection
 *  - Tuple class X (기호 이용(
 *  - 수정 불가(initialize)
 *  - 순서 존재 (index)
 *  - 서로 다른 type 저장
 *  
 *  Set Collection
 *  - 순서 없음
 *  - 형식 val 변수 = Set(..)o
 */

import scala.collection.mutable // 수정 가능한 collection object

object S02_List_Tuple {
  def main(args : Array[String]): Unit= {

    val num = List(1,2,3,4,5,1,2,3,7)
    println(num.size)
    println(num.mkString(","))
    
    val num2 = List.range(1,11)
    for( n <- num2 ) print(n + " ")
    println()
    val names = ("홍길동" , 35 , "이순신",45, "유관순", 25)
    print(names +"\n")
    
    println(names._1)
        
    val num3 = Set(1,2,3,4,5,1,2,3)
    println(num3.size)
    
    println(num3)
    
    //문장 -> 단어 추출
    val texts = "hello,kim. my name is uk! sung kim."
    val wordArr = texts.split("[ !,.]+")
    //println(wordArr)
    for ( word <- wordArr ) print(word+" ")
    //수정가능한 SET
  val words = mutable.Set.empty[String] // String
  for ( word <- wordArr ) {
    words += word
  }
  println(words)
  }
}