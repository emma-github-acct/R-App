
// Name Space
this.name = "TimeDataCollector";
var RAPP = RAPP || {};

// Initialize
RAPP.TimeDataCollector = ( function() {

    
    /**** Private Methods ****/
    
    var getCurrentWeekday = function() {
        var m = moment();
        return m.weekday();
    };
    
    var getCurrentDate = function() {
        var m = moment();
        return m.get('date');
    };
    
    var getCurrentHour = function() {
        var m = moment();
        return m.get('hour');
    };
    
    var getCurrentMinute = function() {
        var m = moment();
        return m.get('minute');
    };
    
    
    
    /**** Public Methods ****/
    
    return {
        
        dayOfWeek: function() {
            return getCurrentWeekday();
        },
        
        date: function() {
            return getCurrentDate();
        },
        
        hour: function() {
            return getCurrentHour();
        },
        
        minute: function() {
            return getCurrentMinute();
        }
    }
 
})();