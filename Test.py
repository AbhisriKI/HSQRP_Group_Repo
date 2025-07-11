import cirq

qubit_0 = cirq.NamedQubit('q1')
circuit = cirq.Circuit()
circuit.append(cirq.X(qubit_0))
print(qubit_0)
print(circuit)