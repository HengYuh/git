import re
import csv
import pandas as pd
import matplotlib.pyplot as plt

# 步骤 1: 读取文件
file_path_gpt = 'D:\桌面\科研\抽查-gpt.txt'  # 替换为你的文件路径
with open(file_path_gpt, 'r', encoding='utf-8') as file_gpt:
    text_gpt = file_gpt.read()
    
file_path_hum = 'D:\桌面\科研\抽查-人工.txt'  # 替换为你的文件路径
with open(file_path_hum, 'r', encoding='utf-8') as file_hum:
    text_hum = file_hum.read()
    #print(text)

Scores_gpt=re.findall("Score:\s*(\d+)",text_gpt)
Reasons_gpt=re.findall("Reason:\s*(.+?)(?=\s*Score:|\s*$)",text_gpt)
Scores_hum=re.findall("Score:\s*(\d+)",text_hum)
Reasons_hum=re.findall("Reason:\s*(.+?)(?=\s*Score:|\s*$)",text_hum)






# Convert string scores to integers
Scores_gpt_int = [int(score) for score in Scores_gpt]
Scores_hum_int = [int(score) for score in Scores_hum]
# Assuming Scores_gpt_int and Scores_hum_int are lists of integers representing the scores.

# Count the frequency of each score
freq_gpt = pd.Series(Scores_gpt_int).value_counts().sort_index()
freq_hum = pd.Series(Scores_hum_int).value_counts().sort_index()

# Align both Series to have the same indices in case one of them lacks a score
all_scores = range(1, 6)  # This includes scores from 1 to 5
freq_gpt = freq_gpt.reindex(all_scores, fill_value=0)
freq_hum = freq_hum.reindex(all_scores, fill_value=0)

# Create a DataFrame from the frequencies
df_scores = pd.DataFrame({'GPT-4 annotation': freq_gpt, 'Human annotation': freq_hum})

# Plot the bar chart
ax = df_scores.plot(kind='bar', color=['blue', 'orange'])
ax.set_title('Distribution of Scores for Two Groups')
ax.set_xlabel('Scores')
ax.set_ylabel('Counts')
ax.set_xticklabels(all_scores, rotation=0)
ax.legend()
plt.show()





