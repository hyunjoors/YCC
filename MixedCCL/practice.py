#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on September 07, 2019, at 17:55
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
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'test_0904'  # from the Builder filename that created this script
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
    originPath='\\\\itifs04.itap.purdue.edu\\PSYC\\Cognitive\\chiulab\\Kang\\objects\\practice.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instr_text = visual.TextStim(win=win, name='instr_text',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trial_fix = visual.TextStim(win=win, name='trial_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trial_color = visual.ImageStim(
    win=win,
    name='trial_color', 
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

# Initialize components for Routine "break_routine"
break_routineClock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BYE"
BYEClock = core.Clock()
BYE_text = visual.TextStim(win=win, name='BYE_text',
    text='Any text\n\nincluding line breaks',
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
    if t >= 0.0 and instr_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text.tStart = t  # not accounting for scr refresh
        instr_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
        instr_text.setAutoDraw(True)
    
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

# set up handler to look after randomisation of conditions etc
episode_loop = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='episode_loop')
thisExp.addLoop(episode_loop)  # add the loop to the experiment
thisEpisode_loop = episode_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEpisode_loop.rgb)
if thisEpisode_loop != None:
    for paramName in thisEpisode_loop:
        exec('{} = thisEpisode_loop[paramName]'.format(paramName))

for thisEpisode_loop in episode_loop:
    currentLoop = episode_loop
    # abbreviate parameter names if possible (e.g. rgb = thisEpisode_loop.rgb)
    if thisEpisode_loop != None:
        for paramName in thisEpisode_loop:
            exec('{} = thisEpisode_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('data\\MixedCCL_1.csv'),
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
        trial_keyresp = keyboard.Keyboard()
        trial_color.setImage(colorPath)
        # keep track of which components have finished
        trialComponents = [trial_image, trial_keyresp, trial_fix, trial_color]
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
            
            # *trial_image* updates
            if t >= 0.3 and trial_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_image.tStart = t  # not accounting for scr refresh
                trial_image.frameNStart = frameN  # exact frame index
                win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
                trial_image.setAutoDraw(True)
            frameRemains = 0.3 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_image.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_image.tStop = t  # not accounting for scr refresh
                trial_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_image, 'tStopRefresh')  # time at next scr refresh
                trial_image.setAutoDraw(False)
            if trial_image.status == STARTED:  # only update if drawing
                trial_image.setImage(filePath, log=False)
            
            # *trial_keyresp* updates
            if t >= 0.3 and trial_keyresp.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_keyresp.tStart = t  # not accounting for scr refresh
                trial_keyresp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(trial_keyresp, 'tStartRefresh')  # time at next scr refresh
                trial_keyresp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trial_keyresp.clock.reset)  # t=0 on next screen flip
                trial_keyresp.clearEvents(eventType='keyboard')
            frameRemains = 0.3 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_keyresp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_keyresp.tStop = t  # not accounting for scr refresh
                trial_keyresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_keyresp, 'tStopRefresh')  # time at next scr refresh
                trial_keyresp.status = FINISHED
            if trial_keyresp.status == STARTED:
                theseKeys = trial_keyresp.getKeys(keyList=['v', 'n'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    trial_keyresp.keys = theseKeys.name  # just the last key pressed
                    trial_keyresp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (trial_keyresp.keys == str(response)) or (trial_keyresp.keys == response):
                        trial_keyresp.corr = 1
                    else:
                        trial_keyresp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *trial_fix* updates
            if t >= 0.0 and trial_fix.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_fix.tStart = t  # not accounting for scr refresh
                trial_fix.frameNStart = frameN  # exact frame index
                win.timeOnFlip(trial_fix, 'tStartRefresh')  # time at next scr refresh
                trial_fix.setAutoDraw(True)
            frameRemains = 0.0 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_fix.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_fix.tStop = t  # not accounting for scr refresh
                trial_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_fix, 'tStopRefresh')  # time at next scr refresh
                trial_fix.setAutoDraw(False)
            
            # *trial_color* updates
            if t >= 0.3 and trial_color.status == NOT_STARTED:
                # keep track of start time/frame for later
                trial_color.tStart = t  # not accounting for scr refresh
                trial_color.frameNStart = frameN  # exact frame index
                win.timeOnFlip(trial_color, 'tStartRefresh')  # time at next scr refresh
                trial_color.setAutoDraw(True)
            frameRemains = 0.3 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_color.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_color.tStop = t  # not accounting for scr refresh
                trial_color.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_color, 'tStopRefresh')  # time at next scr refresh
                trial_color.setAutoDraw(False)
            
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
        trials.addData('trial_image.started', trial_image.tStartRefresh)
        trials.addData('trial_image.stopped', trial_image.tStopRefresh)
        # check responses
        if trial_keyresp.keys in ['', [], None]:  # No response was made
            trial_keyresp.keys = None
            # was no response the correct answer?!
            if str(response).lower() == 'none':
               trial_keyresp.corr = 1;  # correct non-response
            else:
               trial_keyresp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('trial_keyresp.keys',trial_keyresp.keys)
        trials.addData('trial_keyresp.corr', trial_keyresp.corr)
        if trial_keyresp.keys != None:  # we had a response
            trials.addData('trial_keyresp.rt', trial_keyresp.rt)
        trials.addData('trial_keyresp.started', trial_keyresp.tStartRefresh)
        trials.addData('trial_keyresp.stopped', trial_keyresp.tStopRefresh)
        trials.addData('trial_fix.started', trial_fix.tStartRefresh)
        trials.addData('trial_fix.stopped', trial_fix.tStopRefresh)
        trials.addData('trial_color.started', trial_color.tStartRefresh)
        trials.addData('trial_color.stopped', trial_color.tStopRefresh)
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        # keep track of which components have finished
        feedbackComponents = [feedback_text]
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
            
            # *feedback_text* updates
            if t >= 0.0 and feedback_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_text.tStart = t  # not accounting for scr refresh
                feedback_text.frameNStart = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(True)
            frameRemains = 0.0 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback_text.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
            
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
        trials.addData('feedback_text.started', feedback_text.tStartRefresh)
        trials.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "break_routine"-------
    t = 0
    break_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
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
    while continueRoutine:
        # get current time
        t = break_routineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if t >= 0.0 and break_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_text.tStart = t  # not accounting for scr refresh
            break_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            break_text.setAutoDraw(True)
        
        # *break_key_resp* updates
        if t >= 0.0 and break_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_key_resp.tStart = t  # not accounting for scr refresh
            break_key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(break_key_resp, 'tStartRefresh')  # time at next scr refresh
            break_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(break_key_resp.clock.reset)  # t=0 on next screen flip
            break_key_resp.clearEvents(eventType='keyboard')
        if break_key_resp.status == STARTED:
            theseKeys = break_key_resp.getKeys(keyList=['space'], waitRelease=False)
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
    episode_loop.addData('break_text.started', break_text.tStartRefresh)
    episode_loop.addData('break_text.stopped', break_text.tStopRefresh)
    # check responses
    if break_key_resp.keys in ['', [], None]:  # No response was made
        break_key_resp.keys = None
    episode_loop.addData('break_key_resp.keys',break_key_resp.keys)
    if break_key_resp.keys != None:  # we had a response
        episode_loop.addData('break_key_resp.rt', break_key_resp.rt)
    episode_loop.addData('break_key_resp.started', break_key_resp.tStartRefresh)
    episode_loop.addData('break_key_resp.stopped', break_key_resp.tStopRefresh)
    # the Routine "break_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3 repeats of 'episode_loop'


# ------Prepare to start Routine "BYE"-------
t = 0
BYEClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp = keyboard.Keyboard()
# keep track of which components have finished
BYEComponents = [BYE_text, key_resp]
for thisComponent in BYEComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "BYE"-------
while continueRoutine:
    # get current time
    t = BYEClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BYE_text* updates
    if t >= 0.0 and BYE_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        BYE_text.tStart = t  # not accounting for scr refresh
        BYE_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(BYE_text, 'tStartRefresh')  # time at next scr refresh
        BYE_text.setAutoDraw(True)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BYEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BYE"-------
for thisComponent in BYEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BYE_text.started', BYE_text.tStartRefresh)
thisExp.addData('BYE_text.stopped', BYE_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "BYE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
