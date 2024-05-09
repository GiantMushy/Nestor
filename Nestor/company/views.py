from django.shortcuts import render
from company.models import Company

# Create your views here.


# companies = [
#     { 'id': 3, 'name': 'Marel', 'number_of_employees': 750, 'address': 'Austurhraun 9', 'description': 'We make stuff for fish', 'link': 'http://marel.com',
#       'logo': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcompanieslogo.com%2Fimg%2Forig%2FMAREL.AS_BIG-13790959.png%3Ft%3D1604428470&f=1&nofb=1&ipt=c563754f591d10cbb1cefa26a2fc6ec61185972e69c8aca57d637fb055e64959&ipo=images',
#       'email': 'marel@marel.com', 'phone': '5638000', 'zipcode_id': 13},
# ]



def index(request):
    return render(request, 'company/index.html', context={'companies': Company.objects.all()})
