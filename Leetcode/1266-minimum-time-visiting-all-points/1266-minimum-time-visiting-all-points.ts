/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let time = 0;

    for(let i = 0; i < points.length-1; i++) {
      let start = points[i];
      let end = points[i+1];
      while(end[0]-start[0] > 0 && end[1]-start[1] > 0) {
        start[0]++;
        start[1]++;
        time++;
      }
      while(end[0]-start[0] < 0 && end[1]-start[1] < 0) {
        start[0]--;
        start[1]--;
        time++;
      }      
        while(end[0]-start[0] > 0 && end[1]-start[1] < 0) {
        start[0]++;
        start[1]--;
        time++;
      }
      while(end[0]-start[0] <0 && end[1]-start[1] > 0) {
        start[0]--;
        start[1]++;
        time++;
      }
      while(end[0]-start[0] > 0) {
        start[0]++;
        time++;
      }
      while(end[0]-start[0] < 0) {
        start[0]--;
        time++;
      }
      while(end[1]-start[1] > 0) {
        start[1]++;
        time++;
      }
      while(end[1]-start[1] < 0) {
        start[1]--;
        time++;
      }
    }
    return time;
};

console.log(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]));
