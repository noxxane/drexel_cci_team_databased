async function getRep(userZip) {
  const response = await fetch("../zips_to_reps.json");
  const json = await response.json();
  return json[userZip];
}

async function getSen(userSen){
  const response = await fetch("../states_to_sens.json");
  const json = await response.json();
  return json[userSen];
}

async function findRep() {
  let userZip = document.getElementById("zip_input").value;
  document.getElementById("rep_output").innerHTML = await getRep(userZip);
  
  // alert(await getRep(userZip)); 
}

async function findSen() {
  let userState = document.getElementById("state_input").value;
  document.getElementById("sen_output").innerHTML = await getSen(userState);
  // alert(await getSen(userState));
  }