/************************** 
 * Norming_Study_Exp Test *
 **************************/


// store info about the experiment session:
let expName = 'Norming_Study_exp';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(Intro1RoutineBegin());
flowScheduler.add(Intro1RoutineEachFrame());
flowScheduler.add(Intro1RoutineEnd());
flowScheduler.add(AgeRoutineBegin());
flowScheduler.add(AgeRoutineEachFrame());
flowScheduler.add(AgeRoutineEnd());
flowScheduler.add(MuttersprachlerRoutineBegin());
flowScheduler.add(MuttersprachlerRoutineEachFrame());
flowScheduler.add(MuttersprachlerRoutineEnd());
flowScheduler.add(Intro2RoutineBegin());
flowScheduler.add(Intro2RoutineEachFrame());
flowScheduler.add(Intro2RoutineEnd());
const trials_OtherNameLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_OtherNameLoopBegin(trials_OtherNameLoopScheduler));
flowScheduler.add(trials_OtherNameLoopScheduler);
flowScheduler.add(trials_OtherNameLoopEnd);
flowScheduler.add(Intro3RoutineBegin());
flowScheduler.add(Intro3RoutineEachFrame());
flowScheduler.add(Intro3RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(Blank1000RoutineBegin());
flowScheduler.add(Blank1000RoutineEachFrame());
flowScheduler.add(Blank1000RoutineEnd());
flowScheduler.add(biologicalSexRoutineBegin());
flowScheduler.add(biologicalSexRoutineEachFrame());
flowScheduler.add(biologicalSexRoutineEnd());
flowScheduler.add(GenderIdentityRoutineBegin());
flowScheduler.add(GenderIdentityRoutineEachFrame());
flowScheduler.add(GenderIdentityRoutineEnd());
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
    {'name': 'Norming_Buffer.xlsx', 'path': 'Norming_Buffer.xlsx'},
    {'name': 'Norming_CommonNames_Filtered.xlsx', 'path': 'Norming_CommonNames_Filtered.xlsx'}
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
var key_resp_WelcomeScreen;
var Intro1Clock;
var text_Intro1;
var key_resp_Intro1;
var AgeClock;
var text_Age;
var slider_Age;
var key_Age;
var MuttersprachlerClock;
var text_Muttersprachler;
var slider_Muttersprache;
var key_Muttersprachler;
var Intro2Clock;
var key_Intro2;
var text_Intro2;
var Blank500Clock;
var text_Blank500;
var OtherNameClock;
var text_Buffer;
var slider_Buffer;
var Intro3Clock;
var text_Intro3;
var key_resp_2;
var TrialClock;
var text_Trial;
var slider_Trial;
var Blank1000Clock;
var text_Blank1000;
var biologicalSexClock;
var text_biologicalSex;
var slider_biologicalSex;
var key_biologicalSex;
var GenderIdentityClock;
var text_GenderIdentity;
var slider;
var key_resp;
var GoodbyeScreenClock;
var text_GoodbyeScreen;
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
  
  key_resp_WelcomeScreen = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Intro1"
  Intro1Clock = new util.Clock();
  text_Intro1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Intro1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_Intro1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Age"
  AgeClock = new util.Clock();
  text_Age = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Age',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_Age = new visual.Slider({
    win: psychoJS.window, name: 'slider_Age',
    size: [1.0, 0.1], pos: [0, (- 0.2)], units: 'height',
    labels: ["17-", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30+"], ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  key_Age = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Muttersprachler"
  MuttersprachlerClock = new util.Clock();
  text_Muttersprachler = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Muttersprachler',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_Muttersprache = new visual.Slider({
    win: psychoJS.window, name: 'slider_Muttersprache',
    size: [1.0, 0.1], pos: [0, (- 0.2)], units: 'height',
    labels: ["ja", "nein"], ticks: [1, 2],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  key_Muttersprachler = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Intro2"
  Intro2Clock = new util.Clock();
  key_Intro2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_Intro2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Intro2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
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
  
  // Initialize components for Routine "OtherName"
  OtherNameClock = new util.Clock();
  text_Buffer = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Buffer',
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
  
  // Initialize components for Routine "Intro3"
  Intro3Clock = new util.Clock();
  text_Intro3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Intro3',
    text: 'Wie du gesehen hast geht es sofort weiter nachdem du auf den Slider geklickt hast. Sei also vorsichtig bei deiner Auswahl.\n\nDrücke die Leertaste um das Experiment zu starten.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  // Initialize components for Routine "biologicalSex"
  biologicalSexClock = new util.Clock();
  text_biologicalSex = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_biologicalSex',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_biologicalSex = new visual.Slider({
    win: psychoJS.window, name: 'slider_biologicalSex',
    size: [1.0, 0.1], pos: [0, (- 0.3)], units: 'height',
    labels: ["m\u00e4nnlich", "divers", "weiblich"], ticks: [1, 2, 3],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  key_biologicalSex = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "GenderIdentity"
  GenderIdentityClock = new util.Clock();
  text_GenderIdentity = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_GenderIdentity',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.0, 0.1], pos: [0, (- 0.3)], units: 'height',
    labels: ["m\u00e4nnlich", "", "", "", "", "", "weiblich"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "GoodbyeScreen"
  GoodbyeScreenClock = new util.Clock();
  text_GoodbyeScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_GoodbyeScreen',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_WelcomeScreen_allKeys;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'WelcomeScreen'-------
    t = 0;
    WelcomeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_WelcomeScreen.setText('Hallo und vielen Dank dass Du an meiner Studie teilnimmst.\n\nDrücke die Leertaste um fortzufahren.');
    key_resp_WelcomeScreen.keys = undefined;
    key_resp_WelcomeScreen.rt = undefined;
    _key_resp_WelcomeScreen_allKeys = [];
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(text_WelcomeScreen);
    WelcomeScreenComponents.push(key_resp_WelcomeScreen);
    
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'WelcomeScreen'-------
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_WelcomeScreen* updates
    if (t >= 0.0 && text_WelcomeScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_WelcomeScreen.tStart = t;  // (not accounting for frame time here)
      text_WelcomeScreen.frameNStart = frameN;  // exact frame index
      
      text_WelcomeScreen.setAutoDraw(true);
    }

    
    // *key_resp_WelcomeScreen* updates
    if (t >= 0.0 && key_resp_WelcomeScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_WelcomeScreen.tStart = t;  // (not accounting for frame time here)
      key_resp_WelcomeScreen.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_WelcomeScreen.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_WelcomeScreen.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_WelcomeScreen.clearEvents(); });
    }

    if (key_resp_WelcomeScreen.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_WelcomeScreen.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_WelcomeScreen_allKeys = _key_resp_WelcomeScreen_allKeys.concat(theseKeys);
      if (_key_resp_WelcomeScreen_allKeys.length > 0) {
        key_resp_WelcomeScreen.keys = _key_resp_WelcomeScreen_allKeys[_key_resp_WelcomeScreen_allKeys.length - 1].name;  // just the last key pressed
        key_resp_WelcomeScreen.rt = _key_resp_WelcomeScreen_allKeys[_key_resp_WelcomeScreen_allKeys.length - 1].rt;
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
    WelcomeScreenComponents.forEach( function(thisComponent) {
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


function WelcomeScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'WelcomeScreen'-------
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_WelcomeScreen.keys', key_resp_WelcomeScreen.keys);
    if (typeof key_resp_WelcomeScreen.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_WelcomeScreen.rt', key_resp_WelcomeScreen.rt);
        routineTimer.reset();
        }
    
    key_resp_WelcomeScreen.stop();
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_Intro1_allKeys;
var Intro1Components;
function Intro1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Intro1'-------
    t = 0;
    Intro1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Intro1.setText('Ich versuche zu verstehen wie Vornamen im mentalen Lexikon abgespeichert sind und dafür brauche ich (d)eine Datengrundlage. Vorerst brauche ich jedoch noch personenbezogene Daten.  Keine Sorge die Daten werden anonymisiert.\n\n(Drücke die Leertaste um fortzufahren.)');
    key_resp_Intro1.keys = undefined;
    key_resp_Intro1.rt = undefined;
    _key_resp_Intro1_allKeys = [];
    // keep track of which components have finished
    Intro1Components = [];
    Intro1Components.push(text_Intro1);
    Intro1Components.push(key_resp_Intro1);
    
    Intro1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Intro1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Intro1'-------
    // get current time
    t = Intro1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Intro1* updates
    if (t >= 0.0 && text_Intro1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Intro1.tStart = t;  // (not accounting for frame time here)
      text_Intro1.frameNStart = frameN;  // exact frame index
      
      text_Intro1.setAutoDraw(true);
    }

    
    // *key_resp_Intro1* updates
    if (t >= 0.0 && key_resp_Intro1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_Intro1.tStart = t;  // (not accounting for frame time here)
      key_resp_Intro1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_Intro1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_Intro1.clearEvents(); });
    }

    if (key_resp_Intro1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_Intro1.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_Intro1_allKeys = _key_resp_Intro1_allKeys.concat(theseKeys);
      if (_key_resp_Intro1_allKeys.length > 0) {
        key_resp_Intro1.keys = _key_resp_Intro1_allKeys[_key_resp_Intro1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_Intro1.rt = _key_resp_Intro1_allKeys[_key_resp_Intro1_allKeys.length - 1].rt;
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
    Intro1Components.forEach( function(thisComponent) {
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


function Intro1RoutineEnd() {
  return async function () {
    //------Ending Routine 'Intro1'-------
    Intro1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_Intro1.keys', key_resp_Intro1.keys);
    if (typeof key_resp_Intro1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_Intro1.rt', key_resp_Intro1.rt);
        routineTimer.reset();
        }
    
    key_resp_Intro1.stop();
    // the Routine "Intro1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_Age_allKeys;
var AgeComponents;
function AgeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Age'-------
    t = 0;
    AgeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Age.setText('Bitte trage auf dem Slider dein Alter ein.\n\n(Drücke die Leertaste um fortzufahren.)');
    slider_Age.reset()
    key_Age.keys = undefined;
    key_Age.rt = undefined;
    _key_Age_allKeys = [];
    // keep track of which components have finished
    AgeComponents = [];
    AgeComponents.push(text_Age);
    AgeComponents.push(slider_Age);
    AgeComponents.push(key_Age);
    
    AgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AgeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Age'-------
    // get current time
    t = AgeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Age* updates
    if (t >= 0.0 && text_Age.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Age.tStart = t;  // (not accounting for frame time here)
      text_Age.frameNStart = frameN;  // exact frame index
      
      text_Age.setAutoDraw(true);
    }

    
    // *slider_Age* updates
    if (t >= 0.0 && slider_Age.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_Age.tStart = t;  // (not accounting for frame time here)
      slider_Age.frameNStart = frameN;  // exact frame index
      
      slider_Age.setAutoDraw(true);
    }

    
    // *key_Age* updates
    if (t >= 0.0 && key_Age.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_Age.tStart = t;  // (not accounting for frame time here)
      key_Age.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_Age.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_Age.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_Age.clearEvents(); });
    }

    if (key_Age.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_Age.getKeys({keyList: ['space'], waitRelease: false});
      _key_Age_allKeys = _key_Age_allKeys.concat(theseKeys);
      if (_key_Age_allKeys.length > 0) {
        key_Age.keys = _key_Age_allKeys[_key_Age_allKeys.length - 1].name;  // just the last key pressed
        key_Age.rt = _key_Age_allKeys[_key_Age_allKeys.length - 1].rt;
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
    AgeComponents.forEach( function(thisComponent) {
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


function AgeRoutineEnd() {
  return async function () {
    //------Ending Routine 'Age'-------
    AgeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_Age.response', slider_Age.getRating());
    psychoJS.experiment.addData('slider_Age.rt', slider_Age.getRT());
    psychoJS.experiment.addData('key_Age.keys', key_Age.keys);
    if (typeof key_Age.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_Age.rt', key_Age.rt);
        routineTimer.reset();
        }
    
    key_Age.stop();
    // the Routine "Age" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_Muttersprachler_allKeys;
var MuttersprachlerComponents;
function MuttersprachlerRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Muttersprachler'-------
    t = 0;
    MuttersprachlerClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Muttersprachler.setText('Bist du deutsche Muttersprachlerin oder deutscher Muttersprachler?\n\n(Drücke die Leertaste um fortzufahren.)');
    slider_Muttersprache.reset()
    key_Muttersprachler.keys = undefined;
    key_Muttersprachler.rt = undefined;
    _key_Muttersprachler_allKeys = [];
    // keep track of which components have finished
    MuttersprachlerComponents = [];
    MuttersprachlerComponents.push(text_Muttersprachler);
    MuttersprachlerComponents.push(slider_Muttersprache);
    MuttersprachlerComponents.push(key_Muttersprachler);
    
    MuttersprachlerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MuttersprachlerRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Muttersprachler'-------
    // get current time
    t = MuttersprachlerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Muttersprachler* updates
    if (t >= 0.0 && text_Muttersprachler.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Muttersprachler.tStart = t;  // (not accounting for frame time here)
      text_Muttersprachler.frameNStart = frameN;  // exact frame index
      
      text_Muttersprachler.setAutoDraw(true);
    }

    
    // *slider_Muttersprache* updates
    if (t >= 0.0 && slider_Muttersprache.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_Muttersprache.tStart = t;  // (not accounting for frame time here)
      slider_Muttersprache.frameNStart = frameN;  // exact frame index
      
      slider_Muttersprache.setAutoDraw(true);
    }

    
    // *key_Muttersprachler* updates
    if (t >= 0.0 && key_Muttersprachler.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_Muttersprachler.tStart = t;  // (not accounting for frame time here)
      key_Muttersprachler.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_Muttersprachler.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_Muttersprachler.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_Muttersprachler.clearEvents(); });
    }

    if (key_Muttersprachler.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_Muttersprachler.getKeys({keyList: ['space'], waitRelease: false});
      _key_Muttersprachler_allKeys = _key_Muttersprachler_allKeys.concat(theseKeys);
      if (_key_Muttersprachler_allKeys.length > 0) {
        key_Muttersprachler.keys = _key_Muttersprachler_allKeys[_key_Muttersprachler_allKeys.length - 1].name;  // just the last key pressed
        key_Muttersprachler.rt = _key_Muttersprachler_allKeys[_key_Muttersprachler_allKeys.length - 1].rt;
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
    MuttersprachlerComponents.forEach( function(thisComponent) {
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


function MuttersprachlerRoutineEnd() {
  return async function () {
    //------Ending Routine 'Muttersprachler'-------
    MuttersprachlerComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_Muttersprache.response', slider_Muttersprache.getRating());
    psychoJS.experiment.addData('slider_Muttersprache.rt', slider_Muttersprache.getRT());
    psychoJS.experiment.addData('key_Muttersprachler.keys', key_Muttersprachler.keys);
    if (typeof key_Muttersprachler.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_Muttersprachler.rt', key_Muttersprachler.rt);
        routineTimer.reset();
        }
    
    key_Muttersprachler.stop();
    // the Routine "Muttersprachler" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_Intro2_allKeys;
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
    key_Intro2.keys = undefined;
    key_Intro2.rt = undefined;
    _key_Intro2_allKeys = [];
    text_Intro2.setText('Im Folgenden wirst Du einen Namen sehen sowie einen 7-stelligen Slider. Du bewertest den Namen von ganz links "sehr männlich" bis ganz rechts "sehr weiblich". Die Mitte der Skala zeigt "neutral" an.\n\nZum Beispiel würde ich "Uwe" als "sehr männlich", "Gudrun" als "sehr weiblich" und "Alex" als "neutral" bewerten. \n\nWichtig ist, NICHT die assoziierten Qualitäten des Namens zu bewerten (Gudrun klingt hart/stark also "männlich"), sondern ob Du eher an einen Mann (der Uwe), eine Frau (die Gudrun) oder vielleicht beide (der/die Alex) denkst.\n\nNun Folgen drei Beispiele. Drücke die Leertaste.');
    // keep track of which components have finished
    Intro2Components = [];
    Intro2Components.push(key_Intro2);
    Intro2Components.push(text_Intro2);
    
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
    
    // *key_Intro2* updates
    if (t >= 0.0 && key_Intro2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_Intro2.tStart = t;  // (not accounting for frame time here)
      key_Intro2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_Intro2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_Intro2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_Intro2.clearEvents(); });
    }

    if (key_Intro2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_Intro2.getKeys({keyList: ['space'], waitRelease: false});
      _key_Intro2_allKeys = _key_Intro2_allKeys.concat(theseKeys);
      if (_key_Intro2_allKeys.length > 0) {
        key_Intro2.keys = _key_Intro2_allKeys[_key_Intro2_allKeys.length - 1].name;  // just the last key pressed
        key_Intro2.rt = _key_Intro2_allKeys[_key_Intro2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_Intro2* updates
    if (t >= 0.0 && text_Intro2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Intro2.tStart = t;  // (not accounting for frame time here)
      text_Intro2.frameNStart = frameN;  // exact frame index
      
      text_Intro2.setAutoDraw(true);
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
    psychoJS.experiment.addData('key_Intro2.keys', key_Intro2.keys);
    if (typeof key_Intro2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_Intro2.rt', key_Intro2.rt);
        routineTimer.reset();
        }
    
    key_Intro2.stop();
    // the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_OtherName;
var currentLoop;
function trials_OtherNameLoopBegin(trials_OtherNameLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_OtherName = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Norming_Buffer.xlsx',
      seed: undefined, name: 'trials_OtherName'
    });
    psychoJS.experiment.addLoop(trials_OtherName); // add the loop to the experiment
    currentLoop = trials_OtherName;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_OtherName.forEach(function() {
      const snapshot = trials_OtherName.getSnapshot();
    
      trials_OtherNameLoopScheduler.add(importConditions(snapshot));
      trials_OtherNameLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials_OtherNameLoopScheduler.add(Blank500RoutineEachFrame());
      trials_OtherNameLoopScheduler.add(Blank500RoutineEnd());
      trials_OtherNameLoopScheduler.add(OtherNameRoutineBegin(snapshot));
      trials_OtherNameLoopScheduler.add(OtherNameRoutineEachFrame());
      trials_OtherNameLoopScheduler.add(OtherNameRoutineEnd());
      trials_OtherNameLoopScheduler.add(endLoopIteration(trials_OtherNameLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_OtherNameLoopEnd() {
  psychoJS.experiment.removeLoop(trials_OtherName);

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
      trialList: 'Norming_CommonNames_Filtered.xlsx',
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


var frameRemains;
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


var OtherNameComponents;
function OtherNameRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'OtherName'-------
    t = 0;
    OtherNameClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_Buffer.setText(Name);
    slider_Buffer.reset()
    // keep track of which components have finished
    OtherNameComponents = [];
    OtherNameComponents.push(text_Buffer);
    OtherNameComponents.push(slider_Buffer);
    
    OtherNameComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function OtherNameRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'OtherName'-------
    // get current time
    t = OtherNameClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Buffer* updates
    if (t >= 0.0 && text_Buffer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Buffer.tStart = t;  // (not accounting for frame time here)
      text_Buffer.frameNStart = frameN;  // exact frame index
      
      text_Buffer.setAutoDraw(true);
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
    OtherNameComponents.forEach( function(thisComponent) {
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


function OtherNameRoutineEnd() {
  return async function () {
    //------Ending Routine 'OtherName'-------
    OtherNameComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_Buffer.response', slider_Buffer.getRating());
    psychoJS.experiment.addData('slider_Buffer.rt', slider_Buffer.getRT());
    // the Routine "OtherName" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
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
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    Intro3Components = [];
    Intro3Components.push(text_Intro3);
    Intro3Components.push(key_resp_2);
    
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

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Intro3" was not non-slip safe, so reset the non-slip timer
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
    text_Trial.setText(Name);
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


var _key_biologicalSex_allKeys;
var biologicalSexComponents;
function biologicalSexRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'biologicalSex'-------
    t = 0;
    biologicalSexClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_biologicalSex.setText('Was ist dein biologisches Geschlecht?\n\n(Drücke die Leertaste um fortzufahren.)');
    slider_biologicalSex.reset()
    key_biologicalSex.keys = undefined;
    key_biologicalSex.rt = undefined;
    _key_biologicalSex_allKeys = [];
    // keep track of which components have finished
    biologicalSexComponents = [];
    biologicalSexComponents.push(text_biologicalSex);
    biologicalSexComponents.push(slider_biologicalSex);
    biologicalSexComponents.push(key_biologicalSex);
    
    biologicalSexComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function biologicalSexRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'biologicalSex'-------
    // get current time
    t = biologicalSexClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_biologicalSex* updates
    if (t >= 0.0 && text_biologicalSex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_biologicalSex.tStart = t;  // (not accounting for frame time here)
      text_biologicalSex.frameNStart = frameN;  // exact frame index
      
      text_biologicalSex.setAutoDraw(true);
    }

    
    // *slider_biologicalSex* updates
    if (t >= 0.0 && slider_biologicalSex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_biologicalSex.tStart = t;  // (not accounting for frame time here)
      slider_biologicalSex.frameNStart = frameN;  // exact frame index
      
      slider_biologicalSex.setAutoDraw(true);
    }

    
    // *key_biologicalSex* updates
    if (t >= 0.0 && key_biologicalSex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_biologicalSex.tStart = t;  // (not accounting for frame time here)
      key_biologicalSex.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_biologicalSex.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_biologicalSex.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_biologicalSex.clearEvents(); });
    }

    if (key_biologicalSex.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_biologicalSex.getKeys({keyList: ['space'], waitRelease: false});
      _key_biologicalSex_allKeys = _key_biologicalSex_allKeys.concat(theseKeys);
      if (_key_biologicalSex_allKeys.length > 0) {
        key_biologicalSex.keys = _key_biologicalSex_allKeys[_key_biologicalSex_allKeys.length - 1].name;  // just the last key pressed
        key_biologicalSex.rt = _key_biologicalSex_allKeys[_key_biologicalSex_allKeys.length - 1].rt;
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
    biologicalSexComponents.forEach( function(thisComponent) {
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


function biologicalSexRoutineEnd() {
  return async function () {
    //------Ending Routine 'biologicalSex'-------
    biologicalSexComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_biologicalSex.response', slider_biologicalSex.getRating());
    psychoJS.experiment.addData('slider_biologicalSex.rt', slider_biologicalSex.getRT());
    psychoJS.experiment.addData('key_biologicalSex.keys', key_biologicalSex.keys);
    if (typeof key_biologicalSex.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_biologicalSex.rt', key_biologicalSex.rt);
        routineTimer.reset();
        }
    
    key_biologicalSex.stop();
    // the Routine "biologicalSex" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var GenderIdentityComponents;
function GenderIdentityRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'GenderIdentity'-------
    t = 0;
    GenderIdentityClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_GenderIdentity.setText('Wie würdest du deine Geschlechtsidentität zuordnen?\n\nFalls du dies nicht beantworten möchtest, drücke die Leertaste ohne Auswahl um zu beenden.');
    slider.reset()
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    GenderIdentityComponents = [];
    GenderIdentityComponents.push(text_GenderIdentity);
    GenderIdentityComponents.push(slider);
    GenderIdentityComponents.push(key_resp);
    
    GenderIdentityComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function GenderIdentityRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'GenderIdentity'-------
    // get current time
    t = GenderIdentityClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_GenderIdentity* updates
    if (t >= 0.0 && text_GenderIdentity.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_GenderIdentity.tStart = t;  // (not accounting for frame time here)
      text_GenderIdentity.frameNStart = frameN;  // exact frame index
      
      text_GenderIdentity.setAutoDraw(true);
    }

    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
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
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
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
    GenderIdentityComponents.forEach( function(thisComponent) {
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


function GenderIdentityRoutineEnd() {
  return async function () {
    //------Ending Routine 'GenderIdentity'-------
    GenderIdentityComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "GenderIdentity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var GoodbyeScreenComponents;
function GoodbyeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'GoodbyeScreen'-------
    t = 0;
    GoodbyeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    text_GoodbyeScreen.setText('Vielen Dank, dass Du an meinem Experiment teilgenommen hast.');
    // keep track of which components have finished
    GoodbyeScreenComponents = [];
    GoodbyeScreenComponents.push(text_GoodbyeScreen);
    
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

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_GoodbyeScreen.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_GoodbyeScreen.setAutoDraw(false);
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
    if (continueRoutine && routineTimer.getTime() > 0) {
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
