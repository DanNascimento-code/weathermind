
def behavioral_insight(features):
    if features["avg_temperature"] > 28:
        return "Clima médio elevado nos últimos dias. Pode impactar energia e concentração."

    if features["temperature_trend"] < -5:
        return "Queda acentuada de temperatura recente. Mudanças de rotina podem ser necessárias."

    return "Clima estável recentemente."
