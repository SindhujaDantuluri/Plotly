
import logging

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.generic import TemplateView

from . import plots

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "index.html"


class Plot1DView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot1DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d()
        return context



class Plot1DMultipleView(TemplateView):
    template_name = "plot_multiple.html"

    def get_context_data(self, **kwargs):
        n = int(kwargs['n'])
        # Call the base implementation first to get a context
        context = super(Plot1DMultipleView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d_multiple(n)
        return context


def plot1d_multiple_ajax(request, n):
    """
    Only handles AJAX queries
    """
    logger.debug("Plotting {} plots.".format(n))
    return HttpResponse(plots.plot1d_multiple(int(n)))