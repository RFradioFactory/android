from datetime import datetime
from django.shortcuts import render
from .models import *


class PageRenderer:
    def __init__(self, request):
        self.request = request
        self.context = {'navigation': Navigation.objects.all()}

    def render_page(self, template_name):
        return render(self.request, template_name, self.context)

    def render_home_page(self):
        self.context['context'] = MainPage.objects.all()
        return self.render_page('home.html')

    def render_demand_page(self):
        self.context['context'] = Relevance.objects.all()
        return self.render_page('dem.html')

    def render_geography_page(self):
        self.context['context'] = Location.objects.all()
        return self.render_page('geo.html')

    def render_skills_page(self):
        self.context['context'] = Abilities.objects.all()
        return self.render_page('skill.html')

    def render_last_vacancy_page(self):
        last_vacancies_data = HeadHunterLV.objects.all()

        if last_vacancies_data:
            vacancy_to_parse = last_vacancies_data[0].vacancy_to_analyze
            hh_api = HeadHunterVacancies(vacancy_to_parse)
            vacancies = hh_api.get_data_vacancies('2023-12-20', 10)
        else:
            vacancies = []

        self.context.update({'vacs': vacancies, 'last_vacancies': last_vacancies_data})
        return self.render_page('lv.html')


def home_page(request):
    page_renderer = PageRenderer(request)
    return page_renderer.render_home_page()


def demand_page(request):
    page_renderer = PageRenderer(request)
    return page_renderer.render_demand_page()


def geography_page(request):
    page_renderer = PageRenderer(request)
    return page_renderer.render_geography_page()


def skills_page(request):
    page_renderer = PageRenderer(request)
    return page_renderer.render_skills_page()


def last_vacancy_page(request):
    page_renderer = PageRenderer(request)
    return page_renderer.render_last_vacancy_page()
