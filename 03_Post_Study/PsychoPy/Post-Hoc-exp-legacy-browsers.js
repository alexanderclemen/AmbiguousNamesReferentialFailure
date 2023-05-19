/********************* 
 * Post-Hoc-Exp Test *
 *********************/


// store info about the experiment session:
let expName = 'Post-Hoc-exp';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'Vorname': '', 'Nachname': '', 'Mit welchem Geschlecht identifiziert du dich? (m,w,nicht-binär,keine Angabe)': ''};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
flowScheduler.add(Intro2RoutineBegin());
flowScheduler.add(Intro2RoutineEachFrame());
flowScheduler.add(Intro2RoutineEnd());
flowScheduler.add(Intro3RoutineBegin());
flowScheduler.add(Intro3RoutineEachFrame());
flowScheduler.add(Intro3RoutineEnd());
const trials_Warm_UpLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_Warm_UpLoopBegin(trials_Warm_UpLoopScheduler));
flowScheduler.add(trials_Warm_UpLoopScheduler);
flowScheduler.add(trials_Warm_UpLoopEnd);
flowScheduler.add(Intro4RoutineBegin());
flowScheduler.add(Intro4RoutineEachFrame());
flowScheduler.add(Intro4RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(PauseRoutineBegin());
flowScheduler.add(PauseRoutineEachFrame());
flowScheduler.add(PauseRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(Blank1000RoutineBegin());
flowScheduler.add(Blank1000RoutineEachFrame());
flowScheduler.add(Blank1000RoutineEnd());
flowScheduler.add(GoodbyeScreenRoutineBegin());
flowScheduler.add(GoodbyeScreenRoutineEachFrame());
flowScheduler.add(GoodbyeScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Post-Hoc-List1.xlsx', 'path': 'Post-Hoc-List1.xlsx'},
    {'name': 'Post-Hoc-List2.xlsx', 'path': 'Post-Hoc-List2.xlsx'},
    {'name': 'Post-Hoc-Warm-Up.xlsx', 'path': 'Post-Hoc-Warm-Up.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var text_WelcomeScreen;
var Intro2Clock;
var text_Intro2;
var key_resp_Intro2;
var Intro3Clock;
var text_Intro3;
var key_resp_Intro3;
var Blank500Clock;
var text_Blank500;
var Warm_UpClock;
var text_WarmUp;
var slider_Buffer;
var Intro4Clock;
var text_Intro4;
var key_resp_Intro4;
var TrialClock;
var text_Trial;
var slider_Trial;
var PauseClock;
var text_Pause;
var key_resp;
var Blank1000Clock;
var text_Blank1000;
var GoodbyeScreenClock;
var text_GoodbyeScreen;
var key_resp_Goodbye;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  text_WelcomeScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_WelcomeScreen',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Intro2"
  Intro2Clock = new util.Clock();
  text_Intro2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Intro2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_Intro2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Intro3"
  Intro3Clock = new util.Clock();
  text_Intro3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Intro3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_Intro3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  text_Blank500 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Blank500',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Warm_Up"
  Warm_UpClock = new util.Clock();
  text_WarmUp = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_WarmUp',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_Buffer = new visual.Slider({
    win: psychoJS.window, name: 'slider_Buffer',
    size: [1.0, 0.1], pos: [0, (- 0.2)], units: 'height',
    labels: ["sehr m\u00e4nnlich", "", "", "neutral", "", "", "sehr weiblich"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "Intro4"
  Intro4Clock = new util.Clock();
  text_Intro4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Intro4',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_Intro4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial"
  TrialClock = new util.Clock();
  text_Trial = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Trial',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_Trial = new visual.Slider({
    win: psychoJS.window, name: 'slider_Trial',
    size: [1.0, 0.1], pos: [0, (- 0.2)], units: 'height',
    labels: ["sehr m\u00e4nnlich", "", "", "neutral", "", "", "sehr weiblich"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "Pause"
  PauseClock = new util.Clock();
  text_Pause = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Pause',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank1000"
  Blank1000Clock = new util.Clock();
  text_Blank1000 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Blank1000',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "GoodbyeScreen"
  GoodbyeScreenClock = new util.Clock();
  text_GoodbyeScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_GoodbyeScreen',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_Goodbye = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'WelcomeScreen'-------
    t = 0;
    WelcomeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    text_WelcomeScreen.setText('Hallo und vielen Dank, dass Du am zweiten und letzten Teil meiner Studie teilnimmst.');
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(text_WelcomeScreen);
    
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'WelcomeScreen'-------
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_WelcomeScreen* updates
    if (t >= 0 && text_WelcomeScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_WelcomeScreen.tStart = t;  // (not accounting for frame time here)
      text_WelcomeScreen.frameNStart = frameN;  // exact frame index
      
      text_WelcomeScreen.setAutoDraw(true);
    }

    frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_WelcomeScreen.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_WelcomeScreen.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'WelcomeScreen'-------
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_Intro2_allKeys;
var Intro2Components;
function Intro2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Intro2'-------
    t = 0;
    Intro2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Intro2.setText('Im Folgenden wirst Du einen Namen sehen sowie einen 7-stelligen Slider. Du bewertest den Namen von ganz links "sehr männlich" bis ganz rechts "sehr weiblich". Die Mitte der Skala zeigt "neutral" an.\n\nZum Beispiel würde ich "Uwe" als "sehr männlich", "Gudrun" als "sehr weiblich" und "Alex" als "neutral" bewerten. \n\nEs steht dir frei die Zwischenstufen zu benutzen.\n\n(Drücke die Leertaste.)');
    key_resp_Intro2.keys = undefined;
    key_resp_Intro2.rt = undefined;
    _key_resp_Intro2_allKeys = [];
    // keep track of which components have finished
    Intro2Components = [];
    Intro2Components.push(text_Intro2);
    Intro2Components.push(key_resp_Intro2);
    
    Intro2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Intro2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Intro2'-------
    // get current time
    t = Intro2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Intro2* updates
    if (t >= 0.0 && text_Intro2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Intro2.tStart = t;  // (not accounting for frame time here)
      text_Intro2.frameNStart = frameN;  // exact frame index
      
      text_Intro2.setAutoDraw(true);
    }

    
    // *key_resp_Intro2* updates
    if (t >= 0.0 && key_resp_Intro2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_Intro2.tStart = t;  // (not accounting for frame time here)
      key_resp_Intro2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_Intro2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro2.clearEvents(); });
    }

    if (key_resp_Intro2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_Intro2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_Intro2_allKeys = _key_resp_Intro2_allKeys.concat(theseKeys);
      if (_key_resp_Intro2_allKeys.length > 0) {
        key_resp_Intro2.keys = _key_resp_Intro2_allKeys[_key_resp_Intro2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_Intro2.rt = _key_resp_Intro2_allKeys[_key_resp_Intro2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Intro2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Intro2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Intro2'-------
    Intro2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_Intro2.keys', key_resp_Intro2.keys);
    if (typeof key_resp_Intro2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_Intro2.rt', key_resp_Intro2.rt);
        routineTimer.reset();
        }
    
    key_resp_Intro2.stop();
    // the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_Intro3_allKeys;
var Intro3Components;
function Intro3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Intro3'-------
    t = 0;
    Intro3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Intro3.setText('Wichtig ist, NICHT die assoziierten Qualitäten des Namens zu bewerten (Gudrun klingt hart/stark also "männlich"), sondern ob Du eher an einen Mann (der Uwe), eine Frau (die Gudrun) oder vielleicht beide (der/die Alex) denkst. \n\nKlicke mit der Maus auf einen der sieben Punkte an dem du denkst, wo sich der Name deiner Meinung nach befindet.\n\nNun Folgen drei Beispiele, an denen Du die Steuerung testen kannst. \n\n(Drücke die Leertaste.)');
    key_resp_Intro3.keys = undefined;
    key_resp_Intro3.rt = undefined;
    _key_resp_Intro3_allKeys = [];
    // keep track of which components have finished
    Intro3Components = [];
    Intro3Components.push(text_Intro3);
    Intro3Components.push(key_resp_Intro3);
    
    Intro3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Intro3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Intro3'-------
    // get current time
    t = Intro3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Intro3* updates
    if (t >= 0.0 && text_Intro3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Intro3.tStart = t;  // (not accounting for frame time here)
      text_Intro3.frameNStart = frameN;  // exact frame index
      
      text_Intro3.setAutoDraw(true);
    }

    
    // *key_resp_Intro3* updates
    if (t >= 0.0 && key_resp_Intro3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_Intro3.tStart = t;  // (not accounting for frame time here)
      key_resp_Intro3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_Intro3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro3.clearEvents(); });
    }

    if (key_resp_Intro3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_Intro3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_Intro3_allKeys = _key_resp_Intro3_allKeys.concat(theseKeys);
      if (_key_resp_Intro3_allKeys.length > 0) {
        key_resp_Intro3.keys = _key_resp_Intro3_allKeys[_key_resp_Intro3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_Intro3.rt = _key_resp_Intro3_allKeys[_key_resp_Intro3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Intro3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Intro3RoutineEnd() {
  return async function () {
    //------Ending Routine 'Intro3'-------
    Intro3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_Intro3.keys', key_resp_Intro3.keys);
    if (typeof key_resp_Intro3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_Intro3.rt', key_resp_Intro3.rt);
        routineTimer.reset();
        }
    
    key_resp_Intro3.stop();
    // the Routine "Intro3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_Warm_Up;
var currentLoop;
function trials_Warm_UpLoopBegin(trials_Warm_UpLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_Warm_Up = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Post-Hoc-Warm-Up.xlsx', '0:3'),
      seed: undefined, name: 'trials_Warm_Up'
    });
    psychoJS.experiment.addLoop(trials_Warm_Up); // add the loop to the experiment
    currentLoop = trials_Warm_Up;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_Warm_Up.forEach(function() {
      const snapshot = trials_Warm_Up.getSnapshot();
    
      trials_Warm_UpLoopScheduler.add(importConditions(snapshot));
      trials_Warm_UpLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials_Warm_UpLoopScheduler.add(Blank500RoutineEachFrame());
      trials_Warm_UpLoopScheduler.add(Blank500RoutineEnd());
      trials_Warm_UpLoopScheduler.add(Warm_UpRoutineBegin(snapshot));
      trials_Warm_UpLoopScheduler.add(Warm_UpRoutineEachFrame());
      trials_Warm_UpLoopScheduler.add(Warm_UpRoutineEnd());
      trials_Warm_UpLoopScheduler.add(endLoopIteration(trials_Warm_UpLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_Warm_UpLoopEnd() {
  psychoJS.experiment.removeLoop(trials_Warm_Up);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Post-Hoc-List1.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trialsLoopScheduler.add(Blank500RoutineEachFrame());
      trialsLoopScheduler.add(Blank500RoutineEnd());
      trialsLoopScheduler.add(TrialRoutineBegin(snapshot));
      trialsLoopScheduler.add(TrialRoutineEachFrame());
      trialsLoopScheduler.add(TrialRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Post-Hoc-List2.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      const snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials_2LoopScheduler.add(Blank500RoutineEachFrame());
      trials_2LoopScheduler.add(Blank500RoutineEnd());
      trials_2LoopScheduler.add(TrialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(TrialRoutineEachFrame());
      trials_2LoopScheduler.add(TrialRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var Blank500Components;
function Blank500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Blank500'-------
    t = 0;
    Blank500Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    text_Blank500.setText('');
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(text_Blank500);
    
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Blank500RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Blank500'-------
    // get current time
    t = Blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Blank500* updates
    if (t >= 0.0 && text_Blank500.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Blank500.tStart = t;  // (not accounting for frame time here)
      text_Blank500.frameNStart = frameN;  // exact frame index
      
      text_Blank500.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_Blank500.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_Blank500.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank500RoutineEnd() {
  return async function () {
    //------Ending Routine 'Blank500'-------
    Blank500Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var Warm_UpComponents;
function Warm_UpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Warm_Up'-------
    t = 0;
    Warm_UpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_WarmUp.setText(Post_Hoc_Item);
    slider_Buffer.reset()
    // keep track of which components have finished
    Warm_UpComponents = [];
    Warm_UpComponents.push(text_WarmUp);
    Warm_UpComponents.push(slider_Buffer);
    
    Warm_UpComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Warm_UpRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Warm_Up'-------
    // get current time
    t = Warm_UpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_WarmUp* updates
    if (t >= 0.0 && text_WarmUp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_WarmUp.tStart = t;  // (not accounting for frame time here)
      text_WarmUp.frameNStart = frameN;  // exact frame index
      
      text_WarmUp.setAutoDraw(true);
    }

    
    // *slider_Buffer* updates
    if (t >= 0.0 && slider_Buffer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_Buffer.tStart = t;  // (not accounting for frame time here)
      slider_Buffer.frameNStart = frameN;  // exact frame index
      
      slider_Buffer.setAutoDraw(true);
    }

    
    // Check slider_Buffer for response to end routine
    if (slider_Buffer.getRating() !== undefined && slider_Buffer.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Warm_UpComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Warm_UpRoutineEnd() {
  return async function () {
    //------Ending Routine 'Warm_Up'-------
    Warm_UpComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_Buffer.response', slider_Buffer.getRating());
    psychoJS.experiment.addData('slider_Buffer.rt', slider_Buffer.getRT());
    // the Routine "Warm_Up" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_Intro4_allKeys;
var Intro4Components;
function Intro4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Intro4'-------
    t = 0;
    Intro4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Intro4.setText('Wie Du gesehen hast, geht es nachdem du auf den Slider klickst sofort weiter. Sei also vorsichtig bei deiner Auswahl und klicke bitte auf, und nicht zwischen die Schnittstellen. \n\nDu hast kein Zeitlimit.\n\nNach ca 5 bis 7 Minuten hast du eine Pause\n\nDrücke die Leertaste um das Experiment zu starten.');
    key_resp_Intro4.keys = undefined;
    key_resp_Intro4.rt = undefined;
    _key_resp_Intro4_allKeys = [];
    // keep track of which components have finished
    Intro4Components = [];
    Intro4Components.push(text_Intro4);
    Intro4Components.push(key_resp_Intro4);
    
    Intro4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Intro4RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Intro4'-------
    // get current time
    t = Intro4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Intro4* updates
    if (t >= 0.0 && text_Intro4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Intro4.tStart = t;  // (not accounting for frame time here)
      text_Intro4.frameNStart = frameN;  // exact frame index
      
      text_Intro4.setAutoDraw(true);
    }

    
    // *key_resp_Intro4* updates
    if (t >= 0.0 && key_resp_Intro4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_Intro4.tStart = t;  // (not accounting for frame time here)
      key_resp_Intro4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_Intro4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro4.clearEvents(); });
    }

    if (key_resp_Intro4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_Intro4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_Intro4_allKeys = _key_resp_Intro4_allKeys.concat(theseKeys);
      if (_key_resp_Intro4_allKeys.length > 0) {
        key_resp_Intro4.keys = _key_resp_Intro4_allKeys[_key_resp_Intro4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_Intro4.rt = _key_resp_Intro4_allKeys[_key_resp_Intro4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Intro4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Intro4RoutineEnd() {
  return async function () {
    //------Ending Routine 'Intro4'-------
    Intro4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_Intro4.keys', key_resp_Intro4.keys);
    if (typeof key_resp_Intro4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_Intro4.rt', key_resp_Intro4.rt);
        routineTimer.reset();
        }
    
    key_resp_Intro4.stop();
    // the Routine "Intro4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var TrialComponents;
function TrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Trial'-------
    t = 0;
    TrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Trial.setText(Post_Hoc_Item);
    slider_Trial.reset()
    // keep track of which components have finished
    TrialComponents = [];
    TrialComponents.push(text_Trial);
    TrialComponents.push(slider_Trial);
    
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TrialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Trial'-------
    // get current time
    t = TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Trial* updates
    if (t >= 0.0 && text_Trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Trial.tStart = t;  // (not accounting for frame time here)
      text_Trial.frameNStart = frameN;  // exact frame index
      
      text_Trial.setAutoDraw(true);
    }

    
    // *slider_Trial* updates
    if (t >= 0.0 && slider_Trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_Trial.tStart = t;  // (not accounting for frame time here)
      slider_Trial.frameNStart = frameN;  // exact frame index
      
      slider_Trial.setAutoDraw(true);
    }

    
    // Check slider_Trial for response to end routine
    if (slider_Trial.getRating() !== undefined && slider_Trial.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialRoutineEnd() {
  return async function () {
    //------Ending Routine 'Trial'-------
    TrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_Trial.response', slider_Trial.getRating());
    psychoJS.experiment.addData('slider_Trial.rt', slider_Trial.getRT());
    // the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var PauseComponents;
function PauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pause'-------
    t = 0;
    PauseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Pause.setText('Super! Du hast die Hälfte geschafft.\n\nDu hast dir eine Pause verdient.\n\nWeiter geht es, wenn du "P" drückst');
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    PauseComponents = [];
    PauseComponents.push(text_Pause);
    PauseComponents.push(key_resp);
    
    PauseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PauseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pause'-------
    // get current time
    t = PauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Pause* updates
    if (t >= 0.0 && text_Pause.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Pause.tStart = t;  // (not accounting for frame time here)
      text_Pause.frameNStart = frameN;  // exact frame index
      
      text_Pause.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PauseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PauseRoutineEnd() {
  return async function () {
    //------Ending Routine 'Pause'-------
    PauseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Blank1000Components;
function Blank1000RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Blank1000'-------
    t = 0;
    Blank1000Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    text_Blank1000.setText('');
    // keep track of which components have finished
    Blank1000Components = [];
    Blank1000Components.push(text_Blank1000);
    
    Blank1000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Blank1000RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Blank1000'-------
    // get current time
    t = Blank1000Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Blank1000* updates
    if (t >= 0.0 && text_Blank1000.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Blank1000.tStart = t;  // (not accounting for frame time here)
      text_Blank1000.frameNStart = frameN;  // exact frame index
      
      text_Blank1000.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_Blank1000.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_Blank1000.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank1000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank1000RoutineEnd() {
  return async function () {
    //------Ending Routine 'Blank1000'-------
    Blank1000Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_Goodbye_allKeys;
var GoodbyeScreenComponents;
function GoodbyeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'GoodbyeScreen'-------
    t = 0;
    GoodbyeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_GoodbyeScreen.setText('Vielen Dank, dass Du an meinem Experiment teilgenommen hast.\n\nWenn du mir deine Zahlungsdetails noch nicht genannt hast, kannst du mir gerne eine Email senden.\n\nDrücke die Leertaste um das Experiment zu beenden.\n\nTschüss.');
    key_resp_Goodbye.keys = undefined;
    key_resp_Goodbye.rt = undefined;
    _key_resp_Goodbye_allKeys = [];
    // keep track of which components have finished
    GoodbyeScreenComponents = [];
    GoodbyeScreenComponents.push(text_GoodbyeScreen);
    GoodbyeScreenComponents.push(key_resp_Goodbye);
    
    GoodbyeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function GoodbyeScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'GoodbyeScreen'-------
    // get current time
    t = GoodbyeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_GoodbyeScreen* updates
    if (t >= 0.0 && text_GoodbyeScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_GoodbyeScreen.tStart = t;  // (not accounting for frame time here)
      text_GoodbyeScreen.frameNStart = frameN;  // exact frame index
      
      text_GoodbyeScreen.setAutoDraw(true);
    }

    
    // *key_resp_Goodbye* updates
    if (t >= 0.0 && key_resp_Goodbye.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_Goodbye.tStart = t;  // (not accounting for frame time here)
      key_resp_Goodbye.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_Goodbye.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Goodbye.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Goodbye.clearEvents(); });
    }

    if (key_resp_Goodbye.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_Goodbye.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_Goodbye_allKeys = _key_resp_Goodbye_allKeys.concat(theseKeys);
      if (_key_resp_Goodbye_allKeys.length > 0) {
        key_resp_Goodbye.keys = _key_resp_Goodbye_allKeys[_key_resp_Goodbye_allKeys.length - 1].name;  // just the last key pressed
        key_resp_Goodbye.rt = _key_resp_Goodbye_allKeys[_key_resp_Goodbye_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    GoodbyeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GoodbyeScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'GoodbyeScreen'-------
    GoodbyeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_Goodbye.keys', key_resp_Goodbye.keys);
    if (typeof key_resp_Goodbye.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_Goodbye.rt', key_resp_Goodbye.rt);
        routineTimer.reset();
        }
    
    key_resp_Goodbye.stop();
    // the Routine "GoodbyeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
