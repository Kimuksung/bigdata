package C02_Control

object S01_ifelse {
   def main(args : Array[String]): Unit= {
    var score = 50
    // 1. 블록 없는 if문
    if(score >=60) println("합격") else println("불합격")
    //2. 변수에 if문 저장
    var result = if(score >= 60 ) "합격" else "불합격"
    println(result)
    //3. 블록이 있는 if문
    score = 75
    var grade = ""
    if(score >= 90 &&score <=100){
      grade = "A"
    }else if(score >= 80){
      grade = "B"
    }else{
      grade = "C"
    }
    
    println(grade)
    
  }
}