import streamlit as st

st.set_page_config(page_title="famil.IA - Finanzas Familiares", layout="centered")

st.title("🤖 famil.IA")
st.write("Tu copiloto para organizar las finanzas del hogar")

st.markdown("**Haz una pregunta sobre tus finanzas familiares:**")

user_question = st.text_input("Ej: ¿Cuánto deberíamos ahorrar al mes si ganamos 3000 euros como familia?")

respuestas_simuladas = {
    "ahorrar": "Una buena regla es ahorrar al menos el 20% de los ingresos familiares mensuales.",
    "presupuesto": "Pueden comenzar dividiendo los gastos en esenciales (50%), ahorro (20%) y ocio (30%).",
    "deuda": "Prioriza pagar las deudas con mayor interés primero. Puedes usar el método bola de nieve o avalancha.",
    "hijos": "Considera abrir una cuenta de ahorro o inversión para la educación de tus hijos desde temprano.",
    "gastos": "Lleva un registro mensual de gastos familiares para detectar dónde reducir sin afectar la calidad de vida.",
}

def responder_pregunta(pregunta):
    for clave in respuestas_simuladas:
        if clave in pregunta.lower():
            return respuestas_simuladas[clave]
    return "¡Buena pregunta! En esta versión demo, aún no tengo una respuesta para eso, pero pronto lo haré 😊."

if user_question:
    respuesta = responder_pregunta(user_question)
    st.markdown(f"**Respuesta de famil.IA:** {respuesta}")