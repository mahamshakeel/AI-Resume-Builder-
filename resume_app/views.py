from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        context = {
            'name': request.POST.get('name'),
            'about': request.POST.get('about'),
            'age': request.POST.get('age'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),

            'skill1': request.POST.get('skill1'),
            'skill2': request.POST.get('skill2'),
            'skill3': request.POST.get('skill3'),
            'skill4': request.POST.get('skill4'),
            'skill5': request.POST.get('skill5'),

            'degree1': request.POST.get('degree1'),
            'college1': request.POST.get('college1'),
            'year1': request.POST.get('year1'),

            'degree2': request.POST.get('degree2'),
            'college2': request.POST.get('college2'),
            'year2': request.POST.get('year2'),

            'degree3': request.POST.get('degree3'),  # fixed typo from degre3 to degree3
            'college3': request.POST.get('college3'),
            'year3': request.POST.get('year3'),

            'lang1': request.POST.get('lang1'),
            'lang2': request.POST.get('lang2'),
            'lang3': request.POST.get('lang3'),

            'project1': request.POST.get('project1'),
            'durat1': request.POST.get('durat1'),
            'desc1': request.POST.get('desc1'),

            'project2': request.POST.get('project2'),
            'durat2': request.POST.get('durat2'),
            'desc2': request.POST.get('desc2'),

            'company1': request.POST.get('company1'),
            'post1': request.POST.get('post1'),
            'duration1': request.POST.get('duration1'),
            'lin11': request.POST.get('lin11'),

            'company2': request.POST.get('company2'),
            'post2': request.POST.get('post2'),
            'duration2': request.POST.get('duration2'),
            'lin21': request.POST.get('lin21'),

            'ach1': request.POST.get('ach1'),
            'ach2': request.POST.get('ach2'),
            'ach3': request.POST.get('ach3'),
        }
        resume_score = calculate_resume_score(context)
        context['resume_score'] = resume_score

        # Handle template choice
        template_choice = request.POST.get('template')  # get value from dropdown

        if template_choice == 'modern':
            #return render(request, 'resume_app/resume_modern.html', context)
            return render(request, 'resume_app/resume_modern.html', {**context, 'hide_navbar': True})

        elif template_choice == 'creative':
            #return render(request, 'resume_app/resume_creative.html', context)
            return render(request, 'resume_app/resume_creative.html', {**context, 'hide_navbar': True})

        else:
            return render(request, 'resume_app/resume_classic.html', context)

    return render(request, 'resume_app/home.html')

def about(request):
    return render(request, 'resume_app/about.html')


def calculate_resume_score(data):
    score = 0

    # 1. Resume Length
    all_text = " ".join(str(v) for v in data.values() if v)
    word_count = len(all_text.split())
    if 200 <= word_count <= 600:
        score += 10
    elif 150 <= word_count <= 750:
        score += 5

    # 2. Keyword Check
    target_keywords = ['python', 'django', 'ml', 'data', 'api', 'project', 'resume', 'analysis']
    matched = [kw for kw in target_keywords if kw.lower() in all_text.lower()]
    score += min(len(matched), 10)  # up to 10 points for keyword presence

    # 3. ATS Friendly
    if '-' in all_text or '*' in all_text or '•' in all_text:
        score += 10  # bullet points or ATS format hints

    return score
