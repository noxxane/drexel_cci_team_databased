async function getRep(userZip) {
  const response = await fetch("../zips_to_reps.json");
  const json = await response.json();
  return json[userZip];
}

async function getSen(userSen){
  const response = await fetch("../zips_to_senators.json");
  const json = await response.json();
  return json[userSen];
}

async function findRep() {
  let userZip = document.getElementById("zip_input").value;
  alert(await getRep(userZip)); 
}

async function findSen(){
  let userState
}
