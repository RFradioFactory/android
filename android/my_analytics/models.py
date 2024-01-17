from django.db import models


class Navigation(models.Model):
    role_name = models.TextField(blank=False, verbose_name='Роль', max_length=25)
    business_logo = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False, verbose_name='Логотип компании')
    first_item = models.TextField(blank=False, verbose_name='Первый элемент', max_length=25)
    second_item = models.TextField(blank=False, verbose_name='Второй элемент', max_length=25)
    third_item = models.TextField(blank=False, verbose_name='Третий элемент', max_length=25)
    fourth_item = models.TextField(blank=False, verbose_name='Четвертый элемент', max_length=25)
    fifth_item = models.TextField(blank=False, verbose_name='Пятый элемент', max_length=25)
    creator = models.TextField(blank=False, verbose_name='Создатель', max_length=50)

    class Meta:
        db_table = 'navigation'


class MainPage(models.Model):
    role_description = models.TextField(blank=True, verbose_name='Описание роли')
    role_photo = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False, verbose_name='Фотография роли')

    class Meta:
        db_table = 'main_page'


class Relevance(models.Model):
    salary_chart = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False,
                                     verbose_name='График уровня зарплаты по годам')
    vacancy_chart = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False,
                                      verbose_name='График количества вакансий по годам')
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')

    class Meta:
        db_table = 'relevance_data'


class Location(models.Model):
    city_salary_chart = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False,
                                          verbose_name='График уровня зарплаты по городам')
    city_vacancy_chart = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False,
                                           verbose_name='График доли вакансий по городам')
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')

    class Meta:
        db_table = 'geography'


class Abilities(models.Model):
    table_name = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')
    abilities_chart = models.ImageField(upload_to='images_secret/%Y/%m/%d', blank=False, verbose_name='График навыков')

    class Meta:
        db_table = 'skills'


class HeadHunterLV(models.Model):
    role_name = models.CharField(max_length=100, verbose_name='Роль')
    vacancy_to_analyze = models.TextField(blank=False, verbose_name='Вакансия для анализа', max_length=15)

    class Meta:
        db_table = 'head_hunter_api'
