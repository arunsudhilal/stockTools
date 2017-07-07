$(document).ready(function(){
	$("button").click(function(){
		//$.getJSON("https://www.nseindia.com/products/dynaContent/equities/equities/json/online52NewHigh.json", function(result){
		debugger
		dataJson = JSON.parse(dataJson)
		symbol = dataJson.searchresult[0].ticker
		totalStocks = dataJson.searchresult.length
		totalStocks = totalStocks -1
		/*
		$.getJSON(dataJson, function(result){
			$.each(result, function(i, field){
			totalStocks = field.length
			totalStocks = totalStocks - 1
			debugger
			while(totalStocks > 0) {
				debugger
				$("div").append(field[totalStocks].ticker + " ");
				totalStocks = totalStocks - 1;
			}
			
			});
		});*/
		while(totalStocks >= 0) {
			$("div").append(dataJson.searchresult[totalStocks].ticker + " ");
			totalStocks = totalStocks - 1
		}
		debugger
	});
	
});

function openPage(stock){
	var text = "http://chartink.com/stocks/" + stock + ".html";
	text = text.replace (/"/g,"");
	text = text.replace (/ /g,"");
	console.log(text);
	window.open(text);
}