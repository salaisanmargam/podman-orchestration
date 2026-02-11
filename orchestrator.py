import subprocess
import sys

services = [
    ("add", 5001),
    ("sub", 5002),
    ("mul", 5003),
    ("div", 5004)
]

def run(cmd):
    print(">>", cmd)
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit("❌ Command failed")

# Cleanup
run("podman stop -a || true")
run("podman rm -a || true")

# Build images
for name, _ in services:
    run(f"podman build -t calc-{name} services/{name}")

# Run containers
for name, port in services:
    run(
        f"podman run -d --name {name} "
        f"-p {port}:5000 calc-{name}"
    )

print("✅ All 4 services orchestrated successfully")
