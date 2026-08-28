import sys

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's verify start and end index
start_marker = '// FITUR FORWARD SERVICE AREA'
end_marker = 'function simpanStatusPart()'

idx1 = text.find(start_marker)
idx2 = text.find(end_marker)

print(f'idx1={idx1}, idx2={idx2}')
