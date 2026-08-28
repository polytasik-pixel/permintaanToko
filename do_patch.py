import sys

with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's locate line with '// FITUR FORWARD SERVICE AREA' and 'function simpanStatusPart()'
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '// FITUR FORWARD SERVICE AREA' in line:
        start_idx = i
    if 'function simpanStatusPart()' in line:
        end_idx = i

print(f'start_idx={start_idx}, end_idx={end_idx}')
