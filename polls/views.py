from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
	def detail(request, poll_id):
		p = get_object_or_404(Poll, pk=poll_id)
		return render_to_response('polls/detail.html', {'poll': p},context_instance=RequestContext(request))

		def results(request, poll_id):
			return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))