from django.shortcuts import render


api_key="asdasfasfasda"

def chatbot(request):
    user_input= request.POST.get("user_input")
    response = "water"
    if user_input != "":
        response= "waltermercado"
    
    return render(request, "main.html", {"response": f"{response}"})