// Empty JS for your own code to be here


var sentiment_news = 0
var sentiment_tweet = 0


function setValue(){
	console.log("setValue called");
	// ajax the JSON to the server

	verdict.innerHTML = "-"

	sentiment_news = 0;

	sentiment_tweet = 0;

	var input = document.getElementById('exampleInputEmail1').value;

	$.post("http:\/\/167.99.83.32:443/receiver1", input, function(data){ console.log(data);
	tweet_body.innerHTML = data;
});

	//tweet_body.innerHTML = data;

	$.post("http:\/\/167.99.83.32:443/receiver2", input, function(data){ console.log(data);

	tweet_sentiment.innerHTML = data;
//
//	if(data != "No records found")
//{
//	sentiment_tweet = parseFloat(data
//	fun(parseFloat(data), sentiment_news);
//	//verdict.innerHTML = "AAAAAAA"
//}

});

        //tweet_sentiment.innerHTML = data

	$.post("http:\/\/167.99.83.32:443/receiver3", input, function(data){ console.log(data);
	news_body.innerHTML = data;
});

        //news_body.innerHTML = data;

	$.post("http:\/\/167.99.83.32:443/receiver4", input, function(data){ console.log(data);
	news_sentiment.innerHTML = data

//	 if(data != "No records found")
//{
//	sentiment_news = parseFloat(data)
 //      fun(sentiment_tweet, parseFloat(data));
//	//verdict.innerHTML = "K" + sentiment_news
//}

});

//verdict.innerHTML = "K" + sentiment_news

	//verdict.innerHTML = sentiment_tweet.toString();

//	if(sentiment_news != 0  && sentiment_tweet != 0)
//{

	//verdict.innerHTML = "oi";

//	if (sentiment_news >0 && sentiment_tweet > 0)
//	{
//	verdict.innerHTML = "Both news atricle and tweet reflect positive sentiment for the term - " + input;
//	document.getElementById("verdict").style.color = "00ff00";
//	}

//	else if (sentiment_news >0 && sentiment_tweet < 0)
 //       {
   //     verdict.innerHTML = "The news article reflects positive sentiment and the tweet negative sentiment for the term - " + input;
     //   }

//	else if (sentiment_news <0 && sentiment_tweet > 0)
  //      {
    //    verdict.innerHTML = "The news article reflects negative sentiment and the tweet positive sentiment for the term - " + input;
      //  }

//	else if (sentiment_news <0 && sentiment_tweet < 0)
  //      {
    //    verdict.innerHTML = "Both the news article and reflect negative sentiment for the term - " + input;
//	document.getElementById("verdict").style.color = "ff0000";
  //      }



//}
        //news_sentiment.innerHTML = data;

	// stop link reloading the page
 event.preventDefault();
}


/*
function fun(sentiment_tweet, sentiment_news)
{

verdict.innerHTML = "K" + sentiment_news

if(sentiment_news != 0  && sentiment_tweet != 0)
{

       // verdict.innerHTML = "oi";

        if (sentiment_news >0 && sentiment_tweet > 0)
        {
        verdict.innerHTML = "Both news atricle and tweet reflect positive sentiment for the term - " + input;
        document.getElementById("verdict").style.color = "00ff00";
        }

        else if (sentiment_news >0 && sentiment_tweet < 0)
        {
        verdict.innerHTML = "The news article reflects positive sentiment and the tweet negative sentiment for the term - " + input;
        }

        else if (sentiment_news <0 && sentiment_tweet > 0)
        {
        verdict.innerHTML = "The news article reflects negative sentiment and the tweet positive sentiment for the term - " + input;
        }

        else if (sentiment_news <0 && sentiment_tweet < 0)
        {
        verdict.innerHTML = "Both the news article and reflect negative sentiment for the term - " + input;
        document.getElementById("verdict").style.color = "ff0000";
        }



}
*/

