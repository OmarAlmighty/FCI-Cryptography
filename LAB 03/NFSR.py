class NFSR:
    def __init__(self, initial_state):
        """
        Initialize the LFSR with a seed and tap positions.
        """
        self.current_state = initial_state.copy()

    def shift(self):
        """
        Perform one shift operation on the LFSR.
        """
        n0 = self.current_state[0]
        n1 = self.current_state[1]
        n2 = self.current_state[2]
        n3 = self.current_state[3]

        feedback_bit = n2 ^ n3

        # Shift the state to the right
        output_bit = n0 ^ n1 ^ (n0 & n1) ^ (n2 & n3)

        # Insert the feedback bit at the beginning
        self.current_state.insert(0, feedback_bit)

        return output_bit

    def generate(self, num_bits):
        """
        Generate a sequence of bits using the LFSR.
        """
        output_bits = []
        for _ in range(num_bits):
            output_bits.append(self.shift())
        return output_bits


seed = [1, 1, 0, 1]
lfsr = NFSR(seed)

# Generate 10 bits
generated_bits = lfsr.generate(50)
print("Generated bits:", generated_bits)
