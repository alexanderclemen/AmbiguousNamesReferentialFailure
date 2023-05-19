/************************** 
 * Main-Study-Exp-L5 Test *
 **************************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Main-Study-exp-L5';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'E-Mail-Adresse': '', 'Vorname': '', 'Nachname': '', 'Alter': '', 'Links- oder Rechtshänder': '', 'Zweitsprache (1 geringe Kenntnisse - 10 muttersprachlich)': '', '2. Zweitsprache (1 - 10)': '', '3. Zweitsprache (1 - 10)': '', '4. Zweitsprache (1 - 10)': '', '5. Zweitsprache (1 - 10)': ''};

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
flowScheduler.add(Welcome_ScreenRoutineBegin());
flowScheduler.add(Welcome_ScreenRoutineEachFrame());
flowScheduler.add(Welcome_ScreenRoutineEnd());
flowScheduler.add(Explaination_ScreenRoutineBegin());
flowScheduler.add(Explaination_ScreenRoutineEachFrame());
flowScheduler.add(Explaination_ScreenRoutineEnd());
flowScheduler.add(Explaination2_ScreenRoutineBegin());
flowScheduler.add(Explaination2_ScreenRoutineEachFrame());
flowScheduler.add(Explaination2_ScreenRoutineEnd());
const trials00_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials00_LoopLoopBegin(trials00_LoopLoopScheduler));
flowScheduler.add(trials00_LoopLoopScheduler);
flowScheduler.add(trials00_LoopLoopEnd);
flowScheduler.add(Explaination_Screen3RoutineBegin());
flowScheduler.add(Explaination_Screen3RoutineEachFrame());
flowScheduler.add(Explaination_Screen3RoutineEnd());
const trials01_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials01_LoopLoopBegin(trials01_LoopLoopScheduler));
flowScheduler.add(trials01_LoopLoopScheduler);
flowScheduler.add(trials01_LoopLoopEnd);
flowScheduler.add(PauseRoutineBegin());
flowScheduler.add(PauseRoutineEachFrame());
flowScheduler.add(PauseRoutineEnd());
const trials02_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials02_LoopLoopBegin(trials02_LoopLoopScheduler));
flowScheduler.add(trials02_LoopLoopScheduler);
flowScheduler.add(trials02_LoopLoopEnd);
flowScheduler.add(Pause2RoutineBegin());
flowScheduler.add(Pause2RoutineEachFrame());
flowScheduler.add(Pause2RoutineEnd());
const trials03_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials03_LoopLoopBegin(trials03_LoopLoopScheduler));
flowScheduler.add(trials03_LoopLoopScheduler);
flowScheduler.add(trials03_LoopLoopEnd);
flowScheduler.add(Pause3RoutineBegin());
flowScheduler.add(Pause3RoutineEachFrame());
flowScheduler.add(Pause3RoutineEnd());
const trials04_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials04_LoopLoopBegin(trials04_LoopLoopScheduler));
flowScheduler.add(trials04_LoopLoopScheduler);
flowScheduler.add(trials04_LoopLoopEnd);
flowScheduler.add(Pause4RoutineBegin());
flowScheduler.add(Pause4RoutineEachFrame());
flowScheduler.add(Pause4RoutineEnd());
const trials05_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials05_LoopLoopBegin(trials05_LoopLoopScheduler));
flowScheduler.add(trials05_LoopLoopScheduler);
flowScheduler.add(trials05_LoopLoopEnd);
flowScheduler.add(Pause5RoutineBegin());
flowScheduler.add(Pause5RoutineEachFrame());
flowScheduler.add(Pause5RoutineEnd());
const trials06_LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials06_LoopLoopBegin(trials06_LoopLoopScheduler));
flowScheduler.add(trials06_LoopLoopScheduler);
flowScheduler.add(trials06_LoopLoopEnd);
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
flowScheduler.add(Goodbye_ScreenRoutineBegin());
flowScheduler.add(Goodbye_ScreenRoutineEachFrame());
flowScheduler.add(Goodbye_ScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Main-Study-stimuli-L5-B2.xlsx', 'path': 'Main-Study-stimuli-L5-B2.xlsx'},
    {'name': 'Main-Study-stimuli-L5-B5.xlsx', 'path': 'Main-Study-stimuli-L5-B5.xlsx'},
    {'name': 'Main-Study-stimuli-L5-B1.xlsx', 'path': 'Main-Study-stimuli-L5-B1.xlsx'},
    {'name': 'Main-Study-stimuli-L5-B3.xlsx', 'path': 'Main-Study-stimuli-L5-B3.xlsx'},
    {'name': 'Main-Study-stimuli-L5-B4.xlsx', 'path': 'Main-Study-stimuli-L5-B4.xlsx'},
    {'name': 'Main-Study-stimuli-Examples.xlsx', 'path': 'Main-Study-stimuli-Examples.xlsx'},
    {'name': 'Main-Study-stimuli-L5-B6.xlsx', 'path': 'Main-Study-stimuli-L5-B6.xlsx'}
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


var Welcome_ScreenClock;
var Welcome_text;
var Explaination_ScreenClock;
var Explaination_text;
var Explaination_key_resp;
var Explaination2_ScreenClock;
var Explaination2_text;
var Explaination2_key_resp;
var Blank500Clock;
var Blank500_text;
var Pos01_NameClock;
var Pos01_Name_text;
var Pos01_Name_key_resp;
var Pos02_VClock;
var Pos02_V_text;
var Pos02_V_key_resp;
var Pos03_PPClock;
var Pos03_PP_text;
var Pos03_PP_key_resp;
var Pos04_PROClock;
var Pos04_PRO_text;
var Pos04_PRO_key_resp;
var Pos05_3Clock;
var Pos05_text;
var Pos05_key_resp;
var Pos06_2Clock;
var Pos06_text;
var Pos06_key_resp;
var Pos07_2Clock;
var Pos07_text;
var Pos07_key_resp;
var Pos08_2Clock;
var Pos08_text;
var Pos08_key_resp;
var Pos09_2Clock;
var Pos09_text;
var Pos09_key_resp;
var Comp_qClock;
var Comp_q_key_resp;
var Comp_q_text;
var Comp_respClock;
var Comp_resp_key_resp;
var Comp_Up_resp_text;
var Quest_Down_text;
var Explaination_Screen3Clock;
var Explaination3_text;
var Explaination3_key_resp;
var PauseClock;
var Pause1_text;
var Pause1_key_resp;
var Pause2Clock;
var Pause2_text;
var Pause2_key_resp;
var Pause3Clock;
var Pause3_text;
var Pause3_key_resp;
var Pause4Clock;
var Pause4_text;
var Pause4_key_resp;
var Pause5Clock;
var Pause5_text;
var Pause5_key_resp;
var Goodbye_ScreenClock;
var Goodbye_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome_Screen"
  Welcome_ScreenClock = new util.Clock();
  Welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Welcome_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Explaination_Screen"
  Explaination_ScreenClock = new util.Clock();
  Explaination_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Explaination_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Explaination_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Explaination2_Screen"
  Explaination2_ScreenClock = new util.Clock();
  Explaination2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Explaination2_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Explaination2_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  Blank500_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Blank500_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Pos01_Name"
  Pos01_NameClock = new util.Clock();
  Pos01_Name_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos01_Name_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos01_Name_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos02_V"
  Pos02_VClock = new util.Clock();
  Pos02_V_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos02_V_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos02_V_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos03_PP"
  Pos03_PPClock = new util.Clock();
  Pos03_PP_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos03_PP_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos03_PP_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos04_PRO"
  Pos04_PROClock = new util.Clock();
  Pos04_PRO_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos04_PRO_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos04_PRO_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos05_3"
  Pos05_3Clock = new util.Clock();
  Pos05_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos05_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos05_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos06_2"
  Pos06_2Clock = new util.Clock();
  Pos06_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos06_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos06_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos07_2"
  Pos07_2Clock = new util.Clock();
  Pos07_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos07_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos07_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos08_2"
  Pos08_2Clock = new util.Clock();
  Pos08_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos08_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos08_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pos09_2"
  Pos09_2Clock = new util.Clock();
  Pos09_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pos09_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pos09_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Comp_q"
  Comp_qClock = new util.Clock();
  Comp_q_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Comp_q_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Comp_q_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Comp_resp"
  Comp_respClock = new util.Clock();
  Comp_resp_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Comp_Up_resp_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Comp_Up_resp_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Quest_Down_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Quest_Down_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Explaination_Screen3"
  Explaination_Screen3Clock = new util.Clock();
  Explaination3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Explaination3_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Explaination3_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause"
  PauseClock = new util.Clock();
  Pause1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pause1_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pause1_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause2"
  Pause2Clock = new util.Clock();
  Pause2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pause2_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pause2_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause3"
  Pause3Clock = new util.Clock();
  Pause3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pause3_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pause3_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause4"
  Pause4Clock = new util.Clock();
  Pause4_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pause4_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pause4_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause5"
  Pause5Clock = new util.Clock();
  Pause5_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pause5_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Pause5_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Goodbye_Screen"
  Goodbye_ScreenClock = new util.Clock();
  Goodbye_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Goodbye_text',
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
var Welcome_ScreenComponents;
function Welcome_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Welcome_Screen'-------
    t = 0;
    Welcome_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    Welcome_text.setText('Hallo und vielen Dank für deine Teilnahme.');
    // keep track of which components have finished
    Welcome_ScreenComponents = [];
    Welcome_ScreenComponents.push(Welcome_text);
    
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Welcome_ScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Welcome_Screen'-------
    // get current time
    t = Welcome_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Welcome_text* updates
    if (t >= 0.0 && Welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome_text.tStart = t;  // (not accounting for frame time here)
      Welcome_text.frameNStart = frameN;  // exact frame index
      
      Welcome_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Welcome_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Welcome_text.setAutoDraw(false);
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
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome_ScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'Welcome_Screen'-------
    for (const thisComponent of Welcome_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _Explaination_key_resp_allKeys;
var Explaination_ScreenComponents;
function Explaination_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Explaination_Screen'-------
    t = 0;
    Explaination_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Explaination_text.setText('Im folgenden wirst du je zwei Sätze Stück für Stück lesen. \n\nDas heißt Du wirst immer ein Wort oder ein Satzstück sehen und Du entscheidest, wann du das nächste Stück sehen möchtest. Du kommst immer mit der Leertaste zum nächsten Wort/Satzstück. Es gibt keine Möglichkeit um zurückzukehren.\n\nDrücke nun die Leertaste um weiterzukommen.');
    Explaination_key_resp.keys = undefined;
    Explaination_key_resp.rt = undefined;
    _Explaination_key_resp_allKeys = [];
    // keep track of which components have finished
    Explaination_ScreenComponents = [];
    Explaination_ScreenComponents.push(Explaination_text);
    Explaination_ScreenComponents.push(Explaination_key_resp);
    
    for (const thisComponent of Explaination_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Explaination_ScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Explaination_Screen'-------
    // get current time
    t = Explaination_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Explaination_text* updates
    if (t >= 0.0 && Explaination_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Explaination_text.tStart = t;  // (not accounting for frame time here)
      Explaination_text.frameNStart = frameN;  // exact frame index
      
      Explaination_text.setAutoDraw(true);
    }

    
    // *Explaination_key_resp* updates
    if (t >= 0.0 && Explaination_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Explaination_key_resp.tStart = t;  // (not accounting for frame time here)
      Explaination_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Explaination_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Explaination_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Explaination_key_resp.clearEvents(); });
    }

    if (Explaination_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Explaination_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Explaination_key_resp_allKeys = _Explaination_key_resp_allKeys.concat(theseKeys);
      if (_Explaination_key_resp_allKeys.length > 0) {
        Explaination_key_resp.keys = _Explaination_key_resp_allKeys[_Explaination_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Explaination_key_resp.rt = _Explaination_key_resp_allKeys[_Explaination_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Explaination_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Explaination_ScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'Explaination_Screen'-------
    for (const thisComponent of Explaination_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Explaination_key_resp.keys', Explaination_key_resp.keys);
    if (typeof Explaination_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Explaination_key_resp.rt', Explaination_key_resp.rt);
        routineTimer.reset();
        }
    
    Explaination_key_resp.stop();
    // the Routine "Explaination_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Explaination2_key_resp_allKeys;
var Explaination2_ScreenComponents;
function Explaination2_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Explaination2_Screen'-------
    t = 0;
    Explaination2_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Explaination2_text.setText('\nManchmal wirst du eine Frage mit zwei Antwortmöglichkeiten über die Sätze beantworten. Lies die Sätze also möglichst genau aber auch so schnell wie möglich. Es ist immer nur eine Antwortmöglichkeit korrekt. \n\nDie obere Pfeiltaste wählt die obere Antwort aus und die untere Pfeiltaste wählt die untere Antwortmöglichkeit aus.\n\nCa alle 3 bis 5 Minuten hast Du eine Pause. \n\nJetzt folgen fünf Beispiele an denen Du die Steuerung testen kannst. \n\n(Drücke die Leertaste um weiter zu kommen.)');
    Explaination2_key_resp.keys = undefined;
    Explaination2_key_resp.rt = undefined;
    _Explaination2_key_resp_allKeys = [];
    // keep track of which components have finished
    Explaination2_ScreenComponents = [];
    Explaination2_ScreenComponents.push(Explaination2_text);
    Explaination2_ScreenComponents.push(Explaination2_key_resp);
    
    for (const thisComponent of Explaination2_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Explaination2_ScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Explaination2_Screen'-------
    // get current time
    t = Explaination2_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Explaination2_text* updates
    if (t >= 0.0 && Explaination2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Explaination2_text.tStart = t;  // (not accounting for frame time here)
      Explaination2_text.frameNStart = frameN;  // exact frame index
      
      Explaination2_text.setAutoDraw(true);
    }

    
    // *Explaination2_key_resp* updates
    if (t >= 0.0 && Explaination2_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Explaination2_key_resp.tStart = t;  // (not accounting for frame time here)
      Explaination2_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Explaination2_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Explaination2_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Explaination2_key_resp.clearEvents(); });
    }

    if (Explaination2_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Explaination2_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Explaination2_key_resp_allKeys = _Explaination2_key_resp_allKeys.concat(theseKeys);
      if (_Explaination2_key_resp_allKeys.length > 0) {
        Explaination2_key_resp.keys = _Explaination2_key_resp_allKeys[_Explaination2_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Explaination2_key_resp.rt = _Explaination2_key_resp_allKeys[_Explaination2_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Explaination2_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Explaination2_ScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'Explaination2_Screen'-------
    for (const thisComponent of Explaination2_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Explaination2_key_resp.keys', Explaination2_key_resp.keys);
    if (typeof Explaination2_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Explaination2_key_resp.rt', Explaination2_key_resp.rt);
        routineTimer.reset();
        }
    
    Explaination2_key_resp.stop();
    // the Routine "Explaination2_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials00_Loop;
var currentLoop;
function trials00_LoopLoopBegin(trials00_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials00_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-Examples.xlsx', '0:5'),
      seed: undefined, name: 'trials00_Loop'
    });
    psychoJS.experiment.addLoop(trials00_Loop); // add the loop to the experiment
    currentLoop = trials00_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials00_Loop of trials00_Loop) {
      const snapshot = trials00_Loop.getSnapshot();
      trials00_LoopLoopScheduler.add(importConditions(snapshot));
      trials00_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials00_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials00_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials00_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials00_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials00_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials00_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials00_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials00_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials00_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials00_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials00_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials00_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials00_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials00_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials00_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials00_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials00_LoopLoopScheduler.add(endLoopIteration(trials00_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials00_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials00_Loop);

  return Scheduler.Event.NEXT;
}


var trials01_Loop;
function trials01_LoopLoopBegin(trials01_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials01_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-L5-B1.xlsx', '0:26'),
      seed: undefined, name: 'trials01_Loop'
    });
    psychoJS.experiment.addLoop(trials01_Loop); // add the loop to the experiment
    currentLoop = trials01_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials01_Loop of trials01_Loop) {
      const snapshot = trials01_Loop.getSnapshot();
      trials01_LoopLoopScheduler.add(importConditions(snapshot));
      trials01_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials01_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials01_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials01_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials01_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials01_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials01_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials01_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials01_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials01_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials01_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials01_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials01_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials01_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials01_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials01_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials01_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials01_LoopLoopScheduler.add(endLoopIteration(trials01_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials01_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials01_Loop);

  return Scheduler.Event.NEXT;
}


var trials02_Loop;
function trials02_LoopLoopBegin(trials02_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials02_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-L5-B2.xlsx', '0:21'),
      seed: undefined, name: 'trials02_Loop'
    });
    psychoJS.experiment.addLoop(trials02_Loop); // add the loop to the experiment
    currentLoop = trials02_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials02_Loop of trials02_Loop) {
      const snapshot = trials02_Loop.getSnapshot();
      trials02_LoopLoopScheduler.add(importConditions(snapshot));
      trials02_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials02_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials02_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials02_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials02_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials02_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials02_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials02_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials02_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials02_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials02_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials02_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials02_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials02_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials02_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials02_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials02_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials02_LoopLoopScheduler.add(endLoopIteration(trials02_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials02_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials02_Loop);

  return Scheduler.Event.NEXT;
}


var trials03_Loop;
function trials03_LoopLoopBegin(trials03_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials03_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-L5-B3.xlsx', '0:21'),
      seed: undefined, name: 'trials03_Loop'
    });
    psychoJS.experiment.addLoop(trials03_Loop); // add the loop to the experiment
    currentLoop = trials03_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials03_Loop of trials03_Loop) {
      const snapshot = trials03_Loop.getSnapshot();
      trials03_LoopLoopScheduler.add(importConditions(snapshot));
      trials03_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials03_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials03_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials03_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials03_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials03_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials03_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials03_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials03_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials03_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials03_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials03_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials03_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials03_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials03_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials03_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials03_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials03_LoopLoopScheduler.add(endLoopIteration(trials03_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials03_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials03_Loop);

  return Scheduler.Event.NEXT;
}


var trials04_Loop;
function trials04_LoopLoopBegin(trials04_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials04_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-L5-B4.xlsx', '0:21'),
      seed: undefined, name: 'trials04_Loop'
    });
    psychoJS.experiment.addLoop(trials04_Loop); // add the loop to the experiment
    currentLoop = trials04_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials04_Loop of trials04_Loop) {
      const snapshot = trials04_Loop.getSnapshot();
      trials04_LoopLoopScheduler.add(importConditions(snapshot));
      trials04_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials04_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials04_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials04_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials04_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials04_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials04_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials04_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials04_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials04_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials04_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials04_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials04_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials04_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials04_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials04_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials04_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials04_LoopLoopScheduler.add(endLoopIteration(trials04_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials04_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials04_Loop);

  return Scheduler.Event.NEXT;
}


var trials05_Loop;
function trials05_LoopLoopBegin(trials05_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials05_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-L5-B5.xlsx', '0:21'),
      seed: undefined, name: 'trials05_Loop'
    });
    psychoJS.experiment.addLoop(trials05_Loop); // add the loop to the experiment
    currentLoop = trials05_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials05_Loop of trials05_Loop) {
      const snapshot = trials05_Loop.getSnapshot();
      trials05_LoopLoopScheduler.add(importConditions(snapshot));
      trials05_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials05_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials05_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials05_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials05_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials05_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials05_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials05_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials05_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials05_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials05_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials05_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials05_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials05_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials05_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials05_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials05_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials05_LoopLoopScheduler.add(endLoopIteration(trials05_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials05_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials05_Loop);

  return Scheduler.Event.NEXT;
}


var trials06_Loop;
function trials06_LoopLoopBegin(trials06_LoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials06_Loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Main-Study-stimuli-L5-B6.xlsx', '0:21'),
      seed: undefined, name: 'trials06_Loop'
    });
    psychoJS.experiment.addLoop(trials06_Loop); // add the loop to the experiment
    currentLoop = trials06_Loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials06_Loop of trials06_Loop) {
      const snapshot = trials06_Loop.getSnapshot();
      trials06_LoopLoopScheduler.add(importConditions(snapshot));
      trials06_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials06_LoopLoopScheduler.add(Pos01_NameRoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos01_NameRoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos01_NameRoutineEnd());
      trials06_LoopLoopScheduler.add(Pos02_VRoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos02_VRoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos02_VRoutineEnd());
      trials06_LoopLoopScheduler.add(Pos03_PPRoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos03_PPRoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos03_PPRoutineEnd());
      trials06_LoopLoopScheduler.add(Pos04_PRORoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos04_PRORoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos04_PRORoutineEnd());
      trials06_LoopLoopScheduler.add(Pos05_3RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos05_3RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos05_3RoutineEnd());
      trials06_LoopLoopScheduler.add(Pos06_2RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos06_2RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos06_2RoutineEnd());
      trials06_LoopLoopScheduler.add(Pos07_2RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos07_2RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos07_2RoutineEnd());
      trials06_LoopLoopScheduler.add(Pos08_2RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos08_2RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos08_2RoutineEnd());
      trials06_LoopLoopScheduler.add(Pos09_2RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Pos09_2RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Pos09_2RoutineEnd());
      trials06_LoopLoopScheduler.add(Blank500RoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Blank500RoutineEachFrame());
      trials06_LoopLoopScheduler.add(Blank500RoutineEnd());
      trials06_LoopLoopScheduler.add(Comp_qRoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Comp_qRoutineEachFrame());
      trials06_LoopLoopScheduler.add(Comp_qRoutineEnd());
      trials06_LoopLoopScheduler.add(Comp_respRoutineBegin(snapshot));
      trials06_LoopLoopScheduler.add(Comp_respRoutineEachFrame());
      trials06_LoopLoopScheduler.add(Comp_respRoutineEnd());
      trials06_LoopLoopScheduler.add(endLoopIteration(trials06_LoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials06_LoopLoopEnd() {
  psychoJS.experiment.removeLoop(trials06_Loop);

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
    Blank500_text.setText('');
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(Blank500_text);
    
    for (const thisComponent of Blank500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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
    
    // *Blank500_text* updates
    if (t >= 0.0 && Blank500_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Blank500_text.tStart = t;  // (not accounting for frame time here)
      Blank500_text.frameNStart = frameN;  // exact frame index
      
      Blank500_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Blank500_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Blank500_text.setAutoDraw(false);
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
    for (const thisComponent of Blank500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of Blank500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _Pos01_Name_key_resp_allKeys;
var Pos01_NameComponents;
function Pos01_NameRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos01_Name'-------
    t = 0;
    Pos01_NameClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos01_Name_text.setText(Name);
    Pos01_Name_key_resp.keys = undefined;
    Pos01_Name_key_resp.rt = undefined;
    _Pos01_Name_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos01_NameComponents = [];
    Pos01_NameComponents.push(Pos01_Name_text);
    Pos01_NameComponents.push(Pos01_Name_key_resp);
    
    for (const thisComponent of Pos01_NameComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos01_NameRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos01_Name'-------
    // get current time
    t = Pos01_NameClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos01_Name_text* updates
    if (t >= 0.0 && Pos01_Name_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos01_Name_text.tStart = t;  // (not accounting for frame time here)
      Pos01_Name_text.frameNStart = frameN;  // exact frame index
      
      Pos01_Name_text.setAutoDraw(true);
    }

    
    // *Pos01_Name_key_resp* updates
    if (t >= 0.0 && Pos01_Name_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos01_Name_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos01_Name_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos01_Name_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos01_Name_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos01_Name_key_resp.clearEvents(); });
    }

    if (Pos01_Name_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos01_Name_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos01_Name_key_resp_allKeys = _Pos01_Name_key_resp_allKeys.concat(theseKeys);
      if (_Pos01_Name_key_resp_allKeys.length > 0) {
        Pos01_Name_key_resp.keys = _Pos01_Name_key_resp_allKeys[_Pos01_Name_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos01_Name_key_resp.rt = _Pos01_Name_key_resp_allKeys[_Pos01_Name_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos01_NameComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos01_NameRoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos01_Name'-------
    for (const thisComponent of Pos01_NameComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos01_Name_key_resp.keys', Pos01_Name_key_resp.keys);
    if (typeof Pos01_Name_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos01_Name_key_resp.rt', Pos01_Name_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos01_Name_key_resp.stop();
    // the Routine "Pos01_Name" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos02_V_key_resp_allKeys;
var Pos02_VComponents;
function Pos02_VRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos02_V'-------
    t = 0;
    Pos02_VClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos02_V_text.setText(V);
    Pos02_V_key_resp.keys = undefined;
    Pos02_V_key_resp.rt = undefined;
    _Pos02_V_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos02_VComponents = [];
    Pos02_VComponents.push(Pos02_V_text);
    Pos02_VComponents.push(Pos02_V_key_resp);
    
    for (const thisComponent of Pos02_VComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos02_VRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos02_V'-------
    // get current time
    t = Pos02_VClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos02_V_text* updates
    if (t >= 0.0 && Pos02_V_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos02_V_text.tStart = t;  // (not accounting for frame time here)
      Pos02_V_text.frameNStart = frameN;  // exact frame index
      
      Pos02_V_text.setAutoDraw(true);
    }

    
    // *Pos02_V_key_resp* updates
    if (t >= 0.0 && Pos02_V_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos02_V_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos02_V_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos02_V_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos02_V_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos02_V_key_resp.clearEvents(); });
    }

    if (Pos02_V_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos02_V_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos02_V_key_resp_allKeys = _Pos02_V_key_resp_allKeys.concat(theseKeys);
      if (_Pos02_V_key_resp_allKeys.length > 0) {
        Pos02_V_key_resp.keys = _Pos02_V_key_resp_allKeys[_Pos02_V_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos02_V_key_resp.rt = _Pos02_V_key_resp_allKeys[_Pos02_V_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos02_VComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos02_VRoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos02_V'-------
    for (const thisComponent of Pos02_VComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos02_V_key_resp.keys', Pos02_V_key_resp.keys);
    if (typeof Pos02_V_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos02_V_key_resp.rt', Pos02_V_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos02_V_key_resp.stop();
    // the Routine "Pos02_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos03_PP_key_resp_allKeys;
var Pos03_PPComponents;
function Pos03_PPRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos03_PP'-------
    t = 0;
    Pos03_PPClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos03_PP_text.setText(PP_mitPunkt);
    Pos03_PP_key_resp.keys = undefined;
    Pos03_PP_key_resp.rt = undefined;
    _Pos03_PP_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos03_PPComponents = [];
    Pos03_PPComponents.push(Pos03_PP_text);
    Pos03_PPComponents.push(Pos03_PP_key_resp);
    
    for (const thisComponent of Pos03_PPComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos03_PPRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos03_PP'-------
    // get current time
    t = Pos03_PPClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos03_PP_text* updates
    if (t >= 0.0 && Pos03_PP_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos03_PP_text.tStart = t;  // (not accounting for frame time here)
      Pos03_PP_text.frameNStart = frameN;  // exact frame index
      
      Pos03_PP_text.setAutoDraw(true);
    }

    
    // *Pos03_PP_key_resp* updates
    if (t >= 0.0 && Pos03_PP_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos03_PP_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos03_PP_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos03_PP_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos03_PP_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos03_PP_key_resp.clearEvents(); });
    }

    if (Pos03_PP_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos03_PP_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos03_PP_key_resp_allKeys = _Pos03_PP_key_resp_allKeys.concat(theseKeys);
      if (_Pos03_PP_key_resp_allKeys.length > 0) {
        Pos03_PP_key_resp.keys = _Pos03_PP_key_resp_allKeys[_Pos03_PP_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos03_PP_key_resp.rt = _Pos03_PP_key_resp_allKeys[_Pos03_PP_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos03_PPComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos03_PPRoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos03_PP'-------
    for (const thisComponent of Pos03_PPComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos03_PP_key_resp.keys', Pos03_PP_key_resp.keys);
    if (typeof Pos03_PP_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos03_PP_key_resp.rt', Pos03_PP_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos03_PP_key_resp.stop();
    // the Routine "Pos03_PP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos04_PRO_key_resp_allKeys;
var Pos04_PROComponents;
function Pos04_PRORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos04_PRO'-------
    t = 0;
    Pos04_PROClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos04_PRO_text.setText(PRO);
    Pos04_PRO_key_resp.keys = undefined;
    Pos04_PRO_key_resp.rt = undefined;
    _Pos04_PRO_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos04_PROComponents = [];
    Pos04_PROComponents.push(Pos04_PRO_text);
    Pos04_PROComponents.push(Pos04_PRO_key_resp);
    
    for (const thisComponent of Pos04_PROComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos04_PRORoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos04_PRO'-------
    // get current time
    t = Pos04_PROClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos04_PRO_text* updates
    if (t >= 0.0 && Pos04_PRO_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos04_PRO_text.tStart = t;  // (not accounting for frame time here)
      Pos04_PRO_text.frameNStart = frameN;  // exact frame index
      
      Pos04_PRO_text.setAutoDraw(true);
    }

    
    // *Pos04_PRO_key_resp* updates
    if (t >= 0.0 && Pos04_PRO_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos04_PRO_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos04_PRO_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos04_PRO_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos04_PRO_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos04_PRO_key_resp.clearEvents(); });
    }

    if (Pos04_PRO_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos04_PRO_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos04_PRO_key_resp_allKeys = _Pos04_PRO_key_resp_allKeys.concat(theseKeys);
      if (_Pos04_PRO_key_resp_allKeys.length > 0) {
        Pos04_PRO_key_resp.keys = _Pos04_PRO_key_resp_allKeys[_Pos04_PRO_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos04_PRO_key_resp.rt = _Pos04_PRO_key_resp_allKeys[_Pos04_PRO_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos04_PROComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos04_PRORoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos04_PRO'-------
    for (const thisComponent of Pos04_PROComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos04_PRO_key_resp.keys', Pos04_PRO_key_resp.keys);
    if (typeof Pos04_PRO_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos04_PRO_key_resp.rt', Pos04_PRO_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos04_PRO_key_resp.stop();
    // the Routine "Pos04_PRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos05_key_resp_allKeys;
var Pos05_3Components;
function Pos05_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos05_3'-------
    t = 0;
    Pos05_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos05_text.setText(Pos05);
    Pos05_key_resp.keys = undefined;
    Pos05_key_resp.rt = undefined;
    _Pos05_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos05_3Components = [];
    Pos05_3Components.push(Pos05_text);
    Pos05_3Components.push(Pos05_key_resp);
    
    for (const thisComponent of Pos05_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos05_3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos05_3'-------
    // get current time
    t = Pos05_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos05_text* updates
    if (t >= 0.0 && Pos05_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos05_text.tStart = t;  // (not accounting for frame time here)
      Pos05_text.frameNStart = frameN;  // exact frame index
      
      Pos05_text.setAutoDraw(true);
    }

    
    // *Pos05_key_resp* updates
    if (t >= 0.0 && Pos05_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos05_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos05_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos05_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos05_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos05_key_resp.clearEvents(); });
    }

    if (Pos05_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos05_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos05_key_resp_allKeys = _Pos05_key_resp_allKeys.concat(theseKeys);
      if (_Pos05_key_resp_allKeys.length > 0) {
        Pos05_key_resp.keys = _Pos05_key_resp_allKeys[_Pos05_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos05_key_resp.rt = _Pos05_key_resp_allKeys[_Pos05_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos05_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos05_3RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos05_3'-------
    for (const thisComponent of Pos05_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos05_key_resp.keys', Pos05_key_resp.keys);
    if (typeof Pos05_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos05_key_resp.rt', Pos05_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos05_key_resp.stop();
    // the Routine "Pos05_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos06_key_resp_allKeys;
var Pos06_2Components;
function Pos06_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos06_2'-------
    t = 0;
    Pos06_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos06_text.setText(Pos06);
    Pos06_key_resp.keys = undefined;
    Pos06_key_resp.rt = undefined;
    _Pos06_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos06_2Components = [];
    Pos06_2Components.push(Pos06_text);
    Pos06_2Components.push(Pos06_key_resp);
    
    for (const thisComponent of Pos06_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos06_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos06_2'-------
    // get current time
    t = Pos06_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos06_text* updates
    if (t >= 0.0 && Pos06_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos06_text.tStart = t;  // (not accounting for frame time here)
      Pos06_text.frameNStart = frameN;  // exact frame index
      
      Pos06_text.setAutoDraw(true);
    }

    
    // *Pos06_key_resp* updates
    if (t >= 0.0 && Pos06_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos06_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos06_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos06_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos06_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos06_key_resp.clearEvents(); });
    }

    if (Pos06_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos06_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos06_key_resp_allKeys = _Pos06_key_resp_allKeys.concat(theseKeys);
      if (_Pos06_key_resp_allKeys.length > 0) {
        Pos06_key_resp.keys = _Pos06_key_resp_allKeys[_Pos06_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos06_key_resp.rt = _Pos06_key_resp_allKeys[_Pos06_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos06_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos06_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos06_2'-------
    for (const thisComponent of Pos06_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos06_key_resp.keys', Pos06_key_resp.keys);
    if (typeof Pos06_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos06_key_resp.rt', Pos06_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos06_key_resp.stop();
    // the Routine "Pos06_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos07_key_resp_allKeys;
var Pos07_2Components;
function Pos07_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos07_2'-------
    t = 0;
    Pos07_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos07_text.setText(Pos07);
    Pos07_key_resp.keys = undefined;
    Pos07_key_resp.rt = undefined;
    _Pos07_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos07_2Components = [];
    Pos07_2Components.push(Pos07_text);
    Pos07_2Components.push(Pos07_key_resp);
    
    for (const thisComponent of Pos07_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos07_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos07_2'-------
    // get current time
    t = Pos07_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos07_text* updates
    if (t >= 0.0 && Pos07_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos07_text.tStart = t;  // (not accounting for frame time here)
      Pos07_text.frameNStart = frameN;  // exact frame index
      
      Pos07_text.setAutoDraw(true);
    }

    
    // *Pos07_key_resp* updates
    if (t >= 0.0 && Pos07_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos07_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos07_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos07_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos07_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos07_key_resp.clearEvents(); });
    }

    if (Pos07_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos07_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos07_key_resp_allKeys = _Pos07_key_resp_allKeys.concat(theseKeys);
      if (_Pos07_key_resp_allKeys.length > 0) {
        Pos07_key_resp.keys = _Pos07_key_resp_allKeys[_Pos07_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos07_key_resp.rt = _Pos07_key_resp_allKeys[_Pos07_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos07_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos07_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos07_2'-------
    for (const thisComponent of Pos07_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos07_key_resp.keys', Pos07_key_resp.keys);
    if (typeof Pos07_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos07_key_resp.rt', Pos07_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos07_key_resp.stop();
    // the Routine "Pos07_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos08_key_resp_allKeys;
var Pos08_2Components;
function Pos08_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos08_2'-------
    t = 0;
    Pos08_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos08_text.setText(Pos08);
    Pos08_key_resp.keys = undefined;
    Pos08_key_resp.rt = undefined;
    _Pos08_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos08_2Components = [];
    Pos08_2Components.push(Pos08_text);
    Pos08_2Components.push(Pos08_key_resp);
    
    for (const thisComponent of Pos08_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos08_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos08_2'-------
    // get current time
    t = Pos08_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos08_text* updates
    if (t >= 0.0 && Pos08_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos08_text.tStart = t;  // (not accounting for frame time here)
      Pos08_text.frameNStart = frameN;  // exact frame index
      
      Pos08_text.setAutoDraw(true);
    }

    
    // *Pos08_key_resp* updates
    if (t >= 0.0 && Pos08_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos08_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos08_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos08_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos08_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos08_key_resp.clearEvents(); });
    }

    if (Pos08_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos08_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos08_key_resp_allKeys = _Pos08_key_resp_allKeys.concat(theseKeys);
      if (_Pos08_key_resp_allKeys.length > 0) {
        Pos08_key_resp.keys = _Pos08_key_resp_allKeys[_Pos08_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos08_key_resp.rt = _Pos08_key_resp_allKeys[_Pos08_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos08_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos08_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos08_2'-------
    for (const thisComponent of Pos08_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos08_key_resp.keys', Pos08_key_resp.keys);
    if (typeof Pos08_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos08_key_resp.rt', Pos08_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos08_key_resp.stop();
    // the Routine "Pos08_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pos09_key_resp_allKeys;
var Pos09_2Components;
function Pos09_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pos09_2'-------
    t = 0;
    Pos09_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pos09_text.setText(Pos09_mitPunkt);
    Pos09_key_resp.keys = undefined;
    Pos09_key_resp.rt = undefined;
    _Pos09_key_resp_allKeys = [];
    // keep track of which components have finished
    Pos09_2Components = [];
    Pos09_2Components.push(Pos09_text);
    Pos09_2Components.push(Pos09_key_resp);
    
    for (const thisComponent of Pos09_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pos09_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pos09_2'-------
    // get current time
    t = Pos09_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pos09_text* updates
    if (t >= 0.0 && Pos09_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos09_text.tStart = t;  // (not accounting for frame time here)
      Pos09_text.frameNStart = frameN;  // exact frame index
      
      Pos09_text.setAutoDraw(true);
    }

    
    // *Pos09_key_resp* updates
    if (t >= 0.0 && Pos09_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pos09_key_resp.tStart = t;  // (not accounting for frame time here)
      Pos09_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pos09_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pos09_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pos09_key_resp.clearEvents(); });
    }

    if (Pos09_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pos09_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Pos09_key_resp_allKeys = _Pos09_key_resp_allKeys.concat(theseKeys);
      if (_Pos09_key_resp_allKeys.length > 0) {
        Pos09_key_resp.keys = _Pos09_key_resp_allKeys[_Pos09_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pos09_key_resp.rt = _Pos09_key_resp_allKeys[_Pos09_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pos09_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pos09_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pos09_2'-------
    for (const thisComponent of Pos09_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pos09_key_resp.keys', Pos09_key_resp.keys);
    if (typeof Pos09_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pos09_key_resp.rt', Pos09_key_resp.rt);
        routineTimer.reset();
        }
    
    Pos09_key_resp.stop();
    // the Routine "Pos09_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Comp_q_key_resp_allKeys;
var Comp_qComponents;
function Comp_qRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Comp_q'-------
    t = 0;
    Comp_qClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Comp_q_key_resp.keys = undefined;
    Comp_q_key_resp.rt = undefined;
    _Comp_q_key_resp_allKeys = [];
    Comp_q_text.setText(Quest_Presented);
    if ((followUp === 0)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    Comp_qComponents = [];
    Comp_qComponents.push(Comp_q_key_resp);
    Comp_qComponents.push(Comp_q_text);
    
    for (const thisComponent of Comp_qComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Comp_qRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Comp_q'-------
    // get current time
    t = Comp_qClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Comp_q_key_resp* updates
    if (t >= 0.0 && Comp_q_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comp_q_key_resp.tStart = t;  // (not accounting for frame time here)
      Comp_q_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Comp_q_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Comp_q_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Comp_q_key_resp.clearEvents(); });
    }

    if (Comp_q_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Comp_q_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Comp_q_key_resp_allKeys = _Comp_q_key_resp_allKeys.concat(theseKeys);
      if (_Comp_q_key_resp_allKeys.length > 0) {
        Comp_q_key_resp.keys = _Comp_q_key_resp_allKeys[_Comp_q_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Comp_q_key_resp.rt = _Comp_q_key_resp_allKeys[_Comp_q_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Comp_q_text* updates
    if (t >= 0.0 && Comp_q_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comp_q_text.tStart = t;  // (not accounting for frame time here)
      Comp_q_text.frameNStart = frameN;  // exact frame index
      
      Comp_q_text.setAutoDraw(true);
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
    for (const thisComponent of Comp_qComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Comp_qRoutineEnd() {
  return async function () {
    //------Ending Routine 'Comp_q'-------
    for (const thisComponent of Comp_qComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Comp_q_key_resp.keys', Comp_q_key_resp.keys);
    if (typeof Comp_q_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Comp_q_key_resp.rt', Comp_q_key_resp.rt);
        routineTimer.reset();
        }
    
    Comp_q_key_resp.stop();
    // the Routine "Comp_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Comp_resp_key_resp_allKeys;
var Comp_respComponents;
function Comp_respRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Comp_resp'-------
    t = 0;
    Comp_respClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Comp_resp_key_resp.keys = undefined;
    Comp_resp_key_resp.rt = undefined;
    _Comp_resp_key_resp_allKeys = [];
    Comp_Up_resp_text.setPos([0, 0.1]);
    Comp_Up_resp_text.setText(Quest_Up);
    Quest_Down_text.setText(Quest_Down);
    if ((followUp === 0)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    Comp_respComponents = [];
    Comp_respComponents.push(Comp_resp_key_resp);
    Comp_respComponents.push(Comp_Up_resp_text);
    Comp_respComponents.push(Quest_Down_text);
    
    for (const thisComponent of Comp_respComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Comp_respRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Comp_resp'-------
    // get current time
    t = Comp_respClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Comp_resp_key_resp* updates
    if (t >= 0.0 && Comp_resp_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comp_resp_key_resp.tStart = t;  // (not accounting for frame time here)
      Comp_resp_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Comp_resp_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Comp_resp_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Comp_resp_key_resp.clearEvents(); });
    }

    if (Comp_resp_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Comp_resp_key_resp.getKeys({keyList: ['up', 'down'], waitRelease: false});
      _Comp_resp_key_resp_allKeys = _Comp_resp_key_resp_allKeys.concat(theseKeys);
      if (_Comp_resp_key_resp_allKeys.length > 0) {
        Comp_resp_key_resp.keys = _Comp_resp_key_resp_allKeys[_Comp_resp_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Comp_resp_key_resp.rt = _Comp_resp_key_resp_allKeys[_Comp_resp_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Comp_Up_resp_text* updates
    if (t >= 0.0 && Comp_Up_resp_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comp_Up_resp_text.tStart = t;  // (not accounting for frame time here)
      Comp_Up_resp_text.frameNStart = frameN;  // exact frame index
      
      Comp_Up_resp_text.setAutoDraw(true);
    }

    
    // *Quest_Down_text* updates
    if (t >= 0.0 && Quest_Down_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Quest_Down_text.tStart = t;  // (not accounting for frame time here)
      Quest_Down_text.frameNStart = frameN;  // exact frame index
      
      Quest_Down_text.setAutoDraw(true);
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
    for (const thisComponent of Comp_respComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Comp_respRoutineEnd() {
  return async function () {
    //------Ending Routine 'Comp_resp'-------
    for (const thisComponent of Comp_respComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Comp_resp_key_resp.keys', Comp_resp_key_resp.keys);
    if (typeof Comp_resp_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Comp_resp_key_resp.rt', Comp_resp_key_resp.rt);
        routineTimer.reset();
        }
    
    Comp_resp_key_resp.stop();
    // the Routine "Comp_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Explaination3_key_resp_allKeys;
var Explaination_Screen3Components;
function Explaination_Screen3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Explaination_Screen3'-------
    t = 0;
    Explaination_Screen3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Explaination3_text.setText('Soweit alles startklar?\n\nBitte sorge für ein ruhiges Umfeld und stell dir wenn du magst ein Getränk parat.\n\nFalls du soweit bist, drücke die Leertaste um das Experiment zu starten.');
    Explaination3_key_resp.keys = undefined;
    Explaination3_key_resp.rt = undefined;
    _Explaination3_key_resp_allKeys = [];
    // keep track of which components have finished
    Explaination_Screen3Components = [];
    Explaination_Screen3Components.push(Explaination3_text);
    Explaination_Screen3Components.push(Explaination3_key_resp);
    
    for (const thisComponent of Explaination_Screen3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Explaination_Screen3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Explaination_Screen3'-------
    // get current time
    t = Explaination_Screen3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Explaination3_text* updates
    if (t >= 0.0 && Explaination3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Explaination3_text.tStart = t;  // (not accounting for frame time here)
      Explaination3_text.frameNStart = frameN;  // exact frame index
      
      Explaination3_text.setAutoDraw(true);
    }

    
    // *Explaination3_key_resp* updates
    if (t >= 0.0 && Explaination3_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Explaination3_key_resp.tStart = t;  // (not accounting for frame time here)
      Explaination3_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Explaination3_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Explaination3_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Explaination3_key_resp.clearEvents(); });
    }

    if (Explaination3_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Explaination3_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Explaination3_key_resp_allKeys = _Explaination3_key_resp_allKeys.concat(theseKeys);
      if (_Explaination3_key_resp_allKeys.length > 0) {
        Explaination3_key_resp.keys = _Explaination3_key_resp_allKeys[_Explaination3_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Explaination3_key_resp.rt = _Explaination3_key_resp_allKeys[_Explaination3_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Explaination_Screen3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Explaination_Screen3RoutineEnd() {
  return async function () {
    //------Ending Routine 'Explaination_Screen3'-------
    for (const thisComponent of Explaination_Screen3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Explaination3_key_resp.keys', Explaination3_key_resp.keys);
    if (typeof Explaination3_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Explaination3_key_resp.rt', Explaination3_key_resp.rt);
        routineTimer.reset();
        }
    
    Explaination3_key_resp.stop();
    // the Routine "Explaination_Screen3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pause1_key_resp_allKeys;
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
    Pause1_text.setText('Du hast 17% geschafft.\n\nWenn du möchtest kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.');
    Pause1_key_resp.keys = undefined;
    Pause1_key_resp.rt = undefined;
    _Pause1_key_resp_allKeys = [];
    // keep track of which components have finished
    PauseComponents = [];
    PauseComponents.push(Pause1_text);
    PauseComponents.push(Pause1_key_resp);
    
    for (const thisComponent of PauseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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
    
    // *Pause1_text* updates
    if (t >= 0.0 && Pause1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause1_text.tStart = t;  // (not accounting for frame time here)
      Pause1_text.frameNStart = frameN;  // exact frame index
      
      Pause1_text.setAutoDraw(true);
    }

    
    // *Pause1_key_resp* updates
    if (t >= 0.0 && Pause1_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause1_key_resp.tStart = t;  // (not accounting for frame time here)
      Pause1_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pause1_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pause1_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pause1_key_resp.clearEvents(); });
    }

    if (Pause1_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pause1_key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _Pause1_key_resp_allKeys = _Pause1_key_resp_allKeys.concat(theseKeys);
      if (_Pause1_key_resp_allKeys.length > 0) {
        Pause1_key_resp.keys = _Pause1_key_resp_allKeys[_Pause1_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pause1_key_resp.rt = _Pause1_key_resp_allKeys[_Pause1_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of PauseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of PauseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pause1_key_resp.keys', Pause1_key_resp.keys);
    if (typeof Pause1_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pause1_key_resp.rt', Pause1_key_resp.rt);
        routineTimer.reset();
        }
    
    Pause1_key_resp.stop();
    // the Routine "Pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pause2_key_resp_allKeys;
var Pause2Components;
function Pause2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pause2'-------
    t = 0;
    Pause2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pause2_text.setText('Du hast ein Drittel geschafft.\n\nWenn du möchtest, kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.');
    Pause2_key_resp.keys = undefined;
    Pause2_key_resp.rt = undefined;
    _Pause2_key_resp_allKeys = [];
    // keep track of which components have finished
    Pause2Components = [];
    Pause2Components.push(Pause2_text);
    Pause2Components.push(Pause2_key_resp);
    
    for (const thisComponent of Pause2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pause2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pause2'-------
    // get current time
    t = Pause2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pause2_text* updates
    if (t >= 0.0 && Pause2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause2_text.tStart = t;  // (not accounting for frame time here)
      Pause2_text.frameNStart = frameN;  // exact frame index
      
      Pause2_text.setAutoDraw(true);
    }

    
    // *Pause2_key_resp* updates
    if (t >= 0.0 && Pause2_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause2_key_resp.tStart = t;  // (not accounting for frame time here)
      Pause2_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pause2_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pause2_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pause2_key_resp.clearEvents(); });
    }

    if (Pause2_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pause2_key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _Pause2_key_resp_allKeys = _Pause2_key_resp_allKeys.concat(theseKeys);
      if (_Pause2_key_resp_allKeys.length > 0) {
        Pause2_key_resp.keys = _Pause2_key_resp_allKeys[_Pause2_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pause2_key_resp.rt = _Pause2_key_resp_allKeys[_Pause2_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pause2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pause2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pause2'-------
    for (const thisComponent of Pause2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pause2_key_resp.keys', Pause2_key_resp.keys);
    if (typeof Pause2_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pause2_key_resp.rt', Pause2_key_resp.rt);
        routineTimer.reset();
        }
    
    Pause2_key_resp.stop();
    // the Routine "Pause2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pause3_key_resp_allKeys;
var Pause3Components;
function Pause3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pause3'-------
    t = 0;
    Pause3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pause3_text.setText('Super! Du hast die Hälfte geschafft.\n\nWenn du möchtest, kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.');
    Pause3_key_resp.keys = undefined;
    Pause3_key_resp.rt = undefined;
    _Pause3_key_resp_allKeys = [];
    // keep track of which components have finished
    Pause3Components = [];
    Pause3Components.push(Pause3_text);
    Pause3Components.push(Pause3_key_resp);
    
    for (const thisComponent of Pause3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pause3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pause3'-------
    // get current time
    t = Pause3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pause3_text* updates
    if (t >= 0.0 && Pause3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause3_text.tStart = t;  // (not accounting for frame time here)
      Pause3_text.frameNStart = frameN;  // exact frame index
      
      Pause3_text.setAutoDraw(true);
    }

    
    // *Pause3_key_resp* updates
    if (t >= 0.0 && Pause3_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause3_key_resp.tStart = t;  // (not accounting for frame time here)
      Pause3_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pause3_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pause3_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pause3_key_resp.clearEvents(); });
    }

    if (Pause3_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pause3_key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _Pause3_key_resp_allKeys = _Pause3_key_resp_allKeys.concat(theseKeys);
      if (_Pause3_key_resp_allKeys.length > 0) {
        Pause3_key_resp.keys = _Pause3_key_resp_allKeys[_Pause3_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pause3_key_resp.rt = _Pause3_key_resp_allKeys[_Pause3_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pause3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pause3RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pause3'-------
    for (const thisComponent of Pause3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pause3_key_resp.keys', Pause3_key_resp.keys);
    if (typeof Pause3_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pause3_key_resp.rt', Pause3_key_resp.rt);
        routineTimer.reset();
        }
    
    Pause3_key_resp.stop();
    // the Routine "Pause3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pause4_key_resp_allKeys;
var Pause4Components;
function Pause4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pause4'-------
    t = 0;
    Pause4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pause4_text.setText('Du hast zwei Drittel  geschafft.\n\nWenn du möchtest, kannst du eine  Pause machen.\n\nDrücke "P" um fortzufahren.');
    Pause4_key_resp.keys = undefined;
    Pause4_key_resp.rt = undefined;
    _Pause4_key_resp_allKeys = [];
    // keep track of which components have finished
    Pause4Components = [];
    Pause4Components.push(Pause4_text);
    Pause4Components.push(Pause4_key_resp);
    
    for (const thisComponent of Pause4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pause4RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pause4'-------
    // get current time
    t = Pause4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pause4_text* updates
    if (t >= 0.0 && Pause4_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause4_text.tStart = t;  // (not accounting for frame time here)
      Pause4_text.frameNStart = frameN;  // exact frame index
      
      Pause4_text.setAutoDraw(true);
    }

    
    // *Pause4_key_resp* updates
    if (t >= 0.0 && Pause4_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause4_key_resp.tStart = t;  // (not accounting for frame time here)
      Pause4_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pause4_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pause4_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pause4_key_resp.clearEvents(); });
    }

    if (Pause4_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pause4_key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _Pause4_key_resp_allKeys = _Pause4_key_resp_allKeys.concat(theseKeys);
      if (_Pause4_key_resp_allKeys.length > 0) {
        Pause4_key_resp.keys = _Pause4_key_resp_allKeys[_Pause4_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pause4_key_resp.rt = _Pause4_key_resp_allKeys[_Pause4_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pause4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pause4RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pause4'-------
    for (const thisComponent of Pause4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pause4_key_resp.keys', Pause4_key_resp.keys);
    if (typeof Pause4_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pause4_key_resp.rt', Pause4_key_resp.rt);
        routineTimer.reset();
        }
    
    Pause4_key_resp.stop();
    // the Routine "Pause4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Pause5_key_resp_allKeys;
var Pause5Components;
function Pause5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Pause5'-------
    t = 0;
    Pause5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Pause5_text.setText('Das ist die letzte Pause.\n\nDu hast es fast geschafft.\n\nDrücke "P" um fortzufahren.');
    Pause5_key_resp.keys = undefined;
    Pause5_key_resp.rt = undefined;
    _Pause5_key_resp_allKeys = [];
    // keep track of which components have finished
    Pause5Components = [];
    Pause5Components.push(Pause5_text);
    Pause5Components.push(Pause5_key_resp);
    
    for (const thisComponent of Pause5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pause5RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Pause5'-------
    // get current time
    t = Pause5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pause5_text* updates
    if (t >= 0.0 && Pause5_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause5_text.tStart = t;  // (not accounting for frame time here)
      Pause5_text.frameNStart = frameN;  // exact frame index
      
      Pause5_text.setAutoDraw(true);
    }

    
    // *Pause5_key_resp* updates
    if (t >= 0.0 && Pause5_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pause5_key_resp.tStart = t;  // (not accounting for frame time here)
      Pause5_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Pause5_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Pause5_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Pause5_key_resp.clearEvents(); });
    }

    if (Pause5_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Pause5_key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _Pause5_key_resp_allKeys = _Pause5_key_resp_allKeys.concat(theseKeys);
      if (_Pause5_key_resp_allKeys.length > 0) {
        Pause5_key_resp.keys = _Pause5_key_resp_allKeys[_Pause5_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Pause5_key_resp.rt = _Pause5_key_resp_allKeys[_Pause5_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of Pause5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Pause5RoutineEnd() {
  return async function () {
    //------Ending Routine 'Pause5'-------
    for (const thisComponent of Pause5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Pause5_key_resp.keys', Pause5_key_resp.keys);
    if (typeof Pause5_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Pause5_key_resp.rt', Pause5_key_resp.rt);
        routineTimer.reset();
        }
    
    Pause5_key_resp.stop();
    // the Routine "Pause5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Goodbye_ScreenComponents;
function Goodbye_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Goodbye_Screen'-------
    t = 0;
    Goodbye_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    Goodbye_text.setText('Vielen Dank für deine Teilnahme und bis in zwei Wochen.\n\nDas Programm schließt sich automatisch.');
    // keep track of which components have finished
    Goodbye_ScreenComponents = [];
    Goodbye_ScreenComponents.push(Goodbye_text);
    
    for (const thisComponent of Goodbye_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Goodbye_ScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Goodbye_Screen'-------
    // get current time
    t = Goodbye_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Goodbye_text* updates
    if (t >= 0.0 && Goodbye_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Goodbye_text.tStart = t;  // (not accounting for frame time here)
      Goodbye_text.frameNStart = frameN;  // exact frame index
      
      Goodbye_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Goodbye_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Goodbye_text.setAutoDraw(false);
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
    for (const thisComponent of Goodbye_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Goodbye_ScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'Goodbye_Screen'-------
    for (const thisComponent of Goodbye_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
