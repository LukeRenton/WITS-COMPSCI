=================================================================
🧠 MSCLUSTER USAGE — GENERAL RESEARCH QUICK REFERENCE
=================================================================

Cluster Login:
    SSH Address  : 146.141.21.100
    Username     : <your-username>
    Password     : <default-password>

Project Dir    : ~/my_project/
Environment Dir: ~/my_project/env/
Results Dir    : ~/my_project/results/

=================================================================
1. CONNECTING TO THE CLUSTER (VS CODE SSH)
-----------------------------------------------------------------
~/.ssh/config entry:
    Host mscluster
        HostName 146.141.21.100
        User <your-username>
        IdentityFile ~/.ssh/id_rsa

In VS Code:
    - Open Command Palette → "Remote-SSH: Connect to Host" → mscluster
    - Wait for the "SSH: mscluster" indicator (bottom-left)

=================================================================
2. PYTHON ENVIRONMENT SETUP
-----------------------------------------------------------------
Option A: Virtualenv (venv)
    cd ~/my_project/
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

Option B: Miniconda (Recommended)
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    source ~/.bashrc

    conda create -n env python=3.9
    conda activate env
    conda install numpy matplotlib dill pytorch -c conda-forge -c pytorch

=================================================================
3. RUNNING CODE ON THE CLUSTER
-----------------------------------------------------------------
Activate environment and run:
    source ~/my_project/env/bin/activate
    cd ~/my_project/
    python3 my_script.py

Output will be saved to:
    ~/my_project/results/

=================================================================
4. BACKUP TO LOCAL MACHINE
-----------------------------------------------------------------
    scp -r <user>@146.141.21.100:~/my_project/ ./local_backup/

=================================================================
5. SAFE JOB EXECUTION
-----------------------------------------------------------------
❌ Do NOT just run: `python3 script.py`  
→ It will stop if your session drops.

✅ Use one of the following:

A. `nohup` (for background):
    nohup python3 script.py > out.log 2>&1 &

B. `tmux` (detachable terminal):
    tmux
    python3 script.py
    [Ctrl + B, then D to detach]
    tmux attach  # to resume

C. SLURM:
    sbatch my_job.sh

=================================================================
6. MONITORING TOOLS
-----------------------------------------------------------------
Check job status:
    squeue -u <your-username>

Cancel all jobs:
    scancel -u <your-username>

CPU usage:
    top
    htop  (if installed)

Check CPU info:
    lscpu

See current node:
    hostname

=================================================================
7. SLURM PARTITIONS (CPU/GPU OPTIONS)
-----------------------------------------------------------------
| Partition   | CPUs/Node | Total Nodes | Special     |
|-------------|-----------|--------------|-------------|
| stampede    | 16        | 40           | —           |
| bigbatch    | 28        | 48           | Default     |
| biggpu      | 112       | 4            | GPU-enabled |

Interactive job with full CPU node:
    srun -p bigbatch --cpus-per-task=28 --mem=60G -t 04:00:00 --pty bash

Interactive job with GPU:
    srun -p biggpu --gres=gpu:1 --cpus-per-task=16 --mem=64G -t 02:00:00 --pty bash

NOTE:
• `--pty bash` gives you an interactive shell on the compute node
• Adjust time with `-t HH:MM:SS` or `-t DD-HH:MM:SS`

=================================================================
8. JOB SCRIPTS (SLURM)
-----------------------------------------------------------------
Example SLURM job script (job.sh):

#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --output=output.log
#SBATCH --partition=bigbatch
#SBATCH --cpus-per-task=28
#SBATCH --mem=60G
#SBATCH --time=04:00:00

source ~/my_project/env/bin/activate
cd ~/my_project/
python3 my_script.py

Submit job:
    sbatch job.sh

=================================================================
9. HELPFUL COMMANDS
-----------------------------------------------------------------
Check memory:
    free -h

Check disk usage:
    du -sh *

List nodes:
    sinfo

Job history:
    sacct -u <your-username>

=================================================================
10. TROUBLESHOOTING
-----------------------------------------------------------------
• If a job is stuck in "PD (Pending)", check reasons with:
    squeue -u <your-username> -l

• Use `--exclusive` for exclusive node access if needed.

• Make sure to output logs to different folders per job to avoid overwriting:
    mkdir -p results/$(date +%Y%m%d_%H%M%S)

=================================================================
