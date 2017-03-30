
// Name Space
this.name = "LocationButtonStyler";
var RAPP = RAPP || {};

// Initialize
RAPP.LocationButtonStyler = ( function() {
    var OPEN = "Open";
    var CLOSE = "Close";
    var THRESHOLD = 60;
    var CLOSING_SOON_STYLE = "btn-warning";
    var OPEN_STYLE = "btn-success";
    var CLOSED_STYLE = "btn-danger";
    var TIME_FORMAT = 'h:mm a';

    
    /**** Private Methods ****/
    
    /*
     * param: location_id
     * sets given location_id to have CLOSING_SOON_STYLE class
     */
    var setClosingSoonStyling = function( location_id ) {
        $( location_id ).addClass( CLOSING_SOON_STYLE );
    };
    
    /*
     * param: location_id
     * sets given location_id to have OPEN_STYLE class
     */
    var addOpenStyling = function( location_id ) {
        $( location_id ).addClass( OPEN_STYLE );
    };
    
    /*
     * param: location_id
     * sets given location_id to have CLOSE_STYLE class
     */
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
        var weekDay = RAPP.TimeManager.dayOfWeek();
        var locationAndTimes = RAPP.LocationManager.getLocationIdsToTimeIdsObject();
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
     * for location opening and closing times
     */
    var currentLocationTimes = function() {
        var _today = getTodaysTimeIds();
        var currentLocationTimes = {}
        var timeIdAndValue = RAPP.LocationManager.getTimeIdtoTimeValueObject_Location();
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
    
    /*
     * Sets css styling classes to all location buttons
     * Uses location Id's and current time data 
     * found in currentLocationTimes() return value
     * 
     */ 
    var setLocationButtonStyles = function() {  
        var currentTime = RAPP.TimeManager.getMoment();
        var openTime;
        var closeTime;
        var locationTimesToday = currentLocationTimes();
        for ( location_id in locationTimesToday ) {
            var o_time = locationTimesToday[ location_id ].OPEN;
            openTime = makeMoment( o_time, 0 );
            var c_time = locationTimesToday[ location_id ].CLOSE;
            closeTime = makeMoment( c_time, 0 );
            
            if ( isClosingSoon( currentTime, openTime, closeTime )) {
                setClosingSoonStyling( location_id );
                
            } else if ( isOpen( currentTime, openTime, closeTime )) {
                addOpenStyling( location_id );
            
            } else {
                addClosedSyling( location_id );
            }
        }
    };
    
    /*
     * params: {moment()} currentTime, openTime, closeTime
     * returns: {boolean} If location is currently open
     */ 
    var isOpen = function( currentTime, openTime, closeTime ) {
        if ( currentTime < openTime ) {
            return false; 
            
        } else if ( currentTime > closeTime ) {
            return false;
            
        } else {
            return true;
        }
    }
    
    /*
     * params: {moment()} currentTime, openTime, closeTime 
     * returns: {boolean} If location is closing within time THRESHOLD
     */ 
    var isClosingSoon = function( currentTime, openTime, closeTime ) {
        var thresholdTime = RAPP.TimeManager.getMomentWithOffset( THRESHOLD, 'minute' );
        if ( isOpen( currentTime, openTime, closeTime )) {
            if ( thresholdTime > closeTime ) {
                return true;
                
            } else {
                return false;
            }
        } else {
            return false;
        }
    };
    
    /*
     * Appends today's open and close time to location button
     * on index.html page
     */
    var setTodaysTimesToButton = function() {
        var locationTimes = currentLocationTimes();
        for ( loc_id in locationTimes ){
            var openTime = locationTimes[ loc_id ].OPEN;
            var closeTime = locationTimes[ loc_id ].CLOSE;
            var openMoment = makeMoment( openTime, 0 );
            var closeMoment = makeMoment( closeTime, 0) ;
            var open = openMoment.format( TIME_FORMAT ); 
            var close = closeMoment.format( TIME_FORMAT ); 
            $( loc_id ).append('<p>' + open + ' - ' + close +'</p>');
        }
    };   
    
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
    
    /* 
     * Sets time specfic styles to Location Buttons
     * Displays current day's hours for location button
     */ 
    var init = function() {
        setLocationButtonStyles();
        setTodaysTimesToButton();
    };
         
    /**** Public Methods ****/ 
    return {
        
        init: function() {
            init();
        }
    }
})();