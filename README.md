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
  \[
  y[n] = \alpha \cdot x[n] + (1 - \alpha) \cdot y[n-1]
  \]
  where:
  \[
  \alpha = \frac{1}{RC \cdot f_s + 1}
  \]
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

Let me know if you'd like a Korean version of this README or a shorter summary version for documentation!
