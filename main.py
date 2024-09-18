import flowerLibrary
import time
import random
import turtle
from turtle import Turtle
import psutil

# How long program will run in seconds. Default to 360 for testing parameters.
# Ensure this parameter is divisible by 12 as that is how many leaves will be drawn per simulation.
timeFrame = 360

# Flag to dictate if program will run with DHT sensor or random values
flag = False

# Options for simulated values
lightWeights = [.7, .3]  # [True, False]
numberRange = [50, 70]  # Picks a random inclusive value from this range

if flag:
    try:
        import board
        import adafruit_dht
        from gpiozero import LightSensor
        for proc in psutil.process_iter():
            if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
                proc.kill()
                sensor = adafruit_dht.DHT11(board.D21)
    except ValueError:
        print("Error: Please enter valid integers.")

def getTemp():
    untilT = True
    while untilT:
        try:
            temper = sensor.temperature
            untilT = False
        except RuntimeError as error:
            continue
        except Exception as error:
            sensor.exit()
            raise error
    return temper    

def drawTemperDisplay(t):
    t.setx(-450)
    t.sety(10)
    temperatureS = "Temperature: "
    t.write(temperatureS, font=("arial", 15, "bold"))
    
def drawLightDisplay(t):
    t.setx(-450)
    t.sety(-10)
    temperatureS = "Light: "
    t.write(temperatureS, font=("arial", 15, "bold"))
    
def drawHappyDisplay(t):
    t.setx(-450)
    t.sety(-30)
    temperatureS = "Current Happy Level: "
    t.write(temperatureS, font=("arial", 15, "bold"))

def drawTemper(t, current):
    t.clear()
    t.setx(-315)
    t.sety(10)
    t.write(str(current), font=("arial", 15, "bold"))

def drawLight(t, current):
    t.clear()
    t.setx(-390)
    t.sety(-10)
    t.write(str(current), font=("arial", 15, "bold"))

def drawCurrentHappy(t, current):
    t.clear()
    t.setx(-245)
    t.sety(-30) 
    t.write(str(current), font=("arial", 15, "bold"))

def main():

    if flag:
        l = LightSensor(26)
    screen = turtle.Screen()
    flowerLibrary.welcome.weclomeScreen()
    
    name = flowerLibrary.welcome.get_name()
    
    flowerLibrary.background.drawOverBackground("LightBlue")
    flowerLibrary.background.drawGround()
    flowerLibrary.flower.drawstem()
    flowerLibrary.background.theCategories()

    count = 0
    arr = [60, 70]
    plantBasic = flowerLibrary.plant.plant(name, 50, arr)
    
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(8, 280)
    turtle.write(plantBasic.name, align="center", font=("arial",40,"bold"))
    
    turtleDisplay = Turtle(visible=False)
    turtleDisplay.penup()
    
    drawTemperDisplay(turtleDisplay)
    drawLightDisplay(turtleDisplay)
    drawHappyDisplay(turtleDisplay)
    
    turtleTemp = Turtle(visible=False)
    turtleLight = Turtle(visible=False)
    turtleHappy = Turtle(visible=False)
    turtleTemp.penup()
    turtleLight.penup()
    turtleHappy.penup()
    
    d = flowerLibrary.drawing.drawer()
    
    while count <= timeFrame:

      if count % 30 == 0 and count != 0:
        d.drawLeaf(plantBasic.baseHappy)
      count = count + 1

      if flag:
        # Does a Celsius to Fahrenheit conversion
        temp = (int(getTemp() or 0) * 9/5) + 32
        isLight = l.light_detected

      else:
        isLight = random_bool = random.choices([True, False], weights=lightWeights)[0]
        random_int = random.randint(numberRange[0], numberRange[1])

      plantBasic.calculateLightLevel(isLight, count)
      plantBasic.calculateHappy(temp)
      print("Light level:", l.value)
      print("Temperature:", temp)
      print("Light: ", l.light_detected)
      print("Happy level: ", plantBasic.baseHappy)
      print("Iteration: ", count)
      drawTemper(turtleTemp, temp)
      drawLight(turtleLight, isLight)
      drawCurrentHappy(turtleHappy, plantBasic.baseHappy)
      time.sleep(1)
    d.finish(plantBasic.baseHappy)


if __name__ == "__main__":
    main()
