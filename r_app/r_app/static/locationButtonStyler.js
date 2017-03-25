
// Name Space
this.name = "LocationButtonStyler";
var RAPP = RAPP || {};

// Initialize
RAPP.LocationButtonStyler = ( function() {
    var OPEN = "Open";
    var CLOSE = "Close";
    var THRESHOLD = 30;
    var CLOSING_SOON_STYLE = "closingSoonLocation";
    var OPEN_STYLE = "openLocation";
    var CLOSED_STYLE = "closedLocation";

    
    /**** Private Methods ****/
    
    var setClosingSoonStyling = function( location_id ) {
        $( location_id ).addClass( CLOSING_SOON_STYLE );
    };
    
    var addOpenStyling = function( location_id ) {
        $( location_id ).addClass( OPEN_STYLE );
    };
    
    var addClosedSyling = function( location_id ) {
        $( location_id ).addClass( CLOSED_STYLE );
    };
    
    /*
     * Gathers all location button id's
     * and today's opening and closeing
     * time Id's found in index.hmtl 
     *
     * return: object
     * object's key is location button id
     * object's key-value is array of time Ids for today
     */
    var getTodaysTimeIds = function() {
        var weekDay = RAPP.TimeDataCollector.dayOfWeek();
        var locationAndTimes = RAPP.LocationDataCollector.getLocationIdsToTimeIdsObject();
        var today= {};

        for ( locationId in locationAndTimes ) {
            today[ locationId ] = [];
            var timeIds = locationAndTimes[ locationId ];
            for ( var i = 0; i < timeIds.length; i++ ) {
                if ( timeIds[ i ].includes( weekDay )){
                    today[ locationId ].push( timeIds[ i ]);
                }
            }
        }
        return today;
    }
    
    /*
     * return: object
     * object's key is location button id
     * object's key-value is an Open or Close value
     * Open and Close value are numerical time values
     * for lcoation opening and closing times
     */
    var currentLocationTimes = function() {
        var _today = getTodaysTimeIds();
        var currentLocationTimes = {}
        var timeIdAndValue = RAPP.LocationDataCollector.getTimeIdtoTimeValueObject();
        var openTime;
        var closeTime;
        for ( loc in _today ) {
            currentTimeArray = _today[loc];
            for ( var j = 0; j < currentTimeArray.length; j++ ) {
                if ( currentTimeArray[ j ].includes( OPEN )){
                    openId = currentTimeArray[ j ];
                    openTime = timeIdAndValue[ openId ];
                }
                if ( currentTimeArray[ j ].includes( CLOSE )){
                    closeId = currentTimeArray[ j ];
                    closeTime = timeIdAndValue[ closeId ];
                }
            }
            currentLocationTimes[ loc ] = {
                OPEN: openTime,
                CLOSE: closeTime
            };
        }
        return currentLocationTimes;
    };
    
    
    // TO DO: when times include minutes as well
    // we must add that to time objects
    var setLocationButtonStyles = function() {  
        var currentTime = RAPP.TimeDataCollector.getMoment();
        var openTime = RAPP.TimeDataCollector.getMoment();
        var closeTime = RAPP.TimeDataCollector.getMoment();
        var locationTimesToday = currentLocationTimes();
        for ( location_id in locationTimesToday ) {
            var o_time = locationTimesToday[ location_id ].OPEN;
            openTime.set('hour', o_time);
            openTime.set('minute', 0);
            var c_time = locationTimesToday[ location_id ].CLOSE;
            closeTime.set('hour', c_time);
            closeTime.set('minute', 0);
            
            if ( isClosingSoon( currentTime, openTime, closeTime )) {
                setClosingSoonStyling( location_id );
                
            } else if ( isOpen( currentTime, openTime, closeTime )) {
                addOpenStyling( location_id );
            
            } else {
                addClosedSyling( location_id );
            }
        }
    };
    
    var isOpen = function( currentTime, openTime, closeTime ) {
        if ( currentTime < openTime ) {
            return false; 
            
        } else if ( currentTime > closeTime ) {
            return false;
            
        } else {
            return true;
        }
    }
    
    var isClosingSoon = function( current_time, open_time, close_time ) {
        var thresholdTime = RAPP.TimeDataCollector.getMomentWithOffset( THRESHOLD, 'minute' );
        if ( isOpen( current_time, open_time, close_time )) {
            if ( thresholdTime > close_time ) {
                return true;
            } else if (thresholdTime < close_time ){
                return false;
            }
            else {
                return false;
            } 
        } else {
            return false;
        }
    }
    
    
    
    /**** Public Methods ****/
    
    return {
        
        getTodaysTimeIds: function() {
            return getTodaysTimeIds();
        },
        
        currentLocationTimes: function() {
            return currentLocationTimes();
        },
        
        setLocationButtonStyles: function(){
            setLocationButtonStyles();
        }
    }
 
})();