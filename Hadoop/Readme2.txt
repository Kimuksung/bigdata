* 1. Hadoop/Yarn/Historyserver 시작
[hadoop@master ~]$ start-all.sh # 하둡/얀 시작

[hadoop@master ~]$ mr-jobhistory-daemon.sh start historyserver # 데몬 실행

* Hadoop 상태 확인 
[hadoop@master ~]$ jps   


* 2. Map Reduce(word count 예제)

# /test 디렉터리 생성 
[hadoop@master ~]$ hdfs dfs -mkdir /test

# ./NOTICE.txt 파일을 test 디렉터리에 복사
[hadoop@master ~]$ hdfs dfs -put ./hadoop-2.9.2/NOTICE.txt /test
[hadoop@master ~]$ hdfs dfs -cat /test/NOTICE.txt

# wordcount 실행 
[hadoop@master ~]$ hadoop jar ./hadoop-2.9.2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.2.jar wordcount /test/NOTICE.txt /output

# 3. 워드 카운트 결과 보기 
[hadoop@master ~]$ hdfs dfs -ls /output
[hadoop@master ~]$ hdfs dfs -cat /output/part-r-00000

http://localhost:8088/

* 4. Hadoop/Yarn/Historyserver 종료
[hadoop@master ~]$ stop-all.sh
[hadoop@master ~]$ mr-jobhistory-daemon.sh stop historyserver
