$(function(){
	textTest.run();
});

var textTest = {
	emotionWordsSet : [],
	run : function() {
		textTest.init();
	},
	
	init : function() {
		textTest.event();
		$("#showResult").css('display','none');
	},
	
	event : function() {
		$('#getRBtn').click(function(){
			var text = $('#textArea').val();
			var content = JSON.stringify({'text':text});
			$("#showMsg").html('稍等...');
			$.post(dns.dns+'textTest',{'content':content},function(result){
				text = text.split("\n");
				result = JSON.parse(result);
				var size = text.length;
				var html = '<div>' + result['info'] + '</div><table>';
				var showNum = 0;
				for (var i=0;i<size;i++) {
					if (result['score'][i]>0.4)
						showNum = 1;
					else if (result['score'][i]<-0.4)
						showNum = -1;
					else
						showNum = 0;
					html += '<tr><td>' + showNum + '</td><td>' +text[i] + '</td></tr>';
				}
				html += '</table>';
				$("#showResult").html(html);
				$("#showMsg").html(result['info']);
				$("#container").css("display",'block');
				textTest.showResultCharts(result['score'],result['emotionWords']);
			});
		});
		
		$('#showResultBtn').click(function() {
			$("#showMsg").html('');
			$('#showResult').slideToggle(1000);
		});
		
		$('#showMore').click(function() {
			var num = parseInt($('#numToEmotionWords').val());
			textTest.showEmotionWords(num);
		});
	},
	
	showResultCharts : function(emotionList,emotionWordsSet) {
		var size = emotionList.length;
		var supportNum = 0;
		var nutralNum = 0;
		var nagetiveNum = 0;
		for (var i=0;i<size;i++) {
			if (emotionList[i]>0.4) {
				supportNum += 1 ;
			}
			else if (emotionList[i]<-0.4) {
				nagetiveNum += 1;
			}
			else {
				nutralNum +=1;
			}
		}
		/*emotionWordsSet['0'] = emotionWordsSet['0'].sort();
		emotionWordsSet['1'] = emotionWordsSet['1'].sort();
		emotionWordsSet['-1'] = emotionWordsSet['-1'].sort();*/
		textTest.emotionWordsSet = [emotionWordsSet['-1'],emotionWordsSet['0'],emotionWordsSet['1']];
		var num = parseInt($('#numToEmotionWords').val());
		textTest.showEmotionWords(num);
		
		var html = '<div>积极评论数：' + supportNum + '</div>';
		html += '<div>中间评论数：' + nutralNum + '</div>';
		html += '<div>消极评论数：' + nagetiveNum + '</div>';
		html += '<div>总数：' + size +'</div>';
		html += $('#showResult').html();
		$('#showResult').html(html);
		textTest.showChart([nagetiveNum,supportNum,nutralNum]);
	},
	
	showEmotionWords : function(num) {
		var html = '';
		for (var j=0;j<3;j++) {
			each = textTest.emotionWordsSet[j+''];
			var size = each.length;
			if (j-1==-1)
				html += '消极词汇：';
			else if (j-1==1)
				html += '积极词汇：';
			if (j == 0 || j == 2) {
				var tmp = [];
				for (var i=0;i<size && i<num;i++) {
					tmp.push(each[i]);
				}
				tmp = tmp.join(',');
				html += tmp +'<br/>'
			}
		}
		$('.showEmotionWords').html(html);
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