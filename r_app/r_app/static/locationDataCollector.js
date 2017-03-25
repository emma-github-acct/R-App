
// Name Space
this.name = "LocationDataCollector";
var RAPP = RAPP || {};

// Initialize
RAPP.LocationDataCollector = ( function() {
    
    var LOCATION_DIV= "#locationButtons";
    var LOCATION_TIME_DIV= ".locationRegularHours";
    var BUTTON = "button";
    var SPAN = "span";
    
    /**** Private Methods ****/
    
    /*
     * Main index.html page
     * Location Button ID's
     */   
    var collectLocationIds = function() {
        var _locationIds = [];
        $( LOCATION_DIV ).find( BUTTON ).each( function() {
        _locationIds.push( "#"+ this.id ); 
        });
        return _locationIds;
    }
    
    /*
     * In non-displayed div on index.html page
     * Location Time ID's
     */
    var collectTimeIds = function() {
        var _timeIds = [];
        $( LOCATION_TIME_DIV ).find( SPAN ).each( function() {
        _timeIds.push( "#"+ this.id ); 
        });
        return _timeIds;
    }
    
    var addTimeToContainer = function( locationId, timeId , object ) {
        if ( timeId.includes( locationId )) {
            if ( !object[ locationId ] ){
                object[ locationId ] = [ timeId ];
            }
            else {
                object[ locationId ].push( timeId );
            }
        }      
    };
    
    var createLocationIdToTimeIdsObject = function( _locationIds, _timeIds ) {  
        var locationIdToTimeIdsObject = {};
        for ( var i = 0; i < _timeIds.length; i++ ) {
            for ( var j = 0; j < _timeIds.length; j++ ) {
                var timeId = _timeIds[ i ];
                var locationId =  _locationIds[ j ];
                addTimeToContainer( locationId, timeId, locationIdToTimeIdsObject );   
            } 
        }
        return locationIdToTimeIdsObject;
    }
    
    var createTimeIdtoTimeValueObject = function( locationToTimeObject ) {
        var timeIdtoTimeValueObject = {};
        for ( location_id in locationToTimeObject ){
            var timeIdArray = locationToTimeObject[ location_id ];
            for ( var i = 0; i < timeIdArray.length; i++ ){
                var time_id = timeIdArray[ i ];
                var time_val_html = $( time_id ).html();
                var time_value = Number( time_val_html );
                timeIdtoTimeValueObject[ time_id ] = time_value;
            }
        }
        return timeIdtoTimeValueObject;
    }
    
    /**** Public Methods ****/
    
    return {
        
        getLocationIdsToTimeIdsObject: function() {
            var locIds = collectLocationIds();
            var timeIds = collectTimeIds();
            return createLocationIdToTimeIdsObject( locIds, timeIds );
        }, 
        
        getTimeIdtoTimeValueObject: function( ) {
            var locIds = collectLocationIds();
            var timeIds = collectTimeIds();
            var locationToTimeObject = createLocationIdToTimeIdsObject( locIds, timeIds );
            return createTimeIdtoTimeValueObject( locationToTimeObject );
        }
    }
 
})();