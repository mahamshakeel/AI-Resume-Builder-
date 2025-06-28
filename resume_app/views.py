from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        context = {
            'skills': request.POST.getlist('skills[]'),
            'languages': request.POST.getlist('languages[]'),
            'achievements': request.POST.getlist('achievements[]'),
            'certifications': request.POST.getlist('certification[]'),
            'education': zip(
                request.POST.getlist('degree[]'),
                request.POST.getlist('college[]'),
                request.POST.getlist('year[]')
            ),
            'experience': zip(
                request.POST.getlist('company[]'),
                request.POST.getlist('post[]'),
                request.POST.getlist('duration[]'),
                request.POST.getlist('expdesc[]')
            ),
            'projects': zip(
                request.POST.getlist('project[]'),
                request.POST.getlist('proj_dur[]'),
                request.POST.getlist('proj_desc[]')
            ),

            # Personal Info
            'name': request.POST.get('name'),
            'about': request.POST.get('about'),
            'age': request.POST.get('age'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
        }

        resume_score = calculate_resume_score(context)
        context['resume_score'] = resume_score

        template_choice = request.POST.get('template')
        if template_choice == 'modern':
            return render(request, 'resume_app/resume_modern.html', {**context, 'hide_navbar': True})
        elif template_choice == 'creative':
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
    score += min(len(matched), 10)

    # 3. ATS Friendly
    if '-' in all_text or '*' in all_text or '•' in all_text:
        score += 10

    return score
