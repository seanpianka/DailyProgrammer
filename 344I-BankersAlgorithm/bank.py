with open('bank.txt') as f:
    data = [[int(x) for x in l.strip().strip('[]').split()] for l in f.readlines()]

available = data[0]
processes = {f'P{i}': {'max': p[len(available):], 'allocation': p[:len(available)]} for i, p in enumerate(data[1:])}
order = []

while processes:
    try:
        order.append([name for name, state in processes.items() if all([state['max'][i] - state['allocation'][i] <= available[i] for i in range(len(available))])][0])
        available = [available[i] + processes[order[-1]]['allocation'][i] for i in range(len(available))]
        del[processes[order[-1]]]
    except IndexError: # No process was able to be run with available resources
        print(f'Cannot complete algorithm, the processes <{order}> were able to complete.')
        break
else:
    print(', '.join(order))
