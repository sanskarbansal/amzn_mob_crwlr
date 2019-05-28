import scrapy

class Amazon_Mobile(scrapy.Spider):
	name = "amzn_mob"

	def start_requests(self):
		url = "https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles"
		yield scrapy.Request(url=url, callback=self.some)
	def some(self, res):
		mob_name = res.css("#merchandised-content div.crwTitle a::text").getall()
		price_span = res.css("#merchandised-content .crwActualPrice span").getall()
		rating = res.css("#merchandised-content .a-icon-alt::text").getall(); 
		#price = [i.split("</span>")[-2] for i in price_span]
		#mob_price = res.css('.a-price-whole::text')
		for i in range(len(mob_name)): 
			yield {
				"Mobile Name" : mob_name[i],
				"Price" :  price_span[i*3].split("</span>")[-2],
				"Rating": rating[i], 
			}
		