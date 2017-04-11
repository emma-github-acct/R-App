// Main Core File

var initialize = function() {

    RAPP.LocationButtonStyler.init();
    var a = RAPP.LocationManager.getLocationIdsToTimeIdsObject();
    var b = RAPP.LocationManager.getTimeIdtoTimeValueObject_Location();
    console.log(a);
    console.log(b);

}

$(document).ready(initialize);