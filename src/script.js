async function getRep(userZip) {
  const response = await fetch("../zips_to_reps.json");
  const json = await response.json();
  return json[userZip];
}

async function getSen(userSen) {
  const response = await fetch("../states_to_sens.json");
  const json = await response.json();
  return json[userSen];
}

async function findRep() {
  let userZip = document.getElementById("zip_input").value;
  reps = await getRep(userZip);
  if (reps.length == 1) {
    output_span = reps[0];
  } else if (reps.length == 2) {
    output_span = `${reps[0]} and ${reps[1]}`;
  } else if (reps.length == 3) {
    output_span = `${reps[0]}, ${reps[1]}, and ${reps[2]}`;
  } else {
    output_span = reps;
  }
  document.getElementById("rep_output").innerHTML = output_span;
}

async function findSen() {
  let userState = document.getElementById("state_input").value;
  senators = await getSen(userState);
  output_span = `${senators[0]} and ${senators[1]}`;
  document.getElementById("sen_output").innerHTML = output_span;
}
