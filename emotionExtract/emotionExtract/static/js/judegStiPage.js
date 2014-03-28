$(function() {
	judegSti.run();
});

var judegSti = {
	run : function() {
		judegSti.init();
	},
	
	init : function() {
		judegSti.event();
	},
	
	event : function() {
		$('#getSti').click(function() {
			var sentence = $('#sentence').val();
			var content = JSON.stringify({'sentence':sentence});
			judegSti.getStiFun(content);
		});
	},
	
	getStiFun : function(content) {
		$.post(dns.dns+'judgeSti',{'content':content},function(result){
			result = JSON.parse(result);
			$('#showResult').html(result['info'] + '  ' + result['score']);
		});
	}
}