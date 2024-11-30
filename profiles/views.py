from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact,MyResume
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404


def index(request):
    
    expertise=[
        ["Software Developer",'paint-bucket',"Building applications (e.g.,Python Developer,Java Developer)"],
        ["Web Development","paint-bucket","Developing websites (e.g., Full-Stack developer using Django(REST Framework))"],
        ["AI/ML","paint-bucket","Creating intelligent Systems"],
        ["DataBase Administration","paint-bucket","Managing Databases (e.g., MySQL,MariaDB,SQLite,MongoDB)"],
    ]
    
    resume_expertise=[
        ['Jan 2024','Mar 2024',"Swayam Cloud Computing","It covers cloud models, security, and platforms like AWS and Azure, teaching how to develop and manage cloud-based applications. Ideal for students and professionals."],
        ['Jan 2024','Mar 2024',"Introduction to the Cyber Security","It involves protecting systems, networks, and data from cyber threats like hacking, malware, and phishing. It focuses on securing information through measures like firewalls, encryption, and incident response."],
    ]
    
    resume_education=[
        [2019,2020,"High School (10th)","Jawahar Navodaya Vidyalaya Rudhauli,Basti (U.P)"],
        [2021,2022,"Intermediate (12th PCM + CS)","Jawahar Navodaya Vidyalaya Rudhauli,Basti (U.P)"],
        [2022,2023,"B.Sc IT (1st Year)","A.E. Kalsekar college of Commerse and Management,Nalasopara West,Thane (M.H)"],
        [2023,2025,"B.Sc IT (2nd & 3rd Year)","Thakur College of Science and Commerse, Kandivali East,Mumbai (M.H)"],
    ]
    
    resume_skills=[
        ["width :90%","Python"],
        ["width :80%","Java"],
        ["width :70%","Django (REST Framework)"],
        ["width :90%","DBMS"],
        ["width :80%","C/C++"],
        ["width :90%","HTML,CSS & JavaScript"],
        ["width :90%","dotNET (C#)"],
    ]
    
    resume_languages=[
        [95,"Hindi"],
        [90,"English"],
        [50,"Telugu"],
    ]
    
    services=[
        ["write","Website Development & Design","Build and design responsive websites using HTML, CSS, JavaScript, and WordPress, focusing on both aesthetics and functionality."],
        ["vector","Data Analysis and Visualization","Analyze data using tools like Python (Pandas), Excel, or Tableau, and create visual reports to provide insights and inform decisions."],
        ["vector","Database Management","Design, manage, and optimize relational databases (SQL, MySQL) or NoSQL databases, ensuring data integrity and performance."],
        ["map-alt","Mobile App Development","Develop cross-platform mobile apps using frameworks like Kivy/KivyMD GUI, or build native Android/iOS apps with Python/Java/Kotlin or Swift."],
        ["package","Software Development","Develop custom software solutions, desktop applications, and scripts using languages like Java, Python, and C++."],
    ]
    
    images=[
        ["web","web-1.jpg","",""],
        ["branding new","branding-2.jpg","",""],
        ["advertising","advertising-1.jpg","",""],
        ["web new","web-2.jpg","",""],
        ["branding","branding-1.jpg","",""],
        ["advertising new","advertising-2.jpg","",""],
    ]
    
    news=[
        ["blog1.jpg","yogi","#","My Title","23","12","discription"]
    ]
    
    dct={
        'expertise':expertise,
        'resume_expertise':resume_expertise,
        'resume_education':resume_education,
        'resume_skills':resume_skills,
        'resume_skills':resume_skills,
        'resume_languages':resume_languages,
        'services':services,
        'images':images,
        'news':news,
        'facebook_url':'https://www.facebook.com/profile.php?id=100026209184227',
        'whatsapp_url':'https://wa.link/xjip9w',
        'instagram_url':'https://www.instagram.com/_yogendra__prasad_/',
        'github_url':'https://github.com/pryogendra',
        'linkedIn_url':'https://www.linkedin.com/in/yogendra-prasad-927a96238/',
        'twitter_url':'#',
        'google_url':'#',
        }
    
    return render(request,'index.html',dct)

def ContactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            contact=Contact(name=name,email=email,message=message)
            contact.save()

    return render(request,'index.html')

def download_pdf(request,doc_id):
    document = get_object_or_404(MyResume, id=doc_id)
    file_path = document.file.path
    
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.title}.pdf"'
    return response

