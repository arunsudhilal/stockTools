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
			var req = new XMLHttpRequest();

			req.open('GET', 'http://www.google.com', false);
			req.send(null);

			if(req.status == 200) {
				alert(req.responseText);
			}
			debugger
			$.get("http://json.bselivefeeds.indiatimes.com/ET_Community/Near52WeeksHigh?callback=jQuery111303796357068496068_1499585248089&pagesize=100&pid=7&exchange=50&pageno=1&sortby=percentgap&sortorder=asc", function(data){
				//alert("Data: " + data + "\nStatus: " + status);
				debugger
				alert("Arun")
			});
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