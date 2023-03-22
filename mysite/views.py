from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'mysite/home.html')


def contact(request):
    if request.method == 'POST':
        # Extract the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        send_mail(
            f'{name}({email}) contacted you!',
            message,
            email,
            ['freddymani.fm@gmail.com'], # Replace with your email address
            fail_silently=False,
        )

        # Redirect to home
        # return render(request, 'mysite/home.html')
        messages.success(request, "Your message has been sent successfully.")
        return redirect('home')
    
    else:
        form = ContactForm()

        return render(request, 'mysite/contact.html', {'form': form})

   

   






