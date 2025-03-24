# 숙명여대 메카트로닉스입문 및 실습 2025년도 (심주용)

`2025메카실습1_Low_Pass_Filter_IIR.ipynb`:


---

# 📘 2025 Mechatronics Lab 1: RC Low-Pass Filter using IIR Approximation

This tutorial explores the implementation of an **RC low-pass filter** using a **discrete-time IIR filter approach** to simulate how analog filters behave in digital systems. The input signal is a **PWM (Pulse Width Modulated) waveform**, and the output demonstrates how the low-pass filter smooths the high-frequency components to produce a near-analog voltage signal.

---

## 🧪 Objectives

- Understand how to simulate a **first-order RC low-pass filter** digitally
- Apply the **IIR (Infinite Impulse Response)** filtering technique using recursive difference equations
- Observe the filter's response to PWM signals with varying parameters (frequency, duty cycle, resistance, capacitance)
- Learn how **filtering can convert PWM to analog-like waveforms**

---

## 🔧 Key Components

### 1. **PWM Signal Generation**
- A square wave with a fixed frequency (e.g., 1 kHz)
- Adjustable **duty cycle** to simulate various analog voltage levels
- Simulation conducted using a high sampling rate (e.g., 10 kHz)

### 2. **RC Low-Pass Filter Implementation**
- Filter modeled as:
 ![equation](https://latex.codecogs.com/png.image?\dpi{150}y[n]=\alpha\cdot{}x[n]+(1-\alpha)\cdot{}y[n-1])
  where:
![equation](https://latex.codecogs.com/png.image?\dpi{150}\alpha=1/(RCf_s+1))
- This is an IIR filter that mimics analog exponential decay behavior

### 3. **Parameter Variations**
- Multiple examples are provided with:
  - Different **R (resistance)** and **C (capacitance)** values
  - Different **PWM duty cycles** and simulation durations
  - A two-stage filtering setup for better smoothing
  - A **dynamic duty cycle** (changing from 30% to 80% at a specific time)

---

## 📈 Results & Visualization

Each scenario produces two key plots:
- **PWM Input**: The raw square wave
- **Filtered Output**: The smoothed waveform that approximates analog voltage behavior

These demonstrate:
- How increasing **resistance or capacitance** increases the filter’s smoothing (slower response)
- How the **filtered signal** settles to a voltage level corresponding to the **PWM duty**
- The effect of applying **multiple filtering stages**

---

## 📂 Files & Structure

This notebook is structured as a progressive tutorial:
- Each code block builds on the previous one
- Parameters are gradually modified to explore various filtering behaviors
- Clear and labeled plots accompany each case

---

## 💡 Learning Outcomes

After going through this tutorial, students should be able to:
- Explain how an RC filter smooths PWM signals
- Implement a simple IIR filter using recursive equations
- Tune filter parameters to control responsiveness
- Analyze how digital filters approximate analog behavior

---

## 📎 Reference

Original Colab Notebook: [Open in Google Colab](https://colab.research.google.com/drive/1oaunc-yEYhClBSP3KKbjXCcU8qXStEMe)


---

# 📘 2025 메카트로닉스 실습 1: IIR 방식으로 구현한 RC 저역통과필터 (Low-Pass Filter)

이 실습 튜토리얼은 **PWM(Pulse Width Modulation)** 신호에 대해 **디지털 방식으로 RC 저역통과필터**를 구현하고, 그 동작을 관찰하는 것을 목표로 합니다. 필터는 **IIR (무한 임펄스 응답)** 방식으로 구성되며, 아날로그 필터의 거동을 근사합니다.

---

## 🎯 실습 목표

- **RC 저역통과필터**의 동작 원리를 이해하고, 이를 디지털 방식으로 구현  
- **IIR 필터**의 차분 방정식을 이용해 필터링 수행  
- **PWM 신호**의 듀티비 및 필터 파라미터(R, C)에 따른 출력 변화 관찰  
- **디지털 필터**가 어떻게 PWM을 아날로그에 가까운 신호로 변환하는지 이해  

---

## 🔧 주요 내용

### ✅ PWM 신호 생성
- 주파수: 1kHz  
- 듀티비(Duty Cycle): 30%, 50%, 80% 등 다양한 예시  
- 샘플링 주파수: 10kHz  
- `np.where()`와 모듈로 연산을 이용하여 PWM 생성  

### ✅ RC 저역통과필터 구현 (IIR 방식)
- 차분 방정식:
 ![equation](https://latex.codecogs.com/png.image?\dpi{150}y[n]=\alpha\cdot{}x[n]+(1-\alpha)\cdot{}y[n-1])

- 필터 계수 ![equation](https://latex.codecogs.com/png.image?\dpi{150}\alpha=1/(RCf_s+1))
- 여기서:
  - \( R \): 저항 (예: 2kΩ, 10kΩ)
  - \( C \): 커패시터 (예: 0.5µF, 1µF)
  - \( f_s \): 샘플링 주파수 (10kHz)

### ✅ 다양한 실험 조건
- **필터 계수 변경**: R 또는 C 값 변경에 따른 응답 속도 변화
- **PWM 듀티비 변화**: 출력 전압의 steady-state 값이 듀티비에 비례함을 확인
- **2단 필터 구조**: 필터를 2번 적용하여 더 부드러운 출력을 구현
- **시간에 따라 듀티비 변경**: \( t = 0.015s \) 시점에 듀티비 30% → 80%로 변경하여 필터 응답 확인

---

## 📊 출력 결과 (시각화)

- **입력 (PWM)**: 고속 디지털 신호
- **출력 (Filtered)**: 아날로그에 가까운 곡선
- 플롯을 통해 필터링 전후의 차이를 시각적으로 확인 가능

---

## 📚 실습을 통해 얻는 학습 효과

- **IIR 필터**의 원리 및 구현 능력 습득  
- **PWM 신호 처리**에 대한 실무적 이해  
- **필터 파라미터(R, C)**와 시스템 응답 속도의 관계 이해  
- **디지털 필터**로 아날로그 시스템을 시뮬레이션하는 기초 능력 함양

---

## 🔗 원본 노트북

Google Colab에서 열기:  
[https://colab.research.google.com/drive/1oaunc-yEYhClBSP3KKbjXCcU8qXStEMe](https://colab.research.google.com/drive/1oaunc-yEYhClBSP3KKbjXCcU8qXStEMe)

---


라즈베리파이 실습 참고: https://github.com/gilbutITbook/007013
---

