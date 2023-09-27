
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