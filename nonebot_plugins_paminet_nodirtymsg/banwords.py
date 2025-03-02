import json
from pathlib import Path
from typing import Set

def load_banwords(path: str) -> Set[str]:
    file_path = Path(path)
    if not file_path.exists(): 
        init_words = ["赌博", "色情", "诈骗", "毒品", "暴力"]
        file_path.parent.mkdir(exist_ok=True) 
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(init_words,  f)
        return set(init_words)
    
    with open(file_path, "r", encoding="utf-8") as f:
        return set(json.load(f)) 