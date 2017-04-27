
// Name Space
this.name = "TimeDataCollector";
var RAPP = RAPP || {};

// Initialize
RAPP.TimeManager = ( function() {
    
    var WEEK_DAYS = {
        0: "sunday",
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday"
    };
  
    /**** Private Methods ****/
    
    var getCurrentWeekday = function() {
        var m = moment();
        var w = m.weekday();
        var weekDay = WEEK_DAYS[ w ];
        return weekDay;
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
    
    var getMoment = function() {
        return moment();
    };
    
    var getMomentWithOffset = function( offsetAmount, offsetType ) {
        var m = moment();
        var newMoment;
        if ( offsetAmount < 0 ){
            newMoment = m.subtract( abs( offsetAmount ), offsetType );
            
        } else {
            newMoment = m.add( offsetAmount, offsetType );
        }
        return newMoment;
    };
    
    var makeMoment = function( hour, minute ) {
        var m = moment();
        m.set( 'hour', hour );
        m.set( 'minute', minute );
        return m;
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
        },
        
        getMoment: function() {
            return getMoment();
        },
        
        getMomentWithOffset: function( offsetAmount, offsetType ) {
            return getMomentWithOffset( offsetAmount, offsetType );
        },
        
        makeMoment: function( hour, minute ) {
            return makeMoment( hour, minute );
        },  
    }
 
})();