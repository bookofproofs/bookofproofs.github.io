var $j = jQuery.noConflict();

MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']], processEscapes: false},
    extensions: ["tex2jax.js"],
    jax: ["input/TeX","output/HTML-CSS"],
	'fast-preview': {disabled: true},
    TeX: {extensions: ["cancel.js", "noErrors.js", "AMSmath.js","AMSsymbols.js"], equationNumbers: { autoNumber: "AMS" } }
});

$j(document).ready(function() {

    $j( document ).tooltip();

    /* Treeview (thanks to https://www.w3schools.com/howto/howto_js_treeview.asp) */
    var toggler = document.getElementsByClassName("caret");
    var i;
    for (i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", function() {
            this.parentElement.querySelector(".nested").classList.toggle("active");
            this.classList.toggle("caret-down");
        });
        // auto-open treeview (default)
        toggler[i].parentElement.querySelector(".nested").classList.toggle("active");
        toggler[i].classList.toggle("caret-down");
    }

    //create dialog, but keep it closed
    var $div = $j('<div />').appendTo('body');
    $div.attr('id', 'dialog');

    $j("#dialog").dialog({
       autoOpen: false,
       height: 300,
       width: 350,
       modal: true
    });

    var availableTags = [{{ search-links }}];

    var url = "{{ url }}";

    // autocomplete
    $j( "#autocomplete" ).autocomplete({
		source: availableTags,
		minLength: 3,
		delay:500,
		select: function( event, ui ) {
			$j(this).val(ui.item.label);
			window.location.href = url + "/" + ui.item.value;
			return false;
        }
	});

    // don't really need this, but in case we do, store it and chain
    var oldFn = $j.ui.autocomplete.prototype._renderItem;

    // monkey-patch the autocomplete to format search results
    $j.ui.autocomplete.prototype._renderItem = function( ul, item ) {
        var re = new RegExp(this.term, "i") ;
        var t = item.label.replace(re,"<span style='font-weight:bold;color:orange;padding:0;'>$&</span>");
        return $j( "<li></li>" ).data( "item.autocomplete", item ).append("<a>" + t + "</a>").appendTo( ul );
    };

});

function showDialog(url){  //load content and open dialog
    $j("#dialog").load(url, {async: false});
    $j("#dialog").dialog("open");
}