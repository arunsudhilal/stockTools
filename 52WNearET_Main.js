var processedStocks = 0;
var dataJson;
var totalStocks = 0;
$(document).ready(function(){
	$("button").click(function(){
		var buttonID = this.id
		
		//If openchart button is pressed
		if (buttonID == "1") {
			if (processedStocks == 0) {
				dataJson = JSON.parse(dataJson)
				symbol = dataJson.searchresult[0].ticker
				totalStocks = dataJson.searchresult.length
				totalStocks = totalStocks - 1
				debugger
			}
			debugger
			while(totalStocks >= 0) {
				$("div").append(dataJson.searchresult[totalStocks].ticker + " ");
				openPage(dataJson.searchresult[totalStocks].ticker)
				totalStocks = totalStocks - 1
				processedStocks = processedStocks + 1
				if(processedStocks % 5 == 0)
					break;
				debugger
			}
			debugger
		}
		//if Fetch button is pressed
		if (buttonID == "2") {
			dataJson = dataJson.split("jQuery111303796357068496068_1499585248089(", 2)[1];
			dataJson = dataJson.split(')', 1);
			debugger
			
		}
	});	
});

function openPage(stock){
	var text = "http://chartink.com/stocks/" + stock + ".html";
	text = text.replace (/"/g,"");
	text = text.replace (/ /g,"");
	console.log(text);
	window.open(text);
}