import requests, sys
from random import randint, sample
from time import sleep


basePath = r"http://10.39.205.195/api/KQtqYPzVCsndUzGxLgRu2oMDiseGkMneZ0agYdEr/lights/"
lights=[1,3,4,5]

def oneStrobe(light,rainbow):
    lightPath=basePath+str(light)+r"/state"
    requests.put(lightPath,data='{"bri":254,"transitiontime":0' + ('" ,hue":' + str(randint(1,65000)) + '}') if rainbow else "}")
    sleep(.05)
    requests.put(lightPath,data='{"bri":1,"transitiontime":0' + '", hue":48186}' if not rainbow else '}')
    sleep(.1)

def twoStrobe(light1,light2,rainbow):
    lightPath1=basePath+str(light1)+r"/state"
    lightPath2=basePath+str(light2)+r"/state"
    requests.put(lightPath1,data='{"bri":254,"transitiontime":0' + ('" ,hue":' + str(randint(1,65000)) + '}') if rainbow else "}")
    requests.put(lightPath2,data='{"bri":254,"transitiontime":0' + ('" ,hue":' + str(randint(1,65000)) + '}') if rainbow else "}")
    sleep(.05)
    requests.put(lightPath1,data='{"bri":1,"transitiontime":0' + '", hue":48186}' if not rainbow else '}')
    requests.put(lightPath2,data='{"bri":1,"transitiontime":0' + '", hue":48186}' if not rainbow else '}')
    sleep(.1)

def presetLightForStrobe(light,rainbow):
    requests.put(basePath+str(light)+r"/state",data='{"on":true,"bri":0, "transitiontime":0,' +'"sat":254,"hue":48186 }' if rainbow else '"sat:1}"')


def strobeDriver(lights, doubleStrobe, rainbow):
    for light in lights:
        presetLightForStrobe(light,rainbow)
    while True:
        choosenLights=sample(lights,(randint(1,2) if (doubleStrobe and len(lights>2))else 1))
        if len(choosenLights==1):
            oneStrobe(light, rainbow)
        else:
            twoStrobe(light1,light2, rainbow)
    return

def main():
    pass
    

if __name__ == '__main__':
    main()
