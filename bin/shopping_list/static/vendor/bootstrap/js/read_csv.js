function getCSV() {
    const request = new XMLHttpRequest();
    request.open("GET", "supermarket_infomation/174.985.csv", true);
    request.send(null);

   request.onload = function () {
       splitCSV(request.responseText)
   }
}

function splitCSV(str) {
    const result = [];
    const tmp = str.split("\n");

    for (let i = 0; i < tmp.length; ++i) {
       result[i] = tmp[i].split(',');
   }

   document.getElementById("supermarket_infomation").innerHTML = result[0];
}