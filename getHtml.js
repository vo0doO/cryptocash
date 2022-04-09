
var tr = require( 'tor-request' )

URI = 'http://million5utxgrxru4rqmjwn7jji6bf44jkdqn3xyav6md5ebwy5l2ryd.onion/buy.php'

tr.torRequest(URI, function ( err, res, body ) {
  console.log( res.body )
}
)