// Main Core File

var initialize = function() {

    RAPP.LocationButtonStyler.init();
    var a = RAPP.LocationManager.getLocationIdsToTimeIdsObject();
    var b = RAPP.LocationManager.getExceptionTimeIdtoExceptionTimeValueObject();
    console.log(a);
    console.log("Exceptions")
    console.log(b);

}

$(document).ready(initialize);