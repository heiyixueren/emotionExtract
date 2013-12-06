$(function(){
	emotionExtract.run();
});

emotionExtract = {
	run : function(){
		emotionExtract._init();
	},
	
	_init : function() {
		emotionExtract.event();
	},
	
	event : function() {
		$("#btn-1").click(function(){
			textType = $("input[name=textType]:checked").val();
			text = $("#textArea").val();
			keyNum = parseInt($("#numOfKeyWords").val());
			if (!(keyNum>=0)){
				keyNum = 10;
			}
			
			$.post("../../../getMsg/",{'textType':textType,'text':text,'keyNum':keyNum},function(result){
				result = JSON.parse(result);
				keywords = result['keywords'];
				emotion = result['emotion'];
				emotion = [emotion['oppose'],emotion['support'],emotion['neutral']]
				$("#showKeyWordsTitle").text("文本关键词：");
				size = keywords.length;
				strKW = "";
				for (var i=0;i<size;i++)
					strKW += keywords[i]+" ";
				$("#keyWords").text(strKW);
				$("#container").css("display",'block');
				emotionExtract.showChart(emotion);
				
				emotionList = result['emotionList']
				$("#support").html("<strong>支持部分所用到的关键词：</strong>"+emotionList[0]);
				$("#oppose").html("<strong>反对部分所用到的关键词：</strong>"+emotionList[1]);
				$("#neutral").html("<strong>中间部分所用到的关键词：</strong>"+emotionList[2]);
			});
		});
	},
	
	showChart : function(emotion) {
		chart = new Highcharts.Chart({
			chart: {
				renderTo: 'container',
				plotBackgroundColor: null,
				plotBorderWidth: null,
				plotShadow: false
			},
			title: {
				text: '情感饼状图表'
			},
			tooltip: {
				formatter: function() {
					return '<b>'+ this.point.name +'</b>: '+ this.percentage.toFixed(2) +' %';
				}
			},
			plotOptions: {
				pie: {
					allowPointSelect: true,
					cursor: 'pointer',
					dataLabels: {
						enabled: true,
						color: '#000000',
						connectorColor: '#000000',
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.percentage.toFixed(2) +' %';
						}
					}
				}
			},
			series: [{
				type: 'pie',
				name: 'pie',
				data: [
					['负面',  parseInt(emotion[0])],
					['正面',  parseInt(emotion[1])],
					['中性',  parseInt(emotion[2])],
				]
			}]
		});
	}
}