$(document).ready(function(){

	
	$(".panel-detail.panel-default").hide().slideDown(1500);
	$(".post-detail.panel-heading").hide().slideDown("slow");
	$(".post-detail.panel-body").hide().slideDown(1500);

	$('#myModalPostDetail').on('shown.bs.modal', function () {
    	$(this).fadeIn();
})
	

	
});
