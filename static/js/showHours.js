function showHours() {
    
    // Location
    var library = document.getElementById('libHours');
    
    // Get these from database
    var open_hour = 6; 
    var close_hour = 30;
    
    // Get from moment.js
    var current_hour = 12;
    
    if ( current_hour > close_hour ) {
        // lib is closed
        library.innerHTML = "Olin - CLOSED";
        
    } else if ( current_hour < close_hour && current_hour > open_hour ) {
        library.innerHTML = "Olin - OPEN";
    }
    else {
        library.innerHTML = "Olin - CLOSED";
    }
    

}