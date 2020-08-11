# ClusterService
This is a web application which lets the user to create its own cluster of machines for storing large data and processing it in an efficient way.
The user first needs to register to the application. It can select the number of nodes it wants to have in the cluster. When the user stores a file into HDFS the parts of the file are replicated to other nodes too so that data isn't lost when a node is down.
Apache hadoop is used. HDFS for storing and YARN for processing. Ansible is used to automate some of the tasks.
Linux KVM is used for virual machines.
