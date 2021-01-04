# 다시
def solution(skill, skill_trees): # skill : 선행 스킬 순서, skill_trees : 유저들이 만든 스킬트리를 담은 배열

    skill_trees = str(skill_trees)

    for i in range(len(skill)):                        # skill
        for j in range(len(skill_trees)):              # skill_tree[]
            for k in range(len(skill_trees[j])): 
                index = skill_trees.find(skill_trees[j][k])

    return index

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


# skill의 012.. 순으로 skill_trees와 비교 후, 그 인덱스 번호를 따로 리스트에 저장
# 하나라도 없으면 break
# 그게 오름 차순이면 count +1 (for문으로?)




# for index in enumerate(skill_trees[j]): 
            #     index_num.append(index)




    # skill = list(skill) # ['C', 'B', 'D']
    # skill_trees = list(skill_trees) # ['BACDE', 'CBADF', 'AECB', 'BDA']
    # index_num = []

    # for i in range(len(skill)):                        # skill
    #     for j in range(len(skill_trees)):              # skill_tree[]
    #         for k in range(len(skill_trees[j])):       # skill_tree[][]
    #             if skill[i] == skill_trees[j][k]:
    #                 index_num.append(skill_trees[j][k].index(skill_trees[j][k]))
    #             else:
    #                 pass


    # return index_num