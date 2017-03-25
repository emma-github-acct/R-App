
// Name Space
this.name = "LocationDataCollector";
var RAPP = RAPP || {};

// Initialize
RAPP.LocationManager = ( function() {
    
    var LOCATION_DIV= "#locationButtons";
    var LOCATION_TIME_DIV= ".locationRegularHours";
    var LOCATION_IDS = "button";
    var TIME_IDS = "span";
    var WEEKDAY_IDS = "li";
    var REG_TIME_DIV = "#RegularHours"; 
    
    /**** Private Methods ****/
    
    /*
     * Collects an type of html tag ex: button, span, li
     * within the specific div
     */   
    var collectIds = function( _div, _htmlType ) {
        var _ids = [];
        $( _div ).find( _htmlType ).each( function() {
        _ids.push( "#"+ this.id ); 
        });
        return _ids;
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
    
    var createIdToTimeIdsObject = function( _ids, _timeIds ) {  
        var idToTimeIdsObject = {};
        for ( var i = 0; i < _timeIds.length; i++ ) {
            for ( var j = 0; j < _timeIds.length; j++ ) {
                var _timeId = _timeIds[ i ];
                var _id =  _ids[ j ];
                addTimeToContainer( _id, _timeId, idToTimeIdsObject );   
            } 
        }
        return idToTimeIdsObject;
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
        
        collectIds: function( _div, _htmlType ) {
            return collectIds( _div, _htmlType );
        }, 
        
        getLocationIdsToTimeIdsObject: function() {
            var locIds = collectIds( LOCATION_DIV, LOCATION_IDS );
            var timeIds = collectIds( LOCATION_TIME_DIV, TIME_IDS );
            return createIdToTimeIdsObject( locIds, timeIds );
        }, 
        
        getTimeIdtoTimeValueObject_Location: function( ) {
            var locIds = collectIds( LOCATION_DIV, LOCATION_IDS );
            var timeIds = collectIds( LOCATION_TIME_DIV, TIME_IDS );
            var locationToTimeObject = createIdToTimeIdsObject( locIds, timeIds );
            return createTimeIdtoTimeValueObject( locationToTimeObject );
        }, 

        getWeekdayIdsToTimeIdsObject: function() {
            var weekdayIds = collectIds( REG_TIME_DIV, WEEKDAY_IDS );
            var timeIds = collectIds( REG_TIME_DIV, TIME_IDS );
            return createIdToTimeIdsObject( weekdayIds, timeIds );
        }, 
        
        getTimeIdtoTimeValueObject_Weekday: function( ) {
            var weekdayIds = collectIds( REG_TIME_DIV, WEEKDAY_IDS );
            var timeIds = collectIds( REG_TIME_DIV, TIME_IDS );
            var weekdayToTimeObject = createIdToTimeIdsObject( weekdayIds, timeIds );
            return createTimeIdtoTimeValueObject( weekdayToTimeObject );
        },

    }
 
})();