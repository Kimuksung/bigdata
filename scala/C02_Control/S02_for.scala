package C02_Control

/*
 * for (변수 <- collection){
 * 
 * }
 * 
 * Collection? 열거형 data를 저장하는 자료구조(Array , List)
 * 
 * for(변수 <- collection if 조건식) 반복문
 * -가드(guard)
 */

object S02_for {
  def main(args : Array[String]): Unit= {
    var tot = 0
    for( i <- 0 until 11){
      print(i + " ")
      tot += i 
    }
    println(tot)
    
    //start to stop
    
    for ( i <- 1 to 10){
      print(i +" ")
    }
    println()
    //list 커렉션
    var dogList = List("진도개-한국","세퍼트-독일","풍산개-한국","불독-독일")
    for(dog <- dogList) println(dog)
    println("-"*10)    
    //guard
    for(dog <- dogList if(dog.contains("한국" ))) println(dog)
    println("-"*10)  
    for(dog <- dogList if(dog.contains("한국" ) && dog.startsWith("진도개"))) println(dog)
    println("-"*10)
    for(dog <- dogList if(dog.contains("한국" ) || dog.startsWith("풍산개"))) println(dog)
  
    println("-"*10)
    for(dog <- dogList if(dog.contains("독일" ) || dog.startsWith("진도개"))) println(dog)
    var dogvar = for(dog <- dogList if(dog.contains("독일" ) || dog.startsWith("진도개"))) yield dog
    println("-"*10)
    println(dogvar)

  }
}