from django.shortcuts import render


def project_list(request):
    return render(request, 'budget/project-list.html')


def project_detail(request, p_id):
    # fetching the correct project
    return render(request, 'budget/project-detail.html')