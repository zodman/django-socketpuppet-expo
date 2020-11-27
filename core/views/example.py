from django.views.generic.base import TemplateView
from .mixins import MixinBase

class ExampleView(MixinBase, TemplateView):

    template_name = 'example.html'
    files = (
        ('core/views/example.py', 'python3'),
        ('core/reflexes/example_reflex.py', 'python3'),
        ('core/javascript/controllers/example_controller.js', 'typescript'),
        ('core/templates/example.html', 'htmldjango'),
    )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.request.session.get("count", 0)
        return context

example = ExampleView.as_view()


