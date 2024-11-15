import numpy as np

# Исходные данные
signal = np.array([1, 2, 3, 4, 5])
kernel = np.array([0.2, 0.5, 0.2])  # Пример ядра

# Функция для выполнения свертки
def convolve(signal, kernel):
    kernel_size = len(kernel)
    signal_size = len(signal)
    output_size = signal_size + kernel_size - 1
    output = np.zeros(output_size)

    for i in range(output_size):
        for j in range(kernel_size):
            if i - j >= 0 and i - j < signal_size:
                output[i] += signal[i - j] * kernel[j]

    return output

# Выполнение свертки
result = convolve(signal, kernel)
print("Результат свертки:", result)