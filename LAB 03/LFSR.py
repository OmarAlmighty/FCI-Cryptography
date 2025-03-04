class LFSR:
    def __init__(self, initial_state, feedback_poly):
        """
        Initialize the LFSR with a seed and tap positions.
        """
        self.current_state = initial_state.copy()
        self.bits_positions = feedback_poly

    def shift(self):
        """
        Perform one shift operation on the LFSR.
        """
        # Calculate the feedback bit using XOR on the tap positions
        feedback_bit = 0
        for pos in self.bits_positions:
            feedback_bit ^= self.current_state[pos]


        # Shift the state to the right
        output_bit = self.current_state.pop()

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


seed = [1, 0, 1, 1]
polynomial = [0, 3]
lfsr = LFSR(seed, polynomial)

# Generate 10 bits
generated_bits = lfsr.generate(50)
print("Generated bits:", generated_bits)