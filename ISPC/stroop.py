#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on Tue Aug  6 04:02:41 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

sys.path.insert(0, './bin')
from trialGen import practice, exp



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'stroop_outline'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='/Users/HyunJoo/Documents/Yu-Chin Lab/ISPC_new/stroop.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "prac_instr"
prac_instrClock = core.Clock()
prac_instr_body = "Your task here is to identify the \"face\" presented on each trial by pressing the designated key.\nIf the face is [George Clooney], press \'v\'\nIf the face is [Tom Cruise], press \'b\'\nIf the face is [Mat Damon], press \'n\'\n\nTry to respond as fast as you can without sacrificing the accuracy.\nUse ONLY your RIGHT INDEX finger to respond. [in bold & red]\n\nRaise your hand now if you have questions.\nElse, press space bar to start.\n"
prac_instr_text = visual.TextStim(win=win, name='prac_instr_text',
                                  text=prac_instr_body,
                                  font='Arial',
                                  pos=(0, 0), height=0.04, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)

# Initialize components for Routine "prac_trial_routine"
prac_trial_routineClock = core.Clock()
prac_trial_faceImage = visual.ImageStim(
    win=win,
    name='prac_trial_faceImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prac_trial_nameText = visual.TextStim(win=win, name='prac_trial_nameText',
                                      text='default text',
                                      font='Arial',
                                      pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0,
                                      color='white', colorSpace='rgb', opacity=1,
                                      languageStyle='LTR',
                                      depth=-2.0)

# Initialize components for Routine "prac_trial_feedback_routine"
prac_trial_feedback_routineClock = core.Clock()
pract_trial_feedback_text = visual.TextStim(win=win, name='pract_trial_feedback_text',
                                            text='Time Out',
                                            font='Arial',
                                            pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                            color='white', colorSpace='rgb', opacity=1,
                                            languageStyle='LTR',
                                            depth=0.0)
prac_trial_blank_text = visual.TextStim(win=win, name='prac_trial_blank_text',
                                        text=None,
                                        font='Arial',
                                        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                        color='white', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=-1.0)

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_body = "Unlike practice, you will now see names(instead of XXX) written across the face.\nIt may or may not be the name for the current face.\nYour task is to identify the face, not the name.\nIf the face is [George Clooney], press \'v\'\nIf the face is [Tom Cruise], press \'b\'\nIf the face is [Mat Damon], press \'n\'\n\nTry to respond as fast as you can without sacrificing the accuracy.\nUse ONLY your RIGHT INDEX finger to respond. [in bold & red]\n\nRaise your hand now if you have questions.\nElse, press space bar to start.\n"
instr_text = visual.TextStim(win=win, name='instr_text',
                             text=instr_body,
                             font='Arial',
                             pos=(0, 0), height=0.04, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0)

# Initialize components for Routine "trial_routine"
trial_routineClock = core.Clock()
trial_faceImage = visual.ImageStim(
    win=win,
    name='trial_faceImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_nameText = visual.TextStim(win=win, name='trial_nameText',
                                 text='default text',
                                 font='Arial',
                                 pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0,
                                 color='white', colorSpace='rgb', opacity=1,
                                 languageStyle='LTR',
                                 depth=-2.0)

# Initialize components for Routine "feedback_routine"
feedback_routineClock = core.Clock()
trial_feedback_text = visual.TextStim(win=win, name='trial_feedback_text',
                                      text='Time Out',
                                      font='Arial',
                                      pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                      color='white', colorSpace='rgb', opacity=1,
                                      languageStyle='LTR',
                                      depth=0.0)
trial_blank_text = visual.TextStim(win=win, name='trial_blank_text',
                                   text=None,
                                   font='Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=-1.0)

# Initialize components for Routine "break_routine"
break_routineClock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
                             text='This is a break between blocks.\n\nYou have 20 seconds to break.\nYou can also start by pressing any key.',
                             font='Arial',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()

# ------Prepare to start Routine "prac_instr"-------
t = 0
prac_instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr_prac_key_resp = keyboard.Keyboard()
# keep track of which components have finished
prac_instrComponents = [prac_instr_text, instr_prac_key_resp]
for thisComponent in prac_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "prac_instr"-------
while continueRoutine:
    # get current time
    t = prac_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *prac_instr_text* updates
    if t >= 0.0 and prac_instr_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        prac_instr_text.tStart = t  # not accounting for scr refresh
        prac_instr_text.frameNStart = frameN  # exact frame index
        # time at next scr refresh
        win.timeOnFlip(prac_instr_text, 'tStartRefresh')
        prac_instr_text.setAutoDraw(True)

    # *instr_prac_key_resp* updates
    if t >= 0.0 and instr_prac_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_prac_key_resp.tStart = t  # not accounting for scr refresh
        instr_prac_key_resp.frameNStart = frameN  # exact frame index
        # time at next scr refresh
        win.timeOnFlip(instr_prac_key_resp, 'tStartRefresh')
        instr_prac_key_resp.status = STARTED
        # keyboard checking is just starting
        instr_prac_key_resp.clearEvents(eventType='keyboard')
    if instr_prac_key_resp.status == STARTED:
        theseKeys = instr_prac_key_resp.getKeys(
            keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prac_instr"-------
for thisComponent in prac_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials_loop = data.TrialHandler(nReps=1, method='sequential',
                                     extraInfo=expInfo, originPath=-1,
                                     trialList=data.importConditions(
                                         '../data/ISPC_squence_practice.csv'),
                                     seed=None, name='prac_trials_loop')
# so we can initialise stimuli with some values
thisPrac_trials_loop = prac_trials_loop.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trials_loop.rgb)
if thisPrac_trials_loop != None:
    for paramName in thisPrac_trials_loop:
        exec('{} = thisPrac_trials_loop[paramName]'.format(paramName))

for thisPrac_trials_loop in prac_trials_loop:
    currentLoop = prac_trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trials_loop.rgb)
    if thisPrac_trials_loop != None:
        for paramName in thisPrac_trials_loop:
            exec('{} = thisPrac_trials_loop[paramName]'.format(paramName))

    # ------Prepare to start Routine "prac_trial_routine"-------
    t = 0
    prac_trial_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    prac_trial_key_resp = keyboard.Keyboard()
    prac_trial_faceImage.setImage(face_path)
    prac_trial_nameText.setText(nid)
    # keep track of which components have finished
    prac_trial_routineComponents = [
        prac_trial_key_resp, prac_trial_faceImage, prac_trial_nameText]
    for thisComponent in prac_trial_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "prac_trial_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prac_trial_routineClock.getTime()
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *prac_trial_key_resp* updates
        if t >= 0.2 and prac_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_trial_key_resp.tStart = t  # not accounting for scr refresh
            prac_trial_key_resp.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_key_resp, 'tStartRefresh')
            prac_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            # t=0 on next screen flip
            win.callOnFlip(prac_trial_key_resp.clock.reset)
            prac_trial_key_resp.clearEvents(eventType='keyboard')
        frameRemains = 0.2 + 1 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if prac_trial_key_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prac_trial_key_resp.tStop = t  # not accounting for scr refresh
            prac_trial_key_resp.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_key_resp, 'tStopRefresh')
            prac_trial_key_resp.status = FINISHED
        if prac_trial_key_resp.status == STARTED:
            theseKeys = prac_trial_key_resp.getKeys(
                keyList=['v', 'b', 'n'], waitRelease=False)

            pract_trial_feedback_text.setText("Time Out")
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if prac_trial_key_resp.keys == []:  # then this was the first keypress
                    prac_trial_key_resp.keys = theseKeys.name  # just the first key pressed
                    prac_trial_key_resp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (prac_trial_key_resp.keys == str(corrResp)) or (prac_trial_key_resp.keys == corrResp):
                        prac_trial_key_resp.corr = 1
                        pract_trial_feedback_text.setText("Correct")
                    else:
                        prac_trial_key_resp.corr = 0
                        pract_trial_feedback_text.setText("Incorrect")
                    # a response ends the routine
                    continueRoutine = False

        # *prac_trial_faceImage* updates
        if t >= 0.2 and prac_trial_faceImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_trial_faceImage.tStart = t  # not accounting for scr refresh
            prac_trial_faceImage.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_faceImage, 'tStartRefresh')
            prac_trial_faceImage.setAutoDraw(True)
        frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if prac_trial_faceImage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prac_trial_faceImage.tStop = t  # not accounting for scr refresh
            prac_trial_faceImage.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_faceImage, 'tStopRefresh')
            prac_trial_faceImage.setAutoDraw(False)

        # *prac_trial_nameText* updates
        if t >= 0.2 and prac_trial_nameText.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_trial_nameText.tStart = t  # not accounting for scr refresh
            prac_trial_nameText.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_nameText, 'tStartRefresh')
            prac_trial_nameText.setAutoDraw(True)
        frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if prac_trial_nameText.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prac_trial_nameText.tStop = t  # not accounting for scr refresh
            prac_trial_nameText.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_nameText, 'tStopRefresh')
            prac_trial_nameText.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_trial_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "prac_trial_routine"-------
    for thisComponent in prac_trial_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_trial_key_resp.keys in ['', [], None]:  # No response was made
        prac_trial_key_resp.keys = None
        # was no response the correct answer?!
        if str(corrResp).lower() == 'none':
           prac_trial_key_resp.corr = 1  # correct non-response
        else:
           prac_trial_key_resp.corr = 0  # failed to respond (incorrectly)

    # ------Prepare to start Routine "prac_trial_feedback_routine"-------
    t = 0
    prac_trial_feedback_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    prac_trial_feedback_routineComponents = [
        pract_trial_feedback_text, prac_trial_blank_text]
    for thisComponent in prac_trial_feedback_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "prac_trial_feedback_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prac_trial_feedback_routineClock.getTime()
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *pract_trial_feedback_text* updates
        if t >= 0.0 and pract_trial_feedback_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            pract_trial_feedback_text.tStart = t  # not accounting for scr refresh
            pract_trial_feedback_text.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(pract_trial_feedback_text, 'tStartRefresh')
            pract_trial_feedback_text.setAutoDraw(True)
        frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if pract_trial_feedback_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            pract_trial_feedback_text.tStop = t  # not accounting for scr refresh
            pract_trial_feedback_text.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(pract_trial_feedback_text, 'tStopRefresh')
            pract_trial_feedback_text.setAutoDraw(False)

        # *prac_trial_blank_text* updates
        if t >= 0.5 and prac_trial_blank_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_trial_blank_text.tStart = t  # not accounting for scr refresh
            prac_trial_blank_text.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_blank_text, 'tStartRefresh')
            prac_trial_blank_text.setAutoDraw(True)
        frameRemains = 0.5 + 1.0 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if prac_trial_blank_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prac_trial_blank_text.tStop = t  # not accounting for scr refresh
            prac_trial_blank_text.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(prac_trial_blank_text, 'tStopRefresh')
            prac_trial_blank_text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_trial_feedback_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "prac_trial_feedback_routine"-------
    for thisComponent in prac_trial_feedback_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

# completed 1 repeats of 'prac_trials_loop'


# ------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr_key_resp = keyboard.Keyboard()
# keep track of which components have finished
instrComponents = [instr_text, instr_key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instr_text* updates
    if t >= 0.0 and instr_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text.tStart = t  # not accounting for scr refresh
        instr_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
        instr_text.setAutoDraw(True)

    # *instr_key_resp* updates
    if t >= 0.0 and instr_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_key_resp.tStart = t  # not accounting for scr refresh
        instr_key_resp.frameNStart = frameN  # exact frame index
        # time at next scr refresh
        win.timeOnFlip(instr_key_resp, 'tStartRefresh')
        instr_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr_key_resp.clock.reset)  # t=0 on next screen flip
        instr_key_resp.clearEvents(eventType='keyboard')
    if instr_key_resp.status == STARTED:
        theseKeys = instr_key_resp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            instr_key_resp.keys = theseKeys.name  # just the last key pressed
            instr_key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_key_resp.keys in ['', [], None]:  # No response was made
    instr_key_resp.keys = None
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_loop = data.TrialHandler(nReps=5, method='sequential',
                               extraInfo=expInfo, originPath=-1,
                               trialList=[None],
                               seed=None, name='block_loop')
# so we can initialise stimuli with some values
thisBlock_loop = block_loop.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop:
        exec('{} = thisBlock_loop[paramName]'.format(paramName))

blockCount = 0
for thisBlock_loop in block_loop:
    blockCount += 1
    currentLoop = block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop:
            exec('{} = thisBlock_loop[paramName]'.format(paramName))

    # set up handler to look after randomisation of conditions etc
    interval = str((blockCount-1)*72) + ":" + str(blockCount*72)
    trials_loop = data.TrialHandler(nReps=1, method='sequential',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=data.importConditions(
                                        '../data/ISPC_squence_shuffled.csv', selection=interval),
                                    seed=None, name='trials_loop')
    # so we can initialise stimuli with some values
    thisTrials_loop = trials_loop.trialList[0] # this is a dictionary & trialList is a list of dictionary
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))

    for thisTrials_loop in trials_loop:
        currentLoop = trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
        if thisTrials_loop != None:
            for paramName in thisTrials_loop:
                exec('{} = thisTrials_loop[paramName]'.format(paramName))

        # Save the stimuli for the current trial
        for keys in thisTrials_loop.keys():
            thisExp.addData(keys, thisTrials_loop[keys])

        # ------Prepare to start Routine "trial_routine"-------
        t = 0
        trial_routineClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.200000)
        # update component parameters for each repeat
        trial_key_resp = keyboard.Keyboard()
        trial_faceImage.setImage(face_path)
        trial_nameText.setText(nid)
        # keep track of which components have finished
        trial_routineComponents = [trial_key_resp, trial_faceImage, trial_nameText]
        for thisComponent in trial_routineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial_routine"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_routineClock.getTime()
            # number of completed frames (so 0 is the first frame)
            frameN = frameN + 1
            # update/draw components on each frame

            # *trial_key_resp* updates
            if t >= 0.2 and trial_key_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_key_resp.tStart = t  # not accounting for scr refresh
                trial_key_resp.frameNStart = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_key_resp, 'tStartRefresh')
                trial_key_resp.status = STARTED
                # keyboard checking is just starting
                # t=0 on next screen flip
                win.callOnFlip(trial_key_resp.clock.reset)
                trial_key_resp.clearEvents(eventType='keyboard')
            frameRemains = 0.2 + 1 - win.monitorFramePeriod * \
                0.75  # most of one frame period left
            if trial_key_resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_key_resp.tStop = t  # not accounting for scr refresh
                trial_key_resp.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_key_resp, 'tStopRefresh')
                trial_key_resp.status = FINISHED
            if trial_key_resp.status == STARTED:
                theseKeys = trial_key_resp.getKeys(
                    keyList=['v', 'b', 'n'], waitRelease=False)

                trial_feedback_text.setText("Time Out")
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed

                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if trial_key_resp.keys == []:  # then this was the first keypress
                        trial_key_resp.keys = theseKeys.name  # just the first key pressed
                        trial_key_resp.rt = theseKeys.rt
                        # was this 'correct'?
                        if (trial_key_resp.keys == str(corrResp)) or (trial_key_resp.keys == corrResp):
                            trial_key_resp.corr = 1
                            trial_feedback_text.setText("Correct")
                        else:
                            trial_key_resp.corr = 0
                            trial_feedback_text.setText("Incorrect")
                        # a response ends the routine
                        continueRoutine = False

            # *trial_faceImage* updates
            if t >= 0.2 and trial_faceImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_faceImage.tStart = t  # not accounting for scr refresh
                trial_faceImage.frameNStart = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_faceImage, 'tStartRefresh')
                trial_faceImage.setAutoDraw(True)
            frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * \
                0.75  # most of one frame period left
            if trial_faceImage.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_faceImage.tStop = t  # not accounting for scr refresh
                trial_faceImage.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_faceImage, 'tStopRefresh')
                trial_faceImage.setAutoDraw(False)

            # *trial_nameText* updates
            if t >= 0.2 and trial_nameText.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_nameText.tStart = t  # not accounting for scr refresh
                trial_nameText.frameNStart = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_nameText, 'tStartRefresh')
                trial_nameText.setAutoDraw(True)
            frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * \
                0.75  # most of one frame period left
            if trial_nameText.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_nameText.tStop = t  # not accounting for scr refresh
                trial_nameText.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_nameText, 'tStopRefresh')
                trial_nameText.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_routineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial_routine"-------
        for thisComponent in trial_routineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if trial_key_resp.keys in ['', [], None]:  # No response was made
            trial_key_resp.keys = None
            # was no response the correct answer?!
            if str(corrResp).lower() == 'none':
               trial_key_resp.corr = 1  # correct non-response
            else:
               trial_key_resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials_loop (TrialHandler)
        thisExp.addData('trial_key_resp.keys', trial_key_resp.keys)
        thisExp.addData('trial_key_resp.corr', trial_key_resp.corr)
        if trial_key_resp.keys != None:  # we had a response
            thisExp.addData('trial_key_resp.rt', trial_key_resp.rt)

        # ------Prepare to start Routine "feedback_routine"-------
        t = 0
        feedback_routineClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        feedback_routineComponents = [trial_feedback_text, trial_blank_text]
        for thisComponent in feedback_routineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "feedback_routine"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback_routineClock.getTime()
            # number of completed frames (so 0 is the first frame)
            frameN = frameN + 1
            # update/draw components on each frame

            # *trial_feedback_text* updates
            if t >= 0.0 and trial_feedback_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_feedback_text.tStart = t  # not accounting for scr refresh
                trial_feedback_text.frameNStart = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_feedback_text, 'tStartRefresh')
                trial_feedback_text.setAutoDraw(True)
            frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * \
                0.75  # most of one frame period left
            if trial_feedback_text.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_feedback_text.tStop = t  # not accounting for scr refresh
                trial_feedback_text.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_feedback_text, 'tStopRefresh')
                trial_feedback_text.setAutoDraw(False)

            # *trial_blank_text* updates
            if t >= 0.5 and trial_blank_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_blank_text.tStart = t  # not accounting for scr refresh
                trial_blank_text.frameNStart = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_blank_text, 'tStartRefresh')
                trial_blank_text.setAutoDraw(True)
            frameRemains = 0.5 + 1.0 - win.monitorFramePeriod * \
                0.75  # most of one frame period left
            if trial_blank_text.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_blank_text.tStop = t  # not accounting for scr refresh
                trial_blank_text.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_blank_text, 'tStopRefresh')
                trial_blank_text.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_routineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "feedback_routine"-------
        for thisComponent in feedback_routineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()

    # completed 1 repeats of 'trials_loop'

    # ------Prepare to start Routine "break_routine"-------
    t = 0
    break_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    break_key_resp = keyboard.Keyboard()
    # keep track of which components have finished
    break_routineComponents = [break_text, break_key_resp]
    for thisComponent in break_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "break_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_routineClock.getTime()
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *break_text* updates
        if t >= 0.0 and break_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_text.tStart = t  # not accounting for scr refresh
            break_text.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(break_text, 'tStartRefresh')
            break_text.setAutoDraw(True)
        frameRemains = 0.0 + 20 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if break_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            break_text.tStop = t  # not accounting for scr refresh
            break_text.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(break_text, 'tStopRefresh')
            break_text.setAutoDraw(False)

        # *break_key_resp* updates
        if t >= 5.0 and break_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_key_resp.tStart = t  # not accounting for scr refresh
            break_key_resp.frameNStart = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(break_key_resp, 'tStartRefresh')
            break_key_resp.status = STARTED
            # keyboard checking is just starting
            # t=0 on next screen flip
            win.callOnFlip(break_key_resp.clock.reset)
            break_key_resp.clearEvents(eventType='keyboard')
        frameRemains = 5.0 + 15 - win.monitorFramePeriod * \
            0.75  # most of one frame period left
        if break_key_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            break_key_resp.tStop = t  # not accounting for scr refresh
            break_key_resp.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(break_key_resp, 'tStopRefresh')
            break_key_resp.status = FINISHED
        if break_key_resp.status == STARTED:
            theseKeys = break_key_resp.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                break_key_resp.keys = theseKeys.name  # just the last key pressed
                break_key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_routine"-------
    for thisComponent in break_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if break_key_resp.keys in ['', [], None]:  # No response was made
        break_key_resp.keys = None
# completed 5 repeats of 'block_loop'


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

