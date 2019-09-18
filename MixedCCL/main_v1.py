#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on 9월 04, 2019, at 15:36
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
print(_thisDir)
os.chdir(_thisDir)
print(os.getcwd())

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'mixedCCL'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['date'])
print(filename)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\MoonSun\\Desktop\\강문선\\5. purdue\\1st year project\\stimuli\\test_0904.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=False, screen=0, 
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()




# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instr_text = visual.TextStim(win=win, name='instr_text',
    text='This is an instruction page',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
color = visual.ImageStim(
    win=win,
    name='color', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='Time Out',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);




# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr_keyresp = keyboard.Keyboard()
# keep track of which components have finished
instructionComponents = [instr_text, instr_keyresp]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text* updates
    if t >= 1.0 and instr_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text.tStart = t  # not accounting for scr refresh
        instr_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
        instr_text.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        instr_text.tStop = t  # not accounting for scr refresh
        instr_text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(instr_text, 'tStopRefresh')  # time at next scr refresh
        instr_text.setAutoDraw(False)
    
    # *instr_keyresp* updates
    if t >= 0.0 and instr_keyresp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_keyresp.tStart = t  # not accounting for scr refresh
        instr_keyresp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_keyresp, 'tStartRefresh')  # time at next scr refresh
        instr_keyresp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr_keyresp.clock.reset)  # t=0 on next screen flip
        instr_keyresp.clearEvents(eventType='keyboard')
    if instr_keyresp.status == STARTED:
        theseKeys = instr_keyresp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            instr_keyresp.keys = theseKeys.name  # just the last key pressed
            instr_keyresp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_text.started', instr_text.tStartRefresh)
thisExp.addData('instr_text.stopped', instr_text.tStopRefresh)
# check responses
if instr_keyresp.keys in ['', [], None]:  # No response was made
    instr_keyresp.keys = None
thisExp.addData('instr_keyresp.keys',instr_keyresp.keys)
if instr_keyresp.keys != None:  # we had a response
    thisExp.addData('instr_keyresp.rt', instr_keyresp.rt)
thisExp.addData('instr_keyresp.started', instr_keyresp.tStartRefresh)
thisExp.addData('instr_keyresp.stopped', instr_keyresp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




subjectFile = _thisDir + os.sep + 'data\MixedCCL_' + expInfo['participant'] + '.csv'
print(subjectFile)
#filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['date'])

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(subjectFile),
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
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.800000)
    # update component parameters for each repeat
    image.setImage(filePath)
    keyresp = keyboard.Keyboard()
    color.setImage(colorPath)
    # keep track of which components have finished
    trialComponents = [image, keyresp, fix, color]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.3 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        frameRemains = 0.3 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
        
        # *keyresp* updates
        if t >= 0.3 and keyresp.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyresp.tStart = t  # not accounting for scr refresh
            keyresp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(keyresp, 'tStartRefresh')  # time at next scr refresh
            keyresp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(keyresp.clock.reset)  # t=0 on next screen flip
            keyresp.clearEvents(eventType='keyboard')
        frameRemains = 0.3 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if keyresp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            keyresp.tStop = t  # not accounting for scr refresh
            keyresp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(keyresp, 'tStopRefresh')  # time at next scr refresh
            keyresp.status = FINISHED
        if keyresp.status == STARTED:
            theseKeys = keyresp.getKeys(keyList=['v', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                keyresp.keys = theseKeys.name  # just the last key pressed
                keyresp.rt = theseKeys.rt
                # was this 'correct'?
                if (keyresp.keys == str(response)) or (keyresp.keys == response):
                    keyresp.corr = 1
                else:
                    keyresp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # not accounting for scr refresh
            fix.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        frameRemains = 0.0 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fix.tStop = t  # not accounting for scr refresh
            fix.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
            fix.setAutoDraw(False)
        
        # *color* updates
        if t >= 0.3 and color.status == NOT_STARTED:
            # keep track of start time/frame for later
            color.tStart = t  # not accounting for scr refresh
            color.frameNStart = frameN  # exact frame index
            win.timeOnFlip(color, 'tStartRefresh')  # time at next scr refresh
            color.setAutoDraw(True)
        frameRemains = 0.3 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if color.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            color.tStop = t  # not accounting for scr refresh
            color.frameNStop = frameN  # exact frame index
            win.timeOnFlip(color, 'tStopRefresh')  # time at next scr refresh
            color.setAutoDraw(False)
        
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
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    # check responses
    if keyresp.keys in ['', [], None]:  # No response was made
        keyresp.keys = None
        # was no response the correct answer?!
        if str(response).lower() == 'none':
           keyresp.corr = 1;  # correct non-response
        else:
           keyresp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('keyresp.keys',keyresp.keys)
    trials.addData('keyresp.corr', keyresp.corr)
    if keyresp.keys != None:  # we had a response
        trials.addData('keyresp.rt', keyresp.rt)
    trials.addData('keyresp.started', keyresp.tStartRefresh)
    trials.addData('keyresp.stopped', keyresp.tStopRefresh)
    trials.addData('fix.started', fix.tStartRefresh)
    trials.addData('fix.stopped', fix.tStopRefresh)
    trials.addData('color.started', color.tStartRefresh)
    trials.addData('color.stopped', color.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = [feedback_text_25]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text_25* updates
        if t >= 0.0 and feedback_text_25.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_text_25.tStart = t  # not accounting for scr refresh
            feedback_text_25.frameNStart = frameN  # exact frame index
            win.timeOnFlip(feedback_text_25, 'tStartRefresh')  # time at next scr refresh
            feedback_text_25.setAutoDraw(True)
        frameRemains = 0.0 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_text_25.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            feedback_text_25.tStop = t  # not accounting for scr refresh
            feedback_text_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedback_text_25, 'tStopRefresh')  # time at next scr refresh
            feedback_text_25.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedback_text_25.started', feedback_text_25.tStartRefresh)
    trials.addData('feedback_text_25.stopped', feedback_text_25.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


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
