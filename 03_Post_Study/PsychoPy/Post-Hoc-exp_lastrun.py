#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mai 22, 2022, at 12:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'BA-Post-Hoc-Study'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Vorname': '', 'Nachname': '', 'Mit welchem Geschlecht identifiziert du dich? (m,w,nicht-binär,keine Angabe)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\alexa\\Documents\\02_study\\duesseldorf\\BA_Linguistik\\09_BBA_Bachelorarbeit\\02_daten\\03_Post_Study\\PsychoPy\\Post-Hoc-exp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
text_WelcomeScreen = visual.TextStim(win=win, name='text_WelcomeScreen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Intro1"
Intro1Clock = core.Clock()
text_Intro1 = visual.TextStim(win=win, name='text_Intro1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Intro1 = keyboard.Keyboard()

# Initialize components for Routine "Intro2"
Intro2Clock = core.Clock()
text_Intro2 = visual.TextStim(win=win, name='text_Intro2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Intro2 = keyboard.Keyboard()

# Initialize components for Routine "Intro3"
Intro3Clock = core.Clock()
text_Intro3 = visual.TextStim(win=win, name='text_Intro3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Intro3 = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_Blank500 = visual.TextStim(win=win, name='text_Blank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Warm_Up"
Warm_UpClock = core.Clock()
text_WarmUp = visual.TextStim(win=win, name='text_WarmUp',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_Buffer = visual.Slider(win=win, name='slider_Buffer',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["sehr männlich", "", "", "neutral", "", "", "sehr weiblich"], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Intro4"
Intro4Clock = core.Clock()
text_Intro4 = visual.TextStim(win=win, name='text_Intro4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Intro4 = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_Blank500 = visual.TextStim(win=win, name='text_Blank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
text_Trial = visual.TextStim(win=win, name='text_Trial',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_Trial = visual.Slider(win=win, name='slider_Trial',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["sehr männlich", "", "", "neutral", "", "", "sehr weiblich"], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
text_Pause = visual.TextStim(win=win, name='text_Pause',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_Blank500 = visual.TextStim(win=win, name='text_Blank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
text_Trial = visual.TextStim(win=win, name='text_Trial',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_Trial = visual.Slider(win=win, name='slider_Trial',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["sehr männlich", "", "", "neutral", "", "", "sehr weiblich"], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Blank1000"
Blank1000Clock = core.Clock()
text_Blank1000 = visual.TextStim(win=win, name='text_Blank1000',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GoodbyeScreen"
GoodbyeScreenClock = core.Clock()
text_GoodbyeScreen = visual.TextStim(win=win, name='text_GoodbyeScreen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
text_WelcomeScreen.setText('Hallo und vielen Dank, dass Du am zweiten und letzten Teil meiner Studie teilnimmst.')
# keep track of which components have finished
WelcomeScreenComponents = [text_WelcomeScreen]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_WelcomeScreen* updates
    if text_WelcomeScreen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_WelcomeScreen.frameNStart = frameN  # exact frame index
        text_WelcomeScreen.tStart = t  # local t and not account for scr refresh
        text_WelcomeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_WelcomeScreen, 'tStartRefresh')  # time at next scr refresh
        text_WelcomeScreen.setAutoDraw(True)
    if text_WelcomeScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_WelcomeScreen.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_WelcomeScreen.tStop = t  # not accounting for scr refresh
            text_WelcomeScreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_WelcomeScreen, 'tStopRefresh')  # time at next scr refresh
            text_WelcomeScreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_WelcomeScreen.started', text_WelcomeScreen.tStartRefresh)
thisExp.addData('text_WelcomeScreen.stopped', text_WelcomeScreen.tStopRefresh)

# ------Prepare to start Routine "Intro1"-------
continueRoutine = True
# update component parameters for each repeat
text_Intro1.setText('Wie auch beim ersten Teil der Studie navigierst du mit der Leertaste.\n\nAufgrund von Komplexität beschränke ich mich auf diese Begriffe\n\n(Drücke die Leertaste um fortzufahren.)')
key_resp_Intro1.keys = []
key_resp_Intro1.rt = []
_key_resp_Intro1_allKeys = []
# keep track of which components have finished
Intro1Components = [text_Intro1, key_resp_Intro1]
for thisComponent in Intro1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro1"-------
while continueRoutine:
    # get current time
    t = Intro1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Intro1* updates
    if text_Intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Intro1.frameNStart = frameN  # exact frame index
        text_Intro1.tStart = t  # local t and not account for scr refresh
        text_Intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Intro1, 'tStartRefresh')  # time at next scr refresh
        text_Intro1.setAutoDraw(True)
    
    # *key_resp_Intro1* updates
    waitOnFlip = False
    if key_resp_Intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Intro1.frameNStart = frameN  # exact frame index
        key_resp_Intro1.tStart = t  # local t and not account for scr refresh
        key_resp_Intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Intro1, 'tStartRefresh')  # time at next scr refresh
        key_resp_Intro1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Intro1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Intro1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Intro1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Intro1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Intro1_allKeys.extend(theseKeys)
        if len(_key_resp_Intro1_allKeys):
            key_resp_Intro1.keys = _key_resp_Intro1_allKeys[-1].name  # just the last key pressed
            key_resp_Intro1.rt = _key_resp_Intro1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro1"-------
for thisComponent in Intro1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Intro1.started', text_Intro1.tStartRefresh)
thisExp.addData('text_Intro1.stopped', text_Intro1.tStopRefresh)
# check responses
if key_resp_Intro1.keys in ['', [], None]:  # No response was made
    key_resp_Intro1.keys = None
thisExp.addData('key_resp_Intro1.keys',key_resp_Intro1.keys)
if key_resp_Intro1.keys != None:  # we had a response
    thisExp.addData('key_resp_Intro1.rt', key_resp_Intro1.rt)
thisExp.addData('key_resp_Intro1.started', key_resp_Intro1.tStartRefresh)
thisExp.addData('key_resp_Intro1.stopped', key_resp_Intro1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro2"-------
continueRoutine = True
# update component parameters for each repeat
text_Intro2.setText('Im Folgenden wirst Du einen Namen sehen sowie einen 7-stelligen Slider. Du bewertest den Namen von ganz links "sehr männlich" bis ganz rechts "sehr weiblich". Die Mitte der Skala zeigt "neutral" an.\n\nZum Beispiel würde ich "Uwe" als "sehr männlich", "Gudrun" als "sehr weiblich" und "Alex" als "neutral" bewerten. \n\nEs steht dir frei die Zwischenstufen zu benutzen.\n\nWichtig ist, NICHT die assoziierten Qualitäten des Namens zu bewerten (Gudrun klingt hart/stark also "männlich"), sondern ob Du eher an einen Mann (der Uwe), eine Frau (die Gudrun) oder vielleicht beide (der/die Alex) denkst. \n\nNun Folgen drei Beispiele. (Drücke die Leertaste.)')
key_resp_Intro2.keys = []
key_resp_Intro2.rt = []
_key_resp_Intro2_allKeys = []
# keep track of which components have finished
Intro2Components = [text_Intro2, key_resp_Intro2]
for thisComponent in Intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro2"-------
while continueRoutine:
    # get current time
    t = Intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Intro2* updates
    if text_Intro2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Intro2.frameNStart = frameN  # exact frame index
        text_Intro2.tStart = t  # local t and not account for scr refresh
        text_Intro2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Intro2, 'tStartRefresh')  # time at next scr refresh
        text_Intro2.setAutoDraw(True)
    
    # *key_resp_Intro2* updates
    waitOnFlip = False
    if key_resp_Intro2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Intro2.frameNStart = frameN  # exact frame index
        key_resp_Intro2.tStart = t  # local t and not account for scr refresh
        key_resp_Intro2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Intro2, 'tStartRefresh')  # time at next scr refresh
        key_resp_Intro2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Intro2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Intro2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Intro2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Intro2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Intro2_allKeys.extend(theseKeys)
        if len(_key_resp_Intro2_allKeys):
            key_resp_Intro2.keys = _key_resp_Intro2_allKeys[-1].name  # just the last key pressed
            key_resp_Intro2.rt = _key_resp_Intro2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro2"-------
for thisComponent in Intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Intro2.started', text_Intro2.tStartRefresh)
thisExp.addData('text_Intro2.stopped', text_Intro2.tStopRefresh)
# check responses
if key_resp_Intro2.keys in ['', [], None]:  # No response was made
    key_resp_Intro2.keys = None
thisExp.addData('key_resp_Intro2.keys',key_resp_Intro2.keys)
if key_resp_Intro2.keys != None:  # we had a response
    thisExp.addData('key_resp_Intro2.rt', key_resp_Intro2.rt)
thisExp.addData('key_resp_Intro2.started', key_resp_Intro2.tStartRefresh)
thisExp.addData('key_resp_Intro2.stopped', key_resp_Intro2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro3"-------
continueRoutine = True
# update component parameters for each repeat
text_Intro3.setText('Wichtig ist, NICHT die assoziierten Qualitäten des Namens zu bewerten (Gudrun klingt hart/stark also "männlich"), sondern ob Du eher an einen Mann (der Uwe), eine Frau (die Gudrun) oder vielleicht beide (der/die Alex) denkst. \n\nNun Folgen drei Beispiele. (Drücke die Leertaste.)')
key_resp_Intro3.keys = []
key_resp_Intro3.rt = []
_key_resp_Intro3_allKeys = []
# keep track of which components have finished
Intro3Components = [text_Intro3, key_resp_Intro3]
for thisComponent in Intro3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro3"-------
while continueRoutine:
    # get current time
    t = Intro3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Intro3* updates
    if text_Intro3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Intro3.frameNStart = frameN  # exact frame index
        text_Intro3.tStart = t  # local t and not account for scr refresh
        text_Intro3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Intro3, 'tStartRefresh')  # time at next scr refresh
        text_Intro3.setAutoDraw(True)
    
    # *key_resp_Intro3* updates
    waitOnFlip = False
    if key_resp_Intro3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Intro3.frameNStart = frameN  # exact frame index
        key_resp_Intro3.tStart = t  # local t and not account for scr refresh
        key_resp_Intro3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Intro3, 'tStartRefresh')  # time at next scr refresh
        key_resp_Intro3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Intro3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Intro3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Intro3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Intro3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Intro3_allKeys.extend(theseKeys)
        if len(_key_resp_Intro3_allKeys):
            key_resp_Intro3.keys = _key_resp_Intro3_allKeys[-1].name  # just the last key pressed
            key_resp_Intro3.rt = _key_resp_Intro3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro3"-------
for thisComponent in Intro3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Intro3.started', text_Intro3.tStartRefresh)
thisExp.addData('text_Intro3.stopped', text_Intro3.tStopRefresh)
# check responses
if key_resp_Intro3.keys in ['', [], None]:  # No response was made
    key_resp_Intro3.keys = None
thisExp.addData('key_resp_Intro3.keys',key_resp_Intro3.keys)
if key_resp_Intro3.keys != None:  # we had a response
    thisExp.addData('key_resp_Intro3.rt', key_resp_Intro3.rt)
thisExp.addData('key_resp_Intro3.started', key_resp_Intro3.tStartRefresh)
thisExp.addData('key_resp_Intro3.stopped', key_resp_Intro3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_Warm_Up = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Post-Hoc-Warm-Up.xlsx', selection='0:3'),
    seed=None, name='trials_Warm_Up')
thisExp.addLoop(trials_Warm_Up)  # add the loop to the experiment
thisTrials_Warm_Up = trials_Warm_Up.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Warm_Up.rgb)
if thisTrials_Warm_Up != None:
    for paramName in thisTrials_Warm_Up:
        exec('{} = thisTrials_Warm_Up[paramName]'.format(paramName))

for thisTrials_Warm_Up in trials_Warm_Up:
    currentLoop = trials_Warm_Up
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Warm_Up.rgb)
    if thisTrials_Warm_Up != None:
        for paramName in thisTrials_Warm_Up:
            exec('{} = thisTrials_Warm_Up[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    text_Blank500.setText('')
    # keep track of which components have finished
    Blank500Components = [text_Blank500]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Blank500* updates
        if text_Blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Blank500.frameNStart = frameN  # exact frame index
            text_Blank500.tStart = t  # local t and not account for scr refresh
            text_Blank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Blank500, 'tStartRefresh')  # time at next scr refresh
            text_Blank500.setAutoDraw(True)
        if text_Blank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_Blank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_Blank500.tStop = t  # not accounting for scr refresh
                text_Blank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_Blank500, 'tStopRefresh')  # time at next scr refresh
                text_Blank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Warm_Up.addData('text_Blank500.started', text_Blank500.tStartRefresh)
    trials_Warm_Up.addData('text_Blank500.stopped', text_Blank500.tStopRefresh)
    
    # ------Prepare to start Routine "Warm_Up"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_WarmUp.setText(Post_Hoc_Item)
    slider_Buffer.reset()
    # keep track of which components have finished
    Warm_UpComponents = [text_WarmUp, slider_Buffer]
    for thisComponent in Warm_UpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Warm_UpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Warm_Up"-------
    while continueRoutine:
        # get current time
        t = Warm_UpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Warm_UpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_WarmUp* updates
        if text_WarmUp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_WarmUp.frameNStart = frameN  # exact frame index
            text_WarmUp.tStart = t  # local t and not account for scr refresh
            text_WarmUp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_WarmUp, 'tStartRefresh')  # time at next scr refresh
            text_WarmUp.setAutoDraw(True)
        
        # *slider_Buffer* updates
        if slider_Buffer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_Buffer.frameNStart = frameN  # exact frame index
            slider_Buffer.tStart = t  # local t and not account for scr refresh
            slider_Buffer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_Buffer, 'tStartRefresh')  # time at next scr refresh
            slider_Buffer.setAutoDraw(True)
        
        # Check slider_Buffer for response to end routine
        if slider_Buffer.getRating() is not None and slider_Buffer.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Warm_UpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Warm_Up"-------
    for thisComponent in Warm_UpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Warm_Up.addData('text_WarmUp.started', text_WarmUp.tStartRefresh)
    trials_Warm_Up.addData('text_WarmUp.stopped', text_WarmUp.tStopRefresh)
    trials_Warm_Up.addData('slider_Buffer.response', slider_Buffer.getRating())
    trials_Warm_Up.addData('slider_Buffer.rt', slider_Buffer.getRT())
    trials_Warm_Up.addData('slider_Buffer.started', slider_Buffer.tStartRefresh)
    trials_Warm_Up.addData('slider_Buffer.stopped', slider_Buffer.tStopRefresh)
    # the Routine "Warm_Up" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_Warm_Up'


# ------Prepare to start Routine "Intro4"-------
continueRoutine = True
# update component parameters for each repeat
text_Intro4.setText('Wie du gesehen hast, geht es nachdem du auf den Slider klickst sofort weiter. Sei also vorsichtig bei deiner Auswahl. Du hast kein Zeitlimit.\n\nNach ca 5 bis 7 Minuten hast du eine Pause\n\nDrücke die Leertaste um das Experiment zu starten.')
key_resp_Intro4.keys = []
key_resp_Intro4.rt = []
_key_resp_Intro4_allKeys = []
# keep track of which components have finished
Intro4Components = [text_Intro4, key_resp_Intro4]
for thisComponent in Intro4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro4"-------
while continueRoutine:
    # get current time
    t = Intro4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Intro4* updates
    if text_Intro4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Intro4.frameNStart = frameN  # exact frame index
        text_Intro4.tStart = t  # local t and not account for scr refresh
        text_Intro4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Intro4, 'tStartRefresh')  # time at next scr refresh
        text_Intro4.setAutoDraw(True)
    
    # *key_resp_Intro4* updates
    waitOnFlip = False
    if key_resp_Intro4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Intro4.frameNStart = frameN  # exact frame index
        key_resp_Intro4.tStart = t  # local t and not account for scr refresh
        key_resp_Intro4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Intro4, 'tStartRefresh')  # time at next scr refresh
        key_resp_Intro4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Intro4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Intro4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Intro4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Intro4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Intro4_allKeys.extend(theseKeys)
        if len(_key_resp_Intro4_allKeys):
            key_resp_Intro4.keys = _key_resp_Intro4_allKeys[-1].name  # just the last key pressed
            key_resp_Intro4.rt = _key_resp_Intro4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro4"-------
for thisComponent in Intro4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Intro4.started', text_Intro4.tStartRefresh)
thisExp.addData('text_Intro4.stopped', text_Intro4.tStopRefresh)
# check responses
if key_resp_Intro4.keys in ['', [], None]:  # No response was made
    key_resp_Intro4.keys = None
thisExp.addData('key_resp_Intro4.keys',key_resp_Intro4.keys)
if key_resp_Intro4.keys != None:  # we had a response
    thisExp.addData('key_resp_Intro4.rt', key_resp_Intro4.rt)
thisExp.addData('key_resp_Intro4.started', key_resp_Intro4.tStartRefresh)
thisExp.addData('key_resp_Intro4.stopped', key_resp_Intro4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Post-Hoc-List1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    text_Blank500.setText('')
    # keep track of which components have finished
    Blank500Components = [text_Blank500]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Blank500* updates
        if text_Blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Blank500.frameNStart = frameN  # exact frame index
            text_Blank500.tStart = t  # local t and not account for scr refresh
            text_Blank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Blank500, 'tStartRefresh')  # time at next scr refresh
            text_Blank500.setAutoDraw(True)
        if text_Blank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_Blank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_Blank500.tStop = t  # not accounting for scr refresh
                text_Blank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_Blank500, 'tStopRefresh')  # time at next scr refresh
                text_Blank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_Blank500.started', text_Blank500.tStartRefresh)
    trials.addData('text_Blank500.stopped', text_Blank500.tStopRefresh)
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_Trial.setText(Post_Hoc_Item)
    slider_Trial.reset()
    # keep track of which components have finished
    TrialComponents = [text_Trial, slider_Trial]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Trial* updates
        if text_Trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Trial.frameNStart = frameN  # exact frame index
            text_Trial.tStart = t  # local t and not account for scr refresh
            text_Trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Trial, 'tStartRefresh')  # time at next scr refresh
            text_Trial.setAutoDraw(True)
        
        # *slider_Trial* updates
        if slider_Trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_Trial.frameNStart = frameN  # exact frame index
            slider_Trial.tStart = t  # local t and not account for scr refresh
            slider_Trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_Trial, 'tStartRefresh')  # time at next scr refresh
            slider_Trial.setAutoDraw(True)
        
        # Check slider_Trial for response to end routine
        if slider_Trial.getRating() is not None and slider_Trial.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_Trial.started', text_Trial.tStartRefresh)
    trials.addData('text_Trial.stopped', text_Trial.tStopRefresh)
    trials.addData('slider_Trial.response', slider_Trial.getRating())
    trials.addData('slider_Trial.rt', slider_Trial.getRT())
    trials.addData('slider_Trial.started', slider_Trial.tStartRefresh)
    trials.addData('slider_Trial.stopped', slider_Trial.tStopRefresh)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "Pause"-------
continueRoutine = True
# update component parameters for each repeat
text_Pause.setText('Super! Du hast die Hälfte geschafft. Du hast dir eine Pause verdient.\n\nWeiter geht es wenn du "P" drückst\n\n')
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
PauseComponents = [text_Pause, key_resp]
for thisComponent in PauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause"-------
while continueRoutine:
    # get current time
    t = PauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Pause* updates
    if text_Pause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Pause.frameNStart = frameN  # exact frame index
        text_Pause.tStart = t  # local t and not account for scr refresh
        text_Pause.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Pause, 'tStartRefresh')  # time at next scr refresh
        text_Pause.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause"-------
for thisComponent in PauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Pause.started', text_Pause.tStartRefresh)
thisExp.addData('text_Pause.stopped', text_Pause.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Post-Hoc-List2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    text_Blank500.setText('')
    # keep track of which components have finished
    Blank500Components = [text_Blank500]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Blank500* updates
        if text_Blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Blank500.frameNStart = frameN  # exact frame index
            text_Blank500.tStart = t  # local t and not account for scr refresh
            text_Blank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Blank500, 'tStartRefresh')  # time at next scr refresh
            text_Blank500.setAutoDraw(True)
        if text_Blank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_Blank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_Blank500.tStop = t  # not accounting for scr refresh
                text_Blank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_Blank500, 'tStopRefresh')  # time at next scr refresh
                text_Blank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_Blank500.started', text_Blank500.tStartRefresh)
    trials_2.addData('text_Blank500.stopped', text_Blank500.tStopRefresh)
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_Trial.setText(Post_Hoc_Item)
    slider_Trial.reset()
    # keep track of which components have finished
    TrialComponents = [text_Trial, slider_Trial]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Trial* updates
        if text_Trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Trial.frameNStart = frameN  # exact frame index
            text_Trial.tStart = t  # local t and not account for scr refresh
            text_Trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Trial, 'tStartRefresh')  # time at next scr refresh
            text_Trial.setAutoDraw(True)
        
        # *slider_Trial* updates
        if slider_Trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_Trial.frameNStart = frameN  # exact frame index
            slider_Trial.tStart = t  # local t and not account for scr refresh
            slider_Trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_Trial, 'tStartRefresh')  # time at next scr refresh
            slider_Trial.setAutoDraw(True)
        
        # Check slider_Trial for response to end routine
        if slider_Trial.getRating() is not None and slider_Trial.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_Trial.started', text_Trial.tStartRefresh)
    trials_2.addData('text_Trial.stopped', text_Trial.tStopRefresh)
    trials_2.addData('slider_Trial.response', slider_Trial.getRating())
    trials_2.addData('slider_Trial.rt', slider_Trial.getRT())
    trials_2.addData('slider_Trial.started', slider_Trial.tStartRefresh)
    trials_2.addData('slider_Trial.stopped', slider_Trial.tStopRefresh)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "Blank1000"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
text_Blank1000.setText('')
# keep track of which components have finished
Blank1000Components = [text_Blank1000]
for thisComponent in Blank1000Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank1000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank1000"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank1000Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank1000Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Blank1000* updates
    if text_Blank1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Blank1000.frameNStart = frameN  # exact frame index
        text_Blank1000.tStart = t  # local t and not account for scr refresh
        text_Blank1000.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Blank1000, 'tStartRefresh')  # time at next scr refresh
        text_Blank1000.setAutoDraw(True)
    if text_Blank1000.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_Blank1000.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_Blank1000.tStop = t  # not accounting for scr refresh
            text_Blank1000.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_Blank1000, 'tStopRefresh')  # time at next scr refresh
            text_Blank1000.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank1000Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank1000"-------
for thisComponent in Blank1000Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Blank1000.started', text_Blank1000.tStartRefresh)
thisExp.addData('text_Blank1000.stopped', text_Blank1000.tStopRefresh)

# ------Prepare to start Routine "GoodbyeScreen"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
text_GoodbyeScreen.setText('Vielen Dank, dass Du an meinem Experiment teilgenommen hast.\n\nWenn du mir deine Zahlungsdetails noch nicht genannt hast kannst du mir gerne eine Email senden.')
# keep track of which components have finished
GoodbyeScreenComponents = [text_GoodbyeScreen]
for thisComponent in GoodbyeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GoodbyeScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GoodbyeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_GoodbyeScreen* updates
    if text_GoodbyeScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_GoodbyeScreen.frameNStart = frameN  # exact frame index
        text_GoodbyeScreen.tStart = t  # local t and not account for scr refresh
        text_GoodbyeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_GoodbyeScreen, 'tStartRefresh')  # time at next scr refresh
        text_GoodbyeScreen.setAutoDraw(True)
    if text_GoodbyeScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_GoodbyeScreen.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_GoodbyeScreen.tStop = t  # not accounting for scr refresh
            text_GoodbyeScreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_GoodbyeScreen, 'tStopRefresh')  # time at next scr refresh
            text_GoodbyeScreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GoodbyeScreen"-------
for thisComponent in GoodbyeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_GoodbyeScreen.started', text_GoodbyeScreen.tStartRefresh)
thisExp.addData('text_GoodbyeScreen.stopped', text_GoodbyeScreen.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
