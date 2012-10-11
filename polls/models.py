from django.db import models

class Poll(models.Model):
	name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.name
		def was_published_today(self):
			return self.pub_date >= 'Asia/calcutta'.now() - datetime.timedelta(days=1)
		was_published_today.admin_order_field ='pub_date'
		was_published_today.boolean =True
		was_published_today.short_description ='Published today?'
 



		

		
