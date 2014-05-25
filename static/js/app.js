/*
case insensitive :cotains
shamelessly copied from http://css-tricks.com/snippets/jquery/make-jquery-contains-case-insensitive/
*/
$.expr[":"].contains = $.expr.createPseudo(function(arg) {
    return function( elem ) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});

(function($){
    var list = $("#manifesto_items_list");
    var text = $("#qfilter_id");
    text.bind("input keypress change", function(e){
        var input_value = $(this).val();
        if (input_value != '') {
            list.children("li").hide();
            foundLi = $('li:contains("' + input_value + '")');
            foundLi.show();
            $("#no_result_message").show();
        } else {
            list.children("li").show();
            $("#no_result_message").hide();
        }
    });
})(jQuery)