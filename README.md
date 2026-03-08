# Simulation Validation Task (Please read this Readme_Instructions)

The output of the given simulation task is stored in **`newfile.root`**.

For Task Specific code -**`yoo.py`**. 

For Proposal Code - **`trcheck.ipynb`**. 

This root file has been provided so that user **does not need to be rerun heavy test**.
---

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yashg16422-design/GSOC-FASTSim-TASK.git
cd GSOC-FASTSim-TASK
```

2. **Create and Activate a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate     # On Linux / Mac
venv\Scripts\activate        # On Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## Notebook for Validation(Source Code for PROPOSAL)

An interactive notebook **`trcheck.ipynb`** is provided to validate the approaches step-by-step.
Altough Each module is imported independently please run the cells sequentially..
The dataset in **point-cloud format** is already available in:

```
point_cloud_dataset.npy
```

This allows you to run the validation workflow **without regenerating the dataset**.

---
## Task Script(GSOC - Source Code for GIVEN TASK)

**`yoo.py`** contains the implementation specifically written for the **defined task objectives** and should be used when running the core task logic.

---
## Simulation Data

* **`newfile.root`**
  IMPORTANT this is the Default simulation output used for experimentation in this task.

* **Other ROOT file**
  Provided only for **personal testing and demonstration of detector coverage**.
  **`other.root`**
  Is only used in
  **`simu.py`**
  by default to check spatial range only
---

## Project Workflow

1. Install dependencies
2. Open **`trcheck.ipynb`**
3. Validate the pipeline using the provided **point cloud dataset**
4. Use **`newfile.root`** for simulation-based experimentation
5. Run **`yoo.py`** for the task-specific implementation

---
