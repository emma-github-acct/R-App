
// Name Space
this.name = "LocationButtonStyler";
var RAPP = RAPP || {};

// Initialize
RAPP.LocationDetailedStyler = ( function() {
    var OPEN = "Open";
    var CLOSE = "Close";
    var WEEKDAY_IDS = "li";
    var TIME_IDS = "span";
    var REG_TIME_DIV = "#RegularHours"; 
    var TIME_FORMAT = 'h:mm a';

    /**** Private Methods ****/
    
    /*
     * params: {int} hour, minute
     * returns: {moment()} moment
     *
     * Calls on RAPP.TimeManager.makeMoment function to create
     * custom moment
     */
    var makeMoment = function( hour, minute ) {
        return RAPP.TimeManager.makeMoment( hour, minute );
    }
    
    var convertMilitaryToStandard = function() {
        var timesAndValues = RAPP.LocationManager.getTimeIdtoTimeValueObject_Weekday();
        for ( timeId in timesAndValues ){
            var time = timesAndValues[ timeId ];
            var timeMoment = makeMoment( time, 0) ;
            var timeConverted = timeMoment.format( TIME_FORMAT ); 
            $( timeId ).html(timeConverted);
        }
    }
    
    var init = function() {
        convertMilitaryToStandard();
    }

    /**** Public Methods ****/ 
    return {
        
        init: function() {
            init();
        }
    }
})();