import subprocess as sp
n=int(input("Provide no of dockers to run: "))
	
#id_docker = input("Enter Name")


for i in range(n):
	id_docker = input("Enter Name : ")
	# print("Enter Name")
	#sp.getoutput("docker run -itd --name {} centos:latest".format(id_docker))
	sp.getoutput("docker run -itd --name {} centos:latest".format(id_docker))

t= input("Which docker do you want to enter : ")
sp.getoutput("docker start {} ".format(t))
sp.getoutput("docker attach {}".format(t))


# sp.getoutput("bash docker.sh")
