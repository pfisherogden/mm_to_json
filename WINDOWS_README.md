# Windows Build & Verification Instructions

This document provides instructions for compiling the C++ `mm_to_json` application on Windows and verifying its output against the Python version.

## Prerequisites

1.  **Visual Studio 2019 or 2022**:
    *   Ensure the "Desktop development with C++" workload is installed.
    *   Ensure "CMake tools for Windows" is selected (usually default).
2.  **Microsoft Access Database Engine**:
    *   You need the ODBC driver for `.mdb` files (`Microsoft Access Driver (*.mdb)`).
    *   **Architecture Warning**: If you have 64-bit Office installed, your ODBC driver is 64-bit. If 32-bit Office, it's 32-bit.
    *   You must compile `mm_to_json` to match this architecture (x64 or x86).

## Building with Visual Studio

1.  Open Visual Studio.
2.  Select **Open a local folder** and choose `MeetManager-Tools/mm_to_json`.
3.  Visual Studio should detect `CMakeLists.txt`.
4.  Select your configuration (e.g., `x64-Debug` or `x86-Debug`) from the top toolbar dropdown. matches your Access Driver architecture.
    *   To check your driver architecture, search for "ODBC Data Sources" in Windows Start Menu. If you see "Microsoft Access Driver" in the 64-bit administrator, build for x64.
5.  Select **Build > Build All**.
6.  The executable `mm_to_json.exe` will be generated in `out/build/x64-Debug/mm_to_json/` (or similar path).

## Running the C++ Version

Open a **Command Prompt** or **PowerShell** and navigate to the build output directory.

```powershell
# Example path
cd out/build/x64-Debug/mm_to_json

# Run conversion
.\mm_to_json.exe "C:\path\to\Singers23.mdb"
```

This will generate `Singers23.json` in the same directory.

## Running Verification

To compare the C++ output with the Python output:

1.  Generate JSON using Python (on Mac or Windows):
    ```bash
    cd mm_to_json_py
    uv run mm_to_json.py ../Singers23.mdb
    ```
2.  Generate JSON using C++ (as above).
3.  Use the comparison script:
    ```bash
    python compare_json.py path/to/python/Singers23.json path/to/cpp/Singers23.json
    ```

## Common Issues

*   **"Data source name not found and no default driver specified"**: This means the ODBC driver string in `mmToJsonConverter.cpp` doesn't match your installed driver, or (more likely) you are running a 64-bit exe against 32-bit drivers (or vice versa). Switch the build architecture in Visual Studio.
