from time import sleep
# import keyboard  # You'll need to install this with: pip install keyboard

class PiSpigot:
    """Generates pi digits infinitely using the spigot algorithm"""
    def __init__(self):
        self.q, self.r, self.t, self.k, self.n, self.l = 1, 0, 1, 1, 3, 3

    def next_digit(self):
        while True:
            if 4 * self.q + self.r - self.t < self.n * self.t:
                yield self.n
                self.q, self.r, self.t, self.k, self.n, self.l = (
                    10 * self.q,
                    10 * (self.r - self.n * self.t),
                    self.t,
                    self.k,
                    (10 * (3 * self.q + self.r)) // self.t - 10 * self.n,
                    self.l
                )
            else:
                self.q, self.r, self.t, self.k, self.n, self.l = (
                    self.q * self.k,
                    (2 * self.q + self.r) * self.l,
                    self.t * self.l,
                    self.k + 1,
                    (self.q * (7 * self.k + 2) + self.r * self.l) // (self.t * self.l),
                    self.l + 2
                )

# def map_digit_to_input(digit):
#     """Map each digit (0-9) to a game input
#     Modify these mappings according to your game's controls"""
#     mapping = {
#         '0': 'up',    # Up
#         '1': 'down',  # Down
#         '2': 'left',  # Left
#         '3': 'right', # Right
#         '4': 'z',     # A button
#         '5': 'x',     # B button
#         '6': 'a',     # X button
#         '7': 's',     # Y button
#         '8': 'q',     # L button
#         '9': 'w'      # R button
#     }
#     return mapping.get(digit)

def main():
    print("Generating Pi digits and starting input simulation...")
    pi_generator = PiSpigot()
    digit_stream = pi_generator.next_digit()
    count = 0

    # next(digit_stream) # Skip the first digit ??

    print("Starting input simulation...")
    try:
        while True:
            digit = next(digit_stream)
            # input_key = map_digit_to_input(current_digit)
            
            # Print current digit and corresponding input
            # print(f"Digit: {current_digit} -> Input: {input_key}")
            print(digit)
            # Simulate keypress
            # keyboard.press_and_release(input_key)
            
            # Wait a bit between inputs (adjust timing as needed)
            sleep(5)
            
            count += 1
                
    except KeyboardInterrupt:
        print("\nStopping input simulation...")
        print(f"\nProcessed {count} digits of Pi")

if __name__ == "__main__":
    main()
