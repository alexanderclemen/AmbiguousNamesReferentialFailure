#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mai 07, 2022, at 10:40
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
expName = 'Main-Study-exp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Vorname': '', 'Nachname': '', 'Alter': '', 'Links- oder Rechtshänder': '', 'Zweitsprache (1 muttersprachlich - 10 geringe Kenntnisse)': '', '2. Zweitsprache (1 - 10)': '', '3. Zweitsprache (1 - 10)': '', '4. Zweitsprache (1 - 10)': '', '5. Zweitsprache (1 - 10)': ''}
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
    originPath='C:\\Users\\alexa\\Documents\\02_study\\duesseldorf\\BA_Linguistik\\09_BBA_Bachelorarbeit\\02_daten\\02_Main_Study\\PsychoPy\\list2\\Main-Study-exp-L2_lastrun.py',
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

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Explaination_Screen"
Explaination_ScreenClock = core.Clock()
Explaination_text = visual.TextStim(win=win, name='Explaination_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Explaination_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Comp_q"
Comp_qClock = core.Clock()
Comp_q_key_resp = keyboard.Keyboard()
Comp_q_text = visual.TextStim(win=win, name='Comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Explaination_Screen2"
Explaination_Screen2Clock = core.Clock()
Explaination2_text = visual.TextStim(win=win, name='Explaination2_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Explaination2_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Comp_q"
Comp_qClock = core.Clock()
Comp_q_key_resp = keyboard.Keyboard()
Comp_q_text = visual.TextStim(win=win, name='Comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
Pause1_text = visual.TextStim(win=win, name='Pause1_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pause1_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Comp_q"
Comp_qClock = core.Clock()
Comp_q_key_resp = keyboard.Keyboard()
Comp_q_text = visual.TextStim(win=win, name='Comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Pause2"
Pause2Clock = core.Clock()
Pause2_text = visual.TextStim(win=win, name='Pause2_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pause2_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Pause3"
Pause3Clock = core.Clock()
Pause3_text = visual.TextStim(win=win, name='Pause3_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pause3_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Comp_q"
Comp_qClock = core.Clock()
Comp_q_key_resp = keyboard.Keyboard()
Comp_q_text = visual.TextStim(win=win, name='Comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Pause4"
Pause4Clock = core.Clock()
Pause4_text = visual.TextStim(win=win, name='Pause4_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pause4_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Comp_q"
Comp_qClock = core.Clock()
Comp_q_key_resp = keyboard.Keyboard()
Comp_q_text = visual.TextStim(win=win, name='Comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Pause5"
Pause5Clock = core.Clock()
Pause5_text = visual.TextStim(win=win, name='Pause5_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pause5_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Pos01_Name"
Pos01_NameClock = core.Clock()
Pos01_Name_text = visual.TextStim(win=win, name='Pos01_Name_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos01_Name_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos02_V"
Pos02_VClock = core.Clock()
Pos02_V_text = visual.TextStim(win=win, name='Pos02_V_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos02_V_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos03_PP"
Pos03_PPClock = core.Clock()
Pos03_PP_text = visual.TextStim(win=win, name='Pos03_PP_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos03_PP_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos04_PRO"
Pos04_PROClock = core.Clock()
Pos04_PRO_text = visual.TextStim(win=win, name='Pos04_PRO_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos04_PRO_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos05_3"
Pos05_3Clock = core.Clock()
Pos05_text = visual.TextStim(win=win, name='Pos05_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos05_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos06_2"
Pos06_2Clock = core.Clock()
Pos06_text = visual.TextStim(win=win, name='Pos06_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos06_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos07_2"
Pos07_2Clock = core.Clock()
Pos07_text = visual.TextStim(win=win, name='Pos07_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos07_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos08_2"
Pos08_2Clock = core.Clock()
Pos08_text = visual.TextStim(win=win, name='Pos08_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos08_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pos09_2"
Pos09_2Clock = core.Clock()
Pos09_text = visual.TextStim(win=win, name='Pos09_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pos09_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Comp_q"
Comp_qClock = core.Clock()
Comp_q_key_resp = keyboard.Keyboard()
Comp_q_text = visual.TextStim(win=win, name='Comp_q_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Comp_resp"
Comp_respClock = core.Clock()
Comp_resp_key_resp = keyboard.Keyboard()
Comp_Up_resp_text = visual.TextStim(win=win, name='Comp_Up_resp_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Quest_Down_text = visual.TextStim(win=win, name='Quest_Down_text',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
Blank500_text = visual.TextStim(win=win, name='Blank500_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Goodbye_Screen"
Goodbye_ScreenClock = core.Clock()
Goodbye_text = visual.TextStim(win=win, name='Goodbye_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
Welcome_text.setText('Hallo und vielen Dank für deine Teilnahme.')
# keep track of which components have finished
Welcome_ScreenComponents = [Welcome_text]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        Welcome_text.setAutoDraw(True)
    if Welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Welcome_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Welcome_text.tStop = t  # not accounting for scr refresh
            Welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Welcome_text, 'tStopRefresh')  # time at next scr refresh
            Welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome_text.started', Welcome_text.tStartRefresh)
thisExp.addData('Welcome_text.stopped', Welcome_text.tStopRefresh)

# ------Prepare to start Routine "Explaination_Screen"-------
continueRoutine = True
# update component parameters for each repeat
Explaination_text.setText('Im folgenden wirst du je zwei Sätze Stück für Stück lesen. Du kommst immer mit der Lehrtaste zum nächten Satzstück.\n\nManchmal wirst du eine Frage mit zwei Antwortmöglichkeiten über die Sätze beantworten. Lies die Sätze also möglichst genau aber auch so schnell wie möglich. Es ist immer nur eine Antwortmöglichkeit korrekt. \n\nDie obere Pfeiltaste wählt die obere Antwort aus und die untere Pfeiltaste wählt die untere Antwortmöglichkeit aus.\n\nCa alle 3 bis 5 Minuten hast Du eine Pause. \n\nJetzt folgen fünf Beispiele an denen Du die Steuerung testen kannst. Drücke die Lehrtaste um weiter zu kommen.')
Explaination_key_resp.keys = []
Explaination_key_resp.rt = []
_Explaination_key_resp_allKeys = []
# keep track of which components have finished
Explaination_ScreenComponents = [Explaination_text, Explaination_key_resp]
for thisComponent in Explaination_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Explaination_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Explaination_Screen"-------
while continueRoutine:
    # get current time
    t = Explaination_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Explaination_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Explaination_text* updates
    if Explaination_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Explaination_text.frameNStart = frameN  # exact frame index
        Explaination_text.tStart = t  # local t and not account for scr refresh
        Explaination_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Explaination_text, 'tStartRefresh')  # time at next scr refresh
        Explaination_text.setAutoDraw(True)
    
    # *Explaination_key_resp* updates
    waitOnFlip = False
    if Explaination_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Explaination_key_resp.frameNStart = frameN  # exact frame index
        Explaination_key_resp.tStart = t  # local t and not account for scr refresh
        Explaination_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Explaination_key_resp, 'tStartRefresh')  # time at next scr refresh
        Explaination_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Explaination_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Explaination_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Explaination_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Explaination_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _Explaination_key_resp_allKeys.extend(theseKeys)
        if len(_Explaination_key_resp_allKeys):
            Explaination_key_resp.keys = _Explaination_key_resp_allKeys[-1].name  # just the last key pressed
            Explaination_key_resp.rt = _Explaination_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Explaination_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Explaination_Screen"-------
for thisComponent in Explaination_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Explaination_text.started', Explaination_text.tStartRefresh)
thisExp.addData('Explaination_text.stopped', Explaination_text.tStopRefresh)
# check responses
if Explaination_key_resp.keys in ['', [], None]:  # No response was made
    Explaination_key_resp.keys = None
thisExp.addData('Explaination_key_resp.keys',Explaination_key_resp.keys)
if Explaination_key_resp.keys != None:  # we had a response
    thisExp.addData('Explaination_key_resp.rt', Explaination_key_resp.rt)
thisExp.addData('Explaination_key_resp.started', Explaination_key_resp.tStartRefresh)
thisExp.addData('Explaination_key_resp.stopped', Explaination_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Explaination_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials00_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-Examples.xlsx', selection='0:4'),
    seed=None, name='trials00_Loop')
thisExp.addLoop(trials00_Loop)  # add the loop to the experiment
thisTrials00_Loop = trials00_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials00_Loop.rgb)
if thisTrials00_Loop != None:
    for paramName in thisTrials00_Loop:
        exec('{} = thisTrials00_Loop[paramName]'.format(paramName))

for thisTrials00_Loop in trials00_Loop:
    currentLoop = trials00_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials00_Loop.rgb)
    if thisTrials00_Loop != None:
        for paramName in thisTrials00_Loop:
            exec('{} = thisTrials00_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials00_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials00_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials00_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials00_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials00_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials00_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials00_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials00_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials00_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials00_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials00_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials00_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials00_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials00_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials00_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials00_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials00_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials00_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials00_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials00_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials00_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials00_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials00_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials00_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials00_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials00_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials00_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials00_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials00_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials00_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials00_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials00_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials00_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_q_key_resp.keys = []
    Comp_q_key_resp.rt = []
    _Comp_q_key_resp_allKeys = []
    Comp_q_text.setText(Quest_Presented)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_qComponents = [Comp_q_key_resp, Comp_q_text]
    for thisComponent in Comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_q"-------
    while continueRoutine:
        # get current time
        t = Comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_q_key_resp* updates
        waitOnFlip = False
        if Comp_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_key_resp.frameNStart = frameN  # exact frame index
            Comp_q_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_q_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_q_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_q_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_q_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Comp_q_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_q_key_resp_allKeys):
                Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_q_text* updates
        if Comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_text.frameNStart = frameN  # exact frame index
            Comp_q_text.tStart = t  # local t and not account for scr refresh
            Comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_text, 'tStartRefresh')  # time at next scr refresh
            Comp_q_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_q"-------
    for thisComponent in Comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_q_key_resp.keys in ['', [], None]:  # No response was made
        Comp_q_key_resp.keys = None
    trials00_Loop.addData('Comp_q_key_resp.keys',Comp_q_key_resp.keys)
    if Comp_q_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt)
    trials00_Loop.addData('Comp_q_key_resp.started', Comp_q_key_resp.tStartRefresh)
    trials00_Loop.addData('Comp_q_key_resp.stopped', Comp_q_key_resp.tStopRefresh)
    trials00_Loop.addData('Comp_q_text.started', Comp_q_text.tStartRefresh)
    trials00_Loop.addData('Comp_q_text.stopped', Comp_q_text.tStopRefresh)
    # the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials00_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials00_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials00_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials00_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials00_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials00_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials00_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials00_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials00_Loop'


# ------Prepare to start Routine "Explaination_Screen2"-------
continueRoutine = True
# update component parameters for each repeat
Explaination2_text.setText('Soweit alles startklar?\n\nBitte sorge für ein ruhiges Umfeld und stell dir wenn du magst ein Getränk parat.\n\nFalls du soweit bist, drücke die Lehrtaste um das Experiment zu starten.')
Explaination2_key_resp.keys = []
Explaination2_key_resp.rt = []
_Explaination2_key_resp_allKeys = []
# keep track of which components have finished
Explaination_Screen2Components = [Explaination2_text, Explaination2_key_resp]
for thisComponent in Explaination_Screen2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Explaination_Screen2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Explaination_Screen2"-------
while continueRoutine:
    # get current time
    t = Explaination_Screen2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Explaination_Screen2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Explaination2_text* updates
    if Explaination2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Explaination2_text.frameNStart = frameN  # exact frame index
        Explaination2_text.tStart = t  # local t and not account for scr refresh
        Explaination2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Explaination2_text, 'tStartRefresh')  # time at next scr refresh
        Explaination2_text.setAutoDraw(True)
    
    # *Explaination2_key_resp* updates
    waitOnFlip = False
    if Explaination2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Explaination2_key_resp.frameNStart = frameN  # exact frame index
        Explaination2_key_resp.tStart = t  # local t and not account for scr refresh
        Explaination2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Explaination2_key_resp, 'tStartRefresh')  # time at next scr refresh
        Explaination2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Explaination2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Explaination2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Explaination2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Explaination2_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _Explaination2_key_resp_allKeys.extend(theseKeys)
        if len(_Explaination2_key_resp_allKeys):
            Explaination2_key_resp.keys = _Explaination2_key_resp_allKeys[-1].name  # just the last key pressed
            Explaination2_key_resp.rt = _Explaination2_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Explaination_Screen2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Explaination_Screen2"-------
for thisComponent in Explaination_Screen2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Explaination2_text.started', Explaination2_text.tStartRefresh)
thisExp.addData('Explaination2_text.stopped', Explaination2_text.tStopRefresh)
# check responses
if Explaination2_key_resp.keys in ['', [], None]:  # No response was made
    Explaination2_key_resp.keys = None
thisExp.addData('Explaination2_key_resp.keys',Explaination2_key_resp.keys)
if Explaination2_key_resp.keys != None:  # we had a response
    thisExp.addData('Explaination2_key_resp.rt', Explaination2_key_resp.rt)
thisExp.addData('Explaination2_key_resp.started', Explaination2_key_resp.tStartRefresh)
thisExp.addData('Explaination2_key_resp.stopped', Explaination2_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Explaination_Screen2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials01_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-L2-B1.xlsx', selection='0:19'),
    seed=None, name='trials01_Loop')
thisExp.addLoop(trials01_Loop)  # add the loop to the experiment
thisTrials01_Loop = trials01_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials01_Loop.rgb)
if thisTrials01_Loop != None:
    for paramName in thisTrials01_Loop:
        exec('{} = thisTrials01_Loop[paramName]'.format(paramName))

for thisTrials01_Loop in trials01_Loop:
    currentLoop = trials01_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials01_Loop.rgb)
    if thisTrials01_Loop != None:
        for paramName in thisTrials01_Loop:
            exec('{} = thisTrials01_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials01_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials01_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials01_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials01_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials01_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials01_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials01_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials01_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials01_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials01_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials01_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials01_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials01_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials01_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials01_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials01_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials01_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials01_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials01_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials01_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials01_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials01_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials01_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials01_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials01_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials01_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials01_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials01_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials01_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials01_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials01_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials01_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials01_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_q_key_resp.keys = []
    Comp_q_key_resp.rt = []
    _Comp_q_key_resp_allKeys = []
    Comp_q_text.setText(Quest_Presented)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_qComponents = [Comp_q_key_resp, Comp_q_text]
    for thisComponent in Comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_q"-------
    while continueRoutine:
        # get current time
        t = Comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_q_key_resp* updates
        waitOnFlip = False
        if Comp_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_key_resp.frameNStart = frameN  # exact frame index
            Comp_q_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_q_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_q_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_q_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_q_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Comp_q_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_q_key_resp_allKeys):
                Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_q_text* updates
        if Comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_text.frameNStart = frameN  # exact frame index
            Comp_q_text.tStart = t  # local t and not account for scr refresh
            Comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_text, 'tStartRefresh')  # time at next scr refresh
            Comp_q_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_q"-------
    for thisComponent in Comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_q_key_resp.keys in ['', [], None]:  # No response was made
        Comp_q_key_resp.keys = None
    trials01_Loop.addData('Comp_q_key_resp.keys',Comp_q_key_resp.keys)
    if Comp_q_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt)
    trials01_Loop.addData('Comp_q_key_resp.started', Comp_q_key_resp.tStartRefresh)
    trials01_Loop.addData('Comp_q_key_resp.stopped', Comp_q_key_resp.tStopRefresh)
    trials01_Loop.addData('Comp_q_text.started', Comp_q_text.tStartRefresh)
    trials01_Loop.addData('Comp_q_text.stopped', Comp_q_text.tStopRefresh)
    # the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials01_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials01_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials01_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials01_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials01_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials01_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials01_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials01_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials01_Loop'


# ------Prepare to start Routine "Pause"-------
continueRoutine = True
# update component parameters for each repeat
Pause1_text.setText('Du hast 17% geschafft.\n\nWenn du möchtest kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.')
Pause1_key_resp.keys = []
Pause1_key_resp.rt = []
_Pause1_key_resp_allKeys = []
# keep track of which components have finished
PauseComponents = [Pause1_text, Pause1_key_resp]
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
    
    # *Pause1_text* updates
    if Pause1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause1_text.frameNStart = frameN  # exact frame index
        Pause1_text.tStart = t  # local t and not account for scr refresh
        Pause1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause1_text, 'tStartRefresh')  # time at next scr refresh
        Pause1_text.setAutoDraw(True)
    
    # *Pause1_key_resp* updates
    waitOnFlip = False
    if Pause1_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause1_key_resp.frameNStart = frameN  # exact frame index
        Pause1_key_resp.tStart = t  # local t and not account for scr refresh
        Pause1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause1_key_resp, 'tStartRefresh')  # time at next scr refresh
        Pause1_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Pause1_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Pause1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Pause1_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Pause1_key_resp.getKeys(keyList=['p'], waitRelease=False)
        _Pause1_key_resp_allKeys.extend(theseKeys)
        if len(_Pause1_key_resp_allKeys):
            Pause1_key_resp.keys = _Pause1_key_resp_allKeys[-1].name  # just the last key pressed
            Pause1_key_resp.rt = _Pause1_key_resp_allKeys[-1].rt
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
thisExp.addData('Pause1_text.started', Pause1_text.tStartRefresh)
thisExp.addData('Pause1_text.stopped', Pause1_text.tStopRefresh)
# check responses
if Pause1_key_resp.keys in ['', [], None]:  # No response was made
    Pause1_key_resp.keys = None
thisExp.addData('Pause1_key_resp.keys',Pause1_key_resp.keys)
if Pause1_key_resp.keys != None:  # we had a response
    thisExp.addData('Pause1_key_resp.rt', Pause1_key_resp.rt)
thisExp.addData('Pause1_key_resp.started', Pause1_key_resp.tStartRefresh)
thisExp.addData('Pause1_key_resp.stopped', Pause1_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials02_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-L2-B2.xlsx', selection='0:19'),
    seed=None, name='trials02_Loop')
thisExp.addLoop(trials02_Loop)  # add the loop to the experiment
thisTrials02_Loop = trials02_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials02_Loop.rgb)
if thisTrials02_Loop != None:
    for paramName in thisTrials02_Loop:
        exec('{} = thisTrials02_Loop[paramName]'.format(paramName))

for thisTrials02_Loop in trials02_Loop:
    currentLoop = trials02_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials02_Loop.rgb)
    if thisTrials02_Loop != None:
        for paramName in thisTrials02_Loop:
            exec('{} = thisTrials02_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials02_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials02_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials02_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials02_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials02_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials02_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials02_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials02_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials02_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials02_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials02_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials02_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials02_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials02_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials02_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials02_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials02_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials02_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials02_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials02_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials02_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials02_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials02_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials02_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials02_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials02_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials02_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials02_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials02_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials02_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials02_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials02_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials02_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_q_key_resp.keys = []
    Comp_q_key_resp.rt = []
    _Comp_q_key_resp_allKeys = []
    Comp_q_text.setText(Quest_Presented)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_qComponents = [Comp_q_key_resp, Comp_q_text]
    for thisComponent in Comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_q"-------
    while continueRoutine:
        # get current time
        t = Comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_q_key_resp* updates
        waitOnFlip = False
        if Comp_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_key_resp.frameNStart = frameN  # exact frame index
            Comp_q_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_q_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_q_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_q_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_q_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Comp_q_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_q_key_resp_allKeys):
                Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_q_text* updates
        if Comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_text.frameNStart = frameN  # exact frame index
            Comp_q_text.tStart = t  # local t and not account for scr refresh
            Comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_text, 'tStartRefresh')  # time at next scr refresh
            Comp_q_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_q"-------
    for thisComponent in Comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_q_key_resp.keys in ['', [], None]:  # No response was made
        Comp_q_key_resp.keys = None
    trials02_Loop.addData('Comp_q_key_resp.keys',Comp_q_key_resp.keys)
    if Comp_q_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt)
    trials02_Loop.addData('Comp_q_key_resp.started', Comp_q_key_resp.tStartRefresh)
    trials02_Loop.addData('Comp_q_key_resp.stopped', Comp_q_key_resp.tStopRefresh)
    trials02_Loop.addData('Comp_q_text.started', Comp_q_text.tStartRefresh)
    trials02_Loop.addData('Comp_q_text.stopped', Comp_q_text.tStopRefresh)
    # the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials02_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials02_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials02_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials02_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials02_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials02_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials02_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials02_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials02_Loop'


# ------Prepare to start Routine "Pause2"-------
continueRoutine = True
# update component parameters for each repeat
Pause2_text.setText('Du hast ein Drittel geschafft.\n\nWenn du möchtest, kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.')
Pause2_key_resp.keys = []
Pause2_key_resp.rt = []
_Pause2_key_resp_allKeys = []
# keep track of which components have finished
Pause2Components = [Pause2_text, Pause2_key_resp]
for thisComponent in Pause2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pause2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause2"-------
while continueRoutine:
    # get current time
    t = Pause2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pause2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause2_text* updates
    if Pause2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause2_text.frameNStart = frameN  # exact frame index
        Pause2_text.tStart = t  # local t and not account for scr refresh
        Pause2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause2_text, 'tStartRefresh')  # time at next scr refresh
        Pause2_text.setAutoDraw(True)
    
    # *Pause2_key_resp* updates
    waitOnFlip = False
    if Pause2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause2_key_resp.frameNStart = frameN  # exact frame index
        Pause2_key_resp.tStart = t  # local t and not account for scr refresh
        Pause2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause2_key_resp, 'tStartRefresh')  # time at next scr refresh
        Pause2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Pause2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Pause2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Pause2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Pause2_key_resp.getKeys(keyList=['p'], waitRelease=False)
        _Pause2_key_resp_allKeys.extend(theseKeys)
        if len(_Pause2_key_resp_allKeys):
            Pause2_key_resp.keys = _Pause2_key_resp_allKeys[-1].name  # just the last key pressed
            Pause2_key_resp.rt = _Pause2_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pause2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause2"-------
for thisComponent in Pause2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause2_text.started', Pause2_text.tStartRefresh)
thisExp.addData('Pause2_text.stopped', Pause2_text.tStopRefresh)
# check responses
if Pause2_key_resp.keys in ['', [], None]:  # No response was made
    Pause2_key_resp.keys = None
thisExp.addData('Pause2_key_resp.keys',Pause2_key_resp.keys)
if Pause2_key_resp.keys != None:  # we had a response
    thisExp.addData('Pause2_key_resp.rt', Pause2_key_resp.rt)
thisExp.addData('Pause2_key_resp.started', Pause2_key_resp.tStartRefresh)
thisExp.addData('Pause2_key_resp.stopped', Pause2_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials03_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-L2-B3.xlsx', selection='0:19'),
    seed=None, name='trials03_Loop')
thisExp.addLoop(trials03_Loop)  # add the loop to the experiment
thisTrials03_Loop = trials03_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials03_Loop.rgb)
if thisTrials03_Loop != None:
    for paramName in thisTrials03_Loop:
        exec('{} = thisTrials03_Loop[paramName]'.format(paramName))

for thisTrials03_Loop in trials03_Loop:
    currentLoop = trials03_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials03_Loop.rgb)
    if thisTrials03_Loop != None:
        for paramName in thisTrials03_Loop:
            exec('{} = thisTrials03_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials03_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials03_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials03_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials03_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials03_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials03_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials03_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials03_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials03_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials03_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials03_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials03_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials03_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials03_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials03_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials03_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials03_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials03_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials03_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials03_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials03_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials03_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials03_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials03_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials03_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials03_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials03_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials03_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials03_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials03_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials03_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials03_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials03_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials03_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials03_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials03_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials03_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials03_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials03_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials03_Loop'


# ------Prepare to start Routine "Pause3"-------
continueRoutine = True
# update component parameters for each repeat
Pause3_text.setText('Super! Du hast die Hälfte geschafft.\n\nWenn du möchtest, kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.')
Pause3_key_resp.keys = []
Pause3_key_resp.rt = []
_Pause3_key_resp_allKeys = []
# keep track of which components have finished
Pause3Components = [Pause3_text, Pause3_key_resp]
for thisComponent in Pause3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pause3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause3"-------
while continueRoutine:
    # get current time
    t = Pause3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pause3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause3_text* updates
    if Pause3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause3_text.frameNStart = frameN  # exact frame index
        Pause3_text.tStart = t  # local t and not account for scr refresh
        Pause3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause3_text, 'tStartRefresh')  # time at next scr refresh
        Pause3_text.setAutoDraw(True)
    
    # *Pause3_key_resp* updates
    waitOnFlip = False
    if Pause3_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause3_key_resp.frameNStart = frameN  # exact frame index
        Pause3_key_resp.tStart = t  # local t and not account for scr refresh
        Pause3_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause3_key_resp, 'tStartRefresh')  # time at next scr refresh
        Pause3_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Pause3_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Pause3_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Pause3_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Pause3_key_resp.getKeys(keyList=['p'], waitRelease=False)
        _Pause3_key_resp_allKeys.extend(theseKeys)
        if len(_Pause3_key_resp_allKeys):
            Pause3_key_resp.keys = _Pause3_key_resp_allKeys[-1].name  # just the last key pressed
            Pause3_key_resp.rt = _Pause3_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pause3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause3"-------
for thisComponent in Pause3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause3_text.started', Pause3_text.tStartRefresh)
thisExp.addData('Pause3_text.stopped', Pause3_text.tStopRefresh)
# check responses
if Pause3_key_resp.keys in ['', [], None]:  # No response was made
    Pause3_key_resp.keys = None
thisExp.addData('Pause3_key_resp.keys',Pause3_key_resp.keys)
if Pause3_key_resp.keys != None:  # we had a response
    thisExp.addData('Pause3_key_resp.rt', Pause3_key_resp.rt)
thisExp.addData('Pause3_key_resp.started', Pause3_key_resp.tStartRefresh)
thisExp.addData('Pause3_key_resp.stopped', Pause3_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials04_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-L2-B4.xlsx', selection='0:19'),
    seed=None, name='trials04_Loop')
thisExp.addLoop(trials04_Loop)  # add the loop to the experiment
thisTrials04_Loop = trials04_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials04_Loop.rgb)
if thisTrials04_Loop != None:
    for paramName in thisTrials04_Loop:
        exec('{} = thisTrials04_Loop[paramName]'.format(paramName))

for thisTrials04_Loop in trials04_Loop:
    currentLoop = trials04_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials04_Loop.rgb)
    if thisTrials04_Loop != None:
        for paramName in thisTrials04_Loop:
            exec('{} = thisTrials04_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials04_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials04_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials04_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials04_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials04_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials04_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials04_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials04_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials04_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials04_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials04_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials04_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials04_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials04_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials04_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials04_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials04_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials04_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials04_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials04_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials04_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials04_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials04_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials04_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials04_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials04_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials04_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials04_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials04_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials04_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials04_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials04_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials04_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_q_key_resp.keys = []
    Comp_q_key_resp.rt = []
    _Comp_q_key_resp_allKeys = []
    Comp_q_text.setText(Quest_Presented)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_qComponents = [Comp_q_key_resp, Comp_q_text]
    for thisComponent in Comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_q"-------
    while continueRoutine:
        # get current time
        t = Comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_q_key_resp* updates
        waitOnFlip = False
        if Comp_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_key_resp.frameNStart = frameN  # exact frame index
            Comp_q_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_q_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_q_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_q_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_q_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Comp_q_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_q_key_resp_allKeys):
                Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_q_text* updates
        if Comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_text.frameNStart = frameN  # exact frame index
            Comp_q_text.tStart = t  # local t and not account for scr refresh
            Comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_text, 'tStartRefresh')  # time at next scr refresh
            Comp_q_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_q"-------
    for thisComponent in Comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_q_key_resp.keys in ['', [], None]:  # No response was made
        Comp_q_key_resp.keys = None
    trials04_Loop.addData('Comp_q_key_resp.keys',Comp_q_key_resp.keys)
    if Comp_q_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt)
    trials04_Loop.addData('Comp_q_key_resp.started', Comp_q_key_resp.tStartRefresh)
    trials04_Loop.addData('Comp_q_key_resp.stopped', Comp_q_key_resp.tStopRefresh)
    trials04_Loop.addData('Comp_q_text.started', Comp_q_text.tStartRefresh)
    trials04_Loop.addData('Comp_q_text.stopped', Comp_q_text.tStopRefresh)
    # the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials04_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials04_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials04_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials04_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials04_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials04_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials04_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials04_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials04_Loop'


# ------Prepare to start Routine "Pause4"-------
continueRoutine = True
# update component parameters for each repeat
Pause4_text.setText('Du hast zwei Drittel  geschafft.\n\nWenn du möchtest, kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.')
Pause4_key_resp.keys = []
Pause4_key_resp.rt = []
_Pause4_key_resp_allKeys = []
# keep track of which components have finished
Pause4Components = [Pause4_text, Pause4_key_resp]
for thisComponent in Pause4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pause4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause4"-------
while continueRoutine:
    # get current time
    t = Pause4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pause4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause4_text* updates
    if Pause4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause4_text.frameNStart = frameN  # exact frame index
        Pause4_text.tStart = t  # local t and not account for scr refresh
        Pause4_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause4_text, 'tStartRefresh')  # time at next scr refresh
        Pause4_text.setAutoDraw(True)
    
    # *Pause4_key_resp* updates
    waitOnFlip = False
    if Pause4_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause4_key_resp.frameNStart = frameN  # exact frame index
        Pause4_key_resp.tStart = t  # local t and not account for scr refresh
        Pause4_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause4_key_resp, 'tStartRefresh')  # time at next scr refresh
        Pause4_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Pause4_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Pause4_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Pause4_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Pause4_key_resp.getKeys(keyList=['p'], waitRelease=False)
        _Pause4_key_resp_allKeys.extend(theseKeys)
        if len(_Pause4_key_resp_allKeys):
            Pause4_key_resp.keys = _Pause4_key_resp_allKeys[-1].name  # just the last key pressed
            Pause4_key_resp.rt = _Pause4_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pause4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause4"-------
for thisComponent in Pause4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause4_text.started', Pause4_text.tStartRefresh)
thisExp.addData('Pause4_text.stopped', Pause4_text.tStopRefresh)
# check responses
if Pause4_key_resp.keys in ['', [], None]:  # No response was made
    Pause4_key_resp.keys = None
thisExp.addData('Pause4_key_resp.keys',Pause4_key_resp.keys)
if Pause4_key_resp.keys != None:  # we had a response
    thisExp.addData('Pause4_key_resp.rt', Pause4_key_resp.rt)
thisExp.addData('Pause4_key_resp.started', Pause4_key_resp.tStartRefresh)
thisExp.addData('Pause4_key_resp.stopped', Pause4_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials05_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-L2-B5.xlsx', selection='0:19'),
    seed=None, name='trials05_Loop')
thisExp.addLoop(trials05_Loop)  # add the loop to the experiment
thisTrials05_Loop = trials05_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials05_Loop.rgb)
if thisTrials05_Loop != None:
    for paramName in thisTrials05_Loop:
        exec('{} = thisTrials05_Loop[paramName]'.format(paramName))

for thisTrials05_Loop in trials05_Loop:
    currentLoop = trials05_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials05_Loop.rgb)
    if thisTrials05_Loop != None:
        for paramName in thisTrials05_Loop:
            exec('{} = thisTrials05_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials05_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials05_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials05_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials05_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials05_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials05_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials05_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials05_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials05_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials05_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials05_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials05_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials05_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials05_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials05_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials05_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials05_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials05_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials05_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials05_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials05_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials05_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials05_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials05_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials05_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials05_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials05_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials05_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials05_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials05_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials05_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials05_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials05_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_q_key_resp.keys = []
    Comp_q_key_resp.rt = []
    _Comp_q_key_resp_allKeys = []
    Comp_q_text.setText(Quest_Presented)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_qComponents = [Comp_q_key_resp, Comp_q_text]
    for thisComponent in Comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_q"-------
    while continueRoutine:
        # get current time
        t = Comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_q_key_resp* updates
        waitOnFlip = False
        if Comp_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_key_resp.frameNStart = frameN  # exact frame index
            Comp_q_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_q_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_q_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_q_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_q_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Comp_q_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_q_key_resp_allKeys):
                Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_q_text* updates
        if Comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_text.frameNStart = frameN  # exact frame index
            Comp_q_text.tStart = t  # local t and not account for scr refresh
            Comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_text, 'tStartRefresh')  # time at next scr refresh
            Comp_q_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_q"-------
    for thisComponent in Comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_q_key_resp.keys in ['', [], None]:  # No response was made
        Comp_q_key_resp.keys = None
    trials05_Loop.addData('Comp_q_key_resp.keys',Comp_q_key_resp.keys)
    if Comp_q_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt)
    trials05_Loop.addData('Comp_q_key_resp.started', Comp_q_key_resp.tStartRefresh)
    trials05_Loop.addData('Comp_q_key_resp.stopped', Comp_q_key_resp.tStopRefresh)
    trials05_Loop.addData('Comp_q_text.started', Comp_q_text.tStartRefresh)
    trials05_Loop.addData('Comp_q_text.stopped', Comp_q_text.tStopRefresh)
    # the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials05_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials05_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials05_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials05_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials05_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials05_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials05_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials05_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials05_Loop'


# ------Prepare to start Routine "Pause5"-------
continueRoutine = True
# update component parameters for each repeat
Pause5_text.setText('Das ist die letzte Pause.\n\nDu hast es fast geschafft.\n\nDrücke "P" um fortzufahren.')
Pause5_key_resp.keys = []
Pause5_key_resp.rt = []
_Pause5_key_resp_allKeys = []
# keep track of which components have finished
Pause5Components = [Pause5_text, Pause5_key_resp]
for thisComponent in Pause5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pause5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause5"-------
while continueRoutine:
    # get current time
    t = Pause5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pause5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause5_text* updates
    if Pause5_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause5_text.frameNStart = frameN  # exact frame index
        Pause5_text.tStart = t  # local t and not account for scr refresh
        Pause5_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause5_text, 'tStartRefresh')  # time at next scr refresh
        Pause5_text.setAutoDraw(True)
    
    # *Pause5_key_resp* updates
    waitOnFlip = False
    if Pause5_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause5_key_resp.frameNStart = frameN  # exact frame index
        Pause5_key_resp.tStart = t  # local t and not account for scr refresh
        Pause5_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause5_key_resp, 'tStartRefresh')  # time at next scr refresh
        Pause5_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Pause5_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Pause5_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Pause5_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Pause5_key_resp.getKeys(keyList=['p'], waitRelease=False)
        _Pause5_key_resp_allKeys.extend(theseKeys)
        if len(_Pause5_key_resp_allKeys):
            Pause5_key_resp.keys = _Pause5_key_resp_allKeys[-1].name  # just the last key pressed
            Pause5_key_resp.rt = _Pause5_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pause5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause5"-------
for thisComponent in Pause5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause5_text.started', Pause5_text.tStartRefresh)
thisExp.addData('Pause5_text.stopped', Pause5_text.tStopRefresh)
# check responses
if Pause5_key_resp.keys in ['', [], None]:  # No response was made
    Pause5_key_resp.keys = None
thisExp.addData('Pause5_key_resp.keys',Pause5_key_resp.keys)
if Pause5_key_resp.keys != None:  # we had a response
    thisExp.addData('Pause5_key_resp.rt', Pause5_key_resp.rt)
thisExp.addData('Pause5_key_resp.started', Pause5_key_resp.tStartRefresh)
thisExp.addData('Pause5_key_resp.stopped', Pause5_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials06_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main-Study-stimuli-L2-B6.xlsx', selection='0:19'),
    seed=None, name='trials06_Loop')
thisExp.addLoop(trials06_Loop)  # add the loop to the experiment
thisTrials06_Loop = trials06_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials06_Loop.rgb)
if thisTrials06_Loop != None:
    for paramName in thisTrials06_Loop:
        exec('{} = thisTrials06_Loop[paramName]'.format(paramName))

for thisTrials06_Loop in trials06_Loop:
    currentLoop = trials06_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials06_Loop.rgb)
    if thisTrials06_Loop != None:
        for paramName in thisTrials06_Loop:
            exec('{} = thisTrials06_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials06_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials06_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Pos01_Name"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos01_Name_text.setText(Name)
    Pos01_Name_key_resp.keys = []
    Pos01_Name_key_resp.rt = []
    _Pos01_Name_key_resp_allKeys = []
    # keep track of which components have finished
    Pos01_NameComponents = [Pos01_Name_text, Pos01_Name_key_resp]
    for thisComponent in Pos01_NameComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos01_NameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos01_Name"-------
    while continueRoutine:
        # get current time
        t = Pos01_NameClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos01_NameClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos01_Name_text* updates
        if Pos01_Name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_text.frameNStart = frameN  # exact frame index
            Pos01_Name_text.tStart = t  # local t and not account for scr refresh
            Pos01_Name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_text, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_text.setAutoDraw(True)
        
        # *Pos01_Name_key_resp* updates
        waitOnFlip = False
        if Pos01_Name_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos01_Name_key_resp.frameNStart = frameN  # exact frame index
            Pos01_Name_key_resp.tStart = t  # local t and not account for scr refresh
            Pos01_Name_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos01_Name_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos01_Name_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos01_Name_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos01_Name_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos01_Name_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos01_Name_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos01_Name_key_resp_allKeys.extend(theseKeys)
            if len(_Pos01_Name_key_resp_allKeys):
                Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[-1].name  # just the last key pressed
                Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos01_NameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos01_Name"-------
    for thisComponent in Pos01_NameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos01_Name_text.started', Pos01_Name_text.tStartRefresh)
    trials06_Loop.addData('Pos01_Name_text.stopped', Pos01_Name_text.tStopRefresh)
    # check responses
    if Pos01_Name_key_resp.keys in ['', [], None]:  # No response was made
        Pos01_Name_key_resp.keys = None
    trials06_Loop.addData('Pos01_Name_key_resp.keys',Pos01_Name_key_resp.keys)
    if Pos01_Name_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt)
    trials06_Loop.addData('Pos01_Name_key_resp.started', Pos01_Name_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos01_Name_key_resp.stopped', Pos01_Name_key_resp.tStopRefresh)
    # the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos02_V"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos02_V_text.setText(V)
    Pos02_V_key_resp.keys = []
    Pos02_V_key_resp.rt = []
    _Pos02_V_key_resp_allKeys = []
    # keep track of which components have finished
    Pos02_VComponents = [Pos02_V_text, Pos02_V_key_resp]
    for thisComponent in Pos02_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos02_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos02_V"-------
    while continueRoutine:
        # get current time
        t = Pos02_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos02_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos02_V_text* updates
        if Pos02_V_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_text.frameNStart = frameN  # exact frame index
            Pos02_V_text.tStart = t  # local t and not account for scr refresh
            Pos02_V_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_text, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_text.setAutoDraw(True)
        
        # *Pos02_V_key_resp* updates
        waitOnFlip = False
        if Pos02_V_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos02_V_key_resp.frameNStart = frameN  # exact frame index
            Pos02_V_key_resp.tStart = t  # local t and not account for scr refresh
            Pos02_V_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos02_V_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos02_V_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos02_V_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos02_V_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos02_V_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos02_V_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos02_V_key_resp_allKeys.extend(theseKeys)
            if len(_Pos02_V_key_resp_allKeys):
                Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[-1].name  # just the last key pressed
                Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos02_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos02_V"-------
    for thisComponent in Pos02_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos02_V_text.started', Pos02_V_text.tStartRefresh)
    trials06_Loop.addData('Pos02_V_text.stopped', Pos02_V_text.tStopRefresh)
    # check responses
    if Pos02_V_key_resp.keys in ['', [], None]:  # No response was made
        Pos02_V_key_resp.keys = None
    trials06_Loop.addData('Pos02_V_key_resp.keys',Pos02_V_key_resp.keys)
    if Pos02_V_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt)
    trials06_Loop.addData('Pos02_V_key_resp.started', Pos02_V_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos02_V_key_resp.stopped', Pos02_V_key_resp.tStopRefresh)
    # the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos03_PP"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt)
    Pos03_PP_key_resp.keys = []
    Pos03_PP_key_resp.rt = []
    _Pos03_PP_key_resp_allKeys = []
    # keep track of which components have finished
    Pos03_PPComponents = [Pos03_PP_text, Pos03_PP_key_resp]
    for thisComponent in Pos03_PPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos03_PPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos03_PP"-------
    while continueRoutine:
        # get current time
        t = Pos03_PPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos03_PPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos03_PP_text* updates
        if Pos03_PP_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_text.frameNStart = frameN  # exact frame index
            Pos03_PP_text.tStart = t  # local t and not account for scr refresh
            Pos03_PP_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_text, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_text.setAutoDraw(True)
        
        # *Pos03_PP_key_resp* updates
        waitOnFlip = False
        if Pos03_PP_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos03_PP_key_resp.frameNStart = frameN  # exact frame index
            Pos03_PP_key_resp.tStart = t  # local t and not account for scr refresh
            Pos03_PP_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos03_PP_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos03_PP_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos03_PP_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos03_PP_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos03_PP_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos03_PP_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos03_PP_key_resp_allKeys.extend(theseKeys)
            if len(_Pos03_PP_key_resp_allKeys):
                Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[-1].name  # just the last key pressed
                Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos03_PPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos03_PP"-------
    for thisComponent in Pos03_PPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos03_PP_text.started', Pos03_PP_text.tStartRefresh)
    trials06_Loop.addData('Pos03_PP_text.stopped', Pos03_PP_text.tStopRefresh)
    # check responses
    if Pos03_PP_key_resp.keys in ['', [], None]:  # No response was made
        Pos03_PP_key_resp.keys = None
    trials06_Loop.addData('Pos03_PP_key_resp.keys',Pos03_PP_key_resp.keys)
    if Pos03_PP_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt)
    trials06_Loop.addData('Pos03_PP_key_resp.started', Pos03_PP_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos03_PP_key_resp.stopped', Pos03_PP_key_resp.tStopRefresh)
    # the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos04_PRO"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos04_PRO_text.setText(PRO)
    Pos04_PRO_key_resp.keys = []
    Pos04_PRO_key_resp.rt = []
    _Pos04_PRO_key_resp_allKeys = []
    # keep track of which components have finished
    Pos04_PROComponents = [Pos04_PRO_text, Pos04_PRO_key_resp]
    for thisComponent in Pos04_PROComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos04_PROClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos04_PRO"-------
    while continueRoutine:
        # get current time
        t = Pos04_PROClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos04_PROClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos04_PRO_text* updates
        if Pos04_PRO_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_text.frameNStart = frameN  # exact frame index
            Pos04_PRO_text.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_text, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_text.setAutoDraw(True)
        
        # *Pos04_PRO_key_resp* updates
        waitOnFlip = False
        if Pos04_PRO_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos04_PRO_key_resp.frameNStart = frameN  # exact frame index
            Pos04_PRO_key_resp.tStart = t  # local t and not account for scr refresh
            Pos04_PRO_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos04_PRO_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos04_PRO_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos04_PRO_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos04_PRO_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos04_PRO_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos04_PRO_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos04_PRO_key_resp_allKeys.extend(theseKeys)
            if len(_Pos04_PRO_key_resp_allKeys):
                Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[-1].name  # just the last key pressed
                Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos04_PROComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos04_PRO"-------
    for thisComponent in Pos04_PROComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos04_PRO_text.started', Pos04_PRO_text.tStartRefresh)
    trials06_Loop.addData('Pos04_PRO_text.stopped', Pos04_PRO_text.tStopRefresh)
    # check responses
    if Pos04_PRO_key_resp.keys in ['', [], None]:  # No response was made
        Pos04_PRO_key_resp.keys = None
    trials06_Loop.addData('Pos04_PRO_key_resp.keys',Pos04_PRO_key_resp.keys)
    if Pos04_PRO_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt)
    trials06_Loop.addData('Pos04_PRO_key_resp.started', Pos04_PRO_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos04_PRO_key_resp.stopped', Pos04_PRO_key_resp.tStopRefresh)
    # the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos05_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos05_text.setText(Pos05)
    Pos05_key_resp.keys = []
    Pos05_key_resp.rt = []
    _Pos05_key_resp_allKeys = []
    # keep track of which components have finished
    Pos05_3Components = [Pos05_text, Pos05_key_resp]
    for thisComponent in Pos05_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos05_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos05_3"-------
    while continueRoutine:
        # get current time
        t = Pos05_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos05_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos05_text* updates
        if Pos05_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_text.frameNStart = frameN  # exact frame index
            Pos05_text.tStart = t  # local t and not account for scr refresh
            Pos05_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_text, 'tStartRefresh')  # time at next scr refresh
            Pos05_text.setAutoDraw(True)
        
        # *Pos05_key_resp* updates
        waitOnFlip = False
        if Pos05_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos05_key_resp.frameNStart = frameN  # exact frame index
            Pos05_key_resp.tStart = t  # local t and not account for scr refresh
            Pos05_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos05_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos05_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos05_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos05_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos05_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos05_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos05_key_resp_allKeys.extend(theseKeys)
            if len(_Pos05_key_resp_allKeys):
                Pos05_key_resp.keys = _Pos05_key_resp_allKeys[-1].name  # just the last key pressed
                Pos05_key_resp.rt = _Pos05_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos05_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos05_3"-------
    for thisComponent in Pos05_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos05_text.started', Pos05_text.tStartRefresh)
    trials06_Loop.addData('Pos05_text.stopped', Pos05_text.tStopRefresh)
    # check responses
    if Pos05_key_resp.keys in ['', [], None]:  # No response was made
        Pos05_key_resp.keys = None
    trials06_Loop.addData('Pos05_key_resp.keys',Pos05_key_resp.keys)
    if Pos05_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos05_key_resp.rt', Pos05_key_resp.rt)
    trials06_Loop.addData('Pos05_key_resp.started', Pos05_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos05_key_resp.stopped', Pos05_key_resp.tStopRefresh)
    # the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos06_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos06_text.setText(Pos06)
    Pos06_key_resp.keys = []
    Pos06_key_resp.rt = []
    _Pos06_key_resp_allKeys = []
    # keep track of which components have finished
    Pos06_2Components = [Pos06_text, Pos06_key_resp]
    for thisComponent in Pos06_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos06_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos06_2"-------
    while continueRoutine:
        # get current time
        t = Pos06_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos06_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos06_text* updates
        if Pos06_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_text.frameNStart = frameN  # exact frame index
            Pos06_text.tStart = t  # local t and not account for scr refresh
            Pos06_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_text, 'tStartRefresh')  # time at next scr refresh
            Pos06_text.setAutoDraw(True)
        
        # *Pos06_key_resp* updates
        waitOnFlip = False
        if Pos06_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos06_key_resp.frameNStart = frameN  # exact frame index
            Pos06_key_resp.tStart = t  # local t and not account for scr refresh
            Pos06_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos06_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos06_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos06_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos06_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos06_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos06_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos06_key_resp_allKeys.extend(theseKeys)
            if len(_Pos06_key_resp_allKeys):
                Pos06_key_resp.keys = _Pos06_key_resp_allKeys[-1].name  # just the last key pressed
                Pos06_key_resp.rt = _Pos06_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos06_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos06_2"-------
    for thisComponent in Pos06_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos06_text.started', Pos06_text.tStartRefresh)
    trials06_Loop.addData('Pos06_text.stopped', Pos06_text.tStopRefresh)
    # check responses
    if Pos06_key_resp.keys in ['', [], None]:  # No response was made
        Pos06_key_resp.keys = None
    trials06_Loop.addData('Pos06_key_resp.keys',Pos06_key_resp.keys)
    if Pos06_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos06_key_resp.rt', Pos06_key_resp.rt)
    trials06_Loop.addData('Pos06_key_resp.started', Pos06_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos06_key_resp.stopped', Pos06_key_resp.tStopRefresh)
    # the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos07_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos07_text.setText(Pos07)
    Pos07_key_resp.keys = []
    Pos07_key_resp.rt = []
    _Pos07_key_resp_allKeys = []
    # keep track of which components have finished
    Pos07_2Components = [Pos07_text, Pos07_key_resp]
    for thisComponent in Pos07_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos07_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos07_2"-------
    while continueRoutine:
        # get current time
        t = Pos07_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos07_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos07_text* updates
        if Pos07_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_text.frameNStart = frameN  # exact frame index
            Pos07_text.tStart = t  # local t and not account for scr refresh
            Pos07_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_text, 'tStartRefresh')  # time at next scr refresh
            Pos07_text.setAutoDraw(True)
        
        # *Pos07_key_resp* updates
        waitOnFlip = False
        if Pos07_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos07_key_resp.frameNStart = frameN  # exact frame index
            Pos07_key_resp.tStart = t  # local t and not account for scr refresh
            Pos07_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos07_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos07_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos07_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos07_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos07_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos07_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos07_key_resp_allKeys.extend(theseKeys)
            if len(_Pos07_key_resp_allKeys):
                Pos07_key_resp.keys = _Pos07_key_resp_allKeys[-1].name  # just the last key pressed
                Pos07_key_resp.rt = _Pos07_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos07_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos07_2"-------
    for thisComponent in Pos07_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos07_text.started', Pos07_text.tStartRefresh)
    trials06_Loop.addData('Pos07_text.stopped', Pos07_text.tStopRefresh)
    # check responses
    if Pos07_key_resp.keys in ['', [], None]:  # No response was made
        Pos07_key_resp.keys = None
    trials06_Loop.addData('Pos07_key_resp.keys',Pos07_key_resp.keys)
    if Pos07_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos07_key_resp.rt', Pos07_key_resp.rt)
    trials06_Loop.addData('Pos07_key_resp.started', Pos07_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos07_key_resp.stopped', Pos07_key_resp.tStopRefresh)
    # the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos08_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos08_text.setText(Pos08)
    Pos08_key_resp.keys = []
    Pos08_key_resp.rt = []
    _Pos08_key_resp_allKeys = []
    # keep track of which components have finished
    Pos08_2Components = [Pos08_text, Pos08_key_resp]
    for thisComponent in Pos08_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos08_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos08_2"-------
    while continueRoutine:
        # get current time
        t = Pos08_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos08_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos08_text* updates
        if Pos08_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_text.frameNStart = frameN  # exact frame index
            Pos08_text.tStart = t  # local t and not account for scr refresh
            Pos08_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_text, 'tStartRefresh')  # time at next scr refresh
            Pos08_text.setAutoDraw(True)
        
        # *Pos08_key_resp* updates
        waitOnFlip = False
        if Pos08_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos08_key_resp.frameNStart = frameN  # exact frame index
            Pos08_key_resp.tStart = t  # local t and not account for scr refresh
            Pos08_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos08_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos08_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos08_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos08_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos08_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos08_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos08_key_resp_allKeys.extend(theseKeys)
            if len(_Pos08_key_resp_allKeys):
                Pos08_key_resp.keys = _Pos08_key_resp_allKeys[-1].name  # just the last key pressed
                Pos08_key_resp.rt = _Pos08_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos08_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos08_2"-------
    for thisComponent in Pos08_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos08_text.started', Pos08_text.tStartRefresh)
    trials06_Loop.addData('Pos08_text.stopped', Pos08_text.tStopRefresh)
    # check responses
    if Pos08_key_resp.keys in ['', [], None]:  # No response was made
        Pos08_key_resp.keys = None
    trials06_Loop.addData('Pos08_key_resp.keys',Pos08_key_resp.keys)
    if Pos08_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos08_key_resp.rt', Pos08_key_resp.rt)
    trials06_Loop.addData('Pos08_key_resp.started', Pos08_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos08_key_resp.stopped', Pos08_key_resp.tStopRefresh)
    # the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pos09_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt)
    Pos09_key_resp.keys = []
    Pos09_key_resp.rt = []
    _Pos09_key_resp_allKeys = []
    # keep track of which components have finished
    Pos09_2Components = [Pos09_text, Pos09_key_resp]
    for thisComponent in Pos09_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pos09_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pos09_2"-------
    while continueRoutine:
        # get current time
        t = Pos09_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pos09_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pos09_text* updates
        if Pos09_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_text.frameNStart = frameN  # exact frame index
            Pos09_text.tStart = t  # local t and not account for scr refresh
            Pos09_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_text, 'tStartRefresh')  # time at next scr refresh
            Pos09_text.setAutoDraw(True)
        
        # *Pos09_key_resp* updates
        waitOnFlip = False
        if Pos09_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pos09_key_resp.frameNStart = frameN  # exact frame index
            Pos09_key_resp.tStart = t  # local t and not account for scr refresh
            Pos09_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pos09_key_resp, 'tStartRefresh')  # time at next scr refresh
            Pos09_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Pos09_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Pos09_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Pos09_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Pos09_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Pos09_key_resp_allKeys.extend(theseKeys)
            if len(_Pos09_key_resp_allKeys):
                Pos09_key_resp.keys = _Pos09_key_resp_allKeys[-1].name  # just the last key pressed
                Pos09_key_resp.rt = _Pos09_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pos09_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pos09_2"-------
    for thisComponent in Pos09_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials06_Loop.addData('Pos09_text.started', Pos09_text.tStartRefresh)
    trials06_Loop.addData('Pos09_text.stopped', Pos09_text.tStopRefresh)
    # check responses
    if Pos09_key_resp.keys in ['', [], None]:  # No response was made
        Pos09_key_resp.keys = None
    trials06_Loop.addData('Pos09_key_resp.keys',Pos09_key_resp.keys)
    if Pos09_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Pos09_key_resp.rt', Pos09_key_resp.rt)
    trials06_Loop.addData('Pos09_key_resp.started', Pos09_key_resp.tStartRefresh)
    trials06_Loop.addData('Pos09_key_resp.stopped', Pos09_key_resp.tStopRefresh)
    # the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    Blank500_text.setText('')
    # keep track of which components have finished
    Blank500Components = [Blank500_text]
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
        
        # *Blank500_text* updates
        if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank500_text.frameNStart = frameN  # exact frame index
            Blank500_text.tStart = t  # local t and not account for scr refresh
            Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(True)
        if Blank500_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Blank500_text.tStop = t  # not accounting for scr refresh
                Blank500_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
                Blank500_text.setAutoDraw(False)
        
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
    trials06_Loop.addData('Blank500_text.started', Blank500_text.tStartRefresh)
    trials06_Loop.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)
    
    # ------Prepare to start Routine "Comp_q"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_q_key_resp.keys = []
    Comp_q_key_resp.rt = []
    _Comp_q_key_resp_allKeys = []
    Comp_q_text.setText(Quest_Presented)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_qComponents = [Comp_q_key_resp, Comp_q_text]
    for thisComponent in Comp_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_q"-------
    while continueRoutine:
        # get current time
        t = Comp_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_q_key_resp* updates
        waitOnFlip = False
        if Comp_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_key_resp.frameNStart = frameN  # exact frame index
            Comp_q_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_q_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_q_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_q_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_q_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Comp_q_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_q_key_resp_allKeys):
                Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_q_text* updates
        if Comp_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_q_text.frameNStart = frameN  # exact frame index
            Comp_q_text.tStart = t  # local t and not account for scr refresh
            Comp_q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_q_text, 'tStartRefresh')  # time at next scr refresh
            Comp_q_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_q"-------
    for thisComponent in Comp_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_q_key_resp.keys in ['', [], None]:  # No response was made
        Comp_q_key_resp.keys = None
    trials06_Loop.addData('Comp_q_key_resp.keys',Comp_q_key_resp.keys)
    if Comp_q_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt)
    trials06_Loop.addData('Comp_q_key_resp.started', Comp_q_key_resp.tStartRefresh)
    trials06_Loop.addData('Comp_q_key_resp.stopped', Comp_q_key_resp.tStopRefresh)
    trials06_Loop.addData('Comp_q_text.started', Comp_q_text.tStartRefresh)
    trials06_Loop.addData('Comp_q_text.stopped', Comp_q_text.tStopRefresh)
    # the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Comp_resp"-------
    continueRoutine = True
    # update component parameters for each repeat
    Comp_resp_key_resp.keys = []
    Comp_resp_key_resp.rt = []
    _Comp_resp_key_resp_allKeys = []
    Comp_Up_resp_text.setPos((0,0.1))
    Comp_Up_resp_text.setText(Quest_Up)
    Quest_Down_text.setText(Quest_Down)
    if followUp == 0:
        continueRoutine=False
    # keep track of which components have finished
    Comp_respComponents = [Comp_resp_key_resp, Comp_Up_resp_text, Quest_Down_text]
    for thisComponent in Comp_respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Comp_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Comp_resp"-------
    while continueRoutine:
        # get current time
        t = Comp_respClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Comp_respClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Comp_resp_key_resp* updates
        waitOnFlip = False
        if Comp_resp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_resp_key_resp.frameNStart = frameN  # exact frame index
            Comp_resp_key_resp.tStart = t  # local t and not account for scr refresh
            Comp_resp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_resp_key_resp, 'tStartRefresh')  # time at next scr refresh
            Comp_resp_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Comp_resp_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Comp_resp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Comp_resp_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Comp_resp_key_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _Comp_resp_key_resp_allKeys.extend(theseKeys)
            if len(_Comp_resp_key_resp_allKeys):
                Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[-1].name  # just the last key pressed
                Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Comp_Up_resp_text* updates
        if Comp_Up_resp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Comp_Up_resp_text.frameNStart = frameN  # exact frame index
            Comp_Up_resp_text.tStart = t  # local t and not account for scr refresh
            Comp_Up_resp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Comp_Up_resp_text, 'tStartRefresh')  # time at next scr refresh
            Comp_Up_resp_text.setAutoDraw(True)
        
        # *Quest_Down_text* updates
        if Quest_Down_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quest_Down_text.frameNStart = frameN  # exact frame index
            Quest_Down_text.tStart = t  # local t and not account for scr refresh
            Quest_Down_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quest_Down_text, 'tStartRefresh')  # time at next scr refresh
            Quest_Down_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Comp_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Comp_resp"-------
    for thisComponent in Comp_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Comp_resp_key_resp.keys in ['', [], None]:  # No response was made
        Comp_resp_key_resp.keys = None
    trials06_Loop.addData('Comp_resp_key_resp.keys',Comp_resp_key_resp.keys)
    if Comp_resp_key_resp.keys != None:  # we had a response
        trials06_Loop.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt)
    trials06_Loop.addData('Comp_resp_key_resp.started', Comp_resp_key_resp.tStartRefresh)
    trials06_Loop.addData('Comp_resp_key_resp.stopped', Comp_resp_key_resp.tStopRefresh)
    trials06_Loop.addData('Comp_Up_resp_text.started', Comp_Up_resp_text.tStartRefresh)
    trials06_Loop.addData('Comp_Up_resp_text.stopped', Comp_Up_resp_text.tStopRefresh)
    trials06_Loop.addData('Quest_Down_text.started', Quest_Down_text.tStartRefresh)
    trials06_Loop.addData('Quest_Down_text.stopped', Quest_Down_text.tStopRefresh)
    # the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials06_Loop'


# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
Blank500_text.setText('')
# keep track of which components have finished
Blank500Components = [Blank500_text]
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
    
    # *Blank500_text* updates
    if Blank500_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blank500_text.frameNStart = frameN  # exact frame index
        Blank500_text.tStart = t  # local t and not account for scr refresh
        Blank500_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blank500_text, 'tStartRefresh')  # time at next scr refresh
        Blank500_text.setAutoDraw(True)
    if Blank500_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Blank500_text.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            Blank500_text.tStop = t  # not accounting for scr refresh
            Blank500_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Blank500_text, 'tStopRefresh')  # time at next scr refresh
            Blank500_text.setAutoDraw(False)
    
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
thisExp.addData('Blank500_text.started', Blank500_text.tStartRefresh)
thisExp.addData('Blank500_text.stopped', Blank500_text.tStopRefresh)

# ------Prepare to start Routine "Goodbye_Screen"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
Goodbye_text.setText('Vielen Dank für deine Teilnahme und bis in zwei Wochen.\n\nDas Programm schließt sich automatisch.')
# keep track of which components have finished
Goodbye_ScreenComponents = [Goodbye_text]
for thisComponent in Goodbye_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Goodbye_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye_Screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Goodbye_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Goodbye_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Goodbye_text* updates
    if Goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Goodbye_text.frameNStart = frameN  # exact frame index
        Goodbye_text.tStart = t  # local t and not account for scr refresh
        Goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Goodbye_text, 'tStartRefresh')  # time at next scr refresh
        Goodbye_text.setAutoDraw(True)
    if Goodbye_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Goodbye_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Goodbye_text.tStop = t  # not accounting for scr refresh
            Goodbye_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Goodbye_text, 'tStopRefresh')  # time at next scr refresh
            Goodbye_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Goodbye_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye_Screen"-------
for thisComponent in Goodbye_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Goodbye_text.started', Goodbye_text.tStartRefresh)
thisExp.addData('Goodbye_text.stopped', Goodbye_text.tStopRefresh)

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
