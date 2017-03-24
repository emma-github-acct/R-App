
// Name Space
this.name = "LocationDataCollector";
var RAPP = RAPP || {};

// Initialize
RAPP.LocationDataCollector = ( function() {
    
    var LOCATION_DIV= "#locationButtons";
    var LOCATION_HOURS_DIV= ".locationRegularHours";
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
        _locationIds.push( this.id ); 
        });
        return _locationIds;
    }
    
    /*
     * In non-displayed div on index.html page
     * Location Hours ID's
     */
    var collectHourIds = function() {
        var _hourIds = [];
        $( LOCATION_HOURS_DIV ).find( SPAN ).each( function() {
        _hourIds.push( this.id ); 
        });
        return _hourIds;
    }
    
    var addHourToContainer = function( locationId, hourId , object ) {
        if ( hourId.includes( locationId )) {
            if ( !object[ locationId ] ){
                object[ locationId ] = [ hourId ];
            }
            else {
                object[ locationId ].push( hourId );
            }
        }      
    };
    
    var createLocationIdToHourIdsObject = function( _locationIds, _hourIds ) {  
        var locationIdToHourIdsObject = {};
        for ( var i = 0; i < _hourIds.length; i++ ) {
            for ( var j = 0; j < _hourIds.length; j++ ) {
                var hourId = _hourIds[ i ];
                var locationId = _locationIds[ j ];
                addHourToContainer( locationId, hourId, locationIdToHourIdsObject );   
            } 
        }
        return locationIdToHourIdsObject;
    }
    
    var createHourIdtoHourValueObject = function( locationToHoursObject ) {
        var hourIdtoHourValueObject = {};
        for ( location_id in locationToHoursObject ){
            var hoursIdArray = locationToHoursObject[ location_id ];
            for ( var i = 0; i < hoursIdArray.length; i++ ){
                var hour_id = "#" + hoursIdArray[ i ];
                var hour_val_html = $( hour_id ).html();
                var hour_value = Number( hour_val_html );
                hourIdtoHourValueObject[ hour_id ] = hour_value;
            }
        }
        return hourIdtoHourValueObject;
    }
    
    /**** Public Methods ****/
    
    return {
        
        getLocationIdsToHoursIdsObject: function() {
            var locIds = collectLocationIds();
            var hourIds = collectHourIds();
            return createLocationIdToHourIdsObject( locIds, hourIds );
        }, 
        
        getHourIdtoHourValueObject: function( ) {
            var locIds = collectLocationIds();
            var hourIds = collectHourIds();
            var locationToHoursObject = createLocationIdToHourIdsObject( locIds, hourIds );
            return createHourIdtoHourValueObject( locationToHoursObject );
        }
    }
 
})();