$('.carousel').carousel({
     interval: 8000,
     pause:true,
     wrap:false
});

$( document ).ready(function () {
	$(".moreBox").slice(0, 3).show();
	  if ($(".blogBox:hidden").length != 0) {
		$("#loadMore").show();
	  }   
	  $("#loadMore").on('click', function (e) {
		e.preventDefault();
		$(".moreBox:hidden").slice(0, 6).slideDown();
		if ($(".moreBox:hidden").length == 0) {
		  $("#loadMore").fadeOut('slow');
		}
	  });
	});

$(document).ready(function(){
   $("#categories").change(function(e){
   	e.preventDefault();
   	var category = $(this).val();
   	var data = {category};
   	$.ajax({
   		type : 'GET',
   		url :  "{% url 'get_selected_journal_category' %}",
   		data : data,
   		success : function(response){
   			$("#selectcat").html()
   		},
   		error : function(response){
   			console.log(response)
   		}
   	})
   })
})
