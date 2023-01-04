let seconds = 0;
let temMillis = 0;

//요소 선택
const appendTemMillis = document.getElementById("temMillis");
const appendSeconds = document.getElementById("seconds");
const btStart = document.getElementById("start");
const btReset = document.getElementById("reset");
const btStop = document.getElementById("stop");
const recordlist = document.querySelector(".record-list");
const btClickAll = document.getElementById("checkall");
const btDelete = document.getElementById("delete");

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
}

btStop.onclick = function () {
  clearInterval(intervalId);
  HandleRecord();
};

btReset.onclick = function () {
  clearInterval(intervalId);
  temMillis = 0;
  seconds = 0;
  appendSeconds.textContent = "00";
  appendTemMillis.textContent = "00";
};

function HandleRecord(event) {
  if (seconds == 0 && temMillis == 00) {
    event.preventDefault(); //시간이 있지 않을때는 이벤트 막기
  } else {
    const li = document.createElement("li");
    li.className = "item-list";
    const span = document.createElement("span");
    span.className = "span";
    span.innerHTML = `
    <input type="checkbox" name="bt_each"/>
    ${seconds < 10 ? "0" + seconds : seconds}:${
      temMillis < 10 ? "0" + temMillis : temMillis
    }`;

    li.appendChild(span);

    recordlist.prepend(li); //가장 최신의 레코드를 위로 출력하기 위해 위로삽입
  }
}

let each_list = document.getElementsByName("bt_each");
btClickAll.addEventListener("click", (e) => {
  checkAll(each_list);
});

function checkAll() {
  let allcheck = btClickAll.checked;
  for (let i = 0; i < each_list.length; i++) {
    each_list[i].checked = allcheck;
  }
}

btDelete.onclick = function () {
  removelist = [];
  deleteItem(each_list);
};

const p_list = document.getElementsByClassName("span");

function deleteItem() {
  let each_list = document.getElementsByName("bt_each");
  console.log(each_list.length);
  console.log(each_list);
  for (let j = 0; j < each_list.length; j++) {
    if (each_list[j].checked) {
      // let a = each_list[j].parentElement;
      removelist.push(j);
      console.log(j);
      // a.parentElement.remove();
      // console.log(each_list[j].parentElement);

      // each_list[j].parentElement.remove();
    } else {
      continue;
    }
  }
  console.log(removelist.length);

  for (let k = 0; k < removelist.length; k++) {
    let temp = 0;
    temp = each_list[removelist[k]].parentElement;
    console.log(temp);
    temp.parentElement.remove();
    removelist.pop(removelist[k]);
  }
}
