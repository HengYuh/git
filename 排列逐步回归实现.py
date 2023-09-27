#基本思路：
#  1.有4个被替换词，那么组合后就有A44,即4*3*2*1=24种组合，将这24种组合都进行一遍优化。
# 2. 例如这4个被替换词为A,B,C,D,那么我们可以先假如得到一个有A1,B1,C1,D1构成的对抗性样本，我们让B1,C1,D1不变，
# 在保持对抗性的前提下，不断替换A1，直到找到A2,使得A2,B1,C1,D1构成的样本相似度在A的所有替换词中最大，
# 然后我们固定A2，C1,D1，重复操作得到B2,然后固定A2,B2,D2,得到C2，然后是D2,我们得到一组A2,B2,C2,D2组成的对抗性样本
# 3. 更换顺序，例如B1,A1,C1,D1,按照这个顺序得到B2,A2,C2,D2。。。。。直到遍历24种情况
# 4.现在我们得到24种ABCD的组合，我们比较它们构成的对抗性样本与原样本的相似度，选择相似度最高的那一组
#如果你想知道更具体的过程，可以查阅我写代码过程中与gpt4的对话-https://chat.openai.com/share/6a000f3b-4c0f-4d33-920a-e54fde825703


    # 输入: 
    #word to replace-(a,b,c,d)
    # text_ls - 原文本
    # replace_list - [(a, 'A1'), (b, 'B1'), (c, 'C1'), (d, 'D1')]，其中a, b, c, d为原文本中的位置索引
    # best_attack - 初始对抗性样本
    # best_sim - 初始样本与原文本的相似度
    # synonyms_all - 同义词列表
    
    # 定义一个临时的对抗性样本列表
import itertools

def optimized_adversarial_combinations(text_ls, replace_list, best_attack, best_sim, synonyms_all, predictor, orig_label, batch_size, sim_predictor):
    
    # 从replace_list获取所有位置索引，并得到这些索引的全排列
    indices = [t[0] for t in replace_list]
    index_permutations = list(itertools.permutations(indices))

    # 初始化全局的最佳对抗样本和其对应的相似度
    global_best_attack = best_attack[:]
    global_best_sim = best_sim

    # 遍历所有的排列
    for idx_order in index_permutations:
        
        # 根据当前的位置索引排列重新组织replace_list
        current_replace_order = sorted(replace_list, key=lambda x: idx_order.index(x[0]))
        
        attack_temp = global_best_attack[:]
        local_best_sim = global_best_sim
        
        # 对当前排列下的每个被替换的词进行遍历
        for idx, replaced_word in current_replace_order:
            current_best_word = replaced_word
            for synonym in synonyms_all[idx]:
                attack_temp[idx] = synonym
                temp_sim = calc_sim(text_ls, [attack_temp], -1, sim_score_window, sim_predictor)[0]
                
                if temp_sim > local_best_sim and np.sum(get_attack_result([attack_temp], predictor, orig_label, batch_size)) > 0:
                    local_best_sim = temp_sim
                    current_best_word = synonym
                    
            attack_temp[idx] = current_best_word

        # 更新全局的最佳对抗样本
        if local_best_sim > global_best_sim:
            global_best_sim = local_best_sim
            global_best_attack = attack_temp[:]

    return ' '.join(global_best_attack), global_best_sim


