//ProjectTwo text:
document.getElementById("projectone").textContent =
  "A little bit about my secondary project";
document.getElementById("projectonetext").textContent =
  "This is a form that takes input and outputs a message to the user.";

document.getElementById("submit").onclick = function () {
  username = document.getElementById("username").value;
  age = document.getElementById("age").value;
  let online = true;
  let forSale = true;
  let isWorking = false;
  document.getElementById(
    "textcontent"
  ).textContent = `Hello, ${username} ${age}, are you ${online}?, are you for sale? ${forSale}, and are you able to work? ${isWorking}`;
};
