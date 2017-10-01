var unirest=require('unirest');
var cheerio=require('cheerio');
var Q=require('q');

var URL='http://www.imdb.com/find?';


function movieDetails(movieKeyWord)
{
	var defer=Q.defer();
	unirest.get(URL+'q='+movieKeyWord)
			.send()
			.end(function(resp)
			{
				if(resp.status!==200){
					defer.reject('no match found');
					return;
				}
				var $=cheerio.load(resp.body);
				var text=$('.findResult').eq(0).html();
				if(!text){
					defer.reject('no match found');
					return;	
				}
				defer.resolve(extractData($));
			})
	return defer.promise;
}
function extractData($){
	var defer=Q.defer();
	var parent=$('.findResult').eq(0);
	var url=parent.find('a').attr('href').split('?')[0];
	var img=parent.find('img').attr('src');
	var id=url.replace(/\//g,' ').trim().split(' ')[1];
	var obj={
		id 	: id,
		url : 'http://www.imdb.com'+url,
		img : img
	};
	fetchRating(id).then(function(resp)
	{
		obj.rating=resp;
		defer.resolve(obj);
	}).catch(function(err)
	{
		defer.reject(err);
	})

	return defer.promise;
}

function fetchRating(id){
	var defer=Q.defer();

	var url='http://imdb.com/title/'+id;
	unirest.get(url)
		.send()
		.end(function(resp)
		{
			if(resp.status!==200)
				defer.reject('Error in fetching rating')
			else{
				$=cheerio.load(resp.body);
				var rating=$('[itemProp=ratingValue]').html();
				var max=$('[itemProp=bestRating]').html();
				var name=$('[itemProp=name]').html()
													.split('&')[0];
				var r={
					name : name,
					rating : rating,
					max : max
				}
				defer.resolve(r);
			}
		});
	return defer.promise;
}
function scrap()
{

}
module.exports={
	movieDetails : movieDetails,
	ratings 	 : fetchRating
};