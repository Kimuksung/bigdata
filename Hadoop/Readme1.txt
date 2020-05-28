* 준비 : master/slave1/slave2 서버 on
# - ssh 명령어로 각 서버간 네트워크 통신 확인 : skip시 scp 명령이 안될 수 있음 

* 1. Hadoop 설치  
[hadoop@master ~]$ wget http://apache.mirror.cdnetworks.com/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
[hadoop@master ~]$ tar xvzf hadoop-2.9.2.tar.gz
[hadoop@master ~]$ ls # Hadoop 설치 확인

* 2. java 홈 & Hadoop 홈 디렉터리 지정
-  java 설치 버전 확인
[hadoop@master ~]$ ls /usr/lib/jvm/java-1.8.0*   
# /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-2.el7_8.x86_64

- java 홈 & Hadoop 홈 디렉터리 지정 
[hadoop@master ~]$ vi .bash_profile
# User specific environment and startup programs

# 내용 추가
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-2.el7_8.x86_64
export HADOOP_HOME=/home/hadoop/hadoop-2.9.2 
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin


- .bash_profile의 수정된 내용 적용/확인 
[hadoop@master ~]$ source .bash_profile    
[hadoop@master ~]$ cd $JAVA_HOME        # java 홈 디렉터리 이동
[hadoop@master ~]$ cd $HADOOP_HOME   # hadoop 홈 디렉터리 이동 


* 3. Hadoop 환경 설정 : #  java 설치 버전 확인
- Hadoop 환경 설정 (jdk 추가)
[hadoop@master hadoop]$ vi hadoop-env.sh   
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-2.el7_8.x86_64

- Yarn 환경 설정 (jdk 추가)
[hadoop@master hadoop]$ vi yarn-env.sh 
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-2.el7_8.x86_64

- Data node 지정 : slave 서버 지정  
[hadoop@master hadoop]$ vi slaves 
slave1
slave2

- HDFS의 Name node와 임시 디렉터리 지정
[hadoop@master hadoop]$ vi core-site.xml   
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://master:9000</value>
    </property>
    <property>
         <name>hadoop.tmp.dir</name>
         <value>/home/hadoop/hadoop-2.9.2/tmp/</value>
    </property>
</configuration>


- HDFS에 tmp 디렉토리 생성 (임시 데이터 저장용)
[hadoop@master hadoop]$ mkdir /home/hadoop/hadoop-2.9.2/tmp

- 하둡분산파일시스템(HDFS) 관련 환경 설정
[hadoop@master hadoop]$ vi hdfs-site.xml 
<configuration>
      <property>
          <name>dfs.replication</name>
          <value>3</value>
     </property>
     <property>
          <name>dfs.permissions</name>
          <value>false</value>
     </property>
     <property>
          <name>dfs.namenode.secondary.http-address</name>
          <value>slave1:50090</value>
     </property>
     <property>
          <name>dfs.namenode.secondary.https-address</name>
          <value>slave1:50091</value>
     </property>
</configuration>


- MapReduce 관련 설정
[hadoop@master hadoop]$ cp mapred-site.xml.template  mapred-site.xml

[hadoop@master hadoop]$ vi mapred-site.xml 
<configuration>	
     <property>
          <name>mapreduce.framework.name</name>
          <value>yarn</value>
     </property>
</configuration>


- YARN 설정[Resource Manager, Node Manager 지정]
[hadoop@master hadoop]$ vi yarn-site.xml 
<configuration>
<!-- Site specific YARN configuration properties -->  
     <property>
          <name>yarn.nodemanager.aux-services</name>
          <value>mapreduce_shuffle</value>
     </property>
     <property>
          <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
          <value>org.apache.hadoop.mapred.ShuffleHandler</value>
     </property>
     <property>
          <name>yarn.resourcemanager.resource-tracker.address</name>
          <value>master:8020</value>
     </property>
     <property>
          <name>yarn.resourcemanager.scheduler.address</name>
          <value>master:8030</value>
     </property>
     <property>
          <name>yarn.resourcemanager.address</name>
          <value>master:8040</value>
     </property>
</configuration>

* 4. 하둡 시스템 배포 : 설정 사항을 Slave 서버에 배포 
[hadoop@master hadoop]$ cd   # /home/hadoop 홈 디렉터리 이동 

[hadoop@master ~]$ scp -r /home/hadoop/hadoop-2.9.2 hadoop@slave1:~
[hadoop@master ~]$ scp -r /home/hadoop/hadoop-2.9.2 hadoop@slave2:~

- 계정 profile 배포
[hadoop@master ~]$ scp /home/hadoop/.bash_profile hadoop@slave1:~
[hadoop@master ~]$ scp /home/hadoop/.bash_profile hadoop@slave2:~

- 처음 HDFS를 사용할 때는 HDFS를 포맷
[hadoop@master ~]$ hdfs namenode -format 


* 5. Hadoop/Yarn/Historyserver 시작 : 설치 후 하둡 실행하기 
[hadoop@master ~]$ start-all.sh  # 하둡 관련 모든 데몬 실행[HDFS/YARN 동시 실행] 
Starting namenodes on [master]
master: starting namenode, logging to /home/hadoop/hadoop-2.9.2/logs/hadoop-hadoop-namenode-master.out
slave2: starting datanode, logging to /home/hadoop/hadoop-2.9.2/logs/hadoop-hadoop-datanode-slave2.out
slave1: starting datanode, logging to /home/hadoop/hadoop-2.9.2/logs/hadoop-hadoop-datanode-slave1.out
Starting secondary namenodes [slave1]
slave1: starting secondarynamenode, logging to /home/hadoop/hadoop-2.9.2/logs/hadoop-hadoop-secondarynamenode-slave1.out

starting yarn daemons
starting resourcemanager, logging to /home/hadoop/hadoop-2.9.2/logs/yarn-hadoop-resourcemanager-master.out
slave2: starting nodemanager, logging to /home/hadoop/hadoop-2.9.2/logs/yarn-hadoop-nodemanager-slave2.out
slave1: starting nodemanager, logging to /home/hadoop/hadoop-2.9.2/logs/yarn-hadoop-nodemanager-slave1.out

[hadoop@master ~]$ mr-jobhistory-daemon.sh start historyserver # 데몬 실행[맵리듀스 실행 필요]
starting historyserver, logging to /home/hadoop/hadoop-2.9.2/logs/mapred-hadoop-historyserver-master.out

* 6. Hadoop 상태 확인 
# NameNode 동작여부 확인
[hadoop@master ~]$ jps   

# DataNode의 동작여부 확인
[hadoop@slave1 ~]$ jps

# web에서 동작여부 확인
http://localhost:50070/

# hdfs 내용 보기 
[hadoop@master ~]$ hdfs dfs -ls /tmp
Found 1 items
drwxrwx---   - hadoop supergroup          0 2018-07-09 12:35 /tmp/hadoop-yarn

* 7. Hadoop/Yarn/Historyserver 종료
[hadoop@master ~]$ stop-all.sh
[hadoop@master ~]$ mr-jobhistory-daemon.sh stop historyserver