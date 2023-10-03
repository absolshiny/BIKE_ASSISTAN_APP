from django.shortcuts import render


api_key="asdasfasfasda"

def chatbot(request):
    user_input= request.POST.get("user_input")
    print(user_input)
    return render(request, "main.html", {})