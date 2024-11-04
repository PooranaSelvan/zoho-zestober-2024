let rhinoCounts = [10, 8, 15, 12];
let maxRhinosPerRanger = 10;

let rangers = 0;

for (let i = 0; i < rhinoCounts.length; i++) {
    let rhinos = rhinoCounts[i];

    let rangersNeeded = Math.ceil(rhinos / maxRhinosPerRanger);
    
    rangers += rangersNeeded;
}

console.log(rangers);
