const safetyMarkers = (road) => {
     let markers = 0;

     for (let i = 0; i < road.length; i++) {
         if (road[i] === 1) { 
             markers++;
             i += 2;
         }
     }
 
     return markers;
}

 
const road = [1, 0, 0, 1, 1, 0, 1];
console.log(safetyMarkers(road));