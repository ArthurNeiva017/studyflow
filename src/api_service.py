import random

import requests

STUDY_TIPS = [
    "Estude em blocos curtos e faça pausas para manter o foco.",
    "Revise o conteúdo no mesmo dia para melhorar a retenção.",
    "Defina uma meta simples para cada sessão de estudo.",
    "Evite distrações e mantenha o ambiente organizado.",
    "Faça pequenos resumos com suas próprias palavras.",
    "Pratique exercícios para fixar o conteúdo estudado.",
    "Comece pelas tarefas mais importantes do dia.",
    "Mantenha uma rotina de estudos consistente durante a semana."
]


def get_study_advice():
    local_tip = random.choice(STUDY_TIPS)

    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=5)
        response.raise_for_status()
        data = response.json()

        api_advice = data["slip"]["advice"]

        return {
            "study_tip": local_tip,
            "external_advice": api_advice,
           
        }
    except (requests.RequestException, KeyError, ValueError):
        return {
            "study_tip": local_tip,
            "external_advice": (
                "Mantenha constância nos estudos e avance "
                "um passo por vez."
),
            "source": "Fallback local"
        }