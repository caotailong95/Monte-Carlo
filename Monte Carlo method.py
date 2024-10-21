import numpy as np
import matplotlib.pyplot as plt

# 定义蒙特卡洛模拟次数
n_simulations = 10000

# 不确定度范围
part_uncertainty = np.random.uniform(-0.04, 0.04, n_simulations)
assembly_part_uncertainty = np.random.uniform(-0.04, 0.04, n_simulations)
positioning_uncertainty = np.random.uniform(-0.06, 0.06, n_simulations)
force_uncertainty = np.random.uniform(-10, 10, n_simulations)

# 常数值
A = 1.0  # 假设的接触面积
E2 = 200  # 假设的弹性模量
lambda_factor = 0.8  # 假设的回弹系数

# 初始压紧力
initial_pressure = 100  # 初始压紧力 N

# 计算压缩量的不确定度
compression_uncertainty = (initial_pressure + force_uncertainty) * lambda_factor / (A * E2)

# 计算总装配偏差
total_assembly_deviation = part_uncertainty + assembly_part_uncertainty + positioning_uncertainty + compression_uncertainty

# 分析结果
mean_deviation = np.mean(total_assembly_deviation)
std_deviation = np.std(total_assembly_deviation)

# 输出结果
print(f"平均装配偏差: {mean_deviation:.3f} mm")
print(f"标准差: {std_deviation:.3f} mm")

# 可视化部分
# 1. 装配偏差的直方图
plt.figure(figsize=(10, 6))
plt.hist(total_assembly_deviation, bins=50, color='skyblue', edgecolor='black', density=True)
plt.title('Distribution of Total Assembly Deviation', fontsize=16)
plt.xlabel('Assembly Deviation (mm)', fontsize=14)
plt.ylabel('Probability Density', fontsize=14)
plt.grid(True)

# 2. 压缩量与装配偏差的关系散点图
plt.figure(figsize=(10, 6))
plt.scatter(compression_uncertainty, total_assembly_deviation, alpha=0.5, color='blue')
plt.title('Compression Uncertainty vs Total Assembly Deviation', fontsize=16)
plt.xlabel('Compression Uncertainty (mm)', fontsize=14)
plt.ylabel('Total Assembly Deviation (mm)', fontsize=14)
plt.grid(True)

# 3. 显示生成的图
plt.show()
