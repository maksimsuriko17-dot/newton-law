import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Второй закон Ньютона",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Второй закон Ньютона")
st.subheader(
    "Движение материальной точки в инерциальной системе отсчёта"
)

st.write("""
Второй закон Ньютона устанавливает связь между силой,
массой тела и его ускорением.
""")

st.latex(r"\vec{F}_{рез} = m\vec{a}")

st.divider()

# Параметры модели
st.header("⚙️ Настройки эксперимента")

col1, col2, col3 = st.columns(3)

with col1:
    mass = st.slider(
        "Масса тела (кг)",
        1.0, 20.0, 5.0, 0.5
    )

with col2:
    force = st.slider(
        "Равнодействующая сила (Н)",
        -50.0, 50.0, 20.0, 1.0
    )

with col3:
    velocity0 = st.slider(
        "Начальная скорость (м/с)",
        -10.0, 10.0, 0.0, 0.5
    )

# Расчёты
acceleration = force / mass

st.divider()

st.header("📊 Результаты эксперимента")

c1, c2, c3 = st.columns(3)

c1.metric("Масса", f"{mass} кг")
c2.metric("Сила", f"{force} Н")
c3.metric("Ускорение", f"{acceleration:.2f} м/с²")

# Время моделирования
duration = st.slider(
    "Продолжительность движения (сек)",
    1, 20, 10
)

time = np.linspace(0, duration, 200)

# Формулы движения
position = velocity0 * time + 0.5 * acceleration * time**2
velocity = velocity0 + acceleration * time

# Анимация положения точки
st.header("🔴 Движение материальной точки")

frame = st.slider(
    "Время наблюдения (сек)",
    0.0,
    float(duration),
    0.0,
    0.1
)

x = velocity0 * frame + 0.5 * acceleration * frame**2

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=position,
    y=np.zeros(len(time)),
    mode="lines",
    name="Траектория"
))

fig.add_trace(go.Scatter(
    x=[x],
    y=[0],
    mode="markers",
    marker=dict(size=20, color="red"),
    name="Материальная точка"
))

fig.update_layout(
    title="Положение тела на оси X",
    xaxis_title="Координата (м)",
    yaxis=dict(visible=False),
    height=350
)

st.plotly_chart(fig, use_container_width=True)

# График скорости
st.header("📈 График скорости")

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=time,
    y=velocity,
    mode="lines",
    name="Скорость"
))

fig2.update_layout(
    xaxis_title="Время (с)",
    yaxis_title="Скорость (м/с)",
    height=350
)

st.plotly_chart(fig2, use_container_width=True)

# Текущие показатели
current_velocity = velocity0 + acceleration * frame

st.subheader("Результаты в выбранный момент")

st.write(f"Ускорение: **{acceleration:.2f} м/с²**")
st.write(f"Скорость: **{current_velocity:.2f} м/с**")
st.write(f"Координата: **{x:.2f} м**")

st.success(
    "Изменяйте силу и массу, чтобы исследовать второй закон Ньютона!"
)

st.caption(
    "Модель рассматривает движение материальной точки "
    "в инерциальной системе отсчёта при постоянной силе."
)
