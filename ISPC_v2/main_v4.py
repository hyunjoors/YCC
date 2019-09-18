#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard
import os  # handy system and path functions
import sys  # to get file system encoding
sys.path.append('./bin')
sys.path.append('./data')
from bin.ISPC_v2_trialGen import ISPC_v2_trialGen


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'ISPC_v2'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp

# generate trial sequences
csv_gen = ISPC_v2_trialGen(expInfo['participant'])
m_exp, map_exp = csv_gen.exp()
instr_body1 = ''.join([
    "Unlike practice, you will now see names (instead of XXX) written across the face.\n",
    "It may or may not be the name for the current face.\n",
    "Your task is to identify the face, not the name.\n",
    "If the face is [%s], press \'%s\'\n",
    "If the face is [%s], press \'%s\'\n",
    "If the face is [%s], press \'%s\'\n\n",
    "Try to respond as fast as you can without sacrificing the accuracy.\n"
]) % (map_exp[0][0], map_exp[0][1], map_exp[1][0], map_exp[1][1], map_exp[2][0], map_exp[2][1])
instr_body2 = "Use ONLY your RIGHT INDEX finger to respond."
instr_body3 = ''.join([
    "Raise your hand now if you have questions.\n",
    "Else, press space bar to start."
])


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expName, expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='/Users/HyunJoo/Documents/Yu-Chin Lab/ISPC_v2/main_v3.py',
                                 savePickle=False, saveWideText=False,
                                 dataFileName=filename)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# # this outputs to the screen, not a file
# logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp
####################
# save an aborted file 

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_text1 = visual.TextStim(win=win, name='instr_text1',
                             text=instr_body1,
                             font='Arial',
                             pos=(-0.5, 0.07), height=0.04, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             alignHoriz='left', languageStyle='LTR',
                             depth=0.0)
# Initialize components for Routine "instr"
instr_text2 = visual.TextStim(win=win, name='instr_text2',
                             text=instr_body2,
                             font='Arial',
                             pos=(-0.5, -0.2), height=0.04, wrapWidth=None, ori=0,
                             color='red', colorSpace='rgb', opacity=1,
                             bold=True, alignHoriz='left', languageStyle='LTR',
                             depth=0.0)
# Initialize components for Routine "instr"
instr_text3 = visual.TextStim(win=win, name='instr_text3',
                             text=instr_body3,
                             font='Arial',
                             pos=(-0.5, -0.3), height=0.04, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             alignHoriz='left', languageStyle='LTR',
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
                             text='This is a break between blocks.\n\nYou have 20 seconds to break.\nYou can also start by pressing \'space\'.',
                             font='Arial',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0)

# Initialize components for Routine "BYE"
BYEClock = core.Clock()
BYETEXT = visual.TextStim(win=win, name='BYETEXT',
    text='THANK YOU FOR YOUR PARTICIPATION.\nRAISE YOUR HAND TO GET RA',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()




# ------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr_key_resp = keyboard.Keyboard()
# keep track of which components have finished
instrComponents = [instr_text1, instr_text2, instr_text3, instr_key_resp]
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

    # *instr_text1* updates
    if t >= 0.0 and instr_text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text1.tStart = t  # not accounting for scr refresh
        instr_text1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_text1, 'tStartRefresh')  # time at next scr refresh
        instr_text1.setAutoDraw(True)
    # *instr_text2* updates
    if t >= 0.0 and instr_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text2.tStart = t  # not accounting for scr refresh
        instr_text2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_text2, 'tStartRefresh')  # time at next scr refresh
        instr_text2.setAutoDraw(True)
    # *instr_text3* updates
    if t >= 0.0 and instr_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_text3.tStart = t  # not accounting for scr refresh
        instr_text3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instr_text3, 'tStartRefresh')  # time at next scr refresh
        instr_text3.setAutoDraw(True)

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
        theseKeys = instr_key_resp.getKeys(keyList=["space"], waitRelease=False)
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
# if instr_key_resp.keys in ['', [], None]:  # No response was made
#     instr_key_resp.keys = None
##HYUN## why do I need to check a response?
instr_key_resp.clearEvents(eventType='keyboard')
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

for bid in range(1,6):
    block_m = m_exp.loc[m_exp.bid == bid]
    # ------ "trial_routine"-------
    for i, currentTrial in block_m.iterrows():
        currentRow = 72 * (bid-1) + i
        # print(bid, i, currentTrial.corrResp, curren   tRow)
        # ------Prepare to start Routine "trial_routine"-------
        t = 0
        trial_routineClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.200000)
        # update component parameters for each repeat
        trial_key_resp = keyboard.Keyboard()
        trial_faceImage.setImage(currentTrial.face_path)
        trial_nameText.setText(currentTrial.nid)
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
            # *Collect keys until a certain
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
            frameRemains = 0.2 + 1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if trial_key_resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                trial_key_resp.tStop = t  # not accounting for scr refresh
                trial_key_resp.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(trial_key_resp, 'tStopRefresh')
                trial_key_resp.status = FINISHED
            if trial_key_resp.status == STARTED:
                theseKeys = trial_key_resp.getKeys(keyList=['v', 'b', 'n'], waitRelease=False)

                trial_feedback_text.setText("Too Slow") ##YCC## re
                trial_feedback_text.setColor('white', 'rgb')
                if len(theseKeys):
                    trial_key_resp.status = FINISHED ##YCC## needs to be changed 
                    theseKeys = theseKeys[0]  # at least one key was pressed

                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if trial_key_resp.keys == []:  # then this was the first keypress
                        trial_key_resp.keys = theseKeys.name  # just the first key pressed
                        trial_key_resp.rt = theseKeys.rt
                        # was this 'correct'?
                        # print(bid, i, currentRow)
                        # print(trial_key_resp.keys, theseKeys.name, currentTrial.corrResp, trial_key_resp.keys == currentTrial.corrResp)
                        if trial_key_resp.keys == currentTrial.corrResp:
                            trial_key_resp.corr = 1
                            m_exp.at[(m_exp.bid == bid) & (m_exp.tid == i+1), 'sbjCorr'] = 1
                            trial_feedback_text.setText("Correct") ##YCC## change the color in green
                            trial_feedback_text.setColor('green', 'rgb')
                        else:
                            trial_key_resp.corr = 0
                            # m_exp[i, 'sbjCorr'] = 0
                            # m_exp.at[currentRow, 'sbjCorr'] = 0
                            m_exp.at[(m_exp.bid == bid) & (m_exp.tid == i+1), 'sbjCorr'] = 0
                            trial_feedback_text.setText("Incorrect") ##YCC## change the color 
                            trial_feedback_text.setColor('red', 'rgb')
                        # m_exp[i, 'sbjResp'] = theseKeys.name
                        # m_exp.at[currentRow, 'sbjResp'] = theseKeys.name
                        m_exp.at[(m_exp.bid == bid) & (m_exp.tid == i+1), 'sbjResp'] = theseKeys.name
                        # m_exp.loc[i, 'sbjCorr'] = 1
                        # m_exp[i, 'sbjRT'] = theseKeys.rt * 1000
                        # m_exp.at[currentRow, 'sbjRT'] = theseKeys.rt * 1000
                        m_exp.at[(m_exp.bid == bid) & (m_exp.tid == i+1), 'sbjRT'] = theseKeys.rt * 1000
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
            frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
            frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
        # print('current trial result')
        # print(m_exp.iloc[currentRow])
        # print()
        # the Routine "trial_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

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
            frameRemains = 0.0 + 0.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
            frameRemains = 0.5 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
        # the Routine "feedback_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    # completed 1 repeats of 'trials_loop'

    if bid < 5:
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
            frameRemains = 0.0 + 20 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
            frameRemains = 5.0 + 15 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if break_key_resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                break_key_resp.tStop = t  # not accounting for scr refresh
                break_key_resp.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(break_key_resp, 'tStopRefresh')
                break_key_resp.status = FINISHED
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
# completed 5 repeats of 'block_loop'


# ------Prepare to start Routine "BYE"-------
t = 0
BYEClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
BYEKEY = keyboard.Keyboard()
# keep track of which components have finished
BYEComponents = [BYETEXT, BYEKEY]
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

    # *BYETEXT* updates
    if t >= 0.0 and BYETEXT.status == NOT_STARTED:
        # keep track of start time/frame for later
        BYETEXT.tStart = t  # not accounting for scr refresh
        BYETEXT.frameNStart = frameN  # exact frame index
        win.timeOnFlip(BYETEXT, 'tStartRefresh')  # time at next scr refresh
        BYETEXT.setAutoDraw(True)

    # *BYEKEY* updates
    if t >= 0.0 and BYEKEY.status == NOT_STARTED:
        # keep track of start time/frame for later
        BYEKEY.tStart = t  # not accounting for scr refresh
        BYEKEY.frameNStart = frameN  # exact frame index
        win.timeOnFlip(BYEKEY, 'tStartRefresh')  # time at next scr refresh
        BYEKEY.status = STARTED
        # keyboard checking is just starting
        BYEKEY.clearEvents(eventType='keyboard')
    if BYEKEY.status == STARTED:
        theseKeys = BYEKEY.getKeys(
            keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
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
# the Routine "BYE" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

m_exp.to_csv(filename+'.csv', index=False)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

