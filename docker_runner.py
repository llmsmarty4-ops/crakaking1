import subprocess
import os
import uuid

def run_py_docker(user_id, script_path, log_path):
    container_name = f"xhost_py_{user_id}_{uuid.uuid4().hex[:6]}"

    user_dir = os.path.dirname(script_path)
    script_name = os.path.basename(script_path)

    cmd = [
        "docker", "run", "--rm",
        "--name", container_name,

        # 🔒 SECURITY
        "--read-only",
        "--network", "none",
        "--pids-limit", "64",
        "--memory", "512m",
        "--cpus", "0.5",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",

        # 📂 user folder only
        "-v", f"{user_dir}:/app:ro",

        "xhost-python",
        "python", f"/app/{script_name}"
    ]

    return subprocess.Popen(
        cmd,
        stdout=open(log_path, "w", encoding="utf-8", errors="ignore"),
        stderr=subprocess.STDOUT
    )


def run_js_docker(user_id, script_path, log_path):
    container_name = f"xhost_js_{user_id}_{uuid.uuid4().hex[:6]}"

    user_dir = os.path.dirname(script_path)
    script_name = os.path.basename(script_path)

    cmd = [
        "docker", "run", "--rm",
        "--name", container_name,

        # 🔒 SECURITY
        "--read-only",
        "--network", "none",
        "--pids-limit", "64",
        "--memory", "512m",
        "--cpus", "0.5",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges",

        "-v", f"{user_dir}:/app:ro",

        "xhost-node",
        "node", f"/app/{script_name}"
    ]

    return subprocess.Popen(
        cmd,
        stdout=open(log_path, "w", encoding="utf-8", errors="ignore"),
        stderr=subprocess.STDOUT
    )
