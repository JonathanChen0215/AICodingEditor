import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

# Try to import msvcrt for keyboard detection on Windows
try:
    import msvcrt
except ImportError:
    msvcrt = None

# Set up Streamlit page configuration
st.set_page_config(page_title="Sin & Cosin Real-time Plot", layout="wide")
st.title("Real-time Sin & Cosin Waveforms")

# Print to console before entering the while loop
print("y1=sin(2*np.pi*x)")
print("y2=cosin(2*np.pi*x)")

# Also display the formula on Streamlit interface
st.write("Formula 1: $y_1 = \\sin(2\\pi x)$")
st.write("Formula 2: $y_2 = \\cos(2\\pi x)$")

# Placeholder for updating matplotlib plot
plot_placeholder = st.empty()

# Add a Stop button in Streamlit to gracefully stop and free resources
stop_button = st.button("Stop Simulation")

# Initial parameters
step_num = 0
dt = 1.0 / 36.0          # Each step is 1/36 second
sleep_time = 1.0 / (5*14.4)   # Every 1/7.2 second we update
window_size = 360        # Approx 360 points in the window

try:
    while True:
        # Force close any unclosed figures before creating a new one to save memory
        plt.close('all')

        # Check if user clicked Stop in Streamlit
        if stop_button:
            st.warning("Simulation stopped via Web UI.")
            break

        # Check for keyboard interrupts (ESC or Ctrl+C) in console
        if msvcrt and msvcrt.kbhit():
            key = msvcrt.getch()
            # ESC key is 27 (b'\x1b'), Ctrl+C key is 3 (b'\x03'), 'c'/'C' for ease
            if key in (b'\x1b', b'\x03', b'c', b'C'):
                print("Exit signal received. Stopping while loop...")
                break

        # Generate x values for the moving window of 360 points
        indices = np.arange(step_num, step_num + window_size)
        x = indices * dt
        
        # Calculate y values
        y1 = np.sin(2 * np.pi * x)
        y2 = np.cos(2 * np.pi * x)

        # Plot using Matplotlib
        fig, ax = plt.subplots(figsize=(10, 2.5))       
        ax.plot(x, y1, label="y1 = sin(2*pi*x)", color="blue", linewidth=1.5)
        ax.plot(x, y2, label="y2 = cosin(2*pi*x)", color="red", linewidth=1.5)
        
        ax.set_xlim(x[0], x[-1])
        ax.set_ylim(-1.2, 1.2)
        ax.set_xlabel("x (seconds)")
        ax.set_ylabel("y")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(loc="upper right")
        
        # Display the updated figure in Streamlit
        plot_placeholder.pyplot(fig)

        # Force close the current figure to free memory immediately
        plt.close(fig)

        # Move window by 10 points (which corresponds to 10 * 1/36 second = 1/3.6 second of real-time shift)
        step_num += 10

        # Delay for 1/3.6 second
        time.sleep(sleep_time)

except KeyboardInterrupt:
    print("KeyboardInterrupt (Ctrl+C) detected in console. Exiting...")
finally:
    # Cleanup all matplotlib plots to avoid resource leakage
    plt.close('all')
    plot_placeholder.empty()
    st.info("Simulation ended and all resources have been released.")