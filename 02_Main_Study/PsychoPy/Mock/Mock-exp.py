#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mai 04, 2022, at 18:19
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
expName = 'Mock-exp'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\alexa\\Documents\\02_study\\duesseldorf\\BA_Linguistik\\09_BBA_Bachelorarbeit\\02_daten\\02_Main_Study\\PsychoPy\\Mock-exp.py',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_key_resp = keyboard.Keyboard()

# Initialize components for Routine "comp_q"
comp_qClock = core.Clock()
comp_q_text = visual.TextStim(win=win, name='comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
comp_p_key_resp = keyboard.Keyboard()

# Initialize components for Routine "resp"
respClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mock.xlsx'),
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial_text.setText(Name)
    trial_key_resp.keys = []
    trial_key_resp.rt = []
    _trial_key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trial_text, trial_key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_text* updates
        if trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_text.frameNStart = frameN  # exact frame index
            trial_text.tStart = t  # local t and not account for scr refresh
            trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
            trial_text.setAutoDraw(True)
        
        # *trial_key_resp* updates
        waitOnFlip = False
        if trial_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_key_resp.frameNStart = frameN  # exact frame index
            trial_key_resp.tStart = t  # local t and not account for scr refresh
            trial_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_key_resp, 'tStartRefresh')  # time at next scr refresh
            trial_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _trial_key_resp_allKeys.extend(theseKeys)
            if len(_trial_key_resp_allKeys):
                trial_key_resp.keys = _trial_key_resp_allKeys[-1].name  # just the last key pressed
                trial_key_resp.rt = _trial_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('trial_text.started', trial_text.tStartRefresh)
    trials.addData('trial_text.stopped', trial_text.tStopRefresh)
    # check responses
    if trial_key_resp.keys in ['', [], None]:  # No response was made
        trial_key_resp.keys = None
    trials.addData('trial_key_resp.keys',trial_key_resp.keys)
    if trial_key_resp.keys != None:  # we had a response
        trials.addData('trial_key_resp.rt', trial_key_resp.rt)
    trials.addData('trial_key_resp.started', trial_key_resp.tStartRefresh)
    trials.addData('trial_key_resp.stopped', trial_key_resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    comp_p_key_resp.keys = []
    comp_p_key_resp.rt = []
    _comp_p_key_resp_allKeys = []
    # keep track of which components have finished
    comp_qComponents = [comp_q_text, comp_p_key_resp]
    for thisComponent in comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "comp_q"-------
    while continueRoutine:
        # get current time
        t = comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *comp_q_text* updates
        if comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comp_q_text.frameNStart = frameN  # exact frame index
            comp_q_text.tStart = t  # local t and not account for scr refresh
            comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comp_q_text, 'tStartRefresh')  # time at next scr refresh
            comp_q_text.setAutoDraw(True)
        if comp_q_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > comp_q_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                comp_q_text.tStop = t  # not accounting for scr refresh
                comp_q_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(comp_q_text, 'tStopRefresh')  # time at next scr refresh
                comp_q_text.setAutoDraw(False)
        if comp_q_text.status == STARTED:  # only update if drawing
            comp_q_text.setText(Quest, log=False)
        
        # *comp_p_key_resp* updates
        waitOnFlip = False
        if comp_p_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comp_p_key_resp.frameNStart = frameN  # exact frame index
            comp_p_key_resp.tStart = t  # local t and not account for scr refresh
            comp_p_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comp_p_key_resp, 'tStartRefresh')  # time at next scr refresh
            comp_p_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(comp_p_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(comp_p_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if comp_p_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = comp_p_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _comp_p_key_resp_allKeys.extend(theseKeys)
            if len(_comp_p_key_resp_allKeys):
                comp_p_key_resp.keys = _comp_p_key_resp_allKeys[-1].name  # just the last key pressed
                comp_p_key_resp.rt = _comp_p_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "comp_q"-------
    for thisComponent in comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('comp_q_text.started', comp_q_text.tStartRefresh)
    trials.addData('comp_q_text.stopped', comp_q_text.tStopRefresh)
    # check responses
    if comp_p_key_resp.keys in ['', [], None]:  # No response was made
        comp_p_key_resp.keys = None
    trials.addData('comp_p_key_resp.keys',comp_p_key_resp.keys)
    if comp_p_key_resp.keys != None:  # we had a response
        trials.addData('comp_p_key_resp.rt', comp_p_key_resp.rt)
    trials.addData('comp_p_key_resp.started', comp_p_key_resp.tStartRefresh)
    trials.addData('comp_p_key_resp.stopped', comp_p_key_resp.tStopRefresh)
    # the Routine "comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    text.setText(Quest_Up)
    resp_key_resp.keys = []
    resp_key_resp.rt = []
    _resp_key_resp_allKeys = []
    # keep track of which components have finished
    respComponents = [text, resp_key_resp]
    for thisComponent in respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resp"-------
    while continueRoutine:
        # get current time
        t = respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *resp_key_resp* updates
        waitOnFlip = False
        if resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_key_resp.frameNStart = frameN  # exact frame index
            resp_key_resp.tStart = t  # local t and not account for scr refresh
            resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = resp_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _resp_key_resp_allKeys.extend(theseKeys)
            if len(_resp_key_resp_allKeys):
                resp_key_resp.keys = _resp_key_resp_allKeys[-1].name  # just the last key pressed
                resp_key_resp.rt = _resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resp"-------
    for thisComponent in respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if resp_key_resp.keys in ['', [], None]:  # No response was made
        resp_key_resp.keys = None
    trials.addData('resp_key_resp.keys',resp_key_resp.keys)
    if resp_key_resp.keys != None:  # we had a response
        trials.addData('resp_key_resp.rt', resp_key_resp.rt)
    trials.addData('resp_key_resp.started', resp_key_resp.tStartRefresh)
    trials.addData('resp_key_resp.stopped', resp_key_resp.tStopRefresh)
    # the Routine "resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
text_2.setText('goodbye')
# keep track of which components have finished
GoodbyeComponents = [text_2]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

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
