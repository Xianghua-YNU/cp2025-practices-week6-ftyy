import numpy as np
import matplotlib.pyplot as plt

def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    任务1: 拍频现象的数值模拟
    参数说明:
        f1, f2: 两个波的频率(Hz)
        A1, A2: 两个波的振幅
        t_start, t_end: 时间范围(s)
        num_points: 采样点数
    """
    # 生成时间范围
    t = np.linspace(t_start, t_end, num_points)
    
    # 生成两个正弦波
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)
    
    # 叠加两个波
    superposed_wave = wave1 + wave2

    # 计算拍频
    beat_frequency = np.abs(f1 - f2)

    # 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 8))
        
        # 绘制第一个波
        plt.subplot(3, 1, 1)
        plt.plot(t, wave1, label=f'Wave 1: {f1} Hz', color='blue')
        plt.title('Wave 1')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        
        # 绘制第二个波
        plt.subplot(3, 1, 2)
        plt.plot(t, wave2, label=f'Wave 2: {f2} Hz', color='orange')
        plt.title('Wave 2')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        
        # 绘制叠加波
        plt.subplot(3, 1, 3)
        plt.plot(t, superposed_wave, label='Superposed Wave', color='green')
        plt.title('Superposed Wave')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        
        plt.tight_layout()
        plt.show()

    return t, superposed_wave, beat_frequency

def parameter_sensitivity_analysis():
    """
    任务2: 参数敏感性分析
    需要完成:
    1. 分析不同频率差对拍频的影响
    2. 分析不同振幅比例对拍频的影响
    """
    base_freq = 440
    freq_diffs = [1, 4, 6, 8]
    
    plt.figure(1,figsize=(12, 8))
    for i, diff in enumerate(freq_diffs):
        t, wave, _ = simulate_beat_frequency(f1=base_freq, f2=base_freq+diff,show_plot=False)
        plt.subplot(2, 2, i+1)
        plt.plot(t, wave)
        plt.title(f'Frequency diff = {diff} Hz')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


    # 不同振幅比例的影响
    amplitude_ratios = [0.5, 2.0, 3.0, 4.0]
    plt.figure(2,figsize=(12, 8))
    for i, ratio in enumerate(amplitude_ratios):
        t, wave, _ = simulate_beat_frequency(A2=ratio,show_plot=False)
        plt.subplot(2, 2, i+1)
        plt.plot(t, wave)
        plt.title(f'Amplitude ratio = {ratio}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    # 示例调用
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency()
    print(f"计算得到的拍频为: {beat_freq} Hz")
    
    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
