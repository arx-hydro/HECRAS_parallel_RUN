# HEC-RAS Parallel Runner

This repository contains Python code to run HEC-RAS hydraulic modeling software in parallel. The goal is to automate and speed up the process of running multiple HEC-RAS simulations using Python, making it more efficient for users who need to perform batch processing or parameter sweeps.

## Features

- Launches multiple HEC-RAS projects or plans in parallel.
- Automates interaction with the HEC-RAS software.
- Saves time for large-scale hydraulic modeling tasks.

## Requirements

- [Python](https://www.python.org/downloads/) (version 3.x recommended)
- [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) installed on your computer
- Python packages: `subprocess`, `concurrent.futures` (standard library), and any others your script uses

## Usage

1. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/your-repo-name.git
   cd your-repo-name
   ```

2. **Edit `run_hecras_parallel.py`:**  
   Set up your list of HEC-RAS projects or plans to run in the script.

3. **Run the script:**
   ```bash
   python run_hecras_parallel.py
   ```

4. **Check outputs:**  
   Results will be saved as defined in your script or HEC-RAS project settings.

## Example

```python
# Example usage in run_hecras_parallel.py
if __name__ == "__main__":
    main()
```

## Notes

- Make sure HEC-RAS is properly installed and accessible from your system’s PATH.
- You may need to adjust the script for your particular HEC-RAS version and project setup.


## Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss what you’d like to change.

## Contact

For questions or feedback, open an issue or contact [@Siamak6565](https://github.com/Siamak6565).
