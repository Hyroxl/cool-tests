
app.background = 'black'
app.stepsPerSecond = 100
target = Circle(0, 0, 30, fill='white')
targetcenter = Circle(0, 0, 5, fill='red')
targetline1 = Circle(0, 0, 15, fill=None, border='red', borderWidth=5)
targetline2 = Circle(0, 0, 25, fill=None, border='red', borderWidth=5)
def crosshair(color):
    Line(180, 200, 220, 200, opacity=70, fill=color)
    Line(200, 180, 200, 220, opacity=70, fill=color)
crosshair('red')
missorhit = Label('miss', 200, 50, size=50, fill='blue', visible=False)
score = Label(0, 10, 10, size=25, fill='blue')
mouse = Circle(0, 0, 1, visible=False)
timer = 0
winloss = "null"
def onStep():
    global timer
    timer+=1
    if (timer>=100):
        if (score.value < 0):
            missorhit.visible = True
            missorhit.value = 'You Lost'
            winloss = "loss"
            app.stop()
            print(winloss)
    print(timer)
def onMouseMove(mouseX, mouseY):
    mouse.centerX = mouseX
    mouse.centerY = mouseY
    target.centerX = 400-mouseX
    target.centerY = 400-mouseY
    targetcenter.centerX = 400-mouseX
    targetcenter.centerY = 400-mouseY
    targetline1.centerX = 400-mouseX
    targetline1.centerY = 400-mouseY
    targetline2.centerX = 400-mouseX
    targetline2.centerY = 400-mouseY
    if (mouseY < 200):
        if (mouseX < 200):
            app.background = rgb(mouseY, mouseX, 0)
        else:
            app.background = rgb(mouseY, 400-mouseX, 0)
    else:
        if (mouseX < 200):
            app.background = rgb(400-mouseY, mouseX, 0)
        else:
            app.background = rgb(400-mouseY, 400-mouseX, 0)
def onMousePress(mouseX, mouseY):
    if (mouse.hitsShape(targetcenter) == True):
        target.fill = 'red'
        targetcenter.fill = 'white'
        targetline1.border = 'white'
        targetline2.border = 'white'
        missorhit.visible = True
        missorhit.value = 'Hit'
        print("hit")
        score.value += 1
    else:
            missorhit.visible = True
            missorhit.value = 'Miss'
            print("miss")
            score.value -= 1
    if (score.value >= 10):
        missorhit.visible = True
        missorhit.value = 'You Win!'
        winloss = "win"
        app.stop()
        print(winloss)
def onMouseRelease(mouseX, mouseY):
    target.fill = 'white'
    targetcenter.fill = 'red'
    targetline1.border = 'red'
    targetline2.border = 'red'
    if (score.value < 10):
        missorhit.visible = False
    else:
        missorhit.visible = True
    if (score.value == 10):
        score.value -= 10
    if (score.value <= 10):
        missorhit.visible = False
