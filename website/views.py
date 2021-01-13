from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def contact(request):

   	#if request.method == "POST":
		#message_name = request.POST['message-name']
		#message_email = request.POST['message-email']
		#message = request.POST['message']

		# send an email
		#send_mail(
			#message_name, # subject
			#message, # message
			#message_email, # from email
			#['usia@gov'], # To Email
			#)

		#return render(request, 'contact.html', {'message_name': message_name})

	#else:
		return render(request, 'contact.html', {})

  

  
  
    

   

