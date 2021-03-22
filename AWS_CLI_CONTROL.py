import os
import pyttsx3 as p
import speech_recognition as sr
r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("-------------------------------------------------------------")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        p.speak('start saying')
        print('start saying')
        audio= r.listen(source ,  phrase_time_limit=5)
        p.speak('got it')
        print('speech done')
        t=r.recognize_google(audio)

    if ("hello"in t) or ("hii" in t):
        p.speak("hii chirag welcome here")
        print("hii chirag welcome here....")

    elif ("show" in t) and ("instances" in t):
        p.speak('this detail i found')
        print('this detail i found....')
        os.system("aws ec2 describe-instances")
        
    elif "start" in t:
        p.speak('give instance name')
        print('give instance name....')
        print("")
        print("master")
        os.system("aws ec2 start-instances --instance-ids i-03c59989d0be4af77")
        p.speak("successfully started")
        
    elif ("generate" in t) and ("new" in t):
        p.speak('got it')
        with sr.Microphone() as source1:
            p.speak(' give key name')
            print('give key name')
            audio1= r.listen(source1 ,  phrase_time_limit=5)
            t1=r.recognize_google(audio1)
        os.system("aws ec2 create-key-pair --key-name {0}".format(t1))
        print("successfully created key")
    
    elif ("show" in t) and ("all" in t):
        p.speak('this detail i found')
        print('this detail i found....')
        os.system("aws ec2 describe-key-pairs")
        
    elif ("i" in t) and ("want" in t) and ("new" in t):
        p.speak('got it')
        with sr.Microphone() as source2:
            p.speak('first give security group name')
            print('first give security group name')
            audio2= r.listen(source2 , phrase_time_limit=5)
            t2=r.recognize_google(audio2)
            
        with sr.Microphone() as source3:
            p.speak('give description also')
            print('description')
            audio3= r.listen(source3 , phrase_time_limit=5)
            t3=r.recognize_google(audio3)
             
        os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(t2,t3))
        print("successfully created security group")
    
    elif "describe" in t:
        p.speak('this detail i found')
        print('this detail i found....')
        os.system("aws ec2 describe-security-groups")
        
    elif ("launch" in t) and ("new" in t) and ("instance" in t):
        p.speak('ok i got it')
        print('wait for a min....')
        p.speak("give image name")
        print("/n")
        print("redhat")
        with sr.Microphone() as source5:
            p.speak('attatch security group name')
            print('attatch security group name')
            audio5= r.listen(source5 , phrase_time_limit=5)
            t5=r.recognize_google(audio5)
            
        with sr.Microphone() as source6:
            p.speak('give keyname also')
            print('keyname')
            audio6= r.listen(source6 , phrase_time_limit=5)
            t6=r.recognize_google(audio6)
        os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --subnet-id subnet-232a234b --security-group-ids sg-0e21f24f09560b6a2 --key-name hadoop")

    elif ("generate" in t) and ("volume" in t):
        p.speak('got it')
        with sr.Microphone() as source7:
            p.speak(' give volume type and size also')
            print('give volume type and size also')
            audio7= r.listen(source7 , phrase_time_limit=5)
            t7=r.recognize_google(audio7)
        os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
        print("successfully created volume")
    

    elif ("attach" in t) and ("volume" in t):
        p.speak('got it')
        p.speak(' give volume id and instance id')
        j3=input('give volume id ')
        j4=input("give instance id  ")
        os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(j3,j4))
        print("successfully attached volume")

    elif ("detach" in t) and ("volume" in t):
        p.speak('got it')
        p.speak(' give volume id ')
        j5=input('give volume id ')
        os.system("aws ec2 detach-volume --volume-id {0}".format(j5))
        print("successfully detached volume")

    elif ("stop" in t) and ("instance" in t):
        p.speak('got it')
        p.speak(' give instance id ')
        s5=input('give instance id ')
        os.system("aws ec2 stop-instances --instance-ids {0}".format(s5))
        print("successfully stopped")
    
    elif "exit" in t:
        exit()
        
    
        
