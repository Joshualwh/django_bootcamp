from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link

# Create your views here.
# What is the difference between class and functional based view?
# Class based view provides you some shortcuts to do some common patters but customizable.
class LinkListView(ListView):
  model = Link
  # Query for all the links Link.objects.all()
  # context={'link: links}
  # return render(request, 'link_list.html', context)

class LinkCreateView(CreateView):
  model = Link
  fields = "__all__"
  success_url = reverse_lazy('link-list')
  # create forms.py file and form
  # check if this was a post or get request
  # return an empty form or save the form data
  # template model_form -> link_form.html

class LinkUpdateView(UpdateView):
  model = Link
  fields = ['text', 'url']
  success_url = reverse_lazy('link-list')
  # create a form
  # check if a get request or a put request
  # a put request is similar to post but put updates while post creates.
  # either render the form or update and save in our db.
  # template model_form -> link_form.html

class LinkDeleteView(DeleteView):
  model = Link
  success_url = reverse_lazy('link-list')
  # take in a id/pk of an object
  # query to db for that object
  # check if it exists -> delete the object
  # return some template or forward to user to some url
  # form to submit to delete the item
  # expect a template name model_confirm_delete.html -> link_confirm_delete.html

def profile_view(request, profile_slug):
  profile = get_object_or_404(Profile, slug=profile_slug)
  links = profile.links.all()
  context = {
    'profile': profile,
    'links': links
  }
  return render(request, 'link_plant/profile.html', context)