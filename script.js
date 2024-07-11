async function getRep(userZip) {
  const response = await fetch("./zips_to_reps.json");
  const json = await response.json();
  return json[userZip];
}

async function findRep() {
  let userZip = document.getElementById("zip_input").value;
  alert(await getRep(userZip));
}