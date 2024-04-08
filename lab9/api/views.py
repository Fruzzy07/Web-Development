from django.forms import model_to_dict
from django.http import JsonResponse
from .models import Company, Vacancy

# Companies API views
def company_list(request):
    companies = Company.objects.all()
    data = {"companies": list(companies.values())}
    return JsonResponse(data)

def company_detail(request, id):
    company = Company.objects.get(pk=id)
    data = {"company": model_to_dict(company)}
    return JsonResponse(data)

def company_vacancies(request, id):
    company = Company.objects.get(pk=id)
    vacancies = company.vacancies.all()  # Access related vacancies using the related name
    data = {"vacancies": list(vacancies.values())}
    return JsonResponse(data)

# Vacancies API views
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = {"vacancies": list(vacancies.values())}
    return JsonResponse(data)

def vacancy_detail(request, id):
    vacancy = Vacancy.objects.get(pk=id)
    data = {"vacancy": model_to_dict(vacancy)}
    return JsonResponse(data)

def top_ten_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {"top_ten_vacancies": list(top_vacancies.values())}
    return JsonResponse(data)

