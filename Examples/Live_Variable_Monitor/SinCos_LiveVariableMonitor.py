# -*- coding: utf-8 -*-
"""
AICodingEditor Live Variable Monitor test
------------------------------------------
y1 = sin(x), y2 = cos(x)
x cycles from 0 to 359 degrees, one sample every 0.2 seconds.

Stop methods:
1. In a normal Windows CMD / Terminal: press ESC.
2. In a normal CMD / Terminal: press Ctrl+C.
3. In AICodingEditor: click the Stop button.
4. In AICodingEditor Program stdin: type esc, stop, q, quit, or exit, then Send.
"""

import math
import os
import sys
import threading
import time

STOP_COMMANDS = {"esc", "stop", "q", "quit", "exit"}


def listen_for_editor_stop(stop_event: threading.Event) -> None:
    """
    Read text commands from AICodingEditor Program stdin.

    This listener is used only when standard input is a pipe rather than
    an interactive terminal. It lets the user send: esc / stop / q / quit.
    """
    while not stop_event.is_set():
        line = sys.stdin.readline()
        if line == "":
            return

        command = line.strip().lower()
        if command in STOP_COMMANDS:
            stop_event.set()
            return


def escape_pressed_in_windows_console() -> bool:
    """
    Return True when ESC is pressed in a normal Windows console.

    AICodingEditor's embedded stdin is a pipe, so its Stop button or
    Program stdin command should be used instead.
    """
    if os.name != "nt":
        return False

    try:
        import msvcrt  # Windows standard library module

        if msvcrt.kbhit():
            return msvcrt.getwch() == "\x1b"  # ESC character
    except OSError:
        # No attached native Windows console.
        pass

    return False


def main() -> None:
    stop_event = threading.Event()

    # In AICodingEditor, stdin is normally a pipe. Start a command listener
    # so the user can type "esc" in Program stdin and press Send.
    if not sys.stdin.isatty():
        threading.Thread(
            target=listen_for_editor_stop,
            args=(stop_event,),
            daemon=True,
        ).start()

    print("Sin/Cos live variable monitor started.", flush=True)
    print("x: 0~359 degrees, period: 0.2 seconds/sample.", flush=True)
    print(
        "Stop: ESC or Ctrl+C in CMD; "
        "AICodingEditor Stop button; or send 'esc' via Program stdin.",
        flush=True,
    )

    x = 0
    sample = 0
    start_time = time.perf_counter()

    try:
        while not stop_event.is_set():
            # Calculate sine and cosine using degree-based x.
            radians = math.radians(x)
            y1 = math.sin(radians)
            y2 = math.cos(radians)
            elapsed_s = time.perf_counter() - start_time

            # AICodingEditor V0.1.26 variable-monitor output format.
            # Select time_s, x, y1 and y2 in VARIABLES / CHARTS.
            print(
                f"AICE_VAR sample={sample} "
                f"time_s={elapsed_s:.3f} "
                f"x={x} "
                f"y1={y1:.6f} "
                f"y2={y2:.6f}",
                flush=True,
            )

            # Advance x cyclically: 0, 1, ..., 359, 0, 1, ...
            x = (x + 1) % 360
            sample += 1

            # 0.2 second output interval.
            stop_event.wait(0.2)

            # ESC works in a normal Windows CMD console.
            if escape_pressed_in_windows_console():
                print("ESC detected. Stopping...", flush=True)
                stop_event.set()

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Stopping...", flush=True)

    finally:
        print("Sin/Cos live variable monitor finished.", flush=True)


if __name__ == "__main__":
    main()
