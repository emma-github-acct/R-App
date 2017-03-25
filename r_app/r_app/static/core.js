// Main Core File

var initialize = function() {
    console.log("Location- DataCollector");
    var o = RAPP.LocationDataCollector.getLocationIdsToTimeIdsObject( );
    var p = RAPP.LocationDataCollector.getTimeIdtoTimeValueObject( );
    console.log(o);
    console.log(p);
    
    console.log("Time- DataCollector");
    var d = RAPP.TimeDataCollector.date();
    var m = RAPP.TimeDataCollector.minute();
    var h = RAPP.TimeDataCollector.hour();
    var w = RAPP.TimeDataCollector.dayOfWeek();
    console.log("Date: "+ d);
    console.log("Minute: "+m);
    console.log("Hour: "+h);
    console.log("DAY of week "+w);
    
    console.log("Location Button Styler");
    var b = RAPP.LocationButtonStyler.currentLocationTimes();
    var a = RAPP.LocationButtonStyler.getTodaysTimeIds();
    RAPP.LocationButtonStyler.setLocationButtonStyles();
    console.log(a);
    console.log(b);
}

$(document).ready(initialize);