#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ToDos
       Reflect the keyboard mapping in the instructionClock
       Practice trial
       Image clash
       Data collect issue
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
import pandas as pd
import numpy as np

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'MixedCCL'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

# Import csv file and store the sequences in 'M'
subjectfile = 'data/MixedCCL_' + expInfo['participant'] + '.csv'
M = pd.read_csv(subjectfile)
episodeOrder = M.episode.unique()
M.sbjResp = M.sbjResp.astype(object) # this didn't happened to me, but data type of 'sbjResp' needs to be 'object' in order to save a pressed key. So set dtype = object here

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\itifs04.itap.purdue.edu\\PSYC\\Cognitive\\chiulab\\Kang\\objects\\test_0904.py',
    savePickle=True, saveWideText=True,
    dataFileName=subjectfile)

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
    text='This is an instruction page. Please change the text in \'instr_text\' in the main script. Please press \'space\' to start trials',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_fix = visual.TextStim(win=win, name='trial_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
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
    text='This is a break routine. Please change the text before running the experiment',
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
        theseKeys = instr_keyresp.getKeys(keyList=['space'], waitRelease=False)
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
# check responses
if instr_keyresp.keys in ['', [], None]:  # No response was made
    instr_keyresp.keys = None
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




for thisEpisode_loop in range(3):
    # What is current loop's episode? [Low, Med, High]
    currentEpisode = episodeOrder[thisEpisode_loop]
    # Select sequences that corresponds to the current episode
    M_current_episode = M.loc[M.episode == currentEpisode]
    
    # Loop thorugh the selected sequences
    for i, currentTrial in M_current_episode.iterrows():
        current_index = i + thisEpisode_loop * M_current_episode.shape[0]
        print(i)
        print(currentTrial.response)
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.800000)
        # update component parameters for each repeat
        trial_image.setImage(currentTrial.imagePath)
        trial_keyresp = keyboard.Keyboard()
        trial_color.setImage(currentTrial.colorPath)
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
                trial_image.setImage(currentTrial.imagePath, log=False)
            
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
                feedback_text.setText('Time Out')
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    M.at[current_index, 'sbjResp'] = theseKeys.name  # just the last key pressed
                    M.at[current_index, 'sbjRT'] = theseKeys.rt
                    # was this 'correct'?
                    print(theseKeys.name)
                    print('check')
                    
                    if (theseKeys.name == str(currentTrial.response)) or (theseKeys.name == currentTrial.response):
                        M.at[current_index, 'sbjCorr'] = 1
                        feedback_text.setText('Correct')
                    else:
                        M.at[current_index, 'sbjCorr'] = 0
                        feedback_text.setText('Incorrect')
                    # a response ends the routine
                    continueRoutine = False
            
            
            
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
        # check responses
        if trial_keyresp.keys in ['', [], None]:  # No response was made
            trial_keyresp.keys = None
        routineTimer.reset()
        
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
    # check responses
    if break_key_resp.keys in ['', [], None]:  # No response was made
        break_key_resp.keys = None
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
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
# the Routine "BYE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
M.to_csv(subjectfile, index=False)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
