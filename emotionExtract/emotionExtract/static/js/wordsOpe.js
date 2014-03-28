$(function() {
	wordsOpe.run();
});

var wordsOpe = {
	run : function() {
		wordsOpe.init();
	},
	
	init : function() {
		wordsOpe.event();
	},
	
	event : function() {
		$('#btn').click(function() {
			var words = $('#words').val();
			var type = $('#type').val();
			var score = $('#score').val();
			var lang = $("#lang").val();
			var content = JSON.stringify({'words':words,'type':type,'score':score,'lang':lang});
			$.post(dns.dns+'insertWords',{'content':content},function(result){
				result = JSON.parse(result);
				$("#showResult").html(result['info']);
			});
		});
		
		$('#btn_1').click(function() {
			$.post(dns.dns+'letterStat',function(result){
				result = JSON.parse(result);
				$("#showResult").html(result['info']);
			});
		});
	}
}