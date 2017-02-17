from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	locations = [
		'Dallas',
		'San Jose',
		'Mountain View',
		'Seattle',
		'Chicago',
		'Atlanta',
		'Boston',
		'Washington, D.C.',
	]

	languages = [
		'PHP',
		'Python',
		'JavaScript',
		'Ruby',
		'C#',
		'Swift',
	]

	context = {
		'locations': locations,
		'languages': languages,
	}

	return render(request, 'main/index.html', context)

def create_survey(request):
	if request.method == 'POST':
		request.session['name'] = request.POST.get('name')
		request.session['language'] = request.POST.get('language')
		request.session['location'] = request.POST.get('location')
		request.session['comment'] = request.POST.get('comment')
		return redirect('/success')
	else:
		return redirect('/')

def success(request):
	return render(request, 'main/success.html')



