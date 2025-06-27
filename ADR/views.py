import cohere
from django.shortcuts import render
import re

co = cohere.Client("ySVNIUqQYTIbW300u8YJ7lcdEOfJ6hSVJfA9Z4Kl")

def extract_info(text):
    # Basic regex to extract info. You can improve this using NLP.
    risk = re.search(r"(?i)risk.*?: (.+?)(\.|\n)", text)
    precautions = re.search(r"(?i)precaution.*?: (.+?)(\.|\n)", text)
    alt = re.search(r"(?i)(alternative|suggestion).*?: (.+?)(\.|\n)", text)

    return {
        "risk_level": risk.group(1) if risk else "Not clearly stated",
        "precautions": precautions.group(1) if precautions else "Not mentioned",
        "alternative": alt.group(2) if alt else "No alternative suggested"
    }

def adr_checker(request):
    result = {}
    if request.method == "POST":
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        drug = request.POST.get("drug")
        gene = request.POST.get("gene")
        disease = request.POST.get("disease")

        prompt = f"""
        Patient Info:
        Age: {age}
        Gender: {gender}
        Drug: {drug}
        Genomics: {gene}
        Past Disease: {disease}

        1. What is the ADR risk?
        2. What precautions should be taken?
        3. Suggest an alternative prescription or dosage change if needed.
        Provide answers clearly labelled as:
        - Risk:
        - Precautions:
        - Alternative:
        """

        try:
            response = co.generate(
                model='command-r-plus',
                prompt=prompt,
                max_tokens=300,
                temperature=0.5
            )
            raw_output = response.generations[0].text.strip()
            result = extract_info(raw_output)
        except Exception as e:
            result = {
                "risk_level": "Error",
                "precautions": str(e),
                "alternative": "—"
            }

    return render(request, "ADR/form.html", {"result": result})


def home(request):
    return render(request, 'ADR/form.html')