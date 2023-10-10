let myLeads = [];
const inputEl = document.getElementById("input-el");
let inputBtn = document.getElementById("input-btn");
let dltBtn = document.getElementById("delete-btn");
const ulEl = document.getElementById("ul-el");
const leadsFromLocalStorage = JSON.parse(localStorage.getItem("myLeads"));
const tabBtn = document.getElementById("tab-btn");

if (leadsFromLocalStorage) {
  myLeads = leadsFromLocalStorage;
  render(myLeads);
}


tabBtn.addEventListener("click", function () {
  chrome.tabs.query({
    active: true,
    currentWindow: true},
    function(tabs) {
      myLeads = JSON.parse(localStorage.getItem("myLeads"))
        ? JSON.parse(localStorage.getItem("myLeads"))
        : [];
      myLeads.push(tabs[0].url);
      localStorage.setItem("myLeads", JSON.stringify(myLeads));
      render(myLeads);
    },
  );
});

function render(leads) {
  let listItems = "";
  for (let i = 0; i < myLeads.length; i++) {
    listItems += ` 
            <li>
                <a target='_blank' href='${myLeads[i]}'>
                    ${myLeads[i]}
                </a>
            </li>
        `;
  }
  ulEl.innerHTML = listItems;
}

dltBtn.addEventListener("dblclick", function () {
  localStorage.clear();
  myLeads = [];
  render(myLeads);
});

inputBtn.addEventListener("click", function (e) {
  e.preventDefault();
  myLeads.push(inputEl.value);
  inputEl.value = "";
  localStorage.setItem("myLeads", JSON.stringify(myLeads));
  renderLeads(myLeads);
});
