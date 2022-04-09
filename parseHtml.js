const getRes = async ( uri ) => {
    try {
      const trReq = await tr.torRequest(uri, function ( err, res, body ) {
          return body
        }
      )
      return trReq
     
    }
    catch ( error ) {
    console.error( error )
    return await getRes()
  }
  }
  
  function getProductList ( html ) {
    
    var prl = html.getElementsByClassName( "product-row" )
    var productList = []
    Object.keys( prl ).forEach( ( item ) => {
      productList.push( prl[ item ] )
    } )
    return productList
  }
  
  function checkActualPrice ( products ) {
    for ( var i = 0; i < products.length; i = i + 1 ) {
      var price = products[ i ].cells[ 4 ].textContent
      var status = products[ i ].cells[ 5 ].textContent
      if ( price == "0.002 BTC" ) {
        console.log( `Есть нужный прайс ${ i }` )
        if ( status == "SOLD" ) {
          console.log( "Увы он продан" )
        }
      }
    }
  }
  // let timerId = setInterval(checkActualPrice(products= getProductList()), 20000);
  
  // timerId()
  
  async function main (u) {
    var res = await getRes( uri = u )
    const productsHtml = res.html
    await checkActualPrice( products = getProductList(productsHtml) )
  
  
  }