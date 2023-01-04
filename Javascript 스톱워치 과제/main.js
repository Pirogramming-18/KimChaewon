let minutes = 0;
let seconds = 0;
let temMillis = 0;

//요소 선택
const appendTemMillis = document.getElementById("temMillis");
const appendSeconds = document.getElementById("seconds");
const appendMinutes = document.getElementById("minutes");
const btStart = document.getElementById("start");
const btReset = document.getElementById("reset");
const btStop = document.getElementById("stop");

let intervalId;

btStart.onclick = function () {
  clearInterval(intervalId);
  intervalId = setInterval(operateTimer, 10);
};

//1ms마다 시간에 대한 숫자 증가.
function operateTimer() {
  temMillis++;
  appendTemMillis.textContent = temMillis > 9 ? temMillis : "0" + temMillis;
  if (temMillis > 99) {
    seconds++;
    appendSeconds.textContent = seconds > 9 ? seconds : "0" + seconds;
    temMillis = 0;
    appendTemMillis.textContent = "00";
  }
  if (seconds > 59) {
    minutes++;
    appendMinutes.textContent = minutes > 9 ? minutes : "0" + minutes;
    seconds = 0;
    appendSeconds.textContent = "00";
  }
}

btStop.onclick = function () {
  clearInterval(intervalId);
};

btReset.onclick = function () {
  clearInterval(intervalId);
  temMillis = 0;
  minutes = 0;
  seconds = 0;
  appendMinutes.textContent = "00";
  appendSeconds.textContent = "00";
  appendTemMillis.textContent = "00";
};
