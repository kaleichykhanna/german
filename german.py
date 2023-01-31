import re

with open("inp.txt", 'r') as file_input:
    ex = file_input.read()
    ex = ex.replace('-\n', '')
    ex = ex.replace('\n', ' ')
with open("ans.txt", 'r') as file_input:
    ans = file_input.read()
    ans = ans.replace('\n', ' ')
ex = re.split(r"\d+\.", ex)
ans = re.split(r"\d+\.", ans)
with open("out.txt", 'w') as file_output:
    for i in range(1, len(ex)):
        file_output.write(f"{ex[i]}\t{ans[i]}\n")
