import pyautogui # type: ignore
import time
import openai # type: ignore
import pyperclip # type: ignore


def newVideo(lawNum):
    # Open CapCutrpReplay_Fi
    # Hold down the Command key
    pyautogui.keyDown('command')
    # Press the Space key
    pyautogui.press('space')
    # Release the Command key
    pyautogui.keyUp('command')

    time.sleep(1)
    pyautogui.write('CapCut')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)  
    # Wait for CapCut to open


    pyautogui.click(x=840, y=240)  # Adjust coordinates to your Import button location
    time.sleep(3)
    pyautogui.click(x=400, y=290)
    time.sleep(2)
    pyautogui.click(x=995, y=252)
    pyautogui.write('48' + str(lawNum) + ".mov", interval=0.1)
    time.sleep(2)
    pyautogui.click(x=530, y=397)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for video to import
    
    
    pyautogui.click(x=250, y=259) #Add video to project
    time.sleep(4)
    pyautogui.click(x=158, y=721) #Click on cover button
    time.sleep(2)
    pyautogui.click(x=789, y=624) #Click local button
    time.sleep(2)
    pyautogui.click(x=725, y=387) #Click import button
    time.sleep(2)
    pyautogui.click(x=1000, y=225) #Click search button
    time.sleep(1)
    pyautogui.write('48LawsCoverMC')
    time.sleep(1)
    pyautogui.click(x=517, y=375) #Open cover image
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=1027, y=752) #Click Edit button
    time.sleep(1)
    
    
    pyautogui.click(x=125, y=344) #Click Text button
    time.sleep(1)
    pyautogui.click(x=283, y=195) #Add text as a title
    time.sleep(1)
    pyautogui.doubleClick(x=916, y=468) #Click on the Text
    time.sleep(1)#Delete filler Text
    
    for i in range(12) :
        pyautogui.press('backspace')
        pyautogui.press('delete')
    time.sleep(1)
    pyautogui.write(str(lawNum)) #CURRENT CHAPTER NUMBER
    time.sleep(1)
    
    
    #pyautogui.click(x=1307, y=211) #Click on the Edit button
    time.sleep(1)
    pyautogui.doubleClick(x=1238, y=247) #Click on the Edit Size button
    time.sleep(1)
    #Delete filler Text
    for i in range(6) :
        pyautogui.press('backspace')
        pyautogui.press('delete')
    time.sleep(1)
    pyautogui.write('128') #SIZE OF TEXT
    time.sleep(1)
    
    pyautogui.click(x=1134, y=246) #Click on the Edit Font button
    time.sleep(1)
    #Delete filler Text
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.keyUp('fn')
    pyautogui.write('kanit-black', interval= 0.1) #FONT STYLE
    time.sleep(5)
    pyautogui.click(x=1148, y=292)
    
    
    #Click and drag the scroll bar down
    pyautogui.moveTo(1284, 372, duration=1)  # duration is optional, adds smooth movement
    # Perform mouse down (click and hold)
    pyautogui.mouseDown()
    # Move the mouse to the ending position while holding down the mouse button
    pyautogui.moveTo(1284, 572, duration=2)  # duration is optional, adds smooth movement
    # Release the mouse button (drop)
    pyautogui.mouseUp()
    
    pyautogui.click(x=1264,y=562) #Click Stroke button
    time.sleep(1)
    pyautogui.click(x=1219,y=590) #Adjust the stroke
    time.sleep(1)
    pyautogui.click(x=1209,y=541) #Edit stroke width
    time.sleep(1)
    #Delete filler Text
    for i in range(3) :
        pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('60')
    time.sleep(1)
    pyautogui.click(x=573, y=430) #Click away
    
    #Click and drag the number to the center of the cover
    pyautogui.moveTo(877, 539, duration=1)  # duration is optional, adds smooth movement
    # Perform mouse down (click and hold)
    pyautogui.mouseDown()
    # Move the mouse to the ending position while holding down the mouse button
    pyautogui.moveTo(877, 497, duration=2)  # duration is optional, adds smooth movement
    # Release the mouse button (drop)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.click(x=1309, y=788) #Save the project
    time.sleep(8)

    pyautogui.click(732,19) #Change title of project
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('Law' + str(lawNum))
    time.sleep(1)
    
    #Export the video
    pyautogui.click(1394, 17) #Click export button
    time.sleep(1)
    pyautogui.click(967, 460) #Click frame rate drop-down button
    time.sleep(1)
    pyautogui.click(895, 620) #Click 60FPS button
    time.sleep(1)
    pyautogui.click(994, 753) #Final export button
    time.sleep(45)

    
    #TikTok
    hashtags = "#mindset #motivation #hopecore #real #48lawsofpower"
    pyautogui.click(778, 479) #Visibility drop-down
    time.sleep(1)
    pyautogui.click(783, 510) #Public visibility
    time.sleep(1)
    pyautogui.click(716, 536) #Comment checkbox
    time.sleep(1)
    pyautogui.click(805, 536) #Duet checkbox
    time.sleep(1)
    pyautogui.click(865, 536) #Stitch checkbox
    time.sleep(1)
    pyautogui.click(751, 403) #Caption Button
    caption = getCaption(lawNum)
    time.sleep(1)
    pyperclip.copy(caption)
    pyautogui.hotkey('command', 'v') #Paste caption
    time.sleep(1)
    pyperclip.copy(hashtags)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command') #Paste hashtags
    time.sleep(1)
    pyautogui.click(987, 752) #Share
    time.sleep(60)
    pyautogui.click(987, 752) #Keep screen from going to sleep
    time.sleep(60)
    pyautogui.click(987, 752) #Keep screen from going to sleep
    time.sleep(60)
    pyautogui.click(987, 752) #Keep screen from going to sleep
    time.sleep(60)
    pyautogui.click(x=985, y=647)  #Click the okay button
    pyautogui.keyDown('command')
    pyautogui.press('q')
    pyautogui.keyUp('command')
    time.sleep(10)



def getCaption(lawNum) :
    systemGuidelines = open("SystemGuidelines", "r").read()
    openai.api_key = "sk-proj-xEb1sMq24CDukBVzybJ5T3BlbkFJY5cUQYTE4qXGeK3kHnqz"
    completion = openai.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": str(systemGuidelines)},
        {"role": "user", "content": str(lawNum)}
      ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


nextLaw = 18
while nextLaw <= 18:
    newVideo(nextLaw)
    nextLaw += 1


print("Video Completed")