function showInfo() {

    var library_hours = document.getElementById('libHours');
    
    var library_open = new Date("2011-02-12 07:00:0.01");
    var open_hour = library_open.getHours(); 
    
    var library_closed = new Date("2011-02-12 30:00:0.01");
    var close_hour = library_closed.getHours();

    
    var today = new Date("2011-02-12 20:43:1.01");
    var current_hour = today.getHours(); // => 20
    
    if ( current_hour > close_hour ) {
        // lib is closed
        library_hours.innerHTML = "CLOSED";
        
    } else if ( current_hour < close_hour && current_hour > open_hour ) {
        library_hours.innerHTML = "OPEN";
    }
    else {
        library_hours.innerHTML = "CLOSED";
    }
    

}