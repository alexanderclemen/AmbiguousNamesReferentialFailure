#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Februar 01, 2022, at 07:27
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
expName = 'Norming_Study_exp_V2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\alexa\\Documents\\02_study\\duesseldorf\\BA_Linguistik\\09_BBA_Bachelorarbeit\\02_daten\\01_Norming_Study\\PsychoPy\\Norming_Study_exp_V2_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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
key_resp_WelcomeScreen = keyboard.Keyboard()

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

# Initialize components for Routine "Age"
AgeClock = core.Clock()
text_Age = visual.TextStim(win=win, name='text_Age',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_Age = visual.Slider(win=win, name='slider_Age',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=("17-", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30+"), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)
key_Age = keyboard.Keyboard()

# Initialize components for Routine "Muttersprachler"
MuttersprachlerClock = core.Clock()
text_Muttersprachler = visual.TextStim(win=win, name='text_Muttersprachler',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_Muttersprache = visual.Slider(win=win, name='slider_Muttersprache',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=("ja", "nein"), ticks=(1, 2), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)
key_Muttersprachler = keyboard.Keyboard()

# Initialize components for Routine "Intro2"
Intro2Clock = core.Clock()
key_Intro2 = keyboard.Keyboard()
text_Intro2 = visual.TextStim(win=win, name='text_Intro2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
text_Blank500 = visual.TextStim(win=win, name='text_Blank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "OtherName"
OtherNameClock = core.Clock()
text_Buffer = visual.TextStim(win=win, name='text_Buffer',
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

# Initialize components for Routine "biologicalSex"
biologicalSexClock = core.Clock()
text_biologicalSex = visual.TextStim(win=win, name='text_biologicalSex',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_biologicalSex = visual.Slider(win=win, name='slider_biologicalSex',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["männlich", "divers", "weiblich"], ticks=(1, 2, 3), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
key_biologicalSex = keyboard.Keyboard()

# Initialize components for Routine "GenderIdentity"
GenderIdentityClock = core.Clock()
text_GenderIdentity = visual.TextStim(win=win, name='text_GenderIdentity',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["männlich", "", "", "", "", "", "weiblich"], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
key_resp = keyboard.Keyboard()

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
# update component parameters for each repeat
text_WelcomeScreen.setText('Hallo und vielen Dank dass Du an meiner Studie teilnimmst.\n\nDrücke die Leertaste um fortzufahren.')
key_resp_WelcomeScreen.keys = []
key_resp_WelcomeScreen.rt = []
_key_resp_WelcomeScreen_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [text_WelcomeScreen, key_resp_WelcomeScreen]
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
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_WelcomeScreen* updates
    if text_WelcomeScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_WelcomeScreen.frameNStart = frameN  # exact frame index
        text_WelcomeScreen.tStart = t  # local t and not account for scr refresh
        text_WelcomeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_WelcomeScreen, 'tStartRefresh')  # time at next scr refresh
        text_WelcomeScreen.setAutoDraw(True)
    
    # *key_resp_WelcomeScreen* updates
    waitOnFlip = False
    if key_resp_WelcomeScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_WelcomeScreen.frameNStart = frameN  # exact frame index
        key_resp_WelcomeScreen.tStart = t  # local t and not account for scr refresh
        key_resp_WelcomeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_WelcomeScreen, 'tStartRefresh')  # time at next scr refresh
        key_resp_WelcomeScreen.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_WelcomeScreen.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_WelcomeScreen.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_WelcomeScreen.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_WelcomeScreen.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_WelcomeScreen_allKeys.extend(theseKeys)
        if len(_key_resp_WelcomeScreen_allKeys):
            key_resp_WelcomeScreen.keys = _key_resp_WelcomeScreen_allKeys[-1].name  # just the last key pressed
            key_resp_WelcomeScreen.rt = _key_resp_WelcomeScreen_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# check responses
if key_resp_WelcomeScreen.keys in ['', [], None]:  # No response was made
    key_resp_WelcomeScreen.keys = None
thisExp.addData('key_resp_WelcomeScreen.keys',key_resp_WelcomeScreen.keys)
if key_resp_WelcomeScreen.keys != None:  # we had a response
    thisExp.addData('key_resp_WelcomeScreen.rt', key_resp_WelcomeScreen.rt)
thisExp.addData('key_resp_WelcomeScreen.started', key_resp_WelcomeScreen.tStartRefresh)
thisExp.addData('key_resp_WelcomeScreen.stopped', key_resp_WelcomeScreen.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro1"-------
continueRoutine = True
# update component parameters for each repeat
text_Intro1.setText('Ich versuche zu verstehen wie Vornamen im mentalen Lexikon abgespeichert sind und dafür brauche ich (d)eine Datengrundlage. Vorerst brauche ich jedoch noch personenbezogene Daten.  Keine Sorge die Daten werden anonymisiert.\n\n(Drücke die Leertaste um fortzufahren.)')
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

# ------Prepare to start Routine "Age"-------
continueRoutine = True
# update component parameters for each repeat
text_Age.setText('Bitte trage auf dem Slider dein Alter ein.\n\n(Drücke die Leertaste um fortzufahren.)')
slider_Age.reset()
key_Age.keys = []
key_Age.rt = []
_key_Age_allKeys = []
# keep track of which components have finished
AgeComponents = [text_Age, slider_Age, key_Age]
for thisComponent in AgeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AgeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Age"-------
while continueRoutine:
    # get current time
    t = AgeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AgeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Age* updates
    if text_Age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Age.frameNStart = frameN  # exact frame index
        text_Age.tStart = t  # local t and not account for scr refresh
        text_Age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Age, 'tStartRefresh')  # time at next scr refresh
        text_Age.setAutoDraw(True)
    
    # *slider_Age* updates
    if slider_Age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_Age.frameNStart = frameN  # exact frame index
        slider_Age.tStart = t  # local t and not account for scr refresh
        slider_Age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_Age, 'tStartRefresh')  # time at next scr refresh
        slider_Age.setAutoDraw(True)
    
    # *key_Age* updates
    waitOnFlip = False
    if key_Age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Age.frameNStart = frameN  # exact frame index
        key_Age.tStart = t  # local t and not account for scr refresh
        key_Age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Age, 'tStartRefresh')  # time at next scr refresh
        key_Age.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Age.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Age.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Age.status == STARTED and not waitOnFlip:
        theseKeys = key_Age.getKeys(keyList=['space'], waitRelease=False)
        _key_Age_allKeys.extend(theseKeys)
        if len(_key_Age_allKeys):
            key_Age.keys = _key_Age_allKeys[-1].name  # just the last key pressed
            key_Age.rt = _key_Age_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Age"-------
for thisComponent in AgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Age.started', text_Age.tStartRefresh)
thisExp.addData('text_Age.stopped', text_Age.tStopRefresh)
thisExp.addData('slider_Age.response', slider_Age.getRating())
thisExp.addData('slider_Age.rt', slider_Age.getRT())
thisExp.addData('slider_Age.started', slider_Age.tStartRefresh)
thisExp.addData('slider_Age.stopped', slider_Age.tStopRefresh)
# check responses
if key_Age.keys in ['', [], None]:  # No response was made
    key_Age.keys = None
thisExp.addData('key_Age.keys',key_Age.keys)
if key_Age.keys != None:  # we had a response
    thisExp.addData('key_Age.rt', key_Age.rt)
thisExp.addData('key_Age.started', key_Age.tStartRefresh)
thisExp.addData('key_Age.stopped', key_Age.tStopRefresh)
thisExp.nextEntry()
# the Routine "Age" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Muttersprachler"-------
continueRoutine = True
# update component parameters for each repeat
text_Muttersprachler.setText('Bist du deutsche Muttersprachlerin oder deutscher Muttersprachler?\n\n(Drücke die Leertaste um fortzufahren.)')
slider_Muttersprache.reset()
key_Muttersprachler.keys = []
key_Muttersprachler.rt = []
_key_Muttersprachler_allKeys = []
# keep track of which components have finished
MuttersprachlerComponents = [text_Muttersprachler, slider_Muttersprache, key_Muttersprachler]
for thisComponent in MuttersprachlerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MuttersprachlerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Muttersprachler"-------
while continueRoutine:
    # get current time
    t = MuttersprachlerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MuttersprachlerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Muttersprachler* updates
    if text_Muttersprachler.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Muttersprachler.frameNStart = frameN  # exact frame index
        text_Muttersprachler.tStart = t  # local t and not account for scr refresh
        text_Muttersprachler.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Muttersprachler, 'tStartRefresh')  # time at next scr refresh
        text_Muttersprachler.setAutoDraw(True)
    
    # *slider_Muttersprache* updates
    if slider_Muttersprache.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_Muttersprache.frameNStart = frameN  # exact frame index
        slider_Muttersprache.tStart = t  # local t and not account for scr refresh
        slider_Muttersprache.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_Muttersprache, 'tStartRefresh')  # time at next scr refresh
        slider_Muttersprache.setAutoDraw(True)
    
    # *key_Muttersprachler* updates
    waitOnFlip = False
    if key_Muttersprachler.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Muttersprachler.frameNStart = frameN  # exact frame index
        key_Muttersprachler.tStart = t  # local t and not account for scr refresh
        key_Muttersprachler.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Muttersprachler, 'tStartRefresh')  # time at next scr refresh
        key_Muttersprachler.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Muttersprachler.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Muttersprachler.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Muttersprachler.status == STARTED and not waitOnFlip:
        theseKeys = key_Muttersprachler.getKeys(keyList=['space'], waitRelease=False)
        _key_Muttersprachler_allKeys.extend(theseKeys)
        if len(_key_Muttersprachler_allKeys):
            key_Muttersprachler.keys = _key_Muttersprachler_allKeys[-1].name  # just the last key pressed
            key_Muttersprachler.rt = _key_Muttersprachler_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MuttersprachlerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Muttersprachler"-------
for thisComponent in MuttersprachlerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Muttersprachler.started', text_Muttersprachler.tStartRefresh)
thisExp.addData('text_Muttersprachler.stopped', text_Muttersprachler.tStopRefresh)
thisExp.addData('slider_Muttersprache.response', slider_Muttersprache.getRating())
thisExp.addData('slider_Muttersprache.rt', slider_Muttersprache.getRT())
thisExp.addData('slider_Muttersprache.started', slider_Muttersprache.tStartRefresh)
thisExp.addData('slider_Muttersprache.stopped', slider_Muttersprache.tStopRefresh)
# check responses
if key_Muttersprachler.keys in ['', [], None]:  # No response was made
    key_Muttersprachler.keys = None
thisExp.addData('key_Muttersprachler.keys',key_Muttersprachler.keys)
if key_Muttersprachler.keys != None:  # we had a response
    thisExp.addData('key_Muttersprachler.rt', key_Muttersprachler.rt)
thisExp.addData('key_Muttersprachler.started', key_Muttersprachler.tStartRefresh)
thisExp.addData('key_Muttersprachler.stopped', key_Muttersprachler.tStopRefresh)
thisExp.nextEntry()
# the Routine "Muttersprachler" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro2"-------
continueRoutine = True
# update component parameters for each repeat
key_Intro2.keys = []
key_Intro2.rt = []
_key_Intro2_allKeys = []
text_Intro2.setText('Im Folgenden wirst Du einen Namen sehen sowie einen 7-stelligen Slider. Du bewertest den Namen von ganz links "sehr männlich" bis ganz rechts "sehr weiblich". Die Mitte der Skala zeigt "neutral" an.\n\nZum Beispiel würde ich "Uwe" als "sehr männlich", "Gudrun" als "sehr weiblich" und "Alex" als "neutral" bewerten. \n\nWichtig ist, NICHT die assoziierten Qualitäten des Namens zu bewerten (Gudrun klingt hart/stark also "männlich"), sondern ob Du eher an einen Mann (der Uwe), eine Frau (die Gudrun) oder vielleicht beide (der/die Alex) denkst.\n\nDrücke die Leertaste um das Experiment zu starten.')
# keep track of which components have finished
Intro2Components = [key_Intro2, text_Intro2]
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
    
    # *key_Intro2* updates
    waitOnFlip = False
    if key_Intro2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Intro2.frameNStart = frameN  # exact frame index
        key_Intro2.tStart = t  # local t and not account for scr refresh
        key_Intro2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Intro2, 'tStartRefresh')  # time at next scr refresh
        key_Intro2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Intro2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Intro2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Intro2.status == STARTED and not waitOnFlip:
        theseKeys = key_Intro2.getKeys(keyList=['space'], waitRelease=False)
        _key_Intro2_allKeys.extend(theseKeys)
        if len(_key_Intro2_allKeys):
            key_Intro2.keys = _key_Intro2_allKeys[-1].name  # just the last key pressed
            key_Intro2.rt = _key_Intro2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_Intro2* updates
    if text_Intro2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Intro2.frameNStart = frameN  # exact frame index
        text_Intro2.tStart = t  # local t and not account for scr refresh
        text_Intro2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Intro2, 'tStartRefresh')  # time at next scr refresh
        text_Intro2.setAutoDraw(True)
    
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
# check responses
if key_Intro2.keys in ['', [], None]:  # No response was made
    key_Intro2.keys = None
thisExp.addData('key_Intro2.keys',key_Intro2.keys)
if key_Intro2.keys != None:  # we had a response
    thisExp.addData('key_Intro2.rt', key_Intro2.rt)
thisExp.addData('key_Intro2.started', key_Intro2.tStartRefresh)
thisExp.addData('key_Intro2.stopped', key_Intro2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_Intro2.started', text_Intro2.tStartRefresh)
thisExp.addData('text_Intro2.stopped', text_Intro2.tStopRefresh)
# the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_OtherName = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Norming_Buffer.xlsx'),
    seed=None, name='trials_OtherName')
thisExp.addLoop(trials_OtherName)  # add the loop to the experiment
thisTrials_OtherName = trials_OtherName.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_OtherName.rgb)
if thisTrials_OtherName != None:
    for paramName in thisTrials_OtherName:
        exec('{} = thisTrials_OtherName[paramName]'.format(paramName))

for thisTrials_OtherName in trials_OtherName:
    currentLoop = trials_OtherName
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_OtherName.rgb)
    if thisTrials_OtherName != None:
        for paramName in thisTrials_OtherName:
            exec('{} = thisTrials_OtherName[paramName]'.format(paramName))
    
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
    trials_OtherName.addData('text_Blank500.started', text_Blank500.tStartRefresh)
    trials_OtherName.addData('text_Blank500.stopped', text_Blank500.tStopRefresh)
    
    # ------Prepare to start Routine "OtherName"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_Buffer.setText(Name)
    slider_Buffer.reset()
    # keep track of which components have finished
    OtherNameComponents = [text_Buffer, slider_Buffer]
    for thisComponent in OtherNameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    OtherNameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "OtherName"-------
    while continueRoutine:
        # get current time
        t = OtherNameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=OtherNameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Buffer* updates
        if text_Buffer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Buffer.frameNStart = frameN  # exact frame index
            text_Buffer.tStart = t  # local t and not account for scr refresh
            text_Buffer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Buffer, 'tStartRefresh')  # time at next scr refresh
            text_Buffer.setAutoDraw(True)
        
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
        for thisComponent in OtherNameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "OtherName"-------
    for thisComponent in OtherNameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_OtherName.addData('text_Buffer.started', text_Buffer.tStartRefresh)
    trials_OtherName.addData('text_Buffer.stopped', text_Buffer.tStopRefresh)
    trials_OtherName.addData('slider_Buffer.response', slider_Buffer.getRating())
    trials_OtherName.addData('slider_Buffer.rt', slider_Buffer.getRT())
    trials_OtherName.addData('slider_Buffer.started', slider_Buffer.tStartRefresh)
    trials_OtherName.addData('slider_Buffer.stopped', slider_Buffer.tStopRefresh)
    # the Routine "OtherName" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_OtherName'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Norming_CommonNames_Filtered.xlsx'),
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
    text_Trial.setText(Name)
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

# ------Prepare to start Routine "biologicalSex"-------
continueRoutine = True
# update component parameters for each repeat
text_biologicalSex.setText('Was ist dein biologisches Geschlecht?\n\n(Drücke die Leertaste um fortzufahren.)')
slider_biologicalSex.reset()
key_biologicalSex.keys = []
key_biologicalSex.rt = []
_key_biologicalSex_allKeys = []
# keep track of which components have finished
biologicalSexComponents = [text_biologicalSex, slider_biologicalSex, key_biologicalSex]
for thisComponent in biologicalSexComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
biologicalSexClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "biologicalSex"-------
while continueRoutine:
    # get current time
    t = biologicalSexClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=biologicalSexClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_biologicalSex* updates
    if text_biologicalSex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_biologicalSex.frameNStart = frameN  # exact frame index
        text_biologicalSex.tStart = t  # local t and not account for scr refresh
        text_biologicalSex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_biologicalSex, 'tStartRefresh')  # time at next scr refresh
        text_biologicalSex.setAutoDraw(True)
    
    # *slider_biologicalSex* updates
    if slider_biologicalSex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_biologicalSex.frameNStart = frameN  # exact frame index
        slider_biologicalSex.tStart = t  # local t and not account for scr refresh
        slider_biologicalSex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_biologicalSex, 'tStartRefresh')  # time at next scr refresh
        slider_biologicalSex.setAutoDraw(True)
    
    # *key_biologicalSex* updates
    waitOnFlip = False
    if key_biologicalSex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_biologicalSex.frameNStart = frameN  # exact frame index
        key_biologicalSex.tStart = t  # local t and not account for scr refresh
        key_biologicalSex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_biologicalSex, 'tStartRefresh')  # time at next scr refresh
        key_biologicalSex.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_biologicalSex.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_biologicalSex.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_biologicalSex.status == STARTED and not waitOnFlip:
        theseKeys = key_biologicalSex.getKeys(keyList=['space'], waitRelease=False)
        _key_biologicalSex_allKeys.extend(theseKeys)
        if len(_key_biologicalSex_allKeys):
            key_biologicalSex.keys = _key_biologicalSex_allKeys[-1].name  # just the last key pressed
            key_biologicalSex.rt = _key_biologicalSex_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in biologicalSexComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "biologicalSex"-------
for thisComponent in biologicalSexComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_biologicalSex.started', text_biologicalSex.tStartRefresh)
thisExp.addData('text_biologicalSex.stopped', text_biologicalSex.tStopRefresh)
thisExp.addData('slider_biologicalSex.response', slider_biologicalSex.getRating())
thisExp.addData('slider_biologicalSex.rt', slider_biologicalSex.getRT())
thisExp.addData('slider_biologicalSex.started', slider_biologicalSex.tStartRefresh)
thisExp.addData('slider_biologicalSex.stopped', slider_biologicalSex.tStopRefresh)
# check responses
if key_biologicalSex.keys in ['', [], None]:  # No response was made
    key_biologicalSex.keys = None
thisExp.addData('key_biologicalSex.keys',key_biologicalSex.keys)
if key_biologicalSex.keys != None:  # we had a response
    thisExp.addData('key_biologicalSex.rt', key_biologicalSex.rt)
thisExp.addData('key_biologicalSex.started', key_biologicalSex.tStartRefresh)
thisExp.addData('key_biologicalSex.stopped', key_biologicalSex.tStopRefresh)
thisExp.nextEntry()
# the Routine "biologicalSex" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "GenderIdentity"-------
continueRoutine = True
# update component parameters for each repeat
text_GenderIdentity.setText('Wie würdest du deine Geschlechtsidentität zuordnen?\n\nFalls du dies nicht beantworten möchtest, drücke die Leertaste ohne Auswahl um zu beenden.')
slider.reset()
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
GenderIdentityComponents = [text_GenderIdentity, slider, key_resp]
for thisComponent in GenderIdentityComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GenderIdentityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GenderIdentity"-------
while continueRoutine:
    # get current time
    t = GenderIdentityClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GenderIdentityClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_GenderIdentity* updates
    if text_GenderIdentity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_GenderIdentity.frameNStart = frameN  # exact frame index
        text_GenderIdentity.tStart = t  # local t and not account for scr refresh
        text_GenderIdentity.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_GenderIdentity, 'tStartRefresh')  # time at next scr refresh
        text_GenderIdentity.setAutoDraw(True)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
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
    for thisComponent in GenderIdentityComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GenderIdentity"-------
for thisComponent in GenderIdentityComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_GenderIdentity.started', text_GenderIdentity.tStartRefresh)
thisExp.addData('text_GenderIdentity.stopped', text_GenderIdentity.tStopRefresh)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('slider.started', slider.tStartRefresh)
thisExp.addData('slider.stopped', slider.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "GenderIdentity" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "GoodbyeScreen"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
text_GoodbyeScreen.setText('Vielen Dank, dass Du an meinem Experiment teilgenommen hast.')
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
