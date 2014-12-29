var address;
var map;

$(document).ready(function() {
   initialize();
});

function codeAddress() {
   var address = $('input#address').val() + ', Chicago, IL';
   $.get($SCRIPT_ROOT + '/_geo',
      { address: address },
      function(data) {
         data = data.substring(1,data.length-1)
         var lat = Number(data.split(',')[0]);
         var lng = Number(data.split(',')[1]);
         map.panTo(new L.LatLng(lat,lng), 2);
         map.setZoom(14);
      }
   );   
}

