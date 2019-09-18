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
expName = 'ISPC_v2_prac'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp

# generate trial sequences
csv_gen = ISPC_v2_trialGen(expInfo['participant'])
m_prac, map_prac = csv_gen.practice()
prac_instr_body1 = ''.join([
    "Your task here is to identify the \"face\" presented on each trial by pressing the designated key.\n",
    "Your task is to identify the face, not the name.\n",
    "If the face is [%s], press \'%s\'\n",
    "If the face is [%s], press \'%s\'\n",
    "If the face is [%s], press \'%s\'\n\n",
    "Try to respond as fast as you can without sacrificing the accuracy.\n"
]) % (map_prac[0][0], map_prac[0][1], map_prac[1][0], map_prac[1][1], map_prac[2][0], map_prac[2][1])
prac_instr_body2 = "Use ONLY your RIGHT HAND's index, middle and ring fingers to press the v/b/n keys."
prac_instr_body3 = ''.join([
    "Raise your hand now if you have questions.\n",
    "Else, press space bar to start."
])

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s' % (expName, expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='/Users/HyunJoo/Documents/Yu-Chin Lab/ISPC_v2/stroop.py',
                                 savePickle=False, saveWideText=False,
                                 dataFileName=filename)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# # this outputs to the screen, not a file
# logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp

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

# Initialize components for Routine "prac_instr"
prac_instrClock = core.Clock()
prac_instr_text1 = visual.TextStim(win=win, name='prac_instr_text1',
                             text=prac_instr_body1,
                             font='Arial',
                             pos=(-0.5, 0.07), height=0.04, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             alignHoriz='left', languageStyle='LTR',
                             depth=0.0)
# Initialize components for Routine "instr"
prac_instr_text2 = visual.TextStim(win=win, name='prac_instr_text2',
                             text=prac_instr_body2,
                             font='Arial',
                             pos=(-0.5, -0.2), height=0.04, wrapWidth=None, ori=0,
                             color='red', colorSpace='rgb', opacity=1,
                             bold=True, alignHoriz='left', languageStyle='LTR',
                             depth=0.0)
# Initialize components for Routine "instr"
prac_instr_text3 = visual.TextStim(win=win, name='prac_instr_text3',
                             text=prac_instr_body3,
                             font='Arial',
                             pos=(-0.5, -0.3), height=0.04, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             alignHoriz='left', languageStyle='LTR',
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
                                      pos=(0, -0.05), height=0.06, wrapWidth=None, ori=0,
                                      color='red', colorSpace='rgb', opacity=1,
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

# Initialize components for Routine "prac_accuracy_routine"
prac_accuracy_routineClock = core.Clock()
prac_accuracy_text = visual.TextStim(win=win, name='prac_accuracy_text',
                                     text='Accuracy check',
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
prac_instrComponents = [prac_instr_text1, prac_instr_text2, prac_instr_text3, instr_prac_key_resp]
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

    # *prac_instr_text1* updates
    if t >= 0.0 and prac_instr_text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        prac_instr_text1.tStart = t  # not accounting for scr refresh
        prac_instr_text1.frameNStart = frameN  # exact frame index
        # time at next scr refresh
        win.timeOnFlip(prac_instr_text1, 'tStartRefresh')
        prac_instr_text1.setAutoDraw(True)
    # *prac_instr_text2* updates
    if t >= 0.0 and prac_instr_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        prac_instr_text2.tStart = t  # not accounting for scr refresh
        prac_instr_text2.frameNStart = frameN  # exact frame index
        # time at next scr refresh
        win.timeOnFlip(prac_instr_text2, 'tStartRefresh')
        prac_instr_text2.setAutoDraw(True)
    # *prac_instr_tex3t* updates
    if t >= 0.0 and prac_instr_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        prac_instr_text3.tStart = t  # not accounting for scr refresh
        prac_instr_text3.frameNStart = frameN  # exact frame index
        # time at next scr refresh
        win.timeOnFlip(prac_instr_text3, 'tStartRefresh')
        prac_instr_text3.setAutoDraw(True)

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
            keyList=["space"], waitRelease=False)
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
# check responses
if instr_prac_key_resp.keys in ['', [], None]:  # No response was made
    instr_prac_key_resp.keys = None
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()





# ------Prepare to start Routine "prac_trial"-------
continueRoutine = True

# -------Start Loop "prac_trial"-------
while 1:
    # -------Start Routine "prac_trial_routine"-------
    for i, currentTrial in m_prac.iterrows():
        # ------Prepare to start Routine "prac_trial_routine"-------
        t = 0
        prac_trial_routineClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.200000)
        # update component parameters for each repeat
        prac_trial_key_resp = keyboard.Keyboard()
        prac_trial_faceImage.setImage(currentTrial.face_path)
        prac_trial_nameText.setText(currentTrial.nid)
        # keep track of which components have finished
        prac_trial_routineComponents = [prac_trial_key_resp, prac_trial_faceImage, prac_trial_nameText]
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
                        if (prac_trial_key_resp.keys == str(currentTrial.corrResp)) or (prac_trial_key_resp.keys == currentTrial.corrResp):
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
            frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
            frameRemains = 0.2 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
        m_prac.loc[i, 'sbjResp'] = prac_trial_key_resp.keys
        m_prac.loc[i, 'sbjCorr'] = prac_trial_key_resp.corr
        if prac_trial_key_resp.keys != None:  # we had a response
            m_prac.loc[i, 'sbjRT'] = prac_trial_key_resp.rt
        else:
            m_prac.loc[i, 'sbjRT'] = 0

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


    # # ------Prepare to start Routine "prac_accuracy_routine"-------
    t = 0
    prac_accuracy_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prac_accuracy_key_resp = keyboard.Keyboard()
    # keep track of which components have finished
    prac_accuracy_routineComponents = [prac_accuracy_text, prac_accuracy_key_resp]
    for thisComponent in prac_accuracy_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "prac_accuracy_routine"-------
    while continueRoutine:
        # get current time
        t = prac_accuracy_routineClock.getTime()
        frameN = frameN + 1 # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n_trial = len(m_prac)
        n_corr = len(m_prac.loc[(m_prac.sbjCorr == 1)])
        prac_accuracy_body = 'Your Accuracy {}%\n\nRaise your hand to get an instructor.\n\nPress \'escape\' to quit the practice.\nPress \'r\' to repeat the practice'.format(n_corr/n_trial*100)
        prac_accuracy_text.setText(prac_accuracy_body)

        # *prac_accuracy_text* updates
        if t >= 0.0 and prac_accuracy_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_accuracy_text.tStart = t  # not accounting for scr refresh
            prac_accuracy_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prac_accuracy_text, 'tStartRefresh') # time at next scr refresh
            prac_accuracy_text.setAutoDraw(True)

        # *prac_accuracy_key_resp* updates
        if t >= 0.0 and prac_accuracy_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_accuracy_key_resp.tStart = t  # not accounting for scr refresh
            prac_accuracy_key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prac_accuracy_key_resp, 'tStartRefresh') # time at next scr refresh
            prac_accuracy_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(prac_accuracy_key_resp.clock.reset) # t=0 on next screen flip
            prac_accuracy_key_resp.clearEvents(eventType='keyboard')
            
        if prac_accuracy_key_resp.status == STARTED:
            theseKeys = prac_accuracy_key_resp.getKeys(keyList=['r'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                prac_accuracy_key_resp.keys = theseKeys.name  # just the last key pressed
                prac_accuracy_key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_accuracy_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "prac_accuracy_routine"-------
    for thisComponent in prac_accuracy_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_accuracy_key_resp.keys in ['', [], None]:  # No response was made
        prac_accuracy_key_resp.keys = None
    
    routineTimer.reset()


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
