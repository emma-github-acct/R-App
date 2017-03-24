// Main Core File

var initialize = function() {
    var o = RAPP.LocationDataCollector.getLocationIdsToHoursIdsObject( );
    var p = RAPP.LocationDataCollector.getHourIdtoHourValueObject( );
    console.log(o);
    console.log(p);
}

$(document).ready(initialize);