$(function(){
	//点击搜索小ICON
	$(".search").on('click',function(){
		if($(".search-new").hasClass("search-show")){
			$(this).addClass("sear-show");
			$(".search-new").removeClass("search-show");
		}else{
			$(this).removeClass("sear-show");
			$(".search-new").addClass("search-show");
		}
	});
	
	$(".close").on('click',function(){
		$(".search-new").removeClass("search-show");
		$(".search").addClass("sear-show");
	});
	
	
	$('.ticket-btn').on('click',function(e){
		e.stopPropagation();
	});
	
})