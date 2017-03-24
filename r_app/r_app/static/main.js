// Main Core File

var initialize = function() {
    var o = RAPP.LocationDataCollector.getLocationIdsToHoursIdsObject( );
    var p = RAPP.LocationDataCollector.getHourIdtoHourValueObject( );
    console.log(o);
    console.log(p);
    
    var d = RAPP.TimeDataCollector.date();
    var m = RAPP.TimeDataCollector.minute();
    var h = RAPP.TimeDataCollector.hour();
    console.log("Date: "+ d);
    console.log("Minute: "+m);
    console.log("Hour: "+h);
}

$(document).ready(initialize);