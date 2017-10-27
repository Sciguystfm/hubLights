import requests, sys
from random import randint, sample
from time import sleep

def strobe():
    path=r"http://10.39.205.195/api/KQtqYPzVCsndUzGxLgRu2oMDiseGkMneZ0agYdEr/lights/2/state"
    while True:
        r = requests.put(path,data='{"bri":1,"transitiontime":0}')
        sleep(.1)
        r = requests.put(path,data='{"bri":254,"transitiontime":0}')

def gay():
    path=r"http://10.39.205.195/api/KQtqYPzVCsndUzGxLgRu2oMDiseGkMneZ0agYdEr/lights/2/state"
    r = requests.put(path,data='{""bri":254,"sat":254,"transitiontime":0}')

    while True:
        r = requests.put(path,data='{"transitiontime":0, "hue":'+str(randint(1,65000))+"}")
        r = requests.put(path,data='{"bri":1,"transitiontime":0}')
        sleep(.1)
        r = requests.put(path,data='{"bri":254,"transitiontime":0}')

def gayGroup():
    path=r"http://10.39.205.195/api/KQtqYPzVCsndUzGxLgRu2oMDiseGkMneZ0agYdEr/groups/3/action"
    r = requests.put(path,data='{""bri":254,"sat":254,"transitiontime":0}')

    while True:
        r = requests.put(path,data='{"transitiontime":0, "hue":'+str(randint(1,65000))+"}")
        r = requests.put(path,data='{"bri":1,"transitiontime":0}')
        sleep(.05)
        r = requests.put(path,data='{"bri":254,"transitiontime":0}')
        sleep(.1)

def oneStrobe(path,light):
    lightPath=path+str(light)+r"/state"
    requests.put(lightPath,data='{"bri":254,"transitiontime":0, "hue":'+str(randint(1,65000))+"}")
    sleep(.05)
    requests.put(lightPath,data='{"bri":1,"transitiontime":0, "hue":48186}')
    sleep(.1)

def twoStrobe(path,light1,light2):
    lightPath1=path+str(light1)+r"/state"
    lightPath2=path+str(light2)+r"/state"
    requests.put(lightPath1,data='{"bri":254,"transitiontime":0, "hue":'+str(randint(1,65000))+"}")
    requests.put(lightPath2,data='{"bri":254,"transitiontime":0, "hue":'+str(randint(1,65000))+"}")
    sleep(.05)
    requests.put(lightPath1,data='{"bri":1,"transitiontime":0, "hue":48186}')
    requests.put(lightPath2,data='{"bri":1,"transitiontime":0, "hue":48186}')
    sleep(.1)

def groupStrobe(path,lights,doubleStrobe):
    for light in lights:
        requests.put(path+str(light)+r"/state",data='{"on":true,"bri":0,"sat":254,"hue":48186, "transitiontime":0}')
    
    while True:
        chosenLights = sample(lights,(randint(1,2) if doubleStrobe else 1))
        if len(chosenLights)==1:
            oneStrobe(path,chosenLights[0])
        elif len(chosenLights)==2:
            twoStrobe(path,chosenLights[0],chosenLights[1])

def oneStrobeWhite(path,light):
    lightPath=path+str(light)+r"/state"
    requests.put(lightPath,data='{"bri":254, "sat":1, "transitiontime":0}')
    sleep(.05)
    requests.put(lightPath,data='{""bri":0,"sat":254, "transitiontime":0, "hue":48186}')
    sleep(.1)

def main():
    doubleStrobe= False if len(sys.argv)==1 or sys.argv[1] != "2" else True
    print("DoubleStrobe: ",doubleStrobe)
    path=r"http://10.39.205.195/api/KQtqYPzVCsndUzGxLgRu2oMDiseGkMneZ0agYdEr/lights/"
    lights=[1,3,4,5]
    groupStrobe(path, lights, doubleStrobe)


if __name__ == '__main__':
    main()