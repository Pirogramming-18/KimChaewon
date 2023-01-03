function loadItems() {
  return fetch("data/data.json")
    .then((response) => response.json())
    .then((json) => json.items);
}

function displayItems(items) {
  const container = document.querySelector(".items");

  container.innerHTML = items.map((item) => creatHTMLString(item)).join("");
}

function creatHTMLString(item) {
  return `
  <li class="item">
      <img src=${item.image} alt=${item.type} class="item__thumbnail" />
      <span class="item__description">${item.gender}, ${item.size}</span>
  </li>
  `;
}

function onButtonClick(e, items) {
  const dataset = e.target.dataset;
  const key = dataset.key;
  const value = dataset.value;
  console.log(dataset);
  if (key == null || value == null) {
    return;
  }

  displayItems(items.filter((item) => item[key] == value));
}

function setEventListeners(items) {
  const logo = document.querySelector(".logo");
  const buttons = document.querySelector(".buttons");
  logo.addEventListener("click", () => displayItems(items));
  console.log(buttons);
  buttons.addEventListener("click", (e) => onButtonClick(e, items));
}

loadItems()
  .then((items) => {
    displayItems(items);
    setEventListeners(items);
  })
  .catch(console.log);
