$(document).ready( function () {
    $('#timetable').DataTable({
        "paging": false,
        "order": [[ 2, "asc" ],[3, "asc"],[4, "asc"]]
    });
    $('#dayFilter').multiselect({
        includeSelectAllOption: true,
        buttonText: function(options, select){
            return 'Days';
        }}
    );
    $('#courseFilter').multiselect({
        includeSelectAllOption: true,
        buttonText: function(options, select){
            return 'Courses';
        }}
    );
} );