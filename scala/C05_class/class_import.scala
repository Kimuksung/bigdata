package C05_class

import scala.io.Source // package내의 한개의 member 사용
import scala.io._ // 전체 member 사용
import scala.io.{ BufferedSource , Source }

// 사용자 class import
import class_test.{TestClass1, TestClass2}

/*
 * class vs object
 * - class : 해당 class를 이용해서 다수 객체(object)
 * var variable = new class
 * - object : 해당 클래스를 이용해서 1개 객체 (singleton)
 * 
 *  class 유형
 *  -class : new keyword
 *  -case class : 생성자 이용 다수 객체
 */

case class Car(var name : String , var cc : Double)

object class_import {
  def main(args : Array[String]): Unit= {
    // class 형식
    var tc1_1 = new TestClass1
    println(tc1_1.display())
    var tc1_2 = new TestClass1
    println(tc1_2.display())
    
    // case class
    var car1 = Car("소나타" , 2.5) // 생성자 -> Object
    var car2 = Car("그랜저" , 3.0) // 생성자 -> Object
    
    println(car1.name)
    println(car2.name , car2.cc)
    
    var tc2 = new TestClass2
    println(tc2.display())
  }
}