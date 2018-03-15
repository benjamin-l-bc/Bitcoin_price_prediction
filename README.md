# Bitcoin_price_prediction

<br> Predict bitcoin price using machine learning tools based on the data from bitcoin_trade_data project
<br> After finished this project, will start another project to autotrade the future in OKex based on machine learning result.

##Updateds
###### Updates 3/9/2018
<br> Adding Analytic scripts(to be competed)

###### Updates 3/10/2018
<br> finished data pre-processing

### Features:
<br>bfx_bids_wall: bids wall from bitfinex (select the largest bids amount from order book)
<br>bfx_asks_wall: asks wall from bitfinex (select the largest asks amount from order book)
<br>bfx_total_bids: total bids from order book(bitfinex)
<br>bfx_total_asks: total asks from order book(bitfinex)
<br>bfx_buy_volumn: total buy volumn from bitfinex during this period
<br>bfx_sell_volumn: total sell volumn from bitfinex during this period
<br>USDT_exceed: Huobi OTC price - USD/CNY enchange rate (This index is to see if the Chinese prople are willing to buy bitcoin with a premium price.
<br>pre_price15: bitcoin future quarterly price from okex 45 minutes ago.
<br>pre_price10: bitcoin future quarterly price from okex 30 minutes ago.
<br>pre_price5: bitcoin future quarterly price from okex 15 minutes ago.
<br>pre_bfx: bitcoin price from bitfinex 3 minutes ago.
<br>pre_news10:  Get news from wallstreet.cn and analyze the emotion(from 0-1). Pre_news10 is the emotion 30 minutes ago 

### Label:
<br>next_price15: bitcoin future quarterly price from okex 45 minutes later.
<br>next_price10: bitcoin future quarterly price from okex 30 minutes later
<br>next_price5: bitcoin future quarterly price from okex 15 minutes later

###### Updates 3/12/2018
<br> Data Modeling: Use sklearn - Test SVM, Random Forest and neural network with different parameters. Try to find out the best strategy.(To be updated)

###### Updates 3/15/2018
<br> 1 Bug fixed
