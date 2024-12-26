from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):

    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        # Validation
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            )
        error_message = self.validateCustomer(first_name, last_name, phone, email, password, customer, confirm_password)

        # Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, first_name, last_name, phone, email, password, customer, confirm_password):
        error_message = None
        if (not (first_name)):
            error_message = "First Name Required !!"
        elif (not (phone)):
            error_message = "Phone Required !!"
        elif (len(phone) < 10 or len(phone) > 10):
            error_message = "Phone number must have 10 digits"
        elif (phone.isnumeric() == False):
            error_message = "Phone number must contain digits only"
        elif (not (email)):
            error_message = "email Required !!"
        elif (not (password)):
            error_message = "Password Required !!"
        elif (len(password) < 6):
            error_message = "Password must be atleast 6 characters long"
        elif (customer.isExists()):
            error_message = "Email address already registered"
        elif (confirm_password != password):
            error_message = "Confirm Password does not match"
        return error_message