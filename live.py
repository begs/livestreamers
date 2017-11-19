curl	-s 'Accept: application/vnd.twitchtv.v5+json' \
   		-H 'Client-ID: dsv0rf69bvzgi9ch6ys16vwncjax1z' \
		-H 'Authorization: OAuth ***' \
		-X GET 'https://api.twitch.tv/kraken/streams/followed' \
		| python -m script