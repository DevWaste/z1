
development_stages = []
print("Введите этапы развития человека. Введите 'конец' для завершения.")

while True:
    stage = input("Введите этап: ")
    if stage.lower() == 'конец':
        break
    development_stages.append(stage)

print(*development_stages, sep=' => ')
